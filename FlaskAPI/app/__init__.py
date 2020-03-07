from flask import Flask
app = Flask(__name__);

#__CONFIGURATIONS__#
app.config['JSON_AS_ASCII'] = False


#__MIDDLEWARE PIPELINE__#
from app.middleware import test, test2
app.wsgi_app = test.TestMiddleware(app.wsgi_app);
app.wsgi_app = test2.TestMiddleware2(app.wsgi_app);


#__ROUTE IMPORTS__#
from app.routes import user_routes