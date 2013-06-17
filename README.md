experimental-results-framework-couchdb
======================================

This repo includes all of the views (couchdb-design-documents) that we will use and any information needed to setup couchdb.


Setting Up/ Configuring CouchDB for CORS:
-----------------------------------------

We need the use of cross-site scripting for the javascript UI to be
able to fetch ajax-style from our DB.  So open up the
builb/etc/couchdb/local.ini file for couchdb add/update the following flags:

    [couchdb]
    delayed_commits = false

    [httpd]
    enable_cors = true

    [cors]
    origins = *

Note: in the default install, [cors] does not exist, so just add it.

We can also just add hosts to the origins, comma separated, but *
allows everything and for development it might be useful.

