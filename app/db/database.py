from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# URL para SQLite asíncrono
DATABASE_URL = "sqlite+aiosqlite:///./test.db"

# Crear motor asíncrono
engine = create_async_engine(
    DATABASE_URL, 
    echo=True,
    connect_args={"check_same_thread": False}  # Necesario para SQLite
)

# Configurar fábrica de sesiones para sesiones asíncronas
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine, 
    class_=AsyncSession, 
    expire_on_commit=False
)

# Base declarativa para los modelos ORM
Base = declarative_base()
