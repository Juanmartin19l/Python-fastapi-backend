from fastapi import FastAPI, Depends
from app.db.database import engine, Base, SessionLocal
from app.crud.user import create_user, get_users
from app.schemas.user import UserCreate, UserRead
from sqlalchemy.ext.asyncio import AsyncSession

app = FastAPI()

# Crear tablas al iniciar
@app.on_event("startup")
async def startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Dependency
async def get_db():
    async with SessionLocal() as session:
        yield session

@app.post("/users/", response_model=UserRead)
async def create(user: UserCreate, db: AsyncSession = Depends(get_db)):
    return await create_user(db, user)

@app.get("/users/", response_model=list[UserRead])
async def read_users(db: AsyncSession = Depends(get_db)):
    return await get_users(db)
