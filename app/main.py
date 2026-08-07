from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from app.database import get_db
from app import crud, schemas

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the URL Shortener API!"}


@app.post("/shorten")
def shorten_url(url: schemas.URLCreate, db: Session = Depends(get_db)):
    return crud.create_url(db, url.original_url)

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):
    url = crud.get_url_by_short_code(db, short_code)

    if url is None:
        raise HTTPException(status_code=404, detail="Short URL not found")

    return RedirectResponse(url.original_url)