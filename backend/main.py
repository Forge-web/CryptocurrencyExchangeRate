from fastapi import FastAPI
from src.router import router as router_main
import uvicorn

app = FastAPI()

app.include_router(router_main)

if __name__ == "__main__":
    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8000)