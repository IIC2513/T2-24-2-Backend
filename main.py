from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import List, Annotated
import models.recipe as models
from config.database import SessionLocal, engine
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(bind=engine)

class Recipe(BaseModel):
    title: str
    description: str
    ingredients: List[str]
    steps: List[str]
    image: str

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/recipes/", response_model=List[Recipe])
async def get_recipes(db: db_dependency):
    recipes = db.query(models.Recipes).all()
    return recipes

@app.get("/recipes/{recipe_id}", response_model=Recipe)
async def get_recipe(recipe_id: int, db: db_dependency):
    recipe = db.query(models.Recipes).filter(models.Recipes.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    return recipe

@app.post("/recipes/", response_model=Recipe)
async def create_recipe(recipe: Recipe, db: db_dependency):
    db_recipe = models.Recipes(title=recipe.title, description=recipe.description, ingredients=recipe.ingredients, steps=recipe.steps, image=recipe.image)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@app.delete("/recipes/{recipe_id}")
async def delete_recipe(recipe_id: int, db: db_dependency):
    recipe = db.query(models.Recipes).filter(models.Recipes.id == recipe_id).first()
    if recipe is None:
        raise HTTPException(status_code=404, detail="Recipe not found")
    db.delete(recipe)
    db.commit()
    return {"message": "Recipe deleted successfully"}
