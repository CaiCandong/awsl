from .admin import admin_blue
from .student import student_blue
from .index import index_blue
from .teacher import teacher_blue

DEFAULT_BLUEPRINT = (
    (index_blue, ''),
    (student_blue, '/student'),
    (admin_blue, '/admin'),
    (teacher_blue, '/teacher'),
)


def config_blueprint(app):
    for blueprint, url_prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=url_prefix)
