from unittest.mock import patch
import random

import pytest

# fun fact, each individual object or method defined in import class have to be called if you want to use it
# hence class file which just encompasses the everything
from guess import get_random_number, Game