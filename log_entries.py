import re
import datetime

class LogEntry(object):
    """
    A class to represent a generic entry in a log file. A log entry is characterized by
    a string consisting of a datetime stamp followed by arbitrary text

    Attributes
    ----------
    timestamp : datetime.datetime
        The date and time the entry was logged
    content : str
        The logged message
    """

    LOG_ENTRY_REGEX = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3})\s*(.*)')

    def __init__(self, timestamp, content):
        """
        Parses the provided timestamp and constructs a LogEntry object

        Parameters
        ----------
            timestamp : str
                Datetime stamp in the format %Y-%m-%d %H:%M:%S.%f
                See the datetime module for more info
            content : str
                The message that was logged

        """
        self.timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
        self.content = content

    @classmethod
    def from_log_string(cls, log_string):
        """
        Creates a new LogEntry object from a raw log string (a line of the log file)

        Parameters
        ----------
            log_string : str
                A string containing a timestamp of the format %Y-%m-%d %H:%M:%S.%f followed by arbitrary text

                Example: 2021-02-09 13:11:29.123	gotcha

        Returns
        -------
        LogEntry: New LogEntry object with the timestamp and content parsed from the log string 
        """
        timestamp, content = cls.LOG_ENTRY_REGEX.findall(log_string)[0]
        return cls(timestamp, content)