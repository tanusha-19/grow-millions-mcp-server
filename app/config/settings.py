from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    MCP_SERVER_NAME: str = "grow-millions"
    MCP_SERVER_VERSION: str = "0.1.0"
    
    # Modern Pydantic V2 configuration
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

settings = Settings()