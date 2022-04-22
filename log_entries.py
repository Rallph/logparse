import re
import datetime

class LogEntry(object):


    LOG_ENTRY_REGEX = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3})\s*(.*)')

    def __init__(self, timestamp, content):
        self.timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")
        self.content = content

    @classmethod
    def from_log_string(cls, log_string):
        timestamp, content = cls.LOG_ENTRY_REGEX.findall(log_string)[0]
        return cls(timestamp, content)