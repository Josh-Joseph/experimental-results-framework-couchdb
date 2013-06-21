

{
   "_id": "_design/ui",
   "_rev": "1-1d1da3619b5b7c8f4526b935ba281f56",
   "language": "javascript",
   "views": {
       "by_cluster_id": {
           "map": "function(doc) {\n  if( doc.job ) {\n    emit(doc.job.cluster_id , doc);\n  }\n}"
       }
   }
}
