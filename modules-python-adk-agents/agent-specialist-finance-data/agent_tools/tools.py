"""
Yahoo Finance tools for the specialist_finances agent.

This module exposes a curated set of tools backed by the yfinance library.
Each tool is designed so that the LLM agent can call it with simple, typed
arguments.  Several guardrails are applied throughout:

Guardrails
----------
- No intraday data: history interval is restricted to 1d or coarser.
- History periods are capped at 5y to avoid enormous payloads.
- DataFrames are serialized to JSON and row counts are capped.
- Ticker.info returns only an analyst-relevant subset of fields.
- News is capped at 10 articles; holder tables at 15 rows.
- Search results are capped at 8 quotes.
- No WebSocket / live-streaming tools (inappropriate for agent use).
- No bulk multi-ticker download (yf.download) to prevent large requests.
"""

from __future__ import annotations

import json
from typing import Any

import yfinance as yf

# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

# Fields exposed from Ticker.info – keeps the payload focused and avoids
# leaking fields that are noisy or very large (e.g. raw description text).
_INFO_ALLOWED_FIELDS: set[str] = {
    "symbol",
    "shortName",
    "longName",
    "sector",
    "industry",
    "country",
    "currency",
    "exchange",
    "quoteType",
    "marketCap",
    "enterpriseValue",
    "currentPrice",
    "previousClose",
    "open",
    "dayLow",
    "dayHigh",
    "fiftyTwoWeekLow",
    "fiftyTwoWeekHigh",
    "volume",
    "averageVolume",
    "averageVolume10days",
    "beta",
    "trailingPE",
    "forwardPE",
    "priceToBook",
    "trailingEps",
    "forwardEps",
    "dividendRate",
    "dividendYield",
    "payoutRatio",
    "returnOnEquity",
    "returnOnAssets",
    "grossMargins",
    "operatingMargins",
    "profitMargins",
    "debtToEquity",
    "revenueGrowth",
    "earningsGrowth",
    "totalRevenue",
    "grossProfits",
    "ebitda",
    "totalCash",
    "totalDebt",
    "freeCashflow",
    "operatingCashflow",
    "numberOfAnalystOpinions",
    "targetMeanPrice",
    "targetLowPrice",
    "targetHighPrice",
    "recommendationMean",
    "recommendationKey",
    "fullTimeEmployees",
    "auditRisk",
    "boardRisk",
    "compensationRisk",
    "shareHolderRightsRisk",
    "overallRisk",
    "lastDividendValue",
    "lastDividendDate",
    "exDividendDate",
    "firstTradeDateEpochUtc",
    "regularMarketPrice",
    "regularMarketChangePercent",
    "52WeekChange",
    "SandP52WeekChange",
}

# Valid periods for history (coarse-only; no 10y/max to limit payload)
_VALID_PERIODS = {"1mo", "3mo", "6mo", "1y", "2y", "5y"}

# Valid intervals (day-level and coarser only; no intraday)
_VALID_INTERVALS = {"1d", "5d", "1wk", "1mo", "3mo"}

# Valid market identifiers
_VALID_MARKETS = {"US", "GB", "BR", "ASIA", "EUROPE", "RATES", "COMMODITIES", "CURRENCIES", "CRYPTOCURRENCIES"}


def _df_to_dict(df, max_rows: int | None = None) -> dict[str, Any]:
    """Serialize a pandas DataFrame to a plain dict, with an optional row cap."""
    if df is None or (hasattr(df, "empty") and df.empty):
        return {}
    if max_rows is not None:
        df = df.head(max_rows)
    # Convert index to string so it serializes cleanly to JSON
    df = df.copy()
    df.index = df.index.astype(str)
    return df.to_dict()


def _safe(fn, *args, **kwargs) -> dict[str, Any]:
    """Call *fn* and wrap any exception in an error dict."""
    try:
        return fn(*args, **kwargs)
    except Exception as exc:  # noqa: BLE001
        return {"error": str(exc)}


# ---------------------------------------------------------------------------
# Ticker – single symbol tools
# ---------------------------------------------------------------------------


def get_ticker_info(symbol: str) -> dict[str, Any]:
    """
    Returns a curated set of fundamental and market data for a single ticker.

    Use this as the starting point when the user asks about a company, stock,
    ETF, crypto asset, or other Yahoo Finance listed symbol.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol (e.g. "AAPL", "BTC-USD", "PETR4.SA").

    Returns
    -------
    dict
        Curated subset of the ticker's info dictionary.
    """
    def _fetch():
        raw = yf.Ticker(symbol.upper()).info
        return {k: v for k, v in raw.items() if k in _INFO_ALLOWED_FIELDS}

    return _safe(_fetch)


def get_ticker_fast_info(symbol: str) -> dict[str, Any]:
    """
    Returns a quick snapshot of live/recent price data for a ticker.

    Preferred over get_ticker_info() when the user only needs current price,
    market cap, or volume without the full fundamentals.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Fast-info fields such as lastPrice, marketCap, fiftyDayAverage, etc.
    """
    def _fetch():
        fi = yf.Ticker(symbol.upper()).fast_info
        # fast_info is a special object; iterate its keys
        return {k: getattr(fi, k, None) for k in fi.keys()}

    return _safe(_fetch)


def get_ticker_history(symbol: str, period: str = "3mo", interval: str = "1d") -> dict[str, Any]:
    """
    Returns OHLCV (Open, High, Low, Close, Volume) price history for a ticker.

    GUARDRAILS
    ----------
    - interval must be one of: 1d, 5d, 1wk, 1mo, 3mo  (no intraday data).
    - period must be one of: 1mo, 3mo, 6mo, 1y, 2y, 5y  (no 10y / max).

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.
    period : str
        Time window to retrieve. Defaults to "3mo".
    interval : str
        Data frequency. Defaults to "1d".

    Returns
    -------
    dict
        OHLCV data as a dictionary of column -> {date -> value}.
    """
    if interval not in _VALID_INTERVALS:
        return {
            "error": (
                f"Interval '{interval}' is not allowed. "
                f"Choose from: {sorted(_VALID_INTERVALS)}"
            )
        }
    if period not in _VALID_PERIODS:
        return {
            "error": (
                f"Period '{period}' is not allowed. "
                f"Choose from: {sorted(_VALID_PERIODS)}"
            )
        }

    def _fetch():
        df = yf.Ticker(symbol.upper()).history(period=period, interval=interval)
        return _df_to_dict(df)

    return _safe(_fetch)


def get_ticker_actions(symbol: str) -> dict[str, Any]:
    """
    Returns the corporate actions (dividends and stock splits) for a ticker.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Date-indexed dictionary with Dividends and Stock Splits columns.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).actions))


def get_ticker_dividends(symbol: str) -> dict[str, Any]:
    """
    Returns the historical dividend payments for a ticker.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Date-indexed dictionary of dividend amounts.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).dividends.to_frame()))


def get_ticker_splits(symbol: str) -> dict[str, Any]:
    """
    Returns the historical stock split events for a ticker.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Date-indexed dictionary of split ratios.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).splits.to_frame()))


def get_ticker_financials(symbol: str, frequency: str = "yearly") -> dict[str, Any]:
    """
    Returns the income statement (profit and loss) for a ticker.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.
    frequency : str
        "yearly" (default) or "quarterly".

    Returns
    -------
    dict
        Income statement data.
    """
    if frequency not in ("yearly", "quarterly"):
        return {"error": "frequency must be 'yearly' or 'quarterly'."}

    def _fetch():
        t = yf.Ticker(symbol.upper())
        df = t.quarterly_income_stmt if frequency == "quarterly" else t.income_stmt
        return _df_to_dict(df)

    return _safe(_fetch)


def get_ticker_balance_sheet(symbol: str, frequency: str = "yearly") -> dict[str, Any]:
    """
    Returns the balance sheet data for a ticker.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.
    frequency : str
        "yearly" (default) or "quarterly".

    Returns
    -------
    dict
        Balance sheet data.
    """
    if frequency not in ("yearly", "quarterly"):
        return {"error": "frequency must be 'yearly' or 'quarterly'."}

    def _fetch():
        t = yf.Ticker(symbol.upper())
        df = t.quarterly_balance_sheet if frequency == "quarterly" else t.balance_sheet
        return _df_to_dict(df)

    return _safe(_fetch)


def get_ticker_cashflow(symbol: str, frequency: str = "yearly") -> dict[str, Any]:
    """
    Returns the cash flow statement for a ticker.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.
    frequency : str
        "yearly" (default) or "quarterly".

    Returns
    -------
    dict
        Cash flow data.
    """
    if frequency not in ("yearly", "quarterly"):
        return {"error": "frequency must be 'yearly' or 'quarterly'."}

    def _fetch():
        t = yf.Ticker(symbol.upper())
        df = t.quarterly_cashflow if frequency == "quarterly" else t.cashflow
        return _df_to_dict(df)

    return _safe(_fetch)


def get_ticker_calendar(symbol: str) -> dict[str, Any]:
    """
    Returns upcoming earnings dates and dividend information for a ticker.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Calendar events (earnings date, ex-dividend date, etc.).
    """
    def _fetch():
        cal = yf.Ticker(symbol.upper()).calendar
        if isinstance(cal, dict):
            # Serialize date/datetime objects
            return json.loads(json.dumps(cal, default=str))
        return _df_to_dict(cal)

    return _safe(_fetch)


def get_ticker_analyst_price_targets(symbol: str) -> dict[str, Any]:
    """
    Returns analyst price target statistics for a ticker.

    Includes current price, low, high, mean, and median analyst targets.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Analyst price target data.
    """
    def _fetch():
        targets = yf.Ticker(symbol.upper()).analyst_price_targets
        if isinstance(targets, dict):
            return json.loads(json.dumps(targets, default=str))
        return _df_to_dict(targets)

    return _safe(_fetch)


def get_ticker_earnings_estimate(symbol: str) -> dict[str, Any]:
    """
    Returns analyst earnings-per-share (EPS) estimates for current and future periods.

    Columns include numberOfAnalysts, avg, low, high, yearAgoEps, growth.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        EPS estimate data indexed by period (0q, +1q, 0y, +1y).
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).earnings_estimate))


