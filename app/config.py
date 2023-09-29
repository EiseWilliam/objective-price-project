from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str | None = None
    MONGO_INITDB_DATABASE: str | None = None

    JWT_PUBLIC_KEY: str | None = None
    JWT_PRIVATE_KEY: str | None = None
    REFRESH_TOKEN_EXPIRES_IN: int | None = None
    ACCESS_TOKEN_EXPIRES_IN: int  | None = None
    JWT_ALGORITHM: str | None = None
    JWT_SECRET_KEY: str | None = None
    
    CLIENT_ORIGIN: str | None = None
    
    # missing
    MONGO_INITDB_ROOT_USERNAME: str | None = None
    MONGO_INITDB_ROOT_PASSWORD: str | None = None
    CLIENT_ID: str | None = None
    GOOGLE_CLIENT_SECRET: str | None = None

    class Config:
        env_file = './.env'


settings = Settings()

