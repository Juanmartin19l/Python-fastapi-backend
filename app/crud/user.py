from sqlalchemy.future import select
from app.models.user import User
from app.schemas.user import UserCreate
from sqlalchemy.ext.asyncio import AsyncSession

async def create_user(db: AsyncSession, user: UserCreate):
    # Usando model_dump() en lugar de dict() para Pydantic v2
    db_user = User(**user.model_dump())
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user

async def get_users(db: AsyncSession):
    result = await db.execute(select(User))
    return result.scalars().all()
