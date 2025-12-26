'''
Système de logging de l'application,
messages propres
Debugging
Observalité
'''

from loguru import logger
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time} | {level} | {message}")
