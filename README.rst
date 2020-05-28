sportscribe-python
==================

sportscribe-python -- Python application to access SportScribe data

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


Usage
=====

.. code:: python


	from sportscribe import SportScribe

	ss = SportScribe('API-KEY-HERE')
	result = ss.getMatchPreviewByDate('YYYY-MM-DD')
	if result:
	  print(result.data)


