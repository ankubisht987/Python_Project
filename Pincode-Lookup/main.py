from fill_form_API import app
import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app",port=9000,reload=True)