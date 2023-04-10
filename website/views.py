from flask import Blueprint

views = Blueprint('views', __name__)

@views.root('/')
def home():
    pass