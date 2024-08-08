import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    SQLALCHEMY_DATABASE_URI: str = os.getenv("DATABASE_URL", "sqlite:///./map-my-world.db")


settings = Settings()
