"""Tests for `wikidata2csv` cli."""

import pytest
from wikidata2df.cli import wikidata2csv
from tempfile import NamedTemporaryFile


def test_wdt2csv():
    result = NamedTemporaryFile(suffix=".csv").name
    wikidata2csv(query_file="tests/cats.rq", outfile=result)
