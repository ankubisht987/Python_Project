from fastapi import FastAPI ,  Request
import uvicorn

app = FastAPI(
    title= "Ankush Page",
    description=(
        "Internal API for Managing App"
        "Handel Creation"
    ),
    version="0.0.1",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openai.json"
)

@app.get("/")
def read_root():
    """---Root End Point---"""
    return {
        "message": "Welcome to phto.com", 
        "Health":"Good",
        "Status" :"Online"
    }

@app.get("/about")
def about():
    """---About App---"""
    return {
        "message":"This is Ankush Page",
        "Status" :"Online"
    }

@app.get("/debug/request-info")
def request_info(request:Request):
    """Inspect the raw request Object"""
    return {
        "method":request.method,
        "url" : str(request.url),
        "headers":dict(request.headers),
        "path_params": request.path_params,
        "query_param":dict(request.query_params),
    }


if __name__ == "__main__":
    uvicorn.run("01_Fast_API_foundation:app" , port=9090 , reload=True)