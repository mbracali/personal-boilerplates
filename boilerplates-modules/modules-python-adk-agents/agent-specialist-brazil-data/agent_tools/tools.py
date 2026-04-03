import requests

BASE_URL = "https://brasilapi.com.br/api"

def _get_request(endpoint: str):
    """Internal helper to perform GET requests to BrasilAPI."""
    try:
        response = requests.get(f"{BASE_URL}{endpoint}", timeout=15)
        if response.status_code == 404:
            return {"error": "Resource not found (404)."}
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": f"API Request failed: {str(e)}"}

# --- BANKS ---
def get_banks():
    """
    USE THIS when the user mentions a specific bank number or code.
    Retrieves info for a specific bank using its numeric code (e.g., 341 for Itaú).
    Prefer this over get_banks() whenever a code is known.
    """
    return _get_request("/banks/v1")

def get_bank_by_code(code: int):
    """Retrieves info for a specific bank using its code (e.g., 1)."""
    return _get_request(f"/banks/v1/{code}")

# --- EXCHANGE RATES (CAMBIO) ---
def get_available_currencies():
    """Lists all currencies available for exchange rate queries."""
    return _get_request("/cambio/v1/moedas")

def get_exchange_rate(currency_code: str, date: str):
    """Retrieves BRL exchange rate for a currency on a specific date (YYYY-MM-DD)."""
    return _get_request(f"/cambio/v1/cotacao/{currency_code}/{date}")

# --- POSTAL CODE (CEP) ---
def get_cep_v1(cep: str):
    """Searches address data based on an 8-digit CEP (v1)."""
    return _get_request(f"/cep/v1/{cep}")

def get_cep_v2(cep: str):
    """Searches address data based on an 8-digit CEP including geolocation (v2)."""
    return _get_request(f"/cep/v2/{cep}")

# --- COMPANY DATA (CNPJ) ---
def get_cnpj_info(cnpj: str):
    """Retrieves corporate information for a given 14-digit CNPJ."""
    return _get_request(f"/cnpj/v1/{cnpj}")

# --- BROKERAGE FIRMS (CORRETORAS) ---
def get_all_brokers():
    """Returns all brokerage firms listed in CVM files."""
    return _get_request("/cvm/corretoras/v1")

def get_broker_by_cnpj(cnpj: str):
    """Retrieves a specific brokerage firm's data via CNPJ."""
    return _get_request(f"/cvm/corretoras/v1/{cnpj}")

# --- WEATHER & OCEAN (CPTEC) ---
def get_cptec_cities():
    """Returns a list of all cities in the CPTEC database."""
    return _get_request("/cptec/v1/cidade")

def search_cptec_city(city_name: str):
    """Searches for cities by name to retrieve their CPTEC ID."""
    return _get_request(f"/cptec/v1/cidade/{city_name}")

def get_capital_weather():
    """Retrieves current weather conditions for all Brazilian state capitals."""
    return _get_request("/cptec/v1/clima/capital")

def get_airport_weather(icao_code: str):
    """Retrieves current conditions at an airport via ICAO code (e.g., 'SBGR')."""
    return _get_request(f"/cptec/v1/clima/aeroporto/{icao_code}")

def get_city_forecast(city_id: int):
    """Retrieves a 24-hour weather forecast for a specific city ID."""
    return _get_request(f"/cptec/v1/clima/previsao/{city_id}")

def get_ocean_forecast(city_id: int):
    """Retrieves oceanic (wave) forecasts for a coastal city ID."""
    return _get_request(f"/cptec/v1/ondas/{city_id}")

# --- AREA CODES (DDD) ---
def get_ddd_info(ddd: str):
    """Retrieves the state and cities corresponding to a 2-digit area code."""
    return _get_request(f"/ddd/v1/{ddd}")

# --- NATIONAL HOLIDAYS ---
def get_holidays(year: int):
    """Lists all Brazilian national holidays for a specific year."""
    return _get_request(f"/feriados/v1/{year}")

# --- VEHICLE PRICES (FIPE) ---
def get_fipe_brands(vehicle_type: str):
    """Lists brands for 'carros', 'motos', or 'caminhoes'."""
    return _get_request(f"/fipe/marcas/v1/{vehicle_type}")

def get_fipe_price(fipe_code: str):
    """Retrieves a vehicle's average price based on its FIPE code."""
    return _get_request(f"/fipe/preco/v1/{fipe_code}")

def get_fipe_reference_tables():
    """Lists available reference tables for historical FIPE prices."""
    return _get_request("/fipe/tabelas/v1")

# --- GEOGRAPHIC DATA (IBGE) ---
def get_ibge_municipalities(state_sigla: str):
    """Retrieves all municipalities within a state (e.g., 'SP')."""
    return _get_request(f"/ibge/municipios/v1/{state_sigla}")

def get_all_states():
    """Retrieves information for all Brazilian states."""
    return _get_request("/ibge/uf/v1")

def get_state_info(state_id: str):
    """Retrieves info for a state via abbreviation (SP) or IBGE code (35)."""
    return _get_request(f"/ibge/uf/v1/{state_id}")

# --- BOOK DATA (ISBN) ---
def get_book_by_isbn(isbn: str):
    """Retrieves book metadata from an ISBN-10 or ISBN-13 code."""
    return _get_request(f"/isbn/v1/{isbn}")

# --- CUSTOMS NOMENCLATURE (NCM) ---
def get_all_ncms():
    """Returns a list of all Mercosul Common Nomenclature (NCM) codes."""
    return _get_request("/ncm/v1")

def search_ncm(query: str):
    """Searches for NCM codes by code or description."""
    return _get_request(f"/ncm/v1?search={query}")

def get_ncm_by_code(code: str):
    """Retrieves detailed info for a specific NCM code."""
    return _get_request(f"/ncm/v1/{code}")

# --- PIX PARTICIPANTS ---
def get_pix_participants():
    """Returns a list of all institutions participating in the PIX network."""
    return _get_request("/pix/v1/participants")

# --- DOMAIN STATUS (REGISTRO.BR) ---
def check_domain_status(domain: str):
    """Checks availability and status of a '.br' domain."""
    return _get_request(f"/registrobr/v1/{domain}")

# --- FINANCIAL RATES (TAXAS) ---
def get_financial_indicators():
    """Retrieves key Brazilian financial indicators (SELIC, CDI, IPCA)."""
    return _get_request("/taxas/v1")

def get_indicator_by_name(name: str):
    """Retrieves a specific indicator (e.g., 'SELIC') by name."""
    return _get_request(f"/taxas/v1/{name}")