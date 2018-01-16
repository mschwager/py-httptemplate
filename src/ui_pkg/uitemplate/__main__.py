#!/usr/bin/env python3

import argparse

import aiohttp

from . import application


def parse_args():
    p = argparse.ArgumentParser(description='''
        Program description.
        ''', formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument(
        '-p',
        '--port',
        action='store',
        type=int,
        default=8080,
        help='port to run server on'
    )
    p.add_argument(
        '-H',
        '--host',
        action='store',
        default='127.0.0.1',
        help='host to run server under'
    )
    p.add_argument(
        '-s',
        '--static',
        action='store_true',
        help='host static files'
    )

    args = p.parse_args()

    return args


def main():
    args = parse_args()

    app = application.get_application(static=args.static)

    aiohttp.web.run_app(app, host=args.host, port=args.port)


if __name__ == "__main__":
    main()
