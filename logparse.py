#! /usr/bin/env python3
import argparse


def main():
    arg_parser = argparse.ArgumentParser(
        description="Simple utility for parsing test log files and calculating Denial of Service (DoS) times for failed test cases"
    )
    
    arg_parser.add_argument('LOG_FILE', help='The input log file to be parsed')
    args = arg_parser.parse_args()



if __name__ == "__main__":
    main()