import pandas as pd
from flask import jsonify
from pandas.core import indexing
from pandas.core.dtypes.missing import notnull
import config as cg
from pandas.io import json