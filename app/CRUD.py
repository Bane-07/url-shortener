from sqlalchemy.orm import Session
from app.models import URL
from app.utils import encode_62

def create_url(db: Session, original_url: str):
    url = URL(original_url=original_url)

    db.add(url)
    db.commit()
    db.refresh(url)
    
    code = encode_62(url.id)
    url.short_code = code
    db.commit()
    db.refresh(url)
    return url

def get_url_by_short_code(db: Session, short_code: str):
    return (
        db.query(URL)
        .filter(URL.short_code == short_code)
        .first()
    )