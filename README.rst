===========
wikidata2df
===========


.. image:: https://img.shields.io/pypi/v/wikidata2df.svg
        :target: https://pypi.python.org/pypi/wikidata2df

.. image:: https://github.com/jvfe/wikidata2df/workflows/pytest/badge.svg
        :target: https://github.com/jvfe/wikidata2df/actions

.. image:: https://readthedocs.org/projects/wikidata2df/badge/?version=latest
        :target: https://wikidata2df.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


Utility package for easily turning a SPARQL query into a dataframe

Ever wished you could easily and programatically get data from Wikidata into a nice and analysable Pandas DataFrame?
Well, this package solves that problem: With a single function you can turn your SPARQL query into a pandas DataFrame,
without having to deal with the messy JSON intermediate.


* Free software: BSD license
* Documentation: https://wikidata2df.readthedocs.io.


Basic Usage
-----------

To install::

    $ pip install wikidata2df


::

    from wikidata2df import wikidata2df

    # A SPARQL query to return all cats in Wikidata!

    cat_query = """
    #Cats
    SELECT ?item ?itemLabel
    WHERE
    {
    ?item wdt:P31 wd:Q146.
    SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    """

    cats_dataframe = wikidata2df(cat_query) # Returns a Pandas DataFrame

You can also use it in the command line, if you have text file with a SPARQL query::

    $ wikidata2csv -q query.rq -o query_results.csv

Alternatives
------------

* Maybe you want more sofisticated functions? Or a way to edit Wikidata programatically? Awesome!

        * Check out `WikidataIntegrator <https://github.com/SuLab/WikidataIntegrator>`__

* Would you rather use R? That's cool too!

        * Check out `WikidataQueryServiceR <https://github.com/wikimedia/WikidataQueryServiceR>`__

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
