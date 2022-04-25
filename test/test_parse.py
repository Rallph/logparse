import unittest
import logparse.parse as parse
from logparse.entries import LogEntry, CANFDMessage
import io
from datetime import timedelta

class TestParseLogLine(unittest.TestCase):

    def test_parse_log_line_valid_input(self):

        log_line = "2021-02-09 13:11:29.123	test log entry"
        entry = parse.parse_log_line(log_line)
        self.assertIsInstance(entry, LogEntry)
        
    def test_parse_log_line_invalid_input(self):
        not_log_line = "This is not a valid log entry"
        entry = parse.parse_log_line(not_log_line)
        self.assertEqual(entry, None)

    def test_parse_log_line_canfd_message(self):
        can_fd_line = "2021-02-09 13:10:55.876		CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1"
        entry = parse.parse_log_line(can_fd_line)
        self.assertIsInstance(entry, CANFDMessage)

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

class TestComputeDosTime(unittest.TestCase):

    def test_compute_dos_time_dos_present(self):

        lines = [
            "2021-02-09 13:10:56.349		CAN-FD	5	Tx	28C       	1	80                                      	CAN_FD_raw_frame_invalid_frame | ID5_80_based_pattern_data | _14DA45F1",
            "2021-02-09 13:10:56.453		CAN-FD	5	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Instrumentation after | Instrumentation request_14DA45F1",
            "2021-02-09 13:10:56.560		CAN-FD	5	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1",
            "2021-02-09 13:10:56.661		CAN-FD	5	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1",
            "2021-02-09 13:11:16.637		CAN-FD	5	Rx	99999999  	8	06 50 03 00 64 01 F4 55                 	Instrumentation | Response | Instrumentation response_14DA45F1"
        ]

        can_fd_msgs = [CANFDMessage.from_log_string(line) for line in lines]

        delta = parse.compute_test_case_dos_time(can_fd_msgs)
        self.assertEqual(delta, timedelta(seconds=20, microseconds=184000))

    def test_compute_dos_time_no_dos(self):
        lines = [
            '2021-02-09 13:10:55.876		CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1',
            '2021-02-09 13:10:55.878		CAN-FD	0	Rx	99999999  	8	06 50 03 00 64 01 F4 55                 	Instrumentation | Response | Instrumentation response_14DA45F1'
        ]

        can_fd_msgs = [CANFDMessage.from_log_string(line) for line in lines]

        delta = parse.compute_test_case_dos_time(can_fd_msgs)
        self.assertIsNone(delta)

    def test_compute_dos_time_no_response(self):
        lines = [
            "2021-02-09 13:10:56.349		CAN-FD	5	Tx	28C       	1	80                                      	CAN_FD_raw_frame_invalid_frame | ID5_80_based_pattern_data | _14DA45F1",
            "2021-02-09 13:10:56.453		CAN-FD	5	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Instrumentation after | Instrumentation request_14DA45F1",
            "2021-02-09 13:10:56.560		CAN-FD	5	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1",
            "2021-02-09 13:10:56.661		CAN-FD	5	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1"
        ]

        can_fd_msgs = [CANFDMessage.from_log_string(line) for line in lines]

        delta = parse.compute_test_case_dos_time(can_fd_msgs)
        self.assertIsNone(delta)