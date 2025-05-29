# create_db.py

import os
from sqlalchemy import create_engine
from dice_roller.models import Base

# Ensure the db/ directory exists
os.makedirs("db", exist_ok=True)

# Create the engine
engine = create_engine("sqlite:///db/dice_game.db")

# Create all tables
Base.metadata.create_all(engine)

print("✅ Database created successfully!")
