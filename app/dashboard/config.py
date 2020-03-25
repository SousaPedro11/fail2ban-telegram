import os

import flask_monitoringdashboard as dashboard

from app import app

basedir = os.path.abspath(os.path.split(os.path.dirname(__file__))[0])
dash_config = os.path.join(basedir, 'dashboard.cfg')
dashboard.config.init_from(dash_config)
dashboard.bind(app=app)
