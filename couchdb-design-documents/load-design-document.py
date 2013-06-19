
import couchdb
import argparse
import os
import os.path
import json



def load_design_document( couch_db, filename ):
    # Now, load the javascript design document as a dictionary and 
    # save it to the db
    doc = None
    with open( filename ) as f:
        doc = json.load( f )

    # kill the _rev since we will be assigning a new one when we save this doc
    if "_rev" in doc:
        del doc["_rev"]
        
    new_doc_id, new_doc_rev = db.save( doc )    
    
    # prin to user
    print "loaded design document '%s' into '%s' databse" % ( new_doc_id, couch_db.name )


if __name__ == "__main__":
    
    parser = argparse.ArgumentParser( description= "Load a particular design document into a specific database" )
    parser.add_argument( "design_document_js" )
    parser.add_argument( "database_name" )
    parser.add_argument( "--couchdb-base-url", default="http://localhost:5984/" )
    parser.add_argument( "--recursive", default=False, 
                         action="store_const", const=True )
    args = parser.parse_args()

    # create a new couchdb session and databse
    couch = couchdb.Server( args.couchdb_base_url )
    db = couch[args.database_name]

    # see if we want to recurse
    if args.recursive:
        
        # walk all files of the given directory and load each
        for root, dirs, files in os.walk( args.design_document_js ):
            for filename in files:
                load_design_document( db, os.path.join( root, filename ) )

    else:
    
        load_design_document( db, args.design_document_js )
