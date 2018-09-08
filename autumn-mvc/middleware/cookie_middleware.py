def cookie_middleware(app, request, response, config):
    request.cookie = cookies()
    if "HTTP_COOKIE" in request.environ:
        for cookie in request.environ["HTTP_COOKIE"].split(";"):
            key = cookie.split("=")[0]
            value = cookie.split("=")[1]
            setattr(request.cookie, key, value)

    def set_cookie(key, value):
        if "Set-Cookie" not in response.heads:
            response.heads["Set-Cookie"] = u"{key}={value};".format(**locals())
        else:
            response.heads["Set-Cookie"] += u";{key}={value}".format(**locals())

    response.cookie = cookies(set_cookie) # NOQA)
    return True


class cookies:
    def __init__(self, set_cooie=None):
        if set_cooie:
            self.__dict__["set_cooie"] = set_cooie

    def __setattr__(self, key, value):
        print(key)
        self.__dict__[key] = value
        if "set_cooie" in self.__dict__ and key != "set_cookie":
            self.__dict__["set_cooie"](key, value)

    def __getattr__(self, key):
        if key not in self.__dict__:
            return None
        return self.__dict__[key]
