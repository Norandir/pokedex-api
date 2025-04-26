import sqlite3
import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Serve static files (images)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define the database path
DB_PATH = os.path.join(os.path.dirname(__file__), "Pokedex.db")

# Database connection function
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Allows dictionary-style access
    return conn

# Pydantic model for Pokémon response
class Pokemon(BaseModel):
    id: int
    name: str
    type1: str
    type2: Optional[str]
    description: str
    image_url: str

# Get all Pokémon
@app.get("/pokemon", response_model=List[Pokemon])
def get_all_pokemon():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon")
    pokemons = cursor.fetchall()
    conn.close()
    return [dict(pokemon) for pokemon in pokemons]

# Get a Pokémon by name
@app.get("/pokemon/{name}", response_model=Pokemon)
def get_pokemon(name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM pokemon WHERE name = ? COLLATE NOCASE", (name,))
    pokemon = cursor.fetchone()
    conn.close()
    if not pokemon:
        raise HTTPException(status_code=404, detail="Pokémon not found")
    return dict(pokemon)

# Get Pokemon by Type 
@app.get("/pokemon/type/{type_name}", response_model=List[Pokemon])
def get_pokemon_by_type(type_name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Query the database for Pokémon with matching type1 OR type2
    cursor.execute(
        "SELECT * FROM pokemon WHERE type1 = ? COLLATE NOCASE OR type2 = ? COLLATE NOCASE", 
        (type_name, type_name)
    )
    pokemons = cursor.fetchall()
    conn.close()

    # If no Pokémon are found, return a 404 error
    if not pokemons:
        raise HTTPException(status_code=404, detail=f"No Pokémon found with type {type_name}")

    return [dict(pokemon) for pokemon in pokemons]
