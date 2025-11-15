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
SPY_DATASET = 'SPY'
NVIDIA_DATASET = 'NVDA'
START_DATE = '2000-01-01'
END_DATE = '2025-09-01'
AI_BOOM_START_DATE = '2015-01-01'
UNRATE_DATASET_COLOR = '#555555'
SPY_DATASET_COLOR = 'blue'
NVIDIA_DATASET_COLOR = '#76B900'
