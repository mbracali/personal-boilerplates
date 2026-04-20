# EDA auto-claude — boilerplate guide

This folder is a **ready-made layout** for an **exploratory data analysis (EDA)** engagement. It is meant to be **copied** into a new project, then filled by you (and optionally driven by an AI assistant using the rules in `CLAUDE.md`).

---

## What you get

- **Numbered stages** (`00` … `06`, plus `99`) so context, data, comms, plans, research, deliverables, and ops notes stay separated.
- **Starter markdown files** with placeholders for instructions, stakeholder inputs, plans, and agent-facing logs.
- **`CLAUDE.md`** — the operational playbook for an assistant: role, analytical principles, step-by-step workflow, folder rules, and **HTML presentation** requirements (Catppuccin, single-file, sidebar structure).

The design assumes work moves from **instructions & data** → **plan** → **research/code** → **presentation**, with **progress and change tracking** in `06_eda_agent_notes/`.

---

## Quick start

1. **Copy** this entire `eda-auto-claude` directory to your project location (rename the root folder if you like, e.g. `customer-name-eda-2026`).
2. **Fill** `00_eda_instructions/`:
   - `EDA - Customer profile.md` — who the customer is and relevant context.
   - `EDA - Instructions.md` — your goals, constraints, and how you want the analysis run.
3. **Add inputs** under `01_eda_datasources/` (CSVs, Excel, PDFs, exports, etc.).
4. **Capture conversations** in `02_eda_interactions/` (emails, meetings, Slack-style notes) so decisions stay traceable.
5. **Write or iterate plans** in `03_eda_plans/` — start from `EDA - Plan V0.md`; for new versions, add files such as `EDA - Plan V1.md` and use `99_eda_file_layouts/EDA LAYOUT - Plan V99.md` as a **template** for structure and checklists.
6. **Put notebooks and scripts** in `04_eda_resarch/` (see note on the folder name below).
7. **Place the final deliverable** (e.g. the self-contained HTML dashboard) in `05_eda_presentation/`.
8. **Keep `06_eda_agent_notes/` updated** when you use an agent or team process: attention points, changelog, and progress per EDA version.

If you use an AI assistant, point it at **`CLAUDE.md`** so it follows the same workflow and presentation rules.

---

## Folder map

Top-level **folder names are fixed** in this boilerplate: do **not** add or remove numbered directories; only add **files inside** them (as described in `CLAUDE.md`).

| Stage | Folder | Purpose |
|:-----:|--------|---------|
| 00 | `00_eda_instructions/` | Customer profile and **your** instructions for the analysis. |
| 01 | `01_eda_datasources/` | Raw and processed inputs (many file types). |
| 02 | `02_eda_interactions/` | Emails, meeting notes, and informal text about the project. |
| 03 | `03_eda_plans/` | Versioned plans (`EDA - Plan V0.md`, `V1`, …) aligned with the presentation version. |
| 04 | `04_eda_resarch/` | Notebooks, Python, and other **technical** work for the EDA. |
| 05 | `05_eda_presentation/` | Final outputs — typically the **single-file HTML** presentation. |
| 06 | `06_eda_agent_notes/` | Operational logs: attention points, changelog, progress. |
| 99 | `99_eda_file_layouts/` | **Templates** (e.g. plan layout) to copy when creating new files. |

**Note:** The research stage folder is named `04_eda_resarch/` in this repo (typo vs “research”). Treat it as the **research & implementation** area; renaming would require updating any tooling or docs that reference the path.

---

## Files you will touch most often

| File | Role |
|------|------|
| `CLAUDE.md` | Assistant playbook: workflow, folder contract, and HTML presentation spec. |
| `00_eda_instructions/EDA - Customer profile.md` | Customer context. |
| `00_eda_instructions/EDA - Instructions.md` | Your priorities and rules for the engagement. |
| `02_eda_interactions/*.md` | Stakeholder and meeting trail. |
| `03_eda_plans/EDA - Plan V0.md` | First formal plan; duplicate the pattern for V1, V2, … |
| `99_eda_file_layouts/EDA LAYOUT - Plan V99.md` | Template for new plan documents (sections + checklist). |
| `06_eda_agent_notes/EDA - Attention points.md` | Risks, issues, and items that need visibility. |
| `06_eda_agent_notes/EDA - Changelog.md` | What changed between EDA versions. |
| `06_eda_agent_notes/EDA - Progress.md` | Status of work per version (intended as a progress log). |

Early in a project, many of these may be empty or placeholder-only; that is expected.

---

## Workflow (summary)

This mirrors the flow documented in `CLAUDE.md`:

1. **Kickoff** — Review instructions, customer profile, datasources, and interactions; draft **Plan V0**; note initial risks in **Attention points**; clarify business goals.
2. **Iterate** — Either refine strategy and plans (**reasoning**) or execute analysis with code (**building**), updating **Progress** and **Changelog** as versions evolve.
3. **Versioning** — When the EDA moves to a new version, add a **new plan file**, update the **changelog**, and keep attention points tied to the right **EDA version**.

For **presentation output**, follow the **EDA Presentation** section in `CLAUDE.md`: one self-contained HTML file, Catppuccin **light** theme, fixed header with **customer name and EDA version**, responsive layout, and the sidebar sections described there.

---

## Tips

- **Precision:** Prefer scripts (e.g. Python) for non-trivial calculations rather than manual arithmetic.
- **Traceability:** Link conclusions to data sources and plan versions when possible.
- **Executive clarity:** Lead with conclusions and “so what” actions; details can follow (see `CLAUDE.md` for Pyramid Principle and “So What?”).

---

*For the full agent instructions and HTML design checklist, open **`CLAUDE.md`** in this directory.*
