# Expency: CLI Expense Tracker app

## Description
The Expency CLI is a Python-based command-line tool designed to help users track their expenses. This application allows users to add, delete, update, list, and manage expenses through various commands. It provides a straightforward way to interact with a expense database using a simple CLI interface.

It is inspired from the [Expense Tracker](https://roadmap.sh/projects/expense-tracker) project featured in the [Backend Roadmap](https://roadmap.sh/backend) from [roadmap.sh](https://roadmap.sh/).

## Features
- **Add Expenses**: Easily add new expenses with details such as amount and description.
- **Delete Expenses**: Delete an expense based on its ID.
- **View Expenses**: Display a list of all recorded expenses.
- **Generate Reports**: Create summary reports of expenses over a specified period.

## Installation via **pip**
    pip install git+https://github.com/tenngage/expency.git   


## Usage
Run the application
```      
expency -h # Show help
expency add --name "Dinner" --amount "150" # Add an expense
expency list # List all expenses
expency summary # Show summary of expenses
expency summary --month 10 # Show summary for a specific month
expency delete --id 1 # Delete an expense by ID
```
