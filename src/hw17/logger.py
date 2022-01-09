import logging
import sys

log = logging.getLogger('My_Log')
log.level = logging.DEBUG
stream_handler = logging.StreamHandler(sys.stdout)
log.addHandler(stream_handler)
