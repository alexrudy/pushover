========
pushover
========


.. image:: https://img.shields.io/pypi/v/pushover.svg
        :target: https://pypi.python.org/pypi/pushover

.. image:: https://img.shields.io/travis/alexrudy/pushover.svg
        :target: https://travis-ci.org/alexrudy/pushover

.. image:: https://readthedocs.org/projects/pushover/badge/?version=latest
        :target: https://pushover.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Send quick notifications to pushover


* Free software: BSD license
* Documentation: https://pushover.readthedocs.io.


Example
-------

You can use pushover to notify yourself of the status of the most recently run command when it finishes::

    make test; pushover -s$? "make test finished!"
