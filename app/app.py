import uvicorn
from fastapi import FastAPI
from app.routers.news import router as news_router

# App Config
app = FastAPI(
    title="H O U Z E O",
    description="An Application to auto commit top headline to db.",
    version="1.0",
)

app.include_router(news_router)


@app.get("/")
def root():
    return {"message": "Welcome to the API"}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
