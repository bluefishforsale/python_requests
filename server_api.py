import logging
import argparse
import json
from flask import Flask, request


app = Flask(__name__)
@app.route("/", methods=['POST'])
def api_post():
  output = request.get_json()
  logging.info(output)
  return output

if __name__ == '__main__':

  parser = argparse.ArgumentParser(
    prog='api server',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
  )

  parser.add_argument(
    "-l", "--log",
    help="logging level eg. [critical, error, warn, warning, info, debug]",
    type=str, default="info"
  )
  parser.add_argument(
    "-i", "--ip",
    help="ip address to bind server to",
    type=str, default="0.0.0.0"
  )
  parser.add_argument(
    "-p", "--port",
    help="port to listen on",
    type=int, default=8080
  )
  args = parser.parse_args()

  levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
  }

  level = levels.get(args.log.lower())
  format = '%(asctime)-25s %(levelname)8s %(pathname)s:%(lineno)-21d %(message)s'
  logger = logging.getLogger(__name__)
  logging.basicConfig(format=format, level=level)

  app.run(host=args.ip, port=args.port)
