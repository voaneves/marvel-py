import logging
import asyncio

from flask import Flask, render_template, flash, request
from marvel_service import MarvelServiceImpl

app = Flask(__name__)
app.secret_key = 'marvel'


@app.route('/', methods=['GET'])
def index():
    logging.debug('Executando método index')

    characters = []
    characters.append(MarvelServiceImpl().find_character('Spider-man'))
    characters.append(MarvelServiceImpl().find_character('Fantastic Four'))
    characters.append(MarvelServiceImpl().find_character('Wolverine'))

    """
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(MarvelServiceImpl().find_character('Spider-man'))
    loop.close()
    """

    if not characters:
        logging.debug('Não há personagens para listar')
        flash('There are no characters to list')

    return render_template('characters.html',
                            title = 'My favorite Marvel characters',
                            characters = characters)


@app.route('/stories/<int:character_id>', methods=['GET'])
def view_stories(character_id):
    logging.debug('Executando método view_stories')

    stories = MarvelServiceImpl().find_stories(character_id)

    if not stories:
        logging.debug('Não há histórias para listar')
        flash('There are no stories to list')

    return render_template('stories.html',
                           title = 'Stories: {}'.format(request.args.get('character_name')),
                           stories = stories)


if __name__ == '__main__':
    logging.debug("Aplicação sendo inicializada...")
    app.run(debug=True)