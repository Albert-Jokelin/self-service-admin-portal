from fastapi import FastAPI

app = FastAPI(title="Self-Service Customer Admin Portal")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
