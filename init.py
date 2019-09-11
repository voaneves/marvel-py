import logging

class Configuration:

    # Realiza a leitura do arquivo properties e converte em um map
    def load_properties(filepath, sep ='=', comment_char = '#'):
        properties = {}
        with open(filepath, "rt") as f:
            for line in f:
                l = line.strip()
                if l and not l.startswith(comment_char):
                    key_value = l.split(sep)
                    key = key_value[0].strip()
                    value = sep.join(key_value[1:]).strip().strip('"')
                    properties[key] = value

        return properties


    # Configura o arquivo de log e em qual level
    logging.basicConfig(filename = 'marvel.log', level = logging.DEBUG)

    # Obtém o map com as configurações do app
    properties = load_properties('configuration.properties')