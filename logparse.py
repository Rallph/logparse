#! /usr/bin/env python3
import argparse
import log_entries

def main():
    arg_parser = argparse.ArgumentParser(
        description="Simple utility for parsing test log files and calculating Denial of Service (DoS) times for failed test cases"
    )
    
    arg_parser.add_argument('log_file', help='The input log file to be parsed')
    args = arg_parser.parse_args()



if __name__ == "__main__":
    main()