# Python standard libs
import os

# Local MCP imports
from ..mcp_instance import mcp

# Base path for the knowledge repo (copied into the image via Dockerfile)
KNOWLEDGE_REPO_PATH = "/app/app-knowledge-repo"

@mcp.tool(annotations={"title": "Get a list of customers from the folders", "readOnlyHint": True, "openWorldHint": False})
def get_customers_list() -> str:
    """
    Get a list of customers from the folders.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/customers"

    # List all folder names (only the folders, not the files)
    customers = [f for f in os.listdir(full_path) if os.path.isdir(f"{full_path}/{f}")]

    # Transform into a string with commas
    customers_str = ", ".join(customers)

    # Return the string
    return customers_str


@mcp.tool(annotations={"title": "Get the customer profile from the repository", "readOnlyHint": True, "openWorldHint": False})
def get_customer_profile(customer_name: str) -> str:
    """
    Get the customer profile from the repository.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/customers"

    # Load the profile.md inside the customer folder
    customer_file = f"{full_path}/{customer_name}/README.md"

    # Read the markdown file
    with open(customer_file, "r") as f:
        customer_info = f.read()

    # Return the string
    return customer_info


@mcp.tool(annotations={"title": "Update the info inside the profile of a customer", "readOnlyHint": True, "openWorldHint": False})
def set_customer_profile(customer_name: str, markdown_content: str) -> str:
    """
    Update the info inside the profile of a customer.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/customers"

    # Overwrite the README.md inside the customer folder
    with open(f"{full_path}/{customer_name}/README.md", "w") as f:
        f.write(markdown_content)

    # Return the string
    return f"Customer profile for {customer_name} updated successfully."


@mcp.tool(annotations={"title": "Get a list of projects from the folders", "readOnlyHint": True, "openWorldHint": False})
def get_projects_list() -> str:
    """
    Get a list of projects from the folders.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/projects"

    # List all folder names (projects are folders, not files)
    projects = [f for f in os.listdir(full_path) if os.path.isdir(f"{full_path}/{f}")]

    # Transform into a string with commas
    projects_str = ", ".join(projects)

    # Return the string
    return projects_str


@mcp.tool(annotations={"title": "Get the project inf card from the repository", "readOnlyHint": True, "openWorldHint": False})
def get_project_info(project_name: str) -> str:
    """
    Get the project inf card from the repository.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/projects/{project_name}/README.md"

    # Read the markdown file
    with open(full_path, "r") as f:
        project_info = f.read()

    # Return the string
    return project_info


@mcp.tool(annotations={"title": "Get the project details from the repository", "readOnlyHint": True, "openWorldHint": False})
def get_project_details(project_name: str) -> str:
    """
    Get the project details from the repository.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/projects/{project_name}/project-details/"

    # List all markdown files in the customers folder
    projects = [f for f in os.listdir(full_path) if f.endswith(".md")]

    # Transform into a string with commas
    projects_str = ", ".join(projects)

    # Return the string
    return projects_str


@mcp.tool(annotations={"title": "Get the a specific document from the detail scope of a project from the repository", "readOnlyHint": True, "openWorldHint": False})
def get_project_detail_doc(project_name: str, doc_name: str) -> str:
    """
    Get the project details from the repository.    
    
    Args:
        project_name (str): The name of the project.
        doc_name (str): The name of the document.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/projects/{project_name}/project-details/{doc_name}.md"

    # Read the markdown file
    with open(full_path, "r") as f:
        project_info = f.read()

    # Return the string
    return project_info


@mcp.tool(annotations={"title": "Get the project executive report from the repository", "readOnlyHint": True, "openWorldHint": False})
def get_project_executive_report(project_name: str) -> str:
    """
    Get the project executive report from the repository.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/projects/{project_name}/executive-report.md"

    # Read the markdown file
    with open(full_path, "r") as f:
        project_info = f.read()

    # Return the string
    return project_info


@mcp.tool(annotations={"title": "Get the project progress report from the repository", "readOnlyHint": True, "openWorldHint": False})
def get_project_progress_report(project_name: str) -> str:
    """
    Get the project progress report from the repository.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/projects/{project_name}/project-details/progress-report.md"

    # Read the markdown file
    with open(full_path, "r") as f:
        project_info = f.read()

    # Return the string
    return project_info


@mcp.tool(annotations={"title": "Get the deep dive index of a project from the repository", "readOnlyHint": True, "openWorldHint": False})
def get_project_deep_dive_index(project_name: str) -> str:
    """
    Get the deep dive index of a project from the repository.    
    
    Args:
        project_name (str): The name of the project.
    """

    # Get the full path of customers
    full_path = f"{KNOWLEDGE_REPO_PATH}/projects/{project_name}/project-details/deep-dive/index.md"

    # Read the markdown file
    with open(full_path, "r") as f:
        project_info = f.read()

    # Return the string
    return project_info
















