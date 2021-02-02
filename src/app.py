import os
import pathlib

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from dotenv import load_dotenv
from functools import lru_cache

BASE_DIR = pathlib.Path(__file__).parent # src

app = FastAPI()
templates = Jinja2Templates(directory = BASE_DIR / "templates")

print("AIRTABLE_BASE_ID", os.environ.get("AIRTABLE_BASE_ID"))

@lru_cache()
def cached_dotenv():
    load_dotenv()

cached_dotenv()
print("AIRTABLE_BASE_ID", os.environ.get("AIRTABLE_BASE_ID"))

# get url/route
@app.get("/")
def home_view(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


# template rendering
@app.post("/")
def home_signup_view(request: Request, email:str = Form(...)):
    return templates.TemplateResponse("home.html", {"request": request, "submitted_email": email})