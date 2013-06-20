{
   "_id": "_design/job_tracker",
   "_rev": "2-841aa3e375460eda5dcddb6dc1d271ab",
   "language": "javascript",
   "views": {
       "all_jobs_by_cluster_and_status": {
           "map": "function(doc) {\n  if( doc.job ) {\n    emit({ \"cluster_id\" : doc.job.cluster_id, \"status\" : doc.job.status } , doc);\n  }\n}"
       },
       "all_jobs_by_status": {
           "map": "function(doc) {\n  if( doc.job ) {\n    emit(doc.job.status , doc);\n  }\n}"
       }
   }
}