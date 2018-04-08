from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from random import shuffle
import sys
from wit import Wit

if len(sys.argv) != 2:
    print('usage: python ' + sys.argv[0] + 'P6HLKSSDR65FN32JXDI4CHICUL5WSRUT')
    exit(1)
access_token = sys.argv[1]



all_jokes={

        'ajokes:' [

            {'Chuck Norris counted to infinity - twice.'},
            {
        'Death once had a near-Chuck Norris experience.'},
    ],
}


def first_entity_value(entities, entity):
    if entity not in entities:
        return None
    val = entities[entity][0]['value']
    if not val:
        return None
    return val['value'] if isinstance(val, dict) else val


def select_joke(ajokes):
    jokes = all_jokes[ajokes]
    shuffle(jokes)
    return jokes[0]


def handle_message(response):
    entities = response['entities']
    get_joke = first_entity_value(entities, 'getJoke')
    greetings = first_entity_value(entities, 'greetings')
    sentiment = first_entity_value(entities, 'sentiment')

    if get_joke:
        return select_joke(all_jokes)
    elif sentiment:
        return 'Glad you liked it.' if sentiment == 'positive' else 'Hmm.'
    elif greetings:
        return 'Hey this is joke bot :)'
    else:
        return 'I can tell jokes! Say "tell me a joke"!'


client = Wit(access_token=access_token)
client.interactive(handle_message=handle_message)
client.message('tell me a joke')