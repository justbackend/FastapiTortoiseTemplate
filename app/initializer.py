# from inspect import getmembers

from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from .database import TORTOISE_ORM


def init(app: FastAPI):
    """
    Init routers and etc.
    :return:
    """
    init_db(app)
    # init_exceptions_handlers(app)


# def init_exceptions_handlers(app: FastAPI):
#     from app.core.exceptions.handlers import tortoise_exception_handler
#     from app.core.exceptions.handlers import BaseORMException
#
#     app.add_exception_handler(BaseORMException, tortoise_exception_handler)



def init_db(app: FastAPI):

    """
    Init database models.
    :param app:
    :return:
    """
    register_tortoise(
        app,
        config=TORTOISE_ORM,
        generate_schemas=True,
        add_exception_handlers=True,
    )