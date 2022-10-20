from functools import lru_cache
import csv


@lru_cache
def read(path):
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path, encoding="utf-8") as file:
        csv_reader = csv.reader(file, delimiter=",")
        header, *jobs = csv_reader

    result = [{header[i]: job[i] for i in range(len(header))} for job in jobs]

    return result
