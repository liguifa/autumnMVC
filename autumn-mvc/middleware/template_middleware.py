import re


def template_middleware(app, request, response, config):
    html = response.template.replace('\n', ' ').replace('\r', '')
    html = re.sub("<%(.*?)%>", replace_function, html)
    html = re.sub("<<(.*?)>>", replate_object, html)
    print(html)
    html = "'{html}'".format(**locals())
    response.template = eval(html)
    return True


def replace_function(match):
    pass


def replate_object(match):
    return "'+response.views[\"{obj}\"]+'".format(obj=match.group(1))
