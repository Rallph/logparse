import unittest
import logparse.parse as parse
from logparse.entries import LogEntry
import io

class TestParseLogLine(unittest.TestCase):

    def test_parse_log_line_valid_input(self):

        log_line = "2021-02-09 13:11:29.123	test log entry"
        entry = parse.parse_log_line(log_line)
        self.assertIsInstance(entry, LogEntry)
        
    def test_parse_log_line_invalid_input(self):
        not_log_line = "This is not a valid log entry"
        entry = parse.parse_log_line(not_log_line)
        self.assertEqual(entry, None)

class TestParseLogFile(unittest.TestCase):


    def test_parse_log_file_contiguous_entries(self):
        lines = [
            '2021-02-09 13:10:55.909 test entry 1',
            '2021-02-09 13:10:56.012 test entry 2',
            '2021-02-09 13:10:56.018 test entry 3'
        ]

        log_file = io.StringIO('\n'.join(lines))
        entries = parse.parse_log_file(log_file)

        self.assertEqual(len(entries), 3)
        for entry in entries:
            self.assertIsInstance(entry, LogEntry)

    def test_parse_log_file_divided_entries(self):
        lines = [
            '2021-02-09 13:10:55.909 test entry 1',
            'not an entry',
            '2021-02-09 13:10:56.012 test entry 2',
            'not an entry',
            'not an entry',
            '2021-02-09 13:10:56.018 test entry 3'
        ]

        log_file = io.StringIO('\n'.join(lines))
        entries = parse.parse_log_file(log_file)

        self.assertEqual(len(entries), 3)
        for entry in entries:
            self.assertIsInstance(entry, LogEntry)
        
    def test_parse_log_file_no_entries(self):
        lines = [
            'not an entry',
            'not an entry',
            'not an entry'
        ]

        log_file = io.StringIO('\n'.join(lines))
        entries = parse.parse_log_file(log_file)

        self.assertEqual(len(entries), 0)
