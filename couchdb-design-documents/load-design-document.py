
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
    
    parser = argparse.ArgumentParser( description= "Load a particular design document into a specific database, or an entire directory strucutre of files into a set of databases." )
    parser.add_argument( "design_document_js" )
    parser.add_argument( "--database_name", default="",
                         help="If given, will be used as the databse to load the design document into. If the --autodetect-database-from-directory-structure flag is also given. this databse will be used for all top-level design documents.")
    parser.add_argument( "--couchdb-base-url", 
                         default="http://localhost:5984/" )
    parser.add_argument( "--recursive", default=False, 
                         action="store_const", const=True,
                         help="If given, the entire directory structure starting at design_document_js will be searched and every non-directory treated as a design document.")
    parser.add_argument( "--autodetect-database-from-directory-structure", 
                         default=False, action="store_const", const=True,
                         help="If given, the database name to store a found design document will be the direct poarent directory name. This option really only makes sense if --recursive is given. Any files without a direct parent in the structure will be loaded into the databse denoted in --database-name")
    args = parser.parse_args()

    # create a new couchdb session and databse
    couch = couchdb.Server( args.couchdb_base_url )
    db = couch[args.database_name]

    # see if we want to recurse
    if args.recursive:
        
        # walk all files of the given directory and load each
        for root, dirs, files in os.walk( args.design_document_js ):
            for filename in files:
                
                # if we want to autodetect hte database name,
                # use the root last directory as the name
                if args.autodect_database_from_directory_structure:
                    toks = root.split( "/" )
                    if tok[-1] == "" and len(toks) > 1:
                        dbname = toks[-2]
                    else:
                        dbname = toks[-1]
                    if dbname == "":
                        dbname = args.database_name
                    try:
                        couch.create( dbname )
                        print "created autodetected databse name: '%s'" % dbname
                    except couchdb.PreconditionFailed:
                        pass
                    db = couch[dbname]
                load_design_document( db, os.path.join( root, filename ) )

    else:
    
        load_design_document( db, args.design_document_js )
