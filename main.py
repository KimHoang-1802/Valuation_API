# from fastapi import FastAPI, Depends, HTTPException 
# from sqlalchemy.orm import Session
# from typing import List
# import models, schemas, database

# # Khởi tạo app
# app = FastAPI(title="Valuation API", description="API cho Project và Sector", version="1.0")

# # Tạo bảng trong DB, nếu chưa có 
# models.Base.metadata.create_all(bind=database.engine)

# # Hàm tạo session
# def get_db():
#     db = database.SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# # ------------------ PROJECT API ------------------ #
# @app.post("/projects/", response_model=schemas.Project)
# def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
#     new_project = models.Project(**project.dict())
#     db.add(new_project)
#     db.commit()
#     db.refresh(new_project)
#     return new_project


# @app.get("/projects/", response_model=List[schemas.Project])
# def get_projects(db: Session = Depends(get_db)):
#     return db.query(models.Project).all()


# @app.get("/projects/{project_id}", response_model=schemas.Project)
# def get_project(project_id: int, db: Session = Depends(get_db)):
#     project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
#     if not project:
#         raise HTTPException(status_code=404, detail="Project not found")
#     return project

# # ------------------ SECTOR API ------------------ #
# @app.post("/sectors/", response_model=schemas.Sector)
# def create_sector(sector: schemas.SectorCreate, db: Session = Depends(get_db)):
#     project = db.query(models.Project).filter(models.Project.project_id == sector.project_id).first()
#     if not project:
#         raise HTTPException(status_code=404, detail="Project not found for this sector")
#     new_sector = models.Sector(**sector.dict())
#     db.add(new_sector)
#     db.commit()
#     db.refresh(new_sector)
#     return new_sector


# @app.get("/sectors/", response_model=List[schemas.Sector])
# def get_sectors(db: Session = Depends(get_db)):
#     return db.query(models.Sector).all()


# @app.get("/sectors/{sector_id}", response_model=schemas.Sector)
# def get_sector(sector_id: int, db: Session = Depends(get_db)):
#     sector = db.query(models.Sector).filter(models.Sector.sector_id == sector_id).first()
#     if not sector:
#         raise HTTPException(status_code=404, detail="Sector not found")
#     return sector

# GIẢ LẬP DỮ LIỆU 
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Valuation API")

# Cho phép Swagger Editor trên web gọi đến localhost
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # hoặc chỉ ["https://editor.swagger.io"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from pydantic import BaseModel

class Project(BaseModel):
    project_id: int
    project_name: str
    description: str
    investor: str
    num_subzones: int
    num_blocks: int
    num_properties: int
    start_date: str
    completion_date: str
    area: float
    land_sheet: str
    land_plot: str
    alley_faces: int
    frontage_faces: int


fake_projects = [
    Project(
        project_id=1,
        project_name="Sunshine City",
        description="Dự án cao cấp ven sông",
        investor="Sun Group",
        num_subzones=3,
        num_blocks=5,
        num_properties=1000,
        start_date="2025-01-01",
        completion_date="2026-12-31",
        area=12500.5,
        land_sheet="A1",
        land_plot="P2",
        alley_faces=2,
        frontage_faces=1
    ),
    Project(
        project_id=2,
        project_name="Vinhomes Central Park",
        description="Khu đô thị hiện đại với công viên ven sông lớn nhất TP.HCM",
        investor="Vingroup",
        num_subzones=5,
        num_blocks=10,
        num_properties=3500,
        start_date="2023-03-15",
        completion_date="2025-10-01",
        area=43000.0,
        land_sheet="B2",
        land_plot="L5",
        alley_faces=1,
        frontage_faces=3
    ),
    Project(
        project_id=3,
        project_name="Eco Green Saigon",
        description="Tổ hợp căn hộ xanh chuẩn quốc tế tại Quận 7",
        investor="Xuan Mai Corp",
        num_subzones=2,
        num_blocks=6,
        num_properties=1200,
        start_date="2024-06-01",
        completion_date="2026-09-30",
        area=20000.0,
        land_sheet="C3",
        land_plot="Q7",
        alley_faces=3,
        frontage_faces=2
    )
]

@app.get("/projects/{project_id}", response_model=Project)
def get_project_by_id(project_id: int):
    for project in fake_projects:
        if project.project_id == project_id:
            return project
    return {"detail": "Not Found"}




