{
   "_id": "_design/javier_test",
   "_rev": "1-49ce2bf0c9513d1c3812846e36fb4a68",
   "language": "javascript",
   "views": {
       "gitcode_means": {
           "map": "function(doc) {\n  if( doc.trial && !doc.trial.code.version.diffs && !doc.trial.code.version.untracked_files ) \n  {\n    emit( doc.trial.result.mean, doc.trial.result.mean );\n  }\n}"
       }
   }
}