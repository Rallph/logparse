import re
from logparse.entries import log_entry

class CANFDMessage(log_entry.LogEntry):
    
    CAN_FD_ENTRY_REGEX = re.compile(r"""
        CAN-FD\s            # CAN-FD protocol string
        (\d+)\s             # Test case number
        (Tx|Rx)\s           # Message direction
        ([0-9A-F]+)\s*      # Frame bytes
        (\d+)\s*            # Message byte length
        ([0-9A-F ]+)\b\s*   # Message bytes
        (.*)                # Message string
    """, re.VERBOSE)

    lol = '2021-02-09 13:10:55.876		CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1'

    def __init__(self, timestamp, original_str, test_num, msg_dir, frame_bytes, msg_length, msg_bytes, msg_str):
        super().__init__(timestamp, original_str)
        self.test_num = test_num
        self.msg_dir = msg_dir
        self.frame_bytes = frame_bytes
        self.msg_length = msg_length
        self.msg_bytes = msg_bytes
        self.msg_str = msg_str

    @classmethod
    def from_log_string(cls, log_string):
        timestamp, original_str = cls.LOG_ENTRY_REGEX.findall(log_string)[0]
        test_num, msg_dir, frame_bytes, msg_length, msg_bytes, msg_str = cls.CAN_FD_ENTRY_REGEX.findall(log_string)[0]
        
        test_num = int(test_num)
        msg_length = int(msg_length)

        return cls(timestamp, original_str, test_num, msg_dir, frame_bytes, msg_length, msg_bytes, msg_str)
