from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from mangum import Mangum  # IMPORTANTE para funcionar en Vercel

app = FastAPI()

class Auto(BaseModel):
    id: int
    marca: str
    modelo: str

class AutoUpdate(BaseModel):
    marca: Optional[str] = None
    modelo: Optional[str] = None

autos = [
    {"id": 1, "marca": "Ford", "modelo": "Mondeo"},
    {"id": 2, "marca": "Fiat", "modelo": "Uno"},
    {"id": 3, "marca": "Renault", "modelo": "Sandero"},
]

@app.get("/")
def mensaje_inicio():
    return {"mensaje": "Bienvenido a la API de autos. Visita /docs para ver la documentación y probar los endpoints."}

@app.get("/auto/ALL", response_model=List[Auto])
def obtener_autos():
    return autos

@app.get("/auto/{auto_id}", response_model=Auto)
def obtener_auto(auto_id: int):
    for auto in autos:
        if auto["id"] == auto_id:
            return auto
    raise HTTPException(status_code=404, detail="Auto no fue encontrado, ingrese un ID valido.")

@app.post("/auto", response_model=Auto)
def crear_auto(auto: Auto):
    for auto_db in autos:
        if auto_db["id"] == auto.id:
            raise HTTPException(status_code=400, detail="El auto ya existe, cree uno nuevo que no exista.")
    autos.append(auto.dict())
    return auto

@app.put("/auto/{auto_id}", response_model=Auto)
def actualizar_auto(auto_id: int, auto_actualizado: Auto):
    for index, auto in enumerate(autos):
        if auto["id"] == auto_id:
            autos[index] = auto_actualizado.dict()
            return auto_actualizado
    raise HTTPException(status_code=404, detail="Auto no encontrado, ingrese un ID valido.")

@app.patch("/auto/{auto_id}", response_model=Auto)
def actualizar_parcial_auto(auto_id: int, auto_update: AutoUpdate):
    for auto in autos:
        if auto["id"] == auto_id:
            if auto_update.marca is not None:
                auto["marca"] = auto_update.marca
            if auto_update.modelo is not None:
                auto["modelo"] = auto_update.modelo
            return auto
    raise HTTPException(status_code=404, detail="Auto no encontrado, ingrese un ID valido.")

@app.delete("/auto/{auto_id}", response_model=Auto)
def eliminar_auto(auto_id: int):
    for index, auto in enumerate(autos):
        if auto["id"] == auto_id:
            return autos.pop(index)
    raise HTTPException(status_code=404, detail="Auto no encontrado, ingrese un ID existente para eliminarlo.")

# Necesario para que funcione en Vercel
handler = Mangum(app)
