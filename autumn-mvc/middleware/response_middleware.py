def response_middleware(app, request, response, config):
    # 获取响应状态信息
    status = statusCodes[response.status]
    # 获取响应头信息
    heads = []
    for (key, value) in response.heads.items():
        heads.append((key, value))
    # 写入响应头
    from pprint import pprint
    pprint(heads)
    response.write(status, heads)
    # 写入响应体
    response.send(response.template)


statusCodes = {
    200: "200 OK"
}
