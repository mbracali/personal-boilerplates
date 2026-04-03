# 📦 Personal boilerplates

A curated collection of **starter templates** for Python services, data work, and AI tooling. Everything here is organized by *what you are building*—applications, containers, analysis, MCP servers, or shared libraries—so you can copy a slice and move fast without hunting through unrelated projects.

---

## 👀 At a glance

| Emoji | Folder | Role |
|:---:|:--------|:------|
| 🚀 | [`boilerplates-app`](#boilerplates-app) | End-to-end app skeletons (APIs, MCP apps, docs, ML playbooks) |
| 🐳 | [`boilerplates-docker`](#boilerplates-docker) | Docker-first stacks built around **`uv`** and common web / UI patterns |
| 📊 | [`boilerplates-eda`](#boilerplates-eda) | Exploratory data analysis workflows and folder conventions |
| 🔌 | [`boilerplates-mcp`](#boilerplates-mcp) | **Model Context Protocol** servers and related experiments |
| 🧩 | [`boilerplates-modules`](#boilerplates-modules) | Reusable Python packages and **ADK-style** agent definitions |

---

## 🚀 `boilerplates-app`

**Full application templates**—not just a single file, but a runnable layout you can grow into a product or client deliverable.

Typical themes under this tree:

- **HTTP & containers** — FastAPI (and related) apps packaged with Docker/Podman, sometimes paired with Streamlit or other UIs.
- **MCP-oriented apps** — FastMCP servers with compose-friendly defaults (e.g. SSE endpoints).
- **Knowledge & documentation** — Repository-style layouts for customers, projects, and long-lived notes.
- **ML / analytics playbooks** — Streamlit-oriented structure plus EDA-style staged folders (instructions → data → research → plans → presentation → notes).
- **General-purpose Python** — Opinionated folders for `app/`, config YAMLs, notebooks, scripts, and assets—good when the stack is still flexible.

Use this folder when you want a **named project** you can open in an IDE and run end to end.

---

## 🐳 `boilerplates-docker`

**Container-centric** recipes where **Docker (or Podman)** and the **`uv`** toolchain are the main story. These are slimmer than full “apps”: they emphasize image layout, `Makefile` or compose flows, and a consistent `src/` style across variants.

You will find spins for things like **FastAPI**, **FastMCP**, **HTMX**, **Streamlit**, and **ADK**-related images—handy when you are standardizing how services are built and shipped, independent of business logic.

---

## 📊 `boilerplates-eda`

**Exploratory data analysis** scaffolding: numbered or staged directories that walk from raw intent through delivery (e.g. instructions, datasources, research, plans, presentations, notes). The goal is a **repeatable EDA narrative**—especially when collaborating with tools or teammates—without mixing concerns in one flat folder.

Today this area is intentionally small; it is the home for EDA-oriented trees such as automation-friendly **`eda-*`** layouts.

---

## 🔌 `boilerplates-mcp`

**Model Context Protocol** projects: Python servers (often **FastMCP**), tooling around **Markdown vaults** or APIs, and sibling templates aimed at **evaluation** or side-by-side experiments. These repos usually ship with Docker/Podman support and clear environment wiring (e.g. mounted repos, SSE ports).

Reach here when the deliverable is **an MCP server** or a sandbox to **test and compare** MCP behavior—not a generic REST app alone.

---

## 🧩 `boilerplates-modules`

**Libraries and building blocks**, not deployable services by themselves.

- **`modules-python`** — Shared packages (named around internal conventions such as Hermes, Pythia, Themis) meant to be imported by apps or other modules.
- **`modules-python-adk-agents`** — **Agent Development Kit**–style agents: role-specific definitions (engineering lanes, project roles, domain specialists) with configs and instructions suitable for orchestration or tooling.

Use this folder when you are extracting **reusable code** or **agent personas** that multiple boilerplates or products should share.

---

## ⚙️ Conventions

- **Naming** — Folders are prefixed (`app-`, `docker-uv-`, `mcp-`, `modules-`, …) so you can grep the repo and see the family at a glance.
- **Python & tooling** — Modern Python (3.12+ in many places), **`uv`** in Docker-oriented trees, and **FastAPI / FastMCP** where the stack is web or MCP-facing.

---

*📝 This README describes **top-level** areas only; each subfolder may carry its own README for specifics.*
