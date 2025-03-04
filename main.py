from sqlalchemy import create_engine

# Define Database URL
DATABASE_URL = "postgresql+psycopg2://user:password@localhost:5432/mydatabase"

# Create Engine
engine = create_engine(DATABASE_URL)

# Test Connection
with engine.connect() as connection:
    print("Connected to the database successfully!")
