from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Carro(BaseModel):
    id: str
    marca: str
    modelo: int

class Usuario(BaseModel):
    id: str
    nombre: str
    email: str

carros = [
    {"id": "1", "marca": "mazda", "modelo": 1983},
    {"id": "2", "marca": "honda", "modelo": 1993}
]

usuarios = [
    {"id": "1", "nombre": "Juan", "email": "juan@example.com"},
    {"id": "2", "nombre": "Ana", "email": "ana@example.com"}
]

@app.get("/carros", response_model=List[Carro])
def get_carros():
    return carros

@app.post("/carros", response_model=Carro)
def post_carros(carro: Carro):
    carros.append(carro.dict())
    return carro

@app.delete("/carros/{id}")
def delete_carro(id: str):
    global carros
    carros = [car for car in carros if car["id"] != id]
    return {"mensaje": f"Carro con id {id} eliminado"}

@app.put("/carros/{id}", response_model=Carro)
def put_carro(id: str, carro: Carro):
    for idx, car in enumerate(carros):
        if car["id"] == id:
            carros[idx] = carro.dict()
            return carro
    raise HTTPException(status_code=404, detail="Carro no encontrado")

@app.get("/usuarios", response_model=List[Usuario])
def get_usuarios():
    return usuarios

@app.post("/usuarios", response_model=Usuario)
def post_usuarios(usuario: Usuario):
    usuarios.append(usuario.dict())
    return usuario

@app.delete("/usuarios/{id}")
def delete_usuario(id: str):
    global usuarios
    usuarios = [user for user in usuarios if user["id"] != id]
    return {"mensaje": f"Usuario con id {id} eliminado"}

@app.put("/usuarios/{id}", response_model=Usuario)
def put_usuario(id: str, usuario: Usuario):
    for idx, user in enumerate(usuarios):
        if user["id"] == id:
            usuarios[idx] = usuario.dict()
            return usuario
    raise HTTPException(status_code=404, detail="Usuario no encontrado")
