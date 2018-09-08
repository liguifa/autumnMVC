def http_middleware(app, request, response, config):
    # 设置 web url
    if 'PATH_INFO' in request.environ:
        request.url = response.url = request.environ["PATH_INFO"]
    else:
        request.url = response.url = ""

    # 设置响应函数
    def send(message):
        html = message.encode("utf-8") if type(message) == str else message
        if not response.messages:
            response.messages = [html]
        else:
            response.messages.append(html)
    response.send = send

    # 状态码
    response.status = 200

    # 设置响应头
    response.heads = {}

    return True
