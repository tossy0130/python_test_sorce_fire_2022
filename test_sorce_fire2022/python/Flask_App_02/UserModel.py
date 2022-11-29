from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from setting import Base
from setting import ENGINE


class User(Base):
    """
    UserModel
    """

    __tablename__ = 'ppp_users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200))
    created_at = Column(DateTime, default=datetime.now, nullable=False)
    updated_at = Column(DateTime, default=datetime.now, nullable=False)

    def __init__(self, name):
        self.name = name


if __name__ == '_main__':
    Base.metadata.create_all(binf=ENGINE)
