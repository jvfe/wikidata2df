"""Main module."""

from collections import defaultdict
from functools import lru_cache
from itertools import product, chain
import pandas as pd
import requests


def perform_query(query):
    """Perform a SPARQL query to the wikidata endpoint.

    A simple request with the header 'Accept' pointing to a json result.

    Args:
        query(str): A string containing a functional sparql query

    Returns:
        A json (dict) with the response content.

    Raises: 
        requests.exceptions.HTTPError
    """

    endpoint_url = "https://query.wikidata.org/sparql"

    try:
        response = requests.get(
            endpoint_url,
            params={"query": query},
            headers={"Accept": "application/sparql-results+json"},
        )
        response.raise_for_status()

    except requests.exceptions.HTTPError as err:
        raise requests.exceptions.HTTPError(err)

    else:
        raw_results = response.json()

        return raw_results


def parse_query_results(query_result):
    """Parse wikidata query json into a nice dataframe
    
    Args:
        query_result(dict): A json dict with the results from the query

    Returns:
        A Pandas DataFrame with the query results.
    """

    parsed_results = defaultdict(list)

    data = query_result["results"]["bindings"]

    keys = frozenset(chain.from_iterable(data))

    for json_key, item in product(data, keys):
        try:
            parsed_results[item].append(json_key[item]["value"])
        except:
            # If there is no data for a key, append None
            parsed_results[item].append(None)

    results_df = pd.DataFrame.from_dict(parsed_results).replace(
        {"http://www.wikidata.org/entity/": ""}, regex=True
    )

    return results_df


@lru_cache(maxsize=10)
def wikidata2df(query):
    """Transform a wikidata SPARQL query into a Pandas DataFrame

    Wrapper function that performs a request to the wikidata endpoint and returns a dataframe. 
    If there is no result found, it will raise an exception. If there were optional
    fields in your query, the result will have rows with value "None", corresponding
    to values that were not found.

    Args:
        query(str): A string containing a valid SPARQL query.

    Returns: 
        A Pandas DataFrame with the results of the query.
    """

    query_res = perform_query(query)

    parsed_res = parse_query_results(query_res)

    return parsed_res
