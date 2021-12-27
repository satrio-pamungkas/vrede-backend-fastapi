from pydantic import BaseModel

class PenggunaSchema(BaseModel):
    name: str 
    message: str 
    
    class Config:
        orm_mode = True
    