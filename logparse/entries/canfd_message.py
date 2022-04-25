import re
from logparse.entries import log_entry

class CANFDMessage(log_entry.LogEntry):
    """
    Python object representation of a CAN-FD protocol message parsed from a log file.

    Class variables
    ---------------
    CAN_FD_ENTRY_REGEX : re.Pattern
        The regular expression that matches CAN-FD message entries in a log file

    Attributes
    ----------
        test_num : int 
            Test case number of the CAN-FD message
        msg_dir : str
            CAN-FD message direction. Either 'Tx' or 'Rx'
        frame_bytes : str
            Bytes of the CAN-FD frame
        msg_length : int
            The length of the CAN-FD message
        msg_bytes : str
            The bytes of the CAN-FD message
        msg_str : str
            The string interpretation of the CAN-FD message bytes

    """
    
    CAN_FD_ENTRY_REGEX = re.compile(r"""
        CAN-FD\s            # CAN-FD protocol string
        (\d+)\s             # Test case number
        (Tx|Rx)\s           # Message direction
        ([0-9A-F]+)\s*      # Frame bytes
        (\d+)\s*            # Message byte length
        ([0-9A-F ]+)\b\s*   # Message bytes
        (.*)                # Message string
    """, re.VERBOSE)

    def __init__(self, timestamp, original_str, test_num, msg_dir, frame_bytes, msg_length, msg_bytes, msg_str):
        super().__init__(timestamp, original_str)
        self.test_num = test_num
        self.msg_dir = msg_dir
        self.frame_bytes = frame_bytes
        self.msg_length = msg_length
        self.msg_bytes = msg_bytes
        self.msg_str = msg_str

    def is_request(self):
        """
        Determine whether the CANFDMessage object is a request message

        Returns
        -------
            bool : True if the object is a request message, False if it isn't
        """
        return self.msg_dir == 'Tx' and self.frame_bytes == '11111111' and self.msg_bytes == '02 10 03 00 00 00 00 00'

    def is_response(self):
        """
        Determine whether the CANFDMessage object is a response message

        Returns
        -------
            bool : True if the object is a response message, False if it isn't 
        """
        return self.msg_dir == 'Rx' and self.frame_bytes == '99999999' and self.msg_bytes == '06 50 03 00 64 01 F4 55'

    @classmethod
    def from_log_string(cls, log_string):
        """
        Creates a new CANFDMessage object from a raw log string (a line of the log file)

        Parameters
        ----------
            log_string : str
                A string containing a timestamp of the format %Y-%m-%d %H:%M:%S.%f followed by a CAN-FD protocol message

                Example: 2021-02-09 13:10:55.876		CAN-FD	0	Tx	11111111  	8	02 10 03 00 00 00 00 00                 	Instrumentation | Attempt | Instrumentation request_14DA45F1

        Returns
        -------
        CANFDMessage: New CANFDMessage object representing the message in the log string
        """
        
        timestamp, original_str = cls.LOG_ENTRY_REGEX.findall(log_string)[0]
        test_num, msg_dir, frame_bytes, msg_length, msg_bytes, msg_str = cls.CAN_FD_ENTRY_REGEX.findall(log_string)[0]
        
        test_num = int(test_num)
        msg_length = int(msg_length)

        return cls(timestamp, original_str, test_num, msg_dir, frame_bytes, msg_length, msg_bytes, msg_str)
