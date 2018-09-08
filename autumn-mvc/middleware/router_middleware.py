def router_middleware(app, request, response, config):
    router_map = {
        1: mvcRouter
    }
    request.router = router_map[config["router"]["model"]](request.url, config)
    return True


class router:
    def __init__(self, url, config):
        self.url = url
        self._controller = config["router"]["controller"]
        self._action = config["router"]["action"]
        self._parameters = None
        self._parse()

    @property
    def controller(self):
        return self._controller

    @property
    def action(self):
        return self._action

    @property
    def parameters(self):
        return self._parameters

    def _parse(self):
        pass


class mvcRouter(router):
    def __init__(self, url, config):
        super().__init__(url, config)

    def _parse(self):
        if self.url:
            str_arr = self.url.split("/")
            if str_arr and len(str_arr) > 2:
                self._controller = str_arr[1]
                self._action = str_arr[2]
