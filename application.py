
from flask import Flask,jsonify
from wordhoard import synonyms
class synonym_model:
    def getSynonyms(word):
        synonym_result_01 = synonyms.query_synonym_com(word)
        synonym_result_02 = synonyms.query_thesaurus_com(word)
        synonym_result_03 = synonyms.query_thesaurus_plus(word)
        synonyms_results = sorted(set([y for x in [synonym_result_01, 
        synonym_result_02, synonym_result_03] for y in x]))
        return synonyms_results
        

application = Flask(__name__)

@application.route('/', methods=['GET'])
def home():
   return 'Welcome To the API'

@application.route('/api/<word>', methods=['GET'])
def syn(word):
   return jsonify(synonym_model.getSynonyms(word));  

if __name__ == '__main__':
    application.run( debug=True)   