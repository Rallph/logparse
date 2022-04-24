from .entries import LogEntry


def parse_log_line(log_line):

    if LogEntry.LOG_ENTRY_REGEX.match(log_line):
        return LogEntry.from_log_string(log_line)

def parse_log_file(log_file):

    entries = []
    for line in log_file.readlines():
        entry = parse_log_line(line)

        if entry:
            entries.append(entry)

    return entries