# EdgeWatch

EdgeWatch is a FastAPI service scaffold for monitoring and evaluating betting edge signals.

## Local development

1. Create a local env file:
   ```bash
   cp .env.example .env
   ```
2. Create/update the lockfile:
   ```bash
   uv lock
   ```
3. Install dependencies (including dev tools):
   ```bash
   uv sync --dev
   ```

## Run the server

```bash
uv run uvicorn app.main:app --reload
```

The API docs are available at `http://127.0.0.1:8000/docs`.

## Run tests

```bash
uv run pytest
```

Environment variables are defined in `.env.example`. Use `.env` for local overrides.
