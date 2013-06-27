
{
   "_id": "_design/ui",
   "_rev": "3-2b0d99538f6c8f1394c3fdcb459c1d86",
   "language": "javascript",
   "views": {
       "by_cluster_id": {
           "map": "function(doc) {\n  if( doc.job ) {\n    emit(doc.job.cluster_id , doc);\n  }\n}"
       },
       "status_count_by_script": {
           "map": "function(doc) {\n  if( doc.job ) {\n    emit([doc.job.script,doc.job.cluster_id] , doc);\n  }\n}",
           "reduce": "function (key, values, rereduce) {\n  val = { done: 0, submitted: 0, other: 0 };\n  if( rereduce ) {\n     values.forEach( function( e ) {\n       val.done += e.done;\n       val.submitted += e.submitted;\n       val.other += e.other;\n     });\n  } else {\n     values.forEach( function( d ) {\n       if( d.job.status == \"done\" ) {\n         val.done += 1;\n       }\n       else if( d.job.status == \"submitted\" ) {\n         val.submitted += 1;\n       } else {\n         val.other += 1;\n       }\n     });\n  }\n  return val;\n}"
       }
   }
}
