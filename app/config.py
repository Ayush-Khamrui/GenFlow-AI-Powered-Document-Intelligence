import os
from dotenv import load_dotenv

load_dotenv()
ABS_PATH = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(ABS_PATH, "..", "data", "embeddings")

class Config:
    DB_DIR = DB_DIR
