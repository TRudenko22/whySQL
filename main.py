#!/bin/python

from tabulate import tabulate
from init import *
import typer
import json
import pretty_errors

app = typer.Typer()

@app.command()
def insert(field1, field2, field3, field4) -> None:
    """ Insert a record into JSON file.
    """
    record = {col_1: field1, col_2: field2, col_3: field3, col_4: field4}

    data = open_db()
    data.append(record)

    writeJSON(data, 'db.json')


@app.command()
def qn(name) -> None:
    """ Query by string.
    """
    
    data = open_db()

    query = []
    for index in range(len(data)):
        if data[index][field1].lower() == name.lower():
            query.append(data[index])

        elif data[index][field2].lower() == name.lower():
                    query.append(data[index])

    if query:
        print(tabulate(query, headers='keys', tablefmt='fancy_grid', showindex=True))
    else:
        print("No Results found")


@app.command()
def show() -> None:
    """ Show JSON data in fancy grid format.
    """
    
    print(title)
    print(tabulate(open_db(), headers='keys', tablefmt='fancy_grid', showindex=True))


@app.command()
def delete(index):
    """ Delete record in JSON file by index
    """
    
    data = open_db()
    data.pop(int(index))
    writeJSON(data,'db.json')


def writeJSON(data, sFile_name):
    with open(sFile_name, 'w') as db:
        json.dump(data, db, indent=4)


def open_db() -> list:
    with open('db.json') as db:
        return json.load(db)


if __name__ == '__main__':
    app()
