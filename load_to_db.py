import os
import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load variables from .env
load_dotenv()

# Access variables
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Construct Connection String
# format: postgresql://user:password@host:port/dbname
url = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(url)

# Load and Upload CSV
df = pd.read_csv('your_data.csv')
df.to_sql('my_table', engine, if_exists='append', index=False)

print("Data uploaded successfully!")