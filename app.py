from fastapi import FastAPI, HTTPException
import json
import requests
import os
from pydantic import BaseModel, Field

app = FastAPI()

try:
    with open("recipes.json", "r") as file:
        recipes = json.load(file)
except FileNotFoundError:
    raise RuntimeError("The recipes.json file is missing. Please make sure it exists.")

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN", "").strip()
TELEGRAM_CHAT_ID = os.getenv("TELEGRAM_CHAT_ID", "").strip()

if not TELEGRAM_BOT_TOKEN or not TELEGRAM_CHAT_ID:
    raise RuntimeError("Telegram bot token or chat ID is not set. Check your environment variables.")

class RecipeSubmission(BaseModel):
    name: str = Field(..., description="Name of the recipe")
    description: str = Field(..., description="Brief description of the recipe")
    ingredients: list[str] = Field(..., description="List of ingredients with amounts")
    procedure: str = Field(..., description="Step-by-step procedure to make the recipe")
    hardness: int = Field(..., ge=1, le=10, description="Difficulty level of the recipe out of 10")

@app.get("/recipes/{recipe_name}")
async def get_recipe(recipe_name: str):
    recipe = recipes.get(recipe_name.lower())
    if not recipe:
        raise HTTPException(status_code=404, detail=f"Recipe for {recipe_name} not found.")
    return recipe

@app.get("/search")
async def search_recipes(keyword: str):
    results = {name: data for name, data in recipes.items() if keyword.lower() in name.lower() or keyword.lower() in data.get("description", "").lower()}
    if not results:
        raise HTTPException(status_code=404, detail="No recipes match your search criteria.")
    return results

@app.get("/recipes")
async def list_recipes():
    return {"endpoints": list(recipes.keys())}

@app.post("/submit")
async def submit_recipe(recipe: RecipeSubmission):
    message = (
        f"New Recipe Submission:\n\n"
        f"Name: {recipe.name}\n"
        f"Description: {recipe.description}\n"
        f"Ingredients: {', '.join(recipe.ingredients)}\n"
        f"Procedure: {recipe.procedure}\n"
        f"Hardness: {recipe.hardness}/10"
    )

    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    response = requests.post(url, data={"chat_id": TELEGRAM_CHAT_ID, "text": message})

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to send new recipe request to Telegram.")
    
    return {"message": "Submission received! It'll be reviewed shortly."}

@app.get("/")
async def ping():
    return {
        "message": "Welcome to BakeBook! Use /recipes to see available recipes, or /submit to submit a new recipe."
    }

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app:app", host="0.0.0.0", port=port, log_level="info", reload=True)
