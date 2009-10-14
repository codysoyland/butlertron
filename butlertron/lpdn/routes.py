from tron.responders import reply
from lpdn import responders

routes = [
    (r'lpdn vote (?P<location>.*)', responders.vote),
    (r'lpdn stats', responders.stats),
    (r'.*lpdn.*', responders.howto),
]
