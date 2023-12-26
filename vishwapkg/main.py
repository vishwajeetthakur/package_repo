import numpy  as np 
import pandas as pd 
import os

# Load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

# Access environment variables
USERNAME = os.getenv("Vishwa")
PASSWORD = os.getenv("Psswd")

from test import abc, pw

class Demo:
    def __init__(self) -> None:
        self.USERNAME = abc 
        self.PASSWORD = pw

    def get_all(self):
        return (self.USERNAME, self.PASSWORD)
