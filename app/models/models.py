from app.database.connection import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey


class Article(Base):
    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    author = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    url = Column(String(255), nullable=True)
    url_to_image = Column(String(500), nullable=True)
    published_at = Column(DateTime, nullable=True)
    content = Column(Text, nullable=True)
    source_id = Column(Integer, ForeignKey("source.id"), nullable=True)

    source = relationship("Source", back_populates="articles")


class Source(Base):
    __tablename__ = "source"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String(100), nullable=True)
    name = Column(String(100), nullable=True)

    articles = relationship("Article", back_populates="source")


class demo(Base):
    __tablename__ = "demo"

    id = Column(Integer, primary_key=True, index=True)
    source_id = Column(String(100), nullable=True)
    name = Column(String(100), nullable=True)
