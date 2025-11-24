# runfastapi.app-testapp

Minimal FastAPI app with a few sample endpoints.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run

```bash
uvicorn app.main:app --reload
```

## Endpoints

- `GET /` welcome message
- `GET /health` status check
- `GET /items/{item_id}?q=optional` item with optional query
- `POST /echo` returns posted JSON
