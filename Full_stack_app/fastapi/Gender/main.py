from fastapi import Body, FastAPI
from routers import router
from pydantic import BaseModel

app = FastAPI()
app.include_router(router.router, prefix='/gender')


@app.get('/healthcheck', status_code=200)
async def healthcheck():
    return 'Gender classifier is all ready to go !'
