#!/bin/python

from tabulate import tabulate
import typer
import json
import pretty_errors

app = typer.Typer()

@app.command()
def insert(first: str, last: str, dob: str, phone: str) -> None:
    record = {"First": first, "Last":last, "DOB":dob, "phone": phone}

    data = open_db()
    data.append(record)

    writeJSON(data, 'db.json')


@app.command()
def qn(name: str) -> None:
    data = open_db()
    
    query = []
    for index in range(len(data)):
        if data[index]["First"].lower() == name.lower():
            query.append(data[index])
        
        elif data[index]["Last"].lower() == name.lower():
                    query.append(data[index])
    
    if query:
        print(tabulate(query, headers='keys', tablefmt='fancy_grid', showindex=True))
    else:
        print("No Results found")


@app.command()
def show() -> None:
    print(tabulate(open_db(), headers='keys', tablefmt='fancy_grid', showindex=True))

def writeJSON(data, sFile_name):
    with open(sFile_name, 'w') as db:
        json.dump(data, db, indent=4)


def open_db() -> list:
    with open('db.json') as db:
        return json.load(db)


if __name__ == '__main__':
    app()
