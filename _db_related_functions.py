import os
import sqlite3

from constants import DATABASE_NAME, TABLE_NAME


def set_up_a_connection(database=DATABASE_NAME):
    """
    Sets up a connection to a database.
    If the latter doesn't exist - it creates it.
    You must create a constant DATABSE_NAME in constants.py as a fallback
    
    Returns connection and cursor
    """
    connection = sqlite3.connect(f"{os.path.join(os.getcwd(), database)}.db")
    return connection, connection.cursor()


def create_a_table(database=None, table_name=None, columns=None):
    """
    Creates a table with name TABLE_NAME from _constants.
    It uses TABLE_COLUMNS from constants.

    :type database: str
    :type table_name: str
    :type columns: dict
    """
    connection, cursor = set_up_a_connection(database)

    table_columns = ""
    for index, name in enumerate(columns):
        table_columns += f"{name} {columns[name]}{', ' if index + 1 != len(columns) else ''}"

    with connection:
        cursor.execute(f"create table {table_name} ({table_columns})")


def add_values_to_db(*args, table_name=TABLE_NAME):
    """
    Accepts any number of values.
    You must create a constant TABLE_NAME in constants.py as a fallback
    """
    connection, cursor = set_up_a_connection()

    with connection:
        values = ''
        for index, value in enumerate(*args):
            value.replace('"', "'")
            if index + 1 != len(args):
                values += f'"{value}"'
            else:
                values += f'"{value}", '

        cursor.execute(f"insert into {table_name} values({values})")


def update_one_value(new_value, column1, column2, column2_value, table_name=TABLE_NAME):
    connection, cursor = set_up_a_connection()

    with connection:
        new_value.replace('"', "'")
        cursor.execute(f'''UPDATE {table_name} SET {column1} = "{new_value}" WHERE {column2} = "{column2_value}"''')


def get_value(target_column, column, column_value, table_name=TABLE_NAME):
    """
    You must create a constant TABLE_NAME in constants.py as a fallback
    """
    _, cursor = set_up_a_connection()

    try:
        albums = cursor.execute(
            f"select {target_column} from {table_name} where {column} = '{column_value}'").fetchall()
        return [item[0] for item in albums]
    except TypeError:
        return None
