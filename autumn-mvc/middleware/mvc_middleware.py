import sys

content_types = {
    1: "text/html",
    2: "application/json"
}


def mvc_middleware(app, request, response, config):
    # 获取controller
    if request.router.controller:
        sys.path.insert(0, config["controller"]["path"])
        controller = getattr(__import__(request.router.controller), request.router.controller)() # NOQA
        controller.request = request
        controller.response = response
        controller.config = config
        # 执行action
        body = getattr(controller, request.router.action)()
        response.template = body["template"]
        response.heads["Content-Type"] = content_types[body["type"]]
    else:
        response.template = ""
    return True