def get_ticker_revenue_estimate(symbol: str) -> dict[str, Any]:
    """
    Returns analyst revenue estimates for current and future periods.

    Columns include numberOfAnalysts, avg, low, high, yearAgoRevenue, growth.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Revenue estimate data indexed by period (0q, +1q, 0y, +1y).
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).revenue_estimate))


def get_ticker_earnings_history(symbol: str) -> dict[str, Any]:
    """
    Returns historical EPS surprises (actual vs estimated earnings).

    Columns include epsEstimate, epsActual, epsDifference, surprisePercent.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Historical earnings surprises indexed by date.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).earnings_history))


def get_ticker_eps_trend(symbol: str) -> dict[str, Any]:
    """
    Returns the trend in analyst EPS estimate revisions over time.

    Columns include current, 7daysAgo, 30daysAgo, 60daysAgo, 90daysAgo.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        EPS trend data indexed by period.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).eps_trend))


def get_ticker_growth_estimates(symbol: str) -> dict[str, Any]:
    """
    Returns analyst growth estimates for the stock vs its sector and market.

    Columns include stock, industry, sector, index.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Growth estimate comparisons across periods.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).growth_estimates))


def get_ticker_recommendations(symbol: str) -> dict[str, Any]:
    """
    Returns the current analyst recommendation summary for a ticker.

    Columns include strongBuy, buy, hold, sell, strongSell for recent periods.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Recommendation counts per period.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).recommendations))


def get_ticker_upgrades_downgrades(symbol: str) -> dict[str, Any]:
    """
    Returns the most recent analyst upgrades and downgrades for a ticker.

    GUARDRAIL: Limited to the 20 most recent events.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Recent upgrades/downgrades with firm, fromGrade, toGrade, action.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).upgrades_downgrades, max_rows=20))


def get_ticker_major_holders(symbol: str) -> dict[str, Any]:
    """
    Returns the major holders breakdown for a ticker.

    Includes percentage held by insiders, institutions, and float.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Major holder statistics.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).major_holders))


def get_ticker_institutional_holders(symbol: str) -> dict[str, Any]:
    """
    Returns the top institutional holders for a ticker.

    GUARDRAIL: Limited to the top 15 institutional holders.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Institutional holder names, shares held, and percentage.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).institutional_holders, max_rows=15))


def get_ticker_mutual_fund_holders(symbol: str) -> dict[str, Any]:
    """
    Returns the top mutual fund holders for a ticker.

    GUARDRAIL: Limited to the top 15 mutual fund holders.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        Mutual fund holder names, shares held, and percentage.
    """
    return _safe(lambda: _df_to_dict(yf.Ticker(symbol.upper()).mutualfund_holders, max_rows=15))


def get_ticker_options_dates(symbol: str) -> dict[str, Any]:
    """
    Returns the available options expiration dates for a ticker.

    Use this before calling get_ticker_option_chain() to find a valid date.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        List of available expiration date strings.
    """
    def _fetch():
        dates = yf.Ticker(symbol.upper()).options
        return {"expiration_dates": list(dates)}

    return _safe(_fetch)


def get_ticker_option_chain(symbol: str, expiration_date: str) -> dict[str, Any]:
    """
    Returns the options chain (calls and puts) for a specific expiration date.

    GUARDRAIL: Returns a summary of the first 25 rows for both calls and puts
            to avoid enormous response payloads.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.
    expiration_date : str
        Expiration date string (e.g. "2025-06-20"). Use get_ticker_options_dates()
        to retrieve valid dates.

    Returns
    -------
    dict
        Dictionary with "calls" and "puts" keys, each a truncated table.
    """
    def _fetch():
        chain = yf.Ticker(symbol.upper()).option_chain(expiration_date)
        return {
            "calls": _df_to_dict(chain.calls, max_rows=25),
            "puts": _df_to_dict(chain.puts, max_rows=25),
        }

    return _safe(_fetch)


def get_ticker_news(symbol: str) -> dict[str, Any]:
    """
    Returns the latest news articles related to a ticker.

    GUARDRAIL: Limited to the 10 most recent articles.

    Parameters
    ----------
    symbol : str
        Yahoo Finance ticker symbol.

    Returns
    -------
    dict
        List of news articles with title, publisher, link, and publish time.
    """
    _ALLOWED_NEWS_FIELDS = {"title", "publisher", "link", "providerPublishTime", "type"}

    def _fetch():
        raw_news = yf.Ticker(symbol.upper()).news or []
        articles = []
        for article in raw_news[:10]:
            articles.append({k: v for k, v in article.items() if k in _ALLOWED_NEWS_FIELDS})
        return {"articles": articles}

    return _safe(_fetch)


# ---------------------------------------------------------------------------
# Search & Lookup
# ---------------------------------------------------------------------------


def search_ticker(query: str) -> dict[str, Any]:
    """
    Searches Yahoo Finance for tickers or companies matching a query string.

    Use this when the user provides a company name instead of a ticker symbol,
    or when you need to resolve an ambiguous name to a specific symbol.

    GUARDRAIL: Returns at most 8 matching quotes.

    Parameters
    ----------
    query : str
        Search term – company name, ticker symbol, or keyword.

    Returns
    -------
    dict
        List of matching quotes with symbol, name, exchange, and type.
    """
    _ALLOWED_QUOTE_FIELDS = {"symbol", "shortname", "longname", "exchange", "quoteType", "score"}

    def _fetch():
        results = yf.Search(query, max_results=8).quotes
        cleaned = []
        for q in results[:8]:
            cleaned.append({k: v for k, v in q.items() if k in _ALLOWED_QUOTE_FIELDS})
        return {"results": cleaned}

    return _safe(_fetch)


# ---------------------------------------------------------------------------
# Market summary
# ---------------------------------------------------------------------------


def get_market_status(market: str) -> dict[str, Any]:
    """
    Returns the current open/closed status of a financial market.

    Parameters
    ----------
    market : str
        Market identifier. Must be one of:
        US, GB, ASIA, EUROPE, RATES, COMMODITIES, CURRENCIES, CRYPTOCURRENCIES

    Returns
    -------
    dict
        Market status information (open/closed, timezone, etc.).
    """
    market = market.upper()
    if market not in _VALID_MARKETS:
        return {
            "error": (
                f"Market '{market}' is not valid. "
                f"Choose from: {sorted(_VALID_MARKETS)}"
            )
        }

    def _fetch():
        status = yf.Market(market).status
        return json.loads(json.dumps(status, default=str)) if status else {}

    return _safe(_fetch)


def get_market_summary(market: str) -> dict[str, Any]:
    """
    Returns a summary of major indices and assets in a financial market.

    Parameters
    ----------
    market : str
        Market identifier. Must be one of:
        US, GB, ASIA, EUROPE, RATES, COMMODITIES, CURRENCIES, CRYPTOCURRENCIES

    Returns
    -------
    dict
        Summary of market symbols, prices, and movements.
    """
    market = market.upper()
    if market not in _VALID_MARKETS:
        return {
            "error": (
                f"Market '{market}' is not valid. "
                f"Choose from: {sorted(_VALID_MARKETS)}"
            )
        }

    def _fetch():
        summary = yf.Market(market).summary
        return json.loads(json.dumps(summary, default=str)) if summary else {}

    return _safe(_fetch)


# ---------------------------------------------------------------------------
# Sector & Industry
# ---------------------------------------------------------------------------


def get_sector_overview(sector_key: str) -> dict[str, Any]:
    """
    Returns a high-level overview of a market sector.

    Example sector keys: technology, healthcare, financial-services,
    consumer-cyclical, energy, utilities, industrials, real-estate,
    basic-materials, communication-services, consumer-defensive.

    Parameters
    ----------
    sector_key : str
        Sector identifier slug (e.g. "technology").

    Returns
    -------
    dict
        Overview metrics for the sector.
    """
    def _fetch():
        overview = yf.Sector(sector_key).overview
        return json.loads(json.dumps(overview, default=str)) if overview else {}

    return _safe(_fetch)


def get_sector_top_companies(sector_key: str) -> dict[str, Any]:
    """
    Returns the top companies (by market cap) within a market sector.

    Parameters
    ----------
    sector_key : str
        Sector identifier slug (e.g. "technology").

    Returns
    -------
    dict
        Top companies with symbol, name, and key metrics.
    """
    return _safe(lambda: _df_to_dict(yf.Sector(sector_key).top_companies))


def get_sector_top_etfs(sector_key: str) -> dict[str, Any]:
    """
    Returns the top ETFs for a given sector.

    Parameters
    ----------
    sector_key : str
        Sector identifier slug (e.g. "technology").

    Returns
    -------
    dict
        Dictionary of ETF symbols and names.
    """
    def _fetch():
        return yf.Sector(sector_key).top_etfs or {}

    return _safe(_fetch)


def get_industry_overview(industry_key: str) -> dict[str, Any]:
    """
    Returns a high-level overview of a specific industry within a sector.

    Example industry keys: semiconductors, software-application,
    drug-manufacturers-general, banks-diversified, oil-gas-integrated.

    Parameters
    ----------
    industry_key : str
        Industry identifier slug (e.g. "semiconductors").

    Returns
    -------
    dict
        Overview metrics for the industry.
    """
    def _fetch():
        overview = yf.Industry(industry_key).overview
        return json.loads(json.dumps(overview, default=str)) if overview else {}

    return _safe(_fetch)


def get_industry_top_companies(industry_key: str) -> dict[str, Any]:
    """
    Returns the top companies (by market cap) within a specific industry.

    Parameters
    ----------
    industry_key : str
        Industry identifier slug (e.g. "semiconductors").

    Returns
    -------
    dict
        Top companies with symbol, name, and key metrics.
    """
    return _safe(lambda: _df_to_dict(yf.Industry(industry_key).top_companies))


def get_industry_top_growth_companies(industry_key: str) -> dict[str, Any]:
    """
    Returns the top growth companies within a specific industry.

    Parameters
    ----------
    industry_key : str
        Industry identifier slug (e.g. "semiconductors").

    Returns
    -------
    dict
        Top growth companies with symbol, name, and key metrics.
    """
    return _safe(lambda: _df_to_dict(yf.Industry(industry_key).top_growth_companies))


# ---------------------------------------------------------------------------
# Screener
# ---------------------------------------------------------------------------


def screen_equities(
    region: str = "us",
    sector_key: str | None = None,
    min_market_cap: float | None = None,
    max_results: int = 20,
) -> dict[str, Any]:
    """
    Screens and filters publicly traded equities using Yahoo Finance's screener.

    GUARDRAIL: Results are capped at 25 even if max_results is set higher.

    Parameters
    ----------
    region : str
        Market region to filter by (e.g. "us", "gb", "hk"). Defaults to "us".
    sector_key : str, optional
        Sector slug to narrow results (e.g. "technology", "healthcare").
    min_market_cap : float, optional
        Minimum market capitalisation in USD (e.g. 1_000_000_000 for $1B).
    max_results : int
        Number of results to return. Capped at 25.

    Returns
    -------
    dict
        List of equities matching the criteria.
    """
    max_results = min(max_results, 25)

    def _fetch():
        filters = [yf.EquityQuery("eq", ["region", region.lower()])]

        if sector_key:
            filters.append(yf.EquityQuery("eq", ["sector", sector_key]))

        if min_market_cap is not None:
            filters.append(yf.EquityQuery("gt", ["intradaymarketcap", min_market_cap]))

        if len(filters) == 1:
            query = filters[0]
        else:
            query = yf.EquityQuery("and", filters)

        result = yf.screen(query, size=max_results)
        quotes = result.get("quotes", [])

        # Return only a curated subset of fields per quote
        _SCREENER_FIELDS = {
            "symbol", "shortName", "sector", "industry",
            "marketCap", "currentPrice", "trailingPE",
            "regularMarketChangePercent", "currency",
        }
        return {
            "count": len(quotes),
            "results": [
                {k: v for k, v in q.items() if k in _SCREENER_FIELDS}
                for q in quotes
            ],
        }

    return _safe(_fetch)