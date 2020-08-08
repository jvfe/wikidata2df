#!/usr/bin/env python

"""Console script for wikidata2df."""

import argparse
import sys
from wikidata2df import wikidata2df
import pandas as pd


def main():
    """Console script for wikidata2df."""
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-q", "--query", help="A path to a file containing a valid SPARQL query"
    )
    parser.add_argument("-o", "--outfile", help="Path to the output csv file")
    args = parser.parse_args()

    if len(sys.argv) != 5:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        wikidata2csv(args.query, args.outfile)

    return 0


def wikidata2csv(query_file, outfile):
    """Runs a wikidata query from a file

    Args: 
        query_file(str): A path to a text file containing a valid SPARQL query
        outfile(str): A path to the output csv file
    
    """
    with open(query_file, "r") as q:
        query_string = q.read()

    results = wikidata2df(query_string)

    results.to_csv(path_or_buf=outfile, index=False)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
