import unittest
import logparse.parse as parse
from logparse.entries import LogEntry
import datetime

class TestLogEntry(unittest.TestCase):

    def test_constructor(self):
        """Test that LogEntry constructor correctly constructs an object given a properly formatted datetime string and message string"""
        timestamp = "2021-02-09 13:10:55.876"
        content = "CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1"

        log_entry = LogEntry(timestamp, content)

        self.assertEqual(log_entry.timestamp, datetime.datetime(2021, 2, 9, 13, 10, 55, 876000))
        self.assertEqual(log_entry.content, content)


    def test_from_log_string(self):
        """Test that LogEntry.from_log_string creates a new LogEntry object from a raw log string"""
        log_string = "2021-02-09 13:10:55.876		CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1"
        expected_content = "CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1"

        log_entry = LogEntry.from_log_string(log_string)
        self.assertEqual(log_entry.timestamp, datetime.datetime(2021, 2, 9, 13, 10, 55, 876000))
        self.assertEqual(log_entry.content, expected_content)

if __name__ == '__main__':
    unittest.main()
