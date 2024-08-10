import uvicorn

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host="localhost",
        log_level="info",
        reload=True,
        port=8004,
    )