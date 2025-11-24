from fastapi import FastAPI

app = FastAPI(title="RunFastAPI Test App")


@app.get("/")
def read_root() -> dict[str, str]:
    return {"message": "Welcome to the FastAPI starter."}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None) -> dict[str, object]:
    item = {"item_id": item_id}
    if q is not None:
        item["query"] = q
    return item


@app.post("/echo")
def echo(payload: dict) -> dict:
    return {"received": payload}
