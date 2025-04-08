import os
from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel
from groq import Groq
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Obtener la clave API de Groq desde las variables de entorno
api_key = os.environ.get('GROQ_API_KEY')

# Verificar que se obtuvo la clave API
if not api_key:
    raise ValueError("La clave API de Groq no está definida en el archivo .env")

# Inicializar el cliente de Groq
client = Groq(api_key=api_key)

# Crear la aplicación FastAPI
app = FastAPI(title="LLM Chat-GPT API", 
              description="API para interactuar con modelos de lenguaje a través de Groq",
              version="1.0.0")

# Definir el modelo de datos para las solicitudes de chat
class ChatRequest(BaseModel):
    message: str
    model: str = "llama-3.3-70b-versatile"

# Definir el modelo de datos para las respuestas de chat
class ChatResponse(BaseModel):
    response: str

@app.get("/")
def read_root():
    """Endpoint de bienvenida"""
    return {"message": "Bienvenido a la API de Chat-GPT con Groq"}

@app.post("/chat", response_model=ChatResponse)
def generate_chat_response(request: ChatRequest = Body(...)):
    """
    Genera una respuesta de chat utilizando el modelo especificado a través de Groq
    """
    try:
        # Crear la solicitud de chat
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "user",
                    "content": request.message,
                }
            ],
            model=request.model,
        )
        
        # Extraer la respuesta
        response_text = chat_completion.choices[0].message.content
        
        return {"response": response_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al generar respuesta: {str(e)}")

# Para ejecutar la aplicación directamente con "python app/main.py"
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)