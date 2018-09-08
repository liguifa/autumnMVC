def session_middleware(app, request, response, config):
    sessionId = getattr(request.cookie, config["session"]["id"])
    if not sessionId:
        sessionId = app.guid()
        setattr(response.cookie, config["session"]["id"], sessionId)
    request.session = response.session = sessions(app, sessionId)
    return True


class sessions:
    def __init__(self, app, sessionId):
        self.__dict__["app"] = app
        self.__dict__["sessionId"] = sessionId

    def __setattr__(self, key, value):
        if not hasattr(self.__dict__["app"], "store"):
            self.__dict__["app"].store = {}
        self.__dict__["app"].store[key] = value

    def __getattr__(self, key):
        return self.__dict__["app"].store[self.__dict__["sessionId"]][key]
