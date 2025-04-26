# Pokedex API - FastAPI Backend

## Description
A simple Pokémon Pokédex API built using FastAPI and SQLite. This backend serves Pokémon data including names, types, descriptions, and images.
## Features
- API endpoints to retrieve all Pokémon, Pokémon by name, or Pokémon by type
- Case-insensitive search for names and types
- Serves static images for each Pokémon from a local directory
- Lightweight and fast with easy local setup

## Installation Instructions
1. Clone this repository:
   ```bash
   git clone https://github.com/norandir/pokedex-api-cli.git
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
Run the FastAPI server using Uvicorn:
```bash
uvicorn main:app --reload
```

Access the API at:
- API base URL: `http://127.0.0.1:8000/`

Example:
```bash
# Get all Pokémon
GET http://127.0.0.1:8000/pokemon

# Get a Pokémon by name
GET http://127.0.0.1:8000/pokemon/Charmander

# Get Pokémon by type
GET http://127.0.0.1:8000/pokemon/type/fire
```

## Tech Stack
- **Python 3**
- **FastAPI** for building APIs
- **SQLite** for database management
- **Pydantic** for data validation
- **Uvicorn** for running the server
- **OS** and **SQLITE3** modules for file and database handling
