from sqlalchemy import *
from sqlalchemy.orm import *
from sqlalchemy.ext.declarative import declarative_base
import psycopg2


DATABASE = 'postgresql://{user}:{password}@{host}:{port}/{dbname}'.format(
    user="postgres",  # ユーザ
    password="jim",  # パスワード
    host="localhost",  # ホスト名
    port="5432",  # ポート
    dbname="postgres")  # データベース名


# Engineの作成
ENGINE = create_engine(
    DATABASE,
    encoding='utf-8',
    echo=True
)

# Session
session = scoped_session(
    # ORM実行時の設定。自動コミットするか、自動反映するなど。
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

# model
Base = declarative_base()
Base.query = session.query_property()
