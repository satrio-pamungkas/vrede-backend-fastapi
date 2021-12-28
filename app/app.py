from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.responses import RedirectResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import *
from prediction import get_prediction
from models import Base, Pengguna, Forum
from schemas import TambahPesanSchema, MessageSchema, TambahPesanResponseSchema
from crud import create_pengguna, create_message, read_message
from datetime import datetime
import uvicorn

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
app = FastAPI()
db = SessionLocal()

@app.get("/dokumentasi")
def docs_redirect():
    return RedirectResponse(url='/docs')


@app.post("/pesan", responses={201: {"model": TambahPesanResponseSchema}, 409: {"model": TambahPesanResponseSchema}})
def add_message(pesan: TambahPesanSchema):
    now = datetime.now()
    user_id = now.strftime("UID%H%M%s")
    message_id = now.strftime("MSG%H%M%s")
    
    if get_prediction(pesan.message):
        create_pengguna(db, pesan, user_id)
        create_message(db, pesan, 0, now, user_id, message_id)
        
        return JSONResponse(status_code=409, content={
            "status_code": 409,
            "message": "Pesan terindikasi hate speech"
        })
        
    create_pengguna(db, pesan, user_id)
    create_message(db, pesan, 1, now, user_id, message_id)

    return JSONResponse(status_code=201, content={
        "status_code": 201,
        "message": "Berhasil ditambahkan"
    })
    

@app.get("/pesan", responses={200: {"model": MessageSchema}})
def get_message():
    result =  jsonable_encoder({
        "pesan": read_message(db)
    })
    
    return JSONResponse(status_code=200, content={
        "status_code": 200,
        "data": result
    })


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=SERVER_PORT, reload=True)