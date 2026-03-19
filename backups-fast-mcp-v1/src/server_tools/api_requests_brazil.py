# Import the custom mcp service layer
from src.modules import service as mcp_svc

# Import the requests library
import requests

# Get the mcp object
mcp = mcp_svc.mcp

# Private method that request data to the API
def _get_request(endpoint: str):
    """
    Internal helper to perform GET requests to BrasilAPI.
    """
    
    # Try to get answer from the API
    try:
        response = requests.get(f"https://brasilapi.com.br/api{endpoint}", timeout=15)

        # Return a error if the request fails
        if response.status_code == 404:
            return {"error": "Resource not found (404)."}
        
        # Return the json of the request
        response.raise_for_status()
        return response.json()
    
    # Raise and return exception during the request
    except requests.exceptions.RequestException as e:
        return {"error": f"API Request failed: {str(e)}"}

# --- BANKS INFO ---

@mcp.tool(
    annotations={
        "title": "Get many informations about all banks in Brazil", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_banks():
    """
    Return a list of banks in Brazil with a bunch of informations about
    them.
    """
    return _get_request("/banks/v1")

@mcp.tool(
    annotations={
        "title": "Retrieves info for a specific bank using its code", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_bank_by_code(code: int):
    """Retrieves info for a specific bank using its code (e.g., 1)."""
    return _get_request(f"/banks/v1/{code}")

# --- EXCHANGE RATES (CAMBIO) ---
@mcp.tool(
    annotations={
        "title": "Lists all currencies available for exchange rate queries", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_available_currencies():
    """Lists all currencies available for exchange rate queries."""
    return _get_request("/cambio/v1/moedas")

@mcp.tool(
    annotations={
        "title": "Retrieves BRL exchange rate for a currency", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_exchange_rate(currency_code: str, date: str):
    """Retrieves BRL exchange rate for a currency on a specific date (YYYY-MM-DD)."""
    return _get_request(f"/cambio/v1/cotacao/{currency_code}/{date}")

# --- POSTAL CODE (CEP) ---
@mcp.tool(
    annotations={
        "title": "Searches address data based on an 8-digit CEP (v1)", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_cep_v1(cep: str):
    """Searches address data based on an 8-digit CEP (v1)."""
    return _get_request(f"/cep/v1/{cep}")

@mcp.tool(
    annotations={
        "title": "Searches address data based on an 8-digit CEP (v2)", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_cep_v2(cep: str):
    """Searches address data based on an 8-digit CEP including geolocation (v2)."""
    return _get_request(f"/cep/v2/{cep}")

# --- COMPANY DATA (CNPJ) ---
@mcp.tool(
    annotations={
        "title": "Retrieves corporate information for a given CNPJ", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_cnpj_info(cnpj: str):
    """Retrieves corporate information for a given 14-digit CNPJ."""
    return _get_request(f"/cnpj/v1/{cnpj}")

# --- BROKERAGE FIRMS (CORRETORAS) ---
@mcp.tool(
    annotations={
        "title": "Returns all brokerage firms listed in CVM files", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_all_brokers():
    """Returns all brokerage firms listed in CVM files."""
    return _get_request("/cvm/corretoras/v1")

@mcp.tool(
    annotations={
        "title": "Retrieves a specific brokerage firm's data via CNPJ", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_broker_by_cnpj(cnpj: str):
    """Retrieves a specific brokerage firm's data via CNPJ."""
    return _get_request(f"/cvm/corretoras/v1/{cnpj}")

# --- WEATHER & OCEAN (CPTEC) ---
@mcp.tool(
    annotations={
        "title": "Returns a list of all cities in the CPTEC database", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_cptec_cities():
    """Returns a list of all cities in the CPTEC database."""
    return _get_request("/cptec/v1/cidade")

@mcp.tool(
    annotations={
        "title": "Searches for cities by name to retrieve their CPTEC ID", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def search_cptec_city(city_name: str):
    """Searches for cities by name to retrieve their CPTEC ID."""
    return _get_request(f"/cptec/v1/cidade/{city_name}")

@mcp.tool(
    annotations={
        "title": "Retrieves weather conditions for all state capitals", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_capital_weather():
    """Retrieves current weather conditions for all Brazilian state capitals."""
    return _get_request("/cptec/v1/clima/capital")

@mcp.tool(
    annotations={
        "title": "Retrieves current conditions at an airport via ICAO code", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_airport_weather(icao_code: str):
    """Retrieves current conditions at an airport via ICAO code (e.g., 'SBGR')."""
    return _get_request(f"/cptec/v1/clima/aeroporto/{icao_code}")

@mcp.tool(
    annotations={
        "title": "Retrieves a 24-hour weather forecast for a specific city ID", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_city_forecast(city_id: int):
    """Retrieves a 24-hour weather forecast for a specific city ID."""
    return _get_request(f"/cptec/v1/clima/previsao/{city_id}")

@mcp.tool(
    annotations={
        "title": "Retrieves oceanic forecasts for a coastal city ID", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_ocean_forecast(city_id: int):
    """Retrieves oceanic (wave) forecasts for a coastal city ID."""
    return _get_request(f"/cptec/v1/ondas/{city_id}")

# --- AREA CODES (DDD) ---
@mcp.tool(
    annotations={
        "title": "Retrieves the state and cities for a 2-digit area code", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_ddd_info(ddd: str):
    """Retrieves the state and cities corresponding to a 2-digit area code."""
    return _get_request(f"/ddd/v1/{ddd}")

# --- NATIONAL HOLIDAYS ---
@mcp.tool(
    annotations={
        "title": "Lists all Brazilian national holidays for a specific year", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_holidays(year: int):
    """Lists all Brazilian national holidays for a specific year."""
    return _get_request(f"/feriados/v1/{year}")

# --- VEHICLE PRICES (FIPE) ---
@mcp.tool(
    annotations={
        "title": "Lists vehicle brands in FIPE table", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_fipe_brands(vehicle_type: str):
    """Lists brands for 'carros', 'motos', or 'caminhoes'."""
    return _get_request(f"/fipe/marcas/v1/{vehicle_type}")

@mcp.tool(
    annotations={
        "title": "Retrieves a vehicle's average price based on FIPE code", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_fipe_price(fipe_code: str):
    """Retrieves a vehicle's average price based on its FIPE code."""
    return _get_request(f"/fipe/preco/v1/{fipe_code}")

@mcp.tool(
    annotations={
        "title": "Lists available reference tables for historical FIPE prices", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_fipe_reference_tables():
    """Lists available reference tables for historical FIPE prices."""
    return _get_request("/fipe/tabelas/v1")

# --- GEOGRAPHIC DATA (IBGE) ---
@mcp.tool(
    annotations={
        "title": "Retrieves all municipalities within a state", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_ibge_municipalities(state_sigla: str):
    """Retrieves all municipalities within a state (e.g., 'SP')."""
    return _get_request(f"/ibge/municipios/v1/{state_sigla}")

@mcp.tool(
    annotations={
        "title": "Retrieves information for all Brazilian states", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_all_states():
    """Retrieves information for all Brazilian states."""
    return _get_request("/ibge/uf/v1")

@mcp.tool(
    annotations={
        "title": "Retrieves info for a state via abbreviation or IBGE code", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_state_info(state_id: str):
    """Retrieves info for a state via abbreviation (SP) or IBGE code (35)."""
    return _get_request(f"/ibge/uf/v1/{state_id}")

# --- BOOK DATA (ISBN) ---
@mcp.tool(
    annotations={
        "title": "Retrieves book metadata from an ISBN code", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_book_by_isbn(isbn: str):
    """Retrieves book metadata from an ISBN-10 or ISBN-13 code."""
    return _get_request(f"/isbn/v1/{isbn}")

# --- CUSTOMS NOMENCLATURE (NCM) ---
@mcp.tool(
    annotations={
        "title": "Returns a list of all NCM codes", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_all_ncms():
    """Returns a list of all Mercosul Common Nomenclature (NCM) codes."""
    return _get_request("/ncm/v1")

@mcp.tool(
    annotations={
        "title": "Searches for NCM codes by code or description", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def search_ncm(query: str):
    """Searches for NCM codes by code or description."""
    return _get_request(f"/ncm/v1?search={query}")

@mcp.tool(
    annotations={
        "title": "Retrieves detailed info for a specific NCM code", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_ncm_by_code(code: str):
    """Retrieves detailed info for a specific NCM code."""
    return _get_request(f"/ncm/v1/{code}")

# --- PIX PARTICIPANTS ---
@mcp.tool(
    annotations={
        "title": "Returns a list of institutions in the PIX network", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_pix_participants():
    """Returns a list of all institutions participating in the PIX network."""
    return _get_request("/pix/v1/participants")

# --- DOMAIN STATUS (REGISTRO.BR) ---
@mcp.tool(
    annotations={
        "title": "Checks availability and status of a '.br' domain", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def check_domain_status(domain: str):
    """Checks availability and status of a '.br' domain."""
    return _get_request(f"/registrobr/v1/{domain}")

# --- FINANCIAL RATES (TAXAS) ---
@mcp.tool(
    annotations={
        "title": "Retrieves key Brazilian financial indicators", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_financial_indicators():
    """Retrieves key Brazilian financial indicators (SELIC, CDI, IPCA)."""
    return _get_request("/taxas/v1")

@mcp.tool(
    annotations={
        "title": "Retrieves a specific indicator by name", 
        "read_only_hint": True,
        "destructive_hint": False,
        "idempotent_hint": True,
        "open_world_hint": False
        }
    )
def get_indicator_by_name(name: str):
    """Retrieves a specific indicator (e.g., 'SELIC') by name."""
    return _get_request(f"/taxas/v1/{name}")