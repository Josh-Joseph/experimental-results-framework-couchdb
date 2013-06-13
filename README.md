experimental-results-framework-couchdb
======================================


Setting Up/ Configuring CouchDB for CORS
========================================

We need the use of cross-site scripting for the javascript UI to be
able to fetch ajax-style from our DB.  So open up the
buil/etc/couchdb/local.ini file for couchdb and make sure the
following sections have the following flags:

[couchdb]
delayed_commits = false

[httpd]
enable_cors = true

[cors]
origins = *

We can also just add hosts to the origins, comma separated, but *
allows everything and for development it might be useful.

