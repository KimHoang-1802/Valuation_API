from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
import models, schemas, database

# Khởi tạo app
app = FastAPI(title="Valuation API", description="API cho Project và Sector", version="1.0")

# Tạo bảng trong DB (nếu chưa có)
models.Base.metadata.create_all(bind=database.engine)

# Hàm tạo session
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ------------------ PROJECT API ------------------ #
@app.post("/projects/", response_model=schemas.Project)
def create_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    new_project = models.Project(**project.dict())
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project


@app.get("/projects/", response_model=List[schemas.Project])
def get_projects(db: Session = Depends(get_db)):
    return db.query(models.Project).all()


@app.get("/projects/{project_id}", response_model=schemas.Project)
def get_project(project_id: int, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.project_id == project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found")
    return project

# ------------------ SECTOR API ------------------ #
@app.post("/sectors/", response_model=schemas.Sector)
def create_sector(sector: schemas.SectorCreate, db: Session = Depends(get_db)):
    project = db.query(models.Project).filter(models.Project.project_id == sector.project_id).first()
    if not project:
        raise HTTPException(status_code=404, detail="Project not found for this sector")
    new_sector = models.Sector(**sector.dict())
    db.add(new_sector)
    db.commit()
    db.refresh(new_sector)
    return new_sector


@app.get("/sectors/", response_model=List[schemas.Sector])
def get_sectors(db: Session = Depends(get_db)):
    return db.query(models.Sector).all()


@app.get("/sectors/{sector_id}", response_model=schemas.Sector)
def get_sector(sector_id: int, db: Session = Depends(get_db)):
    sector = db.query(models.Sector).filter(models.Sector.sector_id == sector_id).first()
    if not sector:
        raise HTTPException(status_code=404, detail="Sector not found")
    return sector
