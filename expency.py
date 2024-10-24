from argparse import ArgumentParser
from tabulate import tabulate
import os
import json

def main():
    homedir_path: str = os.path.expanduser("~")
    DATABASE_PATH: str = os.path.join(homedir_path, "expensy.json")

    database: dict = load_database(DATABASE_PATH)

    supported_queries = get_supported_queries()

    get_query(supported_queries)

    save_database(DATABASE_PATH, database)



def load_database(DATABASE_PATH: str) -> dict:
    try:
        with open(DATABASE_PATH) as f:
            database: dict = json.load(f)
    except:
        database: dict = {}
    return database

def save_database(DATABASE_PATH: str, database: dict) -> None:
    with open(DATABASE_PATH, "w") as f:
        json.dump(database, f, indent=4)

def get_supported_queries() -> dict:
    pass

def get_query(supported_queries: dict):
    pass

def add():
    pass

def update():
    pass

def delete():
    pass

def list_expances():
    pass

if __name__ == "__main__":
    main()