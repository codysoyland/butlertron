from tron.exceptions import NoRoutes
import re

class Dispatcher(object):
    def __init__(self, routes):
        self.routes = routes
    def resolve(self, message):
        for regex, responder in self.routes:
            pattern = re.compile(regex, re.IGNORECASE)
            match = pattern.match(message)
            if match:
                if isinstance(responder, Dispatcher):
                    try:
                        return responder.resolve(message)
                    except NoRoutes:
                        pass
                else:
                    return responder, match.groupdict()
        raise NoRoutes()
