from fastapi import FastAPI

app = FastAPI(
    title="DataMind",
    description="Мультиагентная система анализа данных на базе LangGraph + FastAPI + SQL + Selectel",
    version="0.1.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
