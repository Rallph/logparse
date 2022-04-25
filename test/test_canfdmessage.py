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
