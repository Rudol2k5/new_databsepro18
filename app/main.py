from fastapi import FastAPI
from app.routes import user, type, notification
from app.database import Base, engine

app = FastAPI(title="User Notification System")

app.include_router(user.router)
app.include_router(type.router)
app.include_router(notification.router)

@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

