from fastapi import FastAPI, Depends
from app.db.database import engine, Base, SessionLocal
from app.crud.user import create_user, get_users
from app.schemas.user import UserCreate, UserRead
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException
from sqlalchemy.future import select
from app.models.user import User

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

@app.get("/users/{user_id}", response_model=UserRead)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(User).where(User.id == user_id))
    user = result.scalars().first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user
