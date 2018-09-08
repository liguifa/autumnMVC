def static_middleware(app, request, response, config):
    suffix = request.url.split(".").pop()
    if suffix in config["static"]["suffix"]:
        file = "{path}/{filename}".format(path=config["static"]["path"], filename=request.url) # NOQA
        with open(file, 'rb') as f:
            response.send(f.read())
        response.write("200 OK", [("Content-Type", "application/octet-stream")]) # NOQA
        return False
    return True
