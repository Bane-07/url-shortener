from fastapi import Depends, FastAPI, Request
from sqlalchemy.orm import Session
from fastapi.responses import RedirectResponse
from fastapi import HTTPException
from app.database import get_db
from app import crud, schemas
from app.cache import get_cached_url , cached_url
from app.crud import get_url_by_short_code
from app.rate_limiter import is_rate_limited
from datetime import datetime

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Welcome to the URL Shortener API!"}


@app.post("/shorten")
def shorten_url(
    request: Request,
    url: schemas.URLCreate,
    db: Session = Depends(get_db)
):
    client_ip = request.client.host

    if is_rate_limited(client_ip):
        raise HTTPException(
            status_code=429,
            detail="Too many requests"
        )

    return crud.create_url(db, url.original_url, url.expires_at)

@app.get("/{short_code}")
def redirect_url(short_code: str, db: Session = Depends(get_db)):

    cached_url(short_code, url.original_url, url.expires_at)

    if cached_url:
        return RedirectResponse(cached_url)

    url = get_url_by_short_code(db, short_code)

    if not url:
            raise HTTPException(
            status_code=404,
            detail="Short URL not found"
        )

    if url.expires_at and url.expires_at < datetime.utcnow():
            raise HTTPException(
            status_code=410,
            detail="Short URL has expired"
    )

    cached_url(short_code, url.original_url)

    return RedirectResponse(url.original_url)