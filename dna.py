import csv
import sys

def main():
    # TODO: Check for proper usage

    # TODO: Read database file and DNA sequence file

    # TODO: Find longest match of each STR in DNA sequence

    # TODO: Check database for matching profiles

    return

def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subseq_length = len(subsequence)
    seq_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(seq_length):

        count = 0

        # Check for a match and continue checking until out of consecutive matches
        while True:

            # Adjust window start and end
            start = i + count * subseq_length
            end = start + subseq_length

            # If there is a match in the window
            if sequence[start:end] == subsequence:
                count += 1
            
            # If there is no match in the window
            else:
                break
        
        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run

if __name__ == "__main__":
    main()