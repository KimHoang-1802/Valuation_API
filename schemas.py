from pydantic import BaseModel
from typing import Optional, List
from datetime import date

# Project schema
class ProjectBase(BaseModel):
    project_name: str
    description: Optional[str] = None
    investor: Optional[str] = None
    num_subzones: Optional[int] = None
    num_blocks: Optional[int] = None
    num_properties: Optional[int] = None
    start_date: Optional[date] = None
    completion_date: Optional[date] = None
    area: Optional[float] = None
    land_sheet: Optional[str] = None
    land_plot: Optional[str] = None
    alley_faces: Optional[int] = None
    frontage_faces: Optional[int] = None

class ProjectCreate(ProjectBase):
    pass

class Project(ProjectBase):
    project_id: int
    class Config:
        orm_mode = True


# Sector schema
class SectorBase(BaseModel):
    sector_name: str
    description: Optional[str] = None
    num_building: Optional[int] = None
    sector_area: Optional[float] = None
    project_id: int

class SectorCreate(SectorBase):
    pass

class Sector(SectorBase):
    sector_id: int
    class Config:
        orm_mode = True
