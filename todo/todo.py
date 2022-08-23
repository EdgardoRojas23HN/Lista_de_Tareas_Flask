from flask import (
    Blueprint, flash, g, render_template, request, url_for, session, redirect
)

from werkzeug.exceptions import abort
from todo.auth import login_required
from todo.db import get.db

bp = Blueprint('todo', __name__)