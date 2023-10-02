from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL ="mysql+pymysql://todos:todos1012@todos.ctgmm5zsc3fm.ap-northeast-2.rds.amazonaws.com/todos"

engine = create_engine(DATABASE_URL)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionFactory()

def get_db():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()
