import asyncio
import sys
from app.db.database import Base, engine, SessionLocal
from app.models.user import User
from sqlalchemy.future import select

async def recreate_database():
    """Recrear todas las tablas (eliminar y crear de nuevo)"""
    print("Eliminando tablas existentes...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
    
    print("Creando tablas nuevas...")
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    
    print("¡Base de datos recreada con éxito!")

async def add_sample_data():
    """Agregar datos de ejemplo a la base de datos"""
    print("Agregando datos de prueba...")
    
    # Crear usuarios de prueba
    users = [
        {"name": "Juan Pérez", "email": "juan@example.com", "age": 30},
        {"name": "Ana Gómez", "email": "ana@example.com", "age": 25},
        {"name": "Carlos Rodríguez", "email": "carlos@example.com", "age": 35},
        {"name": "María López", "email": "maria@example.com", "age": 28},
        {"name": "Roberto Fernández", "email": "roberto@example.com", "age": 42}
    ]
    
    async with SessionLocal() as session:
        for user_data in users:
            user = User(**user_data)
            session.add(user)
        
        await session.commit()
    
    print("¡Datos de prueba agregados con éxito!")

async def verify_data():
    """Verificar que los datos se hayan agregado correctamente"""
    print("Verificando datos agregados...")
    
    async with SessionLocal() as session:
        result = await session.execute(select(User))
        users = result.scalars().all()
        
        print(f"Se encontraron {len(users)} usuarios en la base de datos:")
        for user in users:
            print(f"ID: {user.id}, Nombre: {user.name}, Email: {user.email}, Edad: {user.age}")

async def main():
    """Función principal que ejecuta todas las operaciones"""
    if len(sys.argv) > 1 and sys.argv[1] == "--no-recreate":
        print("Modo: solo agregar datos (sin recrear tablas)")
    else:
        await recreate_database()
    
    await add_sample_data()
    await verify_data()

if __name__ == "__main__":
    print("Iniciando script de población de base de datos...")
    asyncio.run(main())
    print("¡Script completado!")