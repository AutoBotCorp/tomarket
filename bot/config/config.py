from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_ignore_empty=True)

    API_ID: int
    API_HASH: str

    REF_ID: str = '0001QQnm'
    
    FAKE_USERAGENT: bool = True
    POINTS_COUNT: list[int] = [450, 600]
    AUTO_PLAY_GAME: bool = True
    AUTO_TASK: bool = True
    AUTO_DAILY_REWARD: bool = True
    AUTO_CLAIM_STARS: bool = True
    AUTO_CLAIM_COMBO: bool = True
    AUTO_RANK_UPGRADE: bool = True

    USE_RANDOM_DELAY_IN_RUN: bool = True
    RANDOM_DELAY_IN_RUN: list[int] = [0, 10]

    USE_PROXY_FROM_FILE: bool = True


settings = Settings()

