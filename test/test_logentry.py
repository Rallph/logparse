import unittest
import log_entries
import datetime

class TestLogEntry(unittest.TestCase):

    def test_constructor(self):
        """Test that LogEntry constructor correctly constructs an object given a properly formatted datetime string and message string"""
        timestamp = "2021-02-09 13:10:55.876"
        content = "CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1"

        log_entry = log_entries.LogEntry(timestamp, content)

        self.assertEqual(log_entry.timestamp, datetime.datetime(2021, 2, 9, 13, 10, 55, 876000))
        self.assertEqual(log_entry.content, content)

if __name__ == '__main__':
    unittest.main()
