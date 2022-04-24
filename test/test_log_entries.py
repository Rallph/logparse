import unittest
import log_entries

class TestParseLogLine(unittest.TestCase):

    def test_parse_log_line_valid_input(self):

        log_line = "2021-02-09 13:11:29.123	test log entry"
        entry = log_entries.parse_log_line(log_line)
        self.assertIsInstance(entry, log_entries.LogEntry)
        
    def test_parse_log_line_invalid_input(self):
        not_log_line = "This is not a valid log entry"
        entry = log_entries.parse_log_line(not_log_line)
        self.assertEqual(entry, None)
