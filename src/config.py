import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()  # loads variables from .env

#FRED API KEY
fred_api_key = os.getenv("FRED_API_KEY")

# project configuration
RESULTS_DIR = "../results"

# data sources configuration
UNRATE_DATASET= 'UNRATE'

