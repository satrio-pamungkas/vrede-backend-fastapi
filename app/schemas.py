from pydantic import BaseModel
from typing import List

class TambahPesanSchema(BaseModel):
    name: str 
    message: str 
    
    class Config:
        orm_mode = True
    
    
class TambahPesanResponseSchema(BaseModel):
    status_code: int 
    message: str
    
    
class Message(BaseModel):
    name: str
    message: str
    created_at: str
    id: str 
    user_id: str
    
        
class MessageSchema(BaseModel):
    pesan: List[Message]
    