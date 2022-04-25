"""
Parse log file contents into Python objects

See module entries for supported log message types

Functions:

    parse_log_line(string) -> entries.LogEntry
    parse_log_file(file) -> [entries.LogEntry]

"""


from logparse import entries
import itertools


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

    if entries.CANFDMessage.CAN_FD_ENTRY_REGEX.search(log_line):
        return entries.CANFDMessage.from_log_string(log_line)
    elif entries.LogEntry.LOG_ENTRY_REGEX.search(log_line):
        return entries.LogEntry.from_log_string(log_line)
    

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

def divide_into_can_fd_test_cases(log_entries):
        can_fd_entries = [entry for entry in log_entries if isinstance(entry, entries.CANFDMessage)]
        divided_entries_iterator = itertools.groupby(can_fd_entries, lambda msg: msg.test_num)
        
        organized_entries = [(test_num, list(can_fd_messages)) for test_num, can_fd_messages in divided_entries_iterator]
        return organized_entries


def compute_test_case_dos_time(test_case_messages):
    initial_request = next(filter(lambda msg : msg.is_request() , test_case_messages), None)
    response = next(filter(lambda msg : msg.is_response(), test_case_messages), None)

    if not initial_request or not response:
        return None

    if test_case_messages.index(response) != (test_case_messages.index(initial_request) + 1):
        delta = response.timestamp - initial_request.timestamp
        return delta