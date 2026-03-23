# Copilot Instructions — Contoso Finance

## What Is Contoso Finance

Contoso Finance is a modern financial services platform that helps mid-size enterprises manage payments, cash flow, and financial operations in one unified experience. It handles everything from day-to-day invoicing to real-time financial insights — replacing the complexity of legacy finance systems with a product that teams actually want to use.

## Architecture — Modular Monolith in a Monorepo

Contoso Finance is built as a **modular monolith**, deployed as a single system but internally structured around clearly separated business domains. The entire platform lives in this monorepo.

This is a deliberate architectural choice. Rather than starting with distributed microservices (and the operational overhead that comes with them), the platform is organized so that each capability area is self-contained, independently evolvable, and ready to be extracted into its own service if and when the business demands it.

### How the system is structured

- **Client layer** — A customer-facing web application that presents a single, cohesive product experience.
- **Server layer** — A unified backend platform that exposes financial capabilities through well-defined interfaces.
- **Domain modules** — Internal business domains such as billing, payments, reporting, and settlements. Each domain owns its logic, data, and boundaries. Domains communicate through explicit contracts, not by reaching into each other's internals.
- **Shared packages** — Cross-cutting concerns like authentication, validation, and common data types that ensure consistency without duplicating effort.

Externally, Contoso Finance behaves as one product. Internally, it is composed of distinct modules that align with how finance teams think and work.

### Why this approach

| Decision | Rationale |
|---|---|
| **Monorepo** | One repository means shared tooling, unified CI, atomic cross-module changes, and a single source of truth. |
| **Modular monolith** | Gives the clarity and scalability benefits of service-oriented design without the deployment and coordination complexity of microservices. |
| **Strong domain boundaries** | Each module can evolve, scale, or be extracted independently — the architecture grows with the business. |
| **Single deployment** | Simplifies operations today while keeping the door open for future decomposition. |

This architecture is designed to move fast now and stay flexible later.

## Expectations for Contributors

### Think in domains

Every change belongs to a domain. Before writing anything, understand which module owns the capability you're working on. Respect boundaries — don't reach across domains to solve a problem that should be solved within one.

### Own your boundaries

If you're building or extending a domain module, you own its contracts, its data, and its behavior. Design interfaces that other modules can depend on without knowing how things work inside yours.

### Keep the monolith modular

The value of this architecture depends on discipline. Shared code should go in shared packages. Domain-specific logic stays in its domain. If something feels like it needs to cut across multiple modules, that's a signal to pause and design the right abstraction — not to take a shortcut.

### Consistency matters

Follow the patterns already established in the codebase. Naming, structure, and conventions exist for a reason — they make the platform predictable for everyone. When in doubt, look at how existing modules are organized and follow the same shape.

### Quality is a default, not a phase

Write code that is clear, tested, and maintainable. This platform is built to last — contributions should reflect that mindset.

## Conventions

### Python tooling — always use `uv`

**All Python package management and script execution in the server (`apps/server/`) MUST use [`uv`](https://docs.astral.sh/uv/).**

- Use `uv pip install` instead of `pip install`.
- Use `uv run` to execute Python tools (`uvicorn`, `pytest`, `ruff`, `alembic`).
- Dependencies are managed via `requirements.txt` and `requirements-dev.txt` — **no `pyproject.toml`** for dependency management.
- Do **not** use raw `pip`, `python -m pip`, or `python -m` commands. Always prefix with `uv`.

```bash
# Install dependencies
uv pip install -r requirements.txt
uv pip install -r requirements-dev.txt

# Run the server
uv run uvicorn contoso_finance.main:app --reload --app-dir src

# Run tests and linting
uv run pytest tests/ -v
uv run ruff check src/ tests/
```

### Skill files

This repo uses **skill files** in `skills/` to define detailed conventions for specific workflows. These are the authoritative references:

- **Diagrams** — `skills/visuals/SKILL.md` defines the Excalidraw-only diagramming workflow, including dark-mode design rules, the export pipeline, naming conventions, and embedding standards. All diagrams must use Excalidraw.
- **Git workflow** — `skills/git-workflow/SKILL.md` defines branching, conventional commits, atomic commit granularity, and the PR workflow using `gh` CLI. All changes go through feature branches and pull requests — never commit directly to `main`.

Refer to the relevant skill file before starting work in either area.
