"""
Tech Lead agent.

The most senior technical voice on the team.
Owns architectural decisions, enforces code quality, and unblocks the technical team.
"""

import os
import tomllib

from google.adk.agents.llm_agent import Agent

from ...agent_tools.tools import read_markdown, write_markdown, list_bucket_structure, create_customer, create_project, list_customers, list_projects, search_bucket

from ..project_tech_analyst_backend.agent import project_tech_analyst_backend
from ..project_tech_analyst_frontend.agent import project_tech_analyst_frontend
from ..project_tech_analyst_data_eng.agent import project_tech_analyst_data_eng
from ..project_tech_analyst_data_science.agent import project_tech_analyst_data_science
from ..project_tech_analyst_infrastructure.agent import project_tech_analyst_infrastructure

base_dir = os.path.dirname(os.path.abspath(__file__))

with open(f"{base_dir}/agent_docs/config.toml", "rb") as f:
    config = tomllib.load(f)

with open(f"{base_dir}/agent_docs/description.md", "r") as f:
    agent_description = f.read()

with open(f"{base_dir}/agent_docs/instructions.md", "r") as f:
    agent_instructions = f.read()

project_tech_lead = Agent(
    model=config['agent']['model_name'],
    name=config['agent']['agent_name'],
    description=agent_description,
    instruction=agent_instructions,
    tools=[read_markdown, write_markdown, list_bucket_structure, create_customer, create_project, list_customers, list_projects, search_bucket],
    sub_agents=[
        project_tech_analyst_backend,
        project_tech_analyst_frontend,
        project_tech_analyst_data_eng,
        project_tech_analyst_data_science,
        project_tech_analyst_infrastructure,
    ],
)
