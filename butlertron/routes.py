from lpdn.routes import routes as lpdn_routes
from tron.dispatcher import Dispatcher
from tron.responders import reply

routes = [
    (r'.*lpdn.*', Dispatcher(lpdn_routes)),
    (r'.*(butlertron).*', Dispatcher([
        # probably not a very appropriate introduction. to clean up sooner rather than later...
        (r'.*(hi|hello|yo|hey).*', reply("Yo bitches. I'm Mr. Butlertron, but you can call me Mr. B. Ask for help if you need an introduction.")),
        (r'.*help.*', reply("I'm a raging alcoholic robot whose only concern is LPDN.  To vote on a location, type 'lpdn vote <location>'")),
    ])), 
    (r'.*rocks da house.*', reply("DANIELLINDSLEYROCKSDAHOUSE!!!!")),
    (r'butlertron: say (?P<msg>.*)', reply('"%(msg)s"')),
]
