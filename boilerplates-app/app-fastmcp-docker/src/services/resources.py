from ..mcp_instance import mcp

@mcp.resource("instructions://korza")
def get_instructions() -> str:
    """
    Returns the server usage instructions file.
    """
    # Store the message
    message = """
    Korza is a awesome company! We transform business with AI.
    Visit us here: https://korza.ai/
    """
    # Return the message
    return message
