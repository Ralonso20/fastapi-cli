main_app_template: str = """from fastapi import FastAPI
from app_controller import router
app = FastAPI()

# Register routers

app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
"""
