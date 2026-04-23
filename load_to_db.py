from pathlib import Path
import os

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL


load_dotenv()


def get_required_env(name: str) -> str:
    value = os.getenv(name)
    if value is None or value == "":
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def build_database_url() -> URL:
    password = os.getenv("POSTGRES_PASSWORD") or None

    return URL.create(
        drivername="postgresql+psycopg",
        username=get_required_env("POSTGRES_USER"),
        password=password,
        host=get_required_env("POSTGRES_HOST"),
        port=int(get_required_env("POSTGRES_PORT")),
        database=get_required_env("POSTGRES_DB"),
    )


def main() -> None:
    csv_path = Path(os.getenv("CSV_PATH", "navigation_ab_test.csv"))
    schema = os.getenv("POSTGRES_SCHEMA", "public")
    table = os.getenv("POSTGRES_TABLE", "navigation_ab_test")
    if_exists = os.getenv("POSTGRES_IF_EXISTS", "replace")
    sslmode = os.getenv("POSTGRES_SSLMODE", "prefer")

    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    df = pd.read_csv(
        csv_path,
        parse_dates=["timestamp"],
        true_values=["TRUE", "true", "True"],
        false_values=["FALSE", "false", "False"],
    )

    engine = create_engine(
        build_database_url(),
        connect_args={"sslmode": sslmode},
    )

    with engine.begin() as connection:
        connection.execute(text(f'CREATE SCHEMA IF NOT EXISTS "{schema}"'))
        df.to_sql(
            table,
            con=connection,
            schema=schema,
            if_exists=if_exists,
            index=False,
            chunksize=1_000,
            method="multi",
        )

    print(f"Loaded {len(df):,} rows into {schema}.{table} from {csv_path}")


if __name__ == "__main__":
    main()
