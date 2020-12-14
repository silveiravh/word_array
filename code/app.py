from flask import Flask, request
from flask_restful import Resource, Api
import nltk
import string
from nltk import ngrams
from typing import List

nltk.download('stopwords')
stopwords = nltk.corpus.stopwords.words('portuguese')

app = Flask(__name__)
api = Api(app)

texts = []

class Text(Resource):
    def post(self):
        data = request.get_json()
        new_text = {'id': data['id'], 'content': data['content']}
        texts.append(new_text)
        return new_text, 201

class Vocabulary(Resource):
    @classmethod
    def build_vocabulary(cls, gram: int) -> List:
        word_list = []
        for text in texts:
            word_list.extend(ngrams(text['content']
            .lower() # transforma tudo em lowercase para desconsiderar o case
            .replace('-', ' ') # substitui '-' por ' ' para considerar duas palavras no caso de palavras compostas (ex. mostre-me será 'mostre' e 'me' separadamente)
            .split(), gram)) # aplica o n-gram conforme o valor de gram passado na request
        word_list = [' '.join(word) for word in word_list] # transforma de tuple para list
        word_list = [word.translate(str.maketrans('', '', string.punctuation)) for word in word_list if word not in stopwords] # remove pontuação e stopwords
        word_list = list(dict.fromkeys(word_list)) # remove duplicatas
        return word_list
    
    def get(self, gram):
        return ({'vocabulary': Vocabulary.build_vocabulary(gram)})

class WordFrequencyList(Resource):
    def get(self, gram):
        word_list = Vocabulary.build_vocabulary(gram)
        list_word_frequency = []
        for text in texts:
            word_frequency = []
            for word in word_list:
                word_frequency.append(text['content']
                .lower()
                .replace('-', ' ') # substitui '-' por ' '
                .translate(str.maketrans('', '', string.punctuation)) # remove pontuação
                .count(word)) #conta a repetição da palavra no texto
            list_word_frequency.append(word_frequency)
        return ({'list_word_frequency': list_word_frequency})
                
api.add_resource(Text, '/text')
api.add_resource(Vocabulary, '/vocabulary/<int:gram>')
api.add_resource(WordFrequencyList, '/wordfrequency/<int:gram>')

app.run(port=5000)