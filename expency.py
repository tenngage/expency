from argparse import ArgumentParser
from tabulate import tabulate
from typing import Callable, Generator, Tuple
from datetime import datetime
import os
import json

def main():
    homedir_path: str = os.path.expanduser("~")
    DATABASE_PATH: str = os.path.join(homedir_path, "expensy.json")

    database: dict = load_database(DATABASE_PATH)

    supported_queries: dict = get_supported_queries()

    args, query = get_query(supported_queries)

    query(database, **args)
    
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
                "argument": ["--name", "-n"],
                "required": True,
                "help": "Name of an expense"
            },
            {
                "argument": ["--amount", "-a"],
                "required": True,
                "help": "Amount of an expense"
            }],
            "help": "Add your expense"
        },
        "update": {
            "target": update,
            "name_or_flags": [{
                "argument": ["--id", "-i"],
                "required": True,
                "help": "ID of an expense you want to update"
            },
            {
                "argument": ["--new-name"],
                "required": False,
                "help": "Updated name of an expense"
            },
            {
                "argument": ["--new-amount"],
                "required": False,
                "help": "Updated amount of an expense"
            }],
            "help": "Update the expense by it's id"  
        },
        "delete": {
            "target": delete,
            "name_or_flags": [{
                "argument": ["--id", "-i"],
                "required": True,
                "help": "ID of an expense you want to delete"
            }],
            "help": "Delete the expense by it's id"
        },
        "list": {
            "target": list_expenses,
            "name_or_flags": [{
                "argument": ["--month", "-m"],
                "required": False,
                "help": "Choose month to display specified expenses"
            }],
            "help": "List all expenses"
        }
    }

def get_query(supported_queries: dict) -> Tuple[dict, Callable[..., None]]:
    parser: ArgumentParser = ArgumentParser(description="CLI application to manage your expenses")
    subparsers = parser.add_subparsers(dest="command", required=True)

    for command, args in supported_queries.items():
        new_parser = subparsers.add_parser(command, help=args["help"])
        for arg in args["name_or_flags"]:
            new_parser.add_argument(*arg["argument"], required=arg["required"], help=arg["help"])

    args: dict = parser.parse_args().__dict__
    query: Callable[..., None] = supported_queries[args.pop("command")]["target"]
    return args, query

def add(database: dict, name: str, amount: str) -> None:
    today = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    id: str = str(max(0, len(database.keys())) + 1)
    database[id] = {
        "name": name,
        "amount": amount,
        "created at": today
    }

def update(database: dict, id: str, new_name: str, new_amount: str) -> None:
    database[id]["name"] = new_name
    database[id]["amount"] = new_amount

def delete(database: dict, id: str) -> None:
    del database[id]

def list_expenses(database: dict, month: str) -> None:
    if month is None:
        month = "all"
    table: Generator = ({
        "id": index,
        "name": properties["name"],
        "amount": properties["amount"],
        "created at": properties["created at"]
    }
        for index, properties in database.items()
        if month == "all" or month == database[index]["created at"].split("-")[1]
    )
    print(tabulate(table, headers="keys", tablefmt="rounded_outline"))

if __name__ == "__main__":
    main()