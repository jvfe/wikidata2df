#!/usr/bin/env python

"""Tests for `wikidata2df` package."""

import pytest
from pytest import raises
import pandas as pd
from requests.exceptions import HTTPError
from wikidata2df import wikidata2df

cat_query = """#Cats
SELECT ?item ?itemLabel 
WHERE 
{
  ?item wdt:P31 wd:Q146.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}
"""

horse_query = """#Horses (showing some info about them)
#Illustrates optional fields, instances of subclasses, date to year conversion
#Horses on Wikidata
SELECT DISTINCT ?horse ?horseLabel ?mother ?father (year(?birthdate) as ?birthyear) (year(?deathdate) as ?deathyear) ?genderLabel
WHERE
{
  ?horse wdt:P31/wdt:P279* wd:Q726 .     
   
  OPTIONAL{?horse wdt:P25 ?mother .}
  OPTIONAL{?horse wdt:P22 ?father .}
  OPTIONAL{?horse wdt:P569 ?birthdate .}
  OPTIONAL{?horse wdt:P570 ?deathdate .}
  OPTIONAL{?horse wdt:P21 ?gender .}      
 
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "en,en"
  }
}
ORDER BY ?horse"""


def test_wikidata2df_cat():

    cat_result = wikidata2df(cat_query)

    cat_columns = cat_result.columns.values.tolist()

    expected = ["item", "itemLabel"]

    assert set(cat_columns) == set(expected)


def test_wikidata2df_horse():

    horse_result = wikidata2df(horse_query)

    horse_columns = horse_result.columns.values.tolist()

    expected = [
        "horse",
        "horseLabel",
        "mother",
        "father",
        "birthyear",
        "deathyear",
        "genderLabel",
    ]

    assert set(horse_columns) == set(expected)


def test_fake_query():

    fake_query = "I am very fake, make me throw an error"
    with raises(HTTPError):
        wikidata2df(fake_query)
