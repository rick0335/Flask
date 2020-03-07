class TestMiddleware2(object):

    def __init__(self, app):
        self.app = app;

    def __call__(self, environ, start_response):
        print("TestMiddleware2");
        return self.app(environ, start_response);