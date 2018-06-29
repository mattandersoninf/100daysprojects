from logging import Logger, StreamHandler
from typing import List

import requests
import collections
import random

Movie = collections.namedtuple('Movie','imdb_code, title, director, keywords,'
                                       'duration, genres, rating, year, imdb_scores')

