from sqlalchemy.orm import Session
from schemas import TambahPesanSchema, MessageSchema
from models import Pengguna, Forum
from datetime import datetime

def create_pengguna(db: Session, pesan: TambahPesanSchema, user_id: str):
    db_pengguna = Pengguna(
        id = user_id,
        name = pesan.name
    )
    db.add(db_pengguna)
    db.commit()
    db.refresh(db_pengguna)
    db.close()
    

def create_message(db: Session, pesan: TambahPesanSchema, kode_status: int, now: datetime, user_id: str, message_id: str):
    db_pesan = Forum(
        id = message_id,
        user_id = user_id,
        message = pesan.message,
        status = kode_status,
        created_at = now
    )
    db.add(db_pesan)
    db.commit()
    db.refresh(db_pesan)
    db.close()
    
    
def read_message(db: Session):
    query = db.query(Pengguna.name, Forum.message, Forum.created_at, Forum.id, Forum.user_id)\
        .join(Forum).filter(Pengguna.id == Forum.user_id)\
        .filter(Forum.status == 1).all()
        
    db.close()
    
    return query
    
     