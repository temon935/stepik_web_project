def simple_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type','text/plain')]
    start_response(status, response_headers)
    return [bytes('\r\n'.join(environ['QUERY_STRING'].split('&')),
                  encoding="utf8")]