from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


# Database connection parameters
username = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASSWORD")
host = 'localhost'
port = os.getenv("POSTGRES_PORT")
database = os.getenv("POSTGRES_DB")
connection_url = f"postgresql://{username}:{password}@{host}:{port}/{database}"

class DatabaseEngineSingleton:
    __instance = None

    def __new__(cls):
        if DatabaseEngineSingleton.__instance is None:
            cls.__instance = \
                super(DatabaseEngineSingleton,cls).__new__(cls)
            cls.__instance._connection_url = connection_url
            cls.__instance._engine = create_engine(cls.__instance.connection_string)   
            cls.__instance._session_factory = sessionmaker(bind=cls.__instance._engine)
        return cls.__instance
    
    @property
    def engine(cls):
        return cls.__instance._engine

    @property
    def connection_url(cls)->str:
        return cls.__instance.connection_url
  

    def session(cls):
        return cls.__instance._session_factory()
    
if __name__ == "__main__":
    db = DatabaseEngineSingleton()
    with db.session() as Session:
        print("Session creation successful")