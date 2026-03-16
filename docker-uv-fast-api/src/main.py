from fastapi import FastAPI

app = FastAPI(
    title="personal-boilerplates",
    version="1.0.0",
)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/")
def root():
    return {"message": "Hello World!"}