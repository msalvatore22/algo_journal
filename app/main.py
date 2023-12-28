from fastapi import FastAPI
from app.routers.users import router as user_router
from app.routers.problems import router as problem_router
from app.routers.solutions import router as solution_router

app = FastAPI()
app.include_router(user_router)
app.include_router(problem_router)
app.include_router(solution_router)

@app.get("/")
async def root():
    return {"message": "Server is running"}

