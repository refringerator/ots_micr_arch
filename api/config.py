import os
import urllib.parse


DATABASE_USERNAME = os.getenv("DATABASE_USERNAME", "postgres")
DATABASE_PASSWORD = urllib.parse.quote_plus(os.getenv("DATABASE_PASSWORD", "s3cr3Tp@$$w0rD"))
DATABASE_HOST = os.getenv("DATABASE_HOST", "localhost")
DATABASE_NAME = os.getenv("DATABASE_NAME", "postgres")
