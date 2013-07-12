experimental-results-framework-couchdb
======================================

This repo includes all of the views (couchdb-design-documents) that we will use and any information needed to setup couchdb.


Getting couchdb running:
------------------------

To get CouchDB running:

    sudo apt-get install help2man make gcc zlib1g-dev libssl-dev rake help2man texinfo flex dctrl-tools libsctp-dev libxslt1-dev libcap2-bin ed

    sudo pip install couchdb gitpython
    
    git clone git://github.com/iriscouch/build-couchdb.git
    
    cd build-couchdb/
    
    rake
    

Configuring CouchDB for CORS:
-----------------------------------------

We need the use of cross-site origin resource sharing (CORS) for the javascript UI to be
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


Configuring Python Map-Reduce for CouchDB Views:
-----------------------------------------

So open up the builb/etc/couchdb/local.ini file for couchdb add/update the following flags:

    [query_servers]
    python = <absolute path to couchpy executable>
    
Note: in the default install, [query_servers] does not exist, so just add it.

See [here](http://pythonhosted.org/CouchDB/) for more information.
