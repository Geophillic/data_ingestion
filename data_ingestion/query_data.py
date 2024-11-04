def query_data(engine, sql_query):
    """
    Load and data from the connected database using the created engine as input, sql_query(text).

    Args:
        engine (str): SQL engine connection that contain the loaded data file.
        sql_query (text, str): SQL query in string, ready to be executed.

    Returns:
        pandas.DatatFrame: DataFrame containing the query result

    """
    try:
        with engine.connect() as connection:
            df = pd.read_sql_query(text(sql_query), connection)
        if df.empty:
            # Log a message or handle the empty DataFrame scenario as needed
            msg = "The query returned an empty DataFrame."
            logger.error(msg)
            raise ValueError(msg)
        logger.info("Query executed successfully.")
        return df
    except ValueError as e: 
        logger.error(f"SQL query failed. Error: {e}")
        raise e
    except Exception as e:
        logger.error(f"An error occurred while querying the database. Error: {e}")
        raise e