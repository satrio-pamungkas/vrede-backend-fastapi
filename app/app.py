from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import *
from prediction import get_prediction
from models import Base, Pengguna, Forum
from schemas import PenggunaSchema
import uvicorn

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def recreate_database():
    Base.metadata.create_all(engine)
    
recreate_database()    

app = FastAPI()
db = SessionLocal()

@app.get("/")
def main_page():
    return {"Hello": "World"}

@app.post("/pesan", response_model=PenggunaSchema)
def add_pesan(pengguna: PenggunaSchema):
    if get_prediction(pengguna.message):
        return JSONResponse(status_code=403, content={
            "status_code": 403,
            "message": "Pesan terindikasi hate speech"
        })
        
    db_pesan = Pengguna(
        id = "CGS32",
        name = pengguna.name
    )
    db.add(db_pesan)
    db.commit()
    db.refresh(db_pesan)
    db.close()
    
    return JSONResponse(status_code=200, content={
        "status_code": 200,
        "message": "success"
    })
    

@app.get("/pesan")
def get_pesan():
    pesan = db.query(Pengguna).all()
    db.close()
    
    result =  jsonable_encoder({
        "pesan": pesan
    })
    
    return JSONResponse(status_code=200, content={
        "status_code": 200,
        "data": result
    })


if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=SERVER_PORT, reload=True)