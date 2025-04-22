def rowcount_handler(cursor: object) -> int:
    """
    Return the number of rows affected by the last SQL statement.
    """
    return cursor.rowcount