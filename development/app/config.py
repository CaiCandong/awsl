import os

base_dir = os.path.abspath(os.path.dirname(__file__))  # 这个就是app的目录


def get_db_uri(dbinfo):
    engine = dbinfo.get("ENGINE") or "sqlite"
    driver = dbinfo.get("DRIVER") or "sqlite"
    user = dbinfo.get("USER") or ""
    password = dbinfo.get("PASSWORD") or ""
    host = dbinfo.get("HOST") or ""
    port = dbinfo.get("PORT") or ""
    name = dbinfo.get("NAME") or ""
    return "{}+{}://{}:{}@{}:{}/{}?charset=utf8mb4".format(
        engine,
        driver,
        user,
        password,
        host,
        port,
        name
    )


class Config:
    #
    SECRET_KEY = 'AFDADD1681W2ED1DFA3'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 邮件配置
    MAIL_SERVER = 'smtp.qq.com'  # 邮件服务器地址
    MAIL_USERNAME = 'oyq_link@foxmail.com'  # 邮件账户名
    MAIL_PASSWORD = 'llwmclwpksfjbdcf'  # 邮件账户授权码

    @staticmethod
    def init_app(app):
        pass


# 开发使用数据库mysql
class DevelpmentConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "abc.123",
        "HOST": "47.101.141.122",
        "PORT": "3306",
        "NAME": "jxust_exam"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


# 本地备用数据库sqlite
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(base_dir, 'bbs_text.sqlite')


# 实际运行环境数据库
class ProductionConfig(Config):
    DEBUG = True
    dbinfo = {
        "ENGINE": "mysql",
        "DRIVER": "pymysql",
        "USER": "root",
        "PASSWORD": "abc.123",
        "HOST": "47.101.141.122",
        "PORT": "3306",
        "NAME": "jxust_exam"
    }
    SQLALCHEMY_DATABASE_URI = get_db_uri(dbinfo)


config_map = {
    'development': DevelpmentConfig,
    'test': TestConfig,
    'product': ProductionConfig,
    'default': DevelpmentConfig
}
