sportscribe-python
==================

sportscribe-python -- Python application to access SportScribe data

v1.0.1

Installation
============

Clone this repo into your working directory

Methods
=======

Return a list of leagues

.. code:: python

	getLeagues()


Return a list of teams for the given leagueId

.. code:: python

	getTeams(leagueId : int)
	

Returns the next match's preview for the given teamId

.. code:: python

	getMatchPreviewByTeam(teamId : int)

Returns a list of all match previews on the given date (YYYY-MM-DD)

.. code:: python

	getMatchPreviewByDate(date : str)


Configuration
=============

edit config.py to point to the correct endpoint URL

Usage
=====

.. code:: python


	from sportscribe import SportScribe

	ss = SportScribe('API-KEY-HERE')
	# Default v1.0 endpoint
	ss.setEndpoint('https://api.sportscribe.co/v1_0/')
	# Optional set language.
	ss.setLanguage('en')
	result = ss.getMatchPreviewByDate('YYYY-MM-DD')
	
	if result:
	  print(result.data)


ChangeLog
=========


| V1.0.2 = added languages support
| V1.0.1 = added setEndpoint instead of config.py
