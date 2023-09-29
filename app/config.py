from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str
    MONGO_INITDB_DATABASE: str

    JWT_PUBLIC_KEY: str
    JWT_PRIVATE_KEY: str
    REFRESH_TOKEN_EXPIRES_IN: int
    ACCESS_TOKEN_EXPIRES_IN: int
    JWT_ALGORITHM: str
    JWT_SECRET_KEY: str
    
    CLIENT_ORIGIN: str
    
    # missing
    MONGO_INITDB_ROOT_USERNAME: str
    MONGO_INITDB_ROOT_PASSWORD: str
    CLIENT_ID: str
    GOOGLE_CLIENT_SECRET: str

    class Config:
        env_file = './.env'


settings = Settings()

