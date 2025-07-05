class RedisSettings:
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    REDIS_ATTEMPTS: int
    REDIS_TIMEOUT: int

    @property
    def redis_url(self) -> str:
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"
