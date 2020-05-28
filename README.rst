sportscribe-python
==================

sportscribe-python -- Python application to access SportScribe data

Installation
============

git clone 


Usage
=====

.. code:: python


	from sportscribe import SportScribe

	ss = SportScribe('API-KEY-HERE')
	req = ss.getMatchPreviewByDate('YYYY-MM-DD')
	if req.result:
	  print(req.data)

