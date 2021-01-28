import datetime

from sqlalchemy import Column, DateTime, Integer, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TimeStampedModelMixin:
    """
     An Mixin base class model that provides self-updating
    ``created_at`` and ``modified_at`` fields.
    """

    created_at = Column(DateTime, default=datetime.datetime.now)
    modified_at = Column(
        DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now
    )


class ChirodirectoryModel(TimeStampedModelMixin, Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True)
    info = Column(Text())
    title = Column(Text())
    mail = Column(Text())
    site = Column(Text())
