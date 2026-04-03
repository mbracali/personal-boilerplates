"""
Frontend Analyst agent.

Builds the user-facing layer of the application.
Turns designs into functional, responsive, and accessible interfaces.
"""

import os
import tomllib

from google.adk.agents.llm_agent import Agent

from ...agent_tools.tools import read_markdown, write_markdown, list_bucket_structure, create_customer, create_project, list_customers, list_projects, search_bucket

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{base_dir}/agent_docs/config.toml", "rb") as f:
    config = tomllib.load(f)

with open(f"{base_dir}/agent_docs/description.md", "r") as f:
    agent_description = f.read()

with open(f"{base_dir}/agent_docs/instructions.md", "r") as f:
    agent_instructions = f.read()

project_tech_analyst_frontend = Agent(
    model=config['agent']['model_name'],
    name=config['agent']['agent_name'],
    description=agent_description,
    instruction=agent_instructions,
    tools=[read_markdown, write_markdown, list_bucket_structure, create_customer, create_project, list_customers, list_projects, search_bucket],
    sub_agents=[],
)
