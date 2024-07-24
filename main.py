from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))  # Obtiene el puerto de la variable de entorno, por defecto 8000
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)  # Ejecuta el servidor en el puerto especificado
