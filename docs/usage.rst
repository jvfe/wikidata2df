=====
Usage
=====

To use wikidata2df in a project::

    from wikidata2df import wikidata2df

    cat_query = """
    #Cats
    SELECT ?item ?itemLabel 
    WHERE 
    {
    ?item wdt:P31 wd:Q146.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    """

    cats_dataframe = wikidata2df(cat_query)
