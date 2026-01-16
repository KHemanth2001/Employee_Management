from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field


class Settings(BaseSettings):
    SECRET_KEY: str = Field(default="G3FJtq9wHfE0ZQ8P4MZC2yF9J7TnX5qA_8sRkLm")
    DATABASE_URL: str = Field(default="sqlite:///./app.db")

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        extra="ignore",
        case_sensitive=False
    )

settings = Settings()