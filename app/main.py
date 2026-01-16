import uvicorn
from fastapi import FastAPI
from app.routers import employee_routers, auth_routers
from app.db.database import engine, Base

from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse


app=FastAPI(
    title="Employee Management",
    docs_url="/employee/swagger/",
    openapi_url="/employee/swagger/openapi.json"
)

Base.metadata.create_all(bind=engine)

app.include_router(auth_routers.router)
app.include_router(employee_routers.router)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=400,
        content={"detail": exc.errors()}
    )

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)