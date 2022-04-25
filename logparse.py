#! /usr/bin/env python3
import argparse
import logparse.parse as parse
import sys

def main():
    arg_parser = argparse.ArgumentParser(
        description="Simple utility for parsing test log files and calculating Denial of Service (DoS) times for failed test cases"
    )
    
    arg_parser.add_argument('log_file', help='The input log file to be parsed')
    arg_parser.add_argument('-o', '--out-file', action='store',dest='out_file', help='File where log analysis results will be stored. By default output stored in {log_file}_analyzed.out if no file specified')
    args = arg_parser.parse_args()
    entries = []
    
    try:
        with open(args.log_file, 'r') as log_file:
            entries = parse.parse_log_file(log_file)
    except UnicodeError:
        print("ERROR: Specified log file cannot be read")
        sys.exit(1)

    case_groups = parse.divide_into_can_fd_test_cases(entries)

    deltas = []

    for case, case_messages in case_groups:
        delta = parse.compute_test_case_dos_time(case_messages)
        if delta:
            deltas.append((case, delta))

    if args.out_file:
        outfile_name = args.out_file
    else:
        outfile_name = f'{args.log_file}_analyzed.out'

    with open(outfile_name, 'w') as outfile:
        outfile.write(f"{args.log_file}: {len(case_groups) - 1} tests, {len(deltas)} failures\n")
        outfile.write('---\nTest Failures\n---\n')
        for case, delta in deltas:
            outfile.write(f"Test case {case}: DoS time {delta}\n")
        outfile.write('---\n')
    

if __name__ == "__main__":
    main()