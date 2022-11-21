# logparse

A simple tool to parse log files containing test case output with CAN-FD protocol messages and calculate Denial of Service times for failing tests. Only supports test cases using the CAN-FD protocol at the moment, but can be easily extended to support additional protocols. Created for a take home assignment given by ETAS / ESCRYPT.
#

Usage:

```
$ ./logparse.py inputFile.log
```

Run
```
$ ./logparse.py -h
```

To see help information

## Tests

Run 
```
python3 -m unittest discover -s test/unit/
```

To run test cases



