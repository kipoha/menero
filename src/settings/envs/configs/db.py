class DBSettings:
    POSTGRES_DB: str
    POSTGRES_PORT: int
    POSTGRES_PASSWORD: str
    POSTGRES_USER: str
    POSTGRES_HOST: str

    @property
    def db_url(self) -> str:
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
