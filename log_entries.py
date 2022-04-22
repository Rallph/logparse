import re


class LogEntry(object):


    LOG_ENTRY_REGEX = re.compile(r'(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}.\d{3})\s*(.*)')

    def __init__(self, timestamp, content):
        self.timestamp = timestamp
        self.content = content
