from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL ="mysql+pymysql://todos:todos1002@todos.ctgmm5zsc3fm.ap-northeast-2.rds.amazonaws.com:3306/todos"

engine = create_engine(DATABASE_URL, echo=True)
SessionFactory = sessionmaker(autocommit=False, autoflush=False, bind=engine)

session = SessionFactory()

def get_db():
    session = SessionFactory()
    try:
        yield session
    finally:
        session.close()
