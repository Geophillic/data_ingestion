def read_from_web_CSV(URL):
    """
    Load a data from web using the web link, and convert it to a csv data file

    Args:
        URL (str): contain link to the web, where data will be loaded
    """
    try:
        df = pd.read_csv(URL)
        logger.info("CSV file read successfully from the web.")
        return df
    except pd.errors.EmptyDataError as e:
        logger.error("The URL does not point to a valid CSV file. Please check the URL and try again.")
        raise e
    except Exception as e:
        logger.error(f"Failed to read CSV from the web. Error: {e}")
        raise e