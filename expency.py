from argparse import ArgumentParser
from tabulate import tabulate
import os
import json

def main():
    homedir_path: str = os.path.expanduser("~")
    DATABASE_PATH: str = os.path.join(homedir_path, "expensy.json")

    database: dict = load_database(DATABASE_PATH)

    supported_queries = get_supported_queries()

    args, query = get_query(supported_queries)
    print(args)
    print(query)
    

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
    return {
        "add": {
            "target": add,
            "name_or_flags": [{
                "argument": "name",
                "help": "Name of an expense"
            },
            {
                "argument": "amount",
                "help": "Amount of an expense"
            }],
            "help": "Add your expense"
        },
        "update": {
            "target": update,
            "name_or_flags": [{
                "argument": "id",
                "help": "ID of an expense you want to update"
            },
            {
                "argument": "new_name",
                "help": "Updated name of an expense"
            },
            {
                "argument": "new_amount",
                "help": "Updated amount of an expense"
            }],
            "help": "Update the expense by it's id"  
        },
        "delete": {
            "target": delete,
            "name_or_flags": [{
                "argument": "id",
                "help": "ID of an expense you want to delete"
            }],
            "help": "Delete the expense by it's id"
        },
        "list": {
            "target": list_expances,
            "name_or_flags": [{
                "argument": "display",
                "help": "Specify what you want to display"
            }],
            "help": "List all expenses"
        }
    }

def get_query(supported_queries: dict):
    parser = ArgumentParser(description="CLI application to manage your expenses")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command, args in supported_queries.items():
        new_parser = subparsers.add_parser(command, help=args["help"])
        for arg in args["name_or_flags"]:
            new_parser.add_argument(arg["argument"], help=arg["help"])

    args = parser.parse_args().__dict__
    query = supported_queries[args["command"]]["target"]
    return args, query

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