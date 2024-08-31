from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from config.database import Base

class Recipes(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    ingredients = Column(String, index=True)
    steps = Column(String, index=True)
    image = Column(String, index=True)
