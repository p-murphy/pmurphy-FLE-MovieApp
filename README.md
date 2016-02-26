## Synopsis

This repository holds a Django web app which displays data based on a JSON file. The JSON file is sourced from the Rotten Tomatoes API.

As such, the decision was made early on to let this be the source of record, rather than create the additional overhead of a Django/SQLite database. This decision was made for 2 reasons:

1. The data is read-only, as far as the scope of this project is concerned.
2. The integrity of the data is being handled ultimately by the Rotten Tomatoes database. Should we like to hook this up to any arbitrary, dynamic output from the Rotten Tomatoes API, this solution may be more manageable.

In the previous version, the choice was made to also implement a SQLite database to display understanding of that route. For this new version, this has been removed in favor of streamlining all of the logic. You can use either movies.json or more_movies.json as the source. This can be changed at the top of starter/views.py

## Stack/Technologies

Python -
Django -
HTML -
CSS -
JavaScript

## 3rd-Party Packages

Bootstrap
http://getbootstrap.com/

Bootswatch
https://bootswatch.com/

jQuery
https://jquery.com/

jQueryUI Autocomplete
https://jqueryui.com/autocomplete/

Magnific Popup
http://dimsemenov.com/plugins/magnific-popup/

