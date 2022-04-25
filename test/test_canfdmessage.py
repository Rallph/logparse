import unittest
from logparse.entries import CANFDMessage
import datetime

class TestCANFDMessage(unittest.TestCase):

    def test_constructor(self):
        timestamp = "2021-02-09 13:10:55.876"
        content = "CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1"
        test_num = 0
        msg_dir = 'Tx'
        frame_bytes = '11111111'
        msg_length = 8
        msg_bytes = '02 10 03 00 00 00 00 00'
        msg_str = 'Instrumentation | Attempt | Instrumentation request_14DA45F1'

        can_fd_message = CANFDMessage(timestamp, content, test_num, msg_dir, frame_bytes, msg_length, msg_bytes, msg_str)

        self.assertEqual(can_fd_message.timestamp, datetime.datetime(2021, 2, 9, 13, 10, 55, 876000))
        self.assertEqual(can_fd_message.content, content)
        self.assertEqual(can_fd_message.test_num, test_num)
        self.assertEqual(can_fd_message.msg_dir, msg_dir)
        self.assertEqual(can_fd_message.frame_bytes, frame_bytes)
        self.assertEqual(can_fd_message.msg_length, msg_length)
        self.assertEqual(can_fd_message.msg_bytes, msg_bytes)
        self.assertEqual(can_fd_message.msg_str, msg_str)

    def test_from_log_string(self):
        log_string = "2021-02-09 13:10:55.876		CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1"
        
        timestamp = "2021-02-09 13:10:55.876"
        content = "CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1"
        test_num = 0
        msg_dir = 'Tx'
        frame_bytes = '11111111'
        msg_length = 8
        msg_bytes = '02 10 03 00 00 00 00 00'
        msg_str = 'Instrumentation | Attempt | Instrumentation request_14DA45F1'

        can_fd_message = CANFDMessage.from_log_string(log_string)

        self.assertEqual(can_fd_message.timestamp, datetime.datetime(2021, 2, 9, 13, 10, 55, 876000))
        self.assertEqual(can_fd_message.content, content)
        self.assertEqual(can_fd_message.test_num, test_num)
        self.assertEqual(can_fd_message.msg_dir, msg_dir)
        self.assertEqual(can_fd_message.frame_bytes, frame_bytes)
        self.assertEqual(can_fd_message.msg_length, msg_length)
        self.assertEqual(can_fd_message.msg_bytes, msg_bytes)
        self.assertEqual(can_fd_message.msg_str, msg_str)


class TestDivideIntoTestCases(unittest.TestCase):

    def test_divide_into_test_cases_normal(self):
        lines = [
            '2021-02-09 13:10:55.876		CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1',
            '2021-02-09 13:10:55.878		CAN-FD	0	Rx	99999999  	8	06 50 03 00 64 01 F4 55                 	Instrumentation | Response | Instrumentation response_14DA45F1',
            '2021-02-09 13:10:55.909		CAN-FD	1	Tx	F3794DC   	10	17 5F E5 45 6F 98 5D AD 0D 42 A0 D7 00 5C D5 F7 	CAN_FD_raw_frame_invalid_frame | ID1_dlc_=_data | _14DA45F1',
            '2021-02-09 13:10:56.012		CAN-FD	1	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Instrumentation after | Instrumentation request_14DA45F1',
            '2021-02-09 13:10:56.018		CAN-FD	1	Rx	99999999  	8	06 50 03 00 64 01 F4 55                 	Instrumentation | Response | Instrumentation response_14DA45F1'
        ]

        can_fd_messages = [CANFDMessage.from_log_string(line) for line in lines]

        organized = CANFDMessage.divide_into_can_fd_test_cases(can_fd_messages)

        case_0_messages = organized[0][1]
        self.assertEqual(2, len(case_0_messages))
        for msg in case_0_messages:
            self.assertEqual(msg.test_num, 0)

        case_1_messages = organized[1][1]
        self.assertEqual(3, len(case_1_messages))
        for msg in case_1_messages:
            self.assertEqual(msg.test_num, 1)
            
