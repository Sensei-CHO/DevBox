from pydantic import BaseSettings


class Settings(BaseSettings):
    api_key: str     # Global API Key
    email: str       # Your Email
    zone_name: str   # Name of your zone (example.com)
    record_name: str # Name of your record (record.example.com)
    proxied: bool    # If your record is proxied or not (true/false)
    log_path: str    # Path and name of log file (/home/use/app/app.log)

    class Config:
        env_file = '.env'


settings = Settings()
