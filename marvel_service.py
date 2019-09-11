import hashlib
import requests
import json
import logging

from init import Configuration
from http import HTTPStatus

class Character:
    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description

    def __str__(self):
        return self.id + " " + self.name + " " + self.description

class Story:
    def __init__(self, id, title, type, description):
        self.id = id
        self.title = title
        self.type = type
        self.description = description

    def __str__(self):
        return self.id + " " + self.title + " " + self.type + " " + self.description


class MarvelServiceImpl:

    properties = Configuration.properties

    # Realiza uma chamada ao Web Service da Marvel API para buscar personagem
    # Retorna um objeto Character
    def find_character(self, name):

        endpoint = self.properties['find_character'].format(name,
                                                       self.properties['public_key'],
                                                       self.generate_hash(),
                                                       self.properties['ts'])

        logging.debug('Url a ser chamada no método find_character: {}'.format(endpoint))
        response = requests.get(endpoint)

        if (response.status_code == HTTPStatus.OK):
            response_json = json.loads(response.text)
            if (response_json['code'] == 200):
                data_json = response_json['data']
                total_registros = data_json['total']
                if (total_registros >= 1):
                    resultados_json = data_json['results']
                    spider_man_json = resultados_json[0]
                    return Character(spider_man_json['id'], spider_man_json['name'], spider_man_json['description'])
                else:
                    logging.debug('Não foi localizado o personagem')
        else:
            logging.error('Ocorreu um erro ao invocar o WS')


    # Realiza uma chamada ao Web Service da Marvel API para buscar as histórias associadas a um personagem
    # Retorna uma lista de objetos Story
    def find_stories(self, character_id):

        stories = []
        endpoint = self.properties['find_stories'].format(character_id,
                                                     self.properties['amount_of_stories'],
                                                     self.properties['public_key'],
                                                     self.generate_hash(),
                                                     self.properties['ts'])

        logging.debug('Url a ser chamada no método find_stories: {}'.format(endpoint))
        response = requests.get(endpoint)

        if (response.status_code == HTTPStatus.OK):
            response_json = json.loads(response.text)
            if (response_json['code'] == 200):
                data_json = response_json['data']
                total_registros = data_json['total']
                if (total_registros >= 1):
                    resultados_json = data_json['results']
                    for story in resultados_json:
                        stories.append(Story(story['id'], story['title'], story['type'], story['description']))
                else:
                    logging.debug('O serviço não contém histórias associadas ao personagem')

        else:
            logging.error('Ocorreu um erro ao invocar o WS')

        return stories

    # Gera a hash necessária para chamar o Web Service da Marvel API
    def generate_hash(self):
        return hashlib.md5((self.properties['ts'] + self.properties['private_key'] + self.properties['public_key'])
                           .encode('utf-8')).hexdigest()