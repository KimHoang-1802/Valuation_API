from sqlalchemy import Column, Integer, String, Text, Date, DECIMAL, SmallInteger, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Project(Base):
    __tablename__ = "projects"

    project_id = Column(Integer, primary_key=True, index=True)
    project_name = Column(String, nullable=False)
    description = Column(Text)
    investor = Column(String)
    num_subzones = Column(Integer)
    num_blocks = Column(Integer)
    num_properties = Column(Integer)
    start_date = Column(Date)
    completion_date = Column(Date)
    area = Column(DECIMAL)
    land_sheet = Column(String)
    land_plot = Column(String)
    alley_faces = Column(SmallInteger)
    frontage_faces = Column(SmallInteger)

    # Quan hệ 1-nhiều với bảng sectors
    sectors = relationship("Sector", back_populates="project")


class Sector(Base):
    __tablename__ = "sectors"

    sector_id = Column(Integer, primary_key=True, index=True)
    project_id = Column(Integer, ForeignKey("projects.project_id"))
    sector_name = Column(String, nullable=False)
    description = Column(Text)
    num_building = Column(Integer)
    sector_area = Column(DECIMAL)

    # Liên kết ngược về Project
    project = relationship("Project", back_populates="sectors")
