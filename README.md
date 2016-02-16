## Synopsis

This repository holds a Django web app which displays data based on a JSON file. The JSON file is sourced from the Rotten Tomatoes API.

As such, the decision was made early on to let this be the source of record, rather than create the additional overhead of a Django model. This decision was made for 2 reasons:

1. The data is read-only, as far as the scope of this project is concerned.
2. The integrity of the data is being handled ultimately by the Rotten Tomatoes database. Should we like to hook this up to any arbitrary, dynamic output from the Rotten Tomatoes API, this solution may be more manageable.

That said, I do also recognize the benefit of anyone reviewing this to be assured that I also understand a more standard Django MV* route, and so I have also implimented a small piece of the data as a proper model. A quick-bird's eye view: In views.py, the "index" and "about" actions are using the original JSON-only parsing option. The "details" and "search" actions are using a hybrid JSON/model scheme. Please see views.py for more information.

## Stack/Technologies

Python -
Django -
SQLite -
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

