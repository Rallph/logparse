"""
Parse log file contents into Python objects

See module entries for supported log message types

Functions:

    parse_log_line(string) -> entries.LogEntry
    parse_log_file(file) -> [entries.LogEntry]

"""


from .entries import LogEntry


def parse_log_line(log_line):
    """
    Determines the log entry type of the provided string and parses it into the corresponding object type
    See module entries for log message object types


    Paramters
    ---------

        log_line : str
            A line of a log file containing a log message to be parsed into a Python object

    Returns
    -------
        LogEntry (or subclass): The Python object representation of the log message
        None: if argument 'log_line' cannot be parsed into a log entry
    """


    if LogEntry.LOG_ENTRY_REGEX.match(log_line):
        return LogEntry.from_log_string(log_line)

def parse_log_file(log_file):
    """
    Parses a file of log messages into Python objects. Parses lines in sequential order by calling 'parse_log_line' on each line

    Parameters
    ----------
        log_file : TextIOBase
            The log file to parse as an opened file object

    Returns
    -------
        entries : [LogEntry]
            List of LogEntry (or subclassed) objects parsed from the file
    """


    entries = []
    for line in log_file.readlines():
        entry = parse_log_line(line)

        if entry:
            entries.append(entry)

    return entries