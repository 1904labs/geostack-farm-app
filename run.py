#!/usr/bin/env python3

from app import create_app
from config import DevConfig as Config


if __name__ == '__main__':
    create_app(Config).run()
