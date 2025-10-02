# ! /usr/bin/env python3     SHEBANG
# Author: Nikhil Ahlawat
# Version: 1.0
# Description:

from flask import Flask

app = Flask(__name__)

from . import routes

