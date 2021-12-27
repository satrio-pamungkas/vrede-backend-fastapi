from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import String, Text, Integer, DateTime , Column, ForeignKey
from sqlalchemy.orm import relationship

Base = declarative_base()

class Pengguna(Base):
    __tablename__ = 'pengguna'
    id = Column(String(255), primary_key=True)
    name = Column(String(75))
    forum = relationship("Forum")
    
    
class Forum(Base):
    __tablename__ = 'forum'
    id = Column(String(255), primary_key=True)
    user_id = Column(String(255), ForeignKey('pengguna.id'))
    message = Column(Text)
    status = Column(Integer)
    created_at = Column(DateTime)
    