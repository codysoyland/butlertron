from collections import defaultdict
from operator import itemgetter
import pickle

# bad data store, should use sqlite instead
class Data(object):
    def __init__(self):
        try:
            file = open('pickle', 'r')
        except IOError:
            self.data = defaultdict(list)
        else:
            self.data = pickle.load(file)

    def commit(self, data=None):
        if data is None:
            data = self.data
        file = open('pickle', 'w')
        pickle.dump(data, file)

def howto(message):
    message.reply('Type "lpdn vote <location>" to vote on a location or "lpdn stats" to see the current results.')

def vote(message, location):
    data = Data()
    results = data.data
    new_location = location.strip('\'" ')
    for location, users in list(results.iteritems()):
        if message.nick in users:
            users.remove(message.nick)
        if len(users) == 0:
            del results[location]
    results[new_location].append(message.nick)
    data.commit(results)
    message.reply('You voted for "%s". Type "lpdn stats" for voting stats.' % new_location)

def stats(message):
    output = ", ".join(["%s has %d votes" % (place, votes) for (place, votes) in generate_stats()])
    message.reply(output)

def generate_stats(data=None):
    if not data:
        data = Data()
    results = {}
    for key, value in data.data.iteritems():
        results[key] = len(value)
    results = sorted(results.items(), key=itemgetter(1))
    results.reverse()
    return results
