from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Cấu hình kết nối database
DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/my_postgres"

# Kết nối
engine = create_engine(DATABASE_URL)

# Tạo session để thao tác với DB
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class cho các model kế thừa
Base = declarative_base()
