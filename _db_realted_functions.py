import sqlite3

from _constants import PATH_TO_DB, TABLE_NAME, TABLE_COLUMNS


def set_up_a_connection():
    """
    Sets up a connection to a database.
    If the latter doesn't exist - it creates it.
    The method uses PATH_TO_DB variable from _constants.
    
    Returns connection and cursor
    """
    connection = sqlite3.connect(PATH_TO_DB)
    return connection, connection.cursor()


def create_a_table():
    """
    Creates a table with name TABLE_NAME from _constants.
    It uses TABLE_COLUMNS from constants.
    """
    connection, cursor = set_up_a_connection()

    table_columns = ""
    for index, name in enumerate(TABLE_COLUMNS):
        table_columns += f"{name} {TABLE_COLUMNS[name]}{', ' if index + 1 != len(TABLE_COLUMNS) else ''}"

    with connection:
        cursor.execute(f"create table {TABLE_NAME} ({table_columns})")


def add_value_to_db(band, album):
    """
    Adds a value to a table TABLE_NAME from constants

    """
    connection, cursor = set_up_a_connection()
    with connection:
        cursor.execute(f"""insert into {TABLE_NAME} values("{band}", "{album}")""")


def get_value(target_column, column, column_value):
    _, cursor = set_up_a_connection()
    try:
        albums = cursor.execute(f"select {target_column} from {TABLE_NAME} where {column} = '{column_value}'").fetchall()
        return [item[0] for item in albums]
    except TypeError:
        return None
