"""Fonts tests

Run this module with python -m tes
"""
from . import *

import os, sys
# todo 12/12/20 is this necessary for tox? if not, remove
# sys.path.insert(0,
#   os.path.join(
#     os.path.dirname(os.path.abspath(__file__)),
#     os.path.join('..', '..')
#   )
# )

from test.utilities import relative_path_to, files_in_dir

def get_ttf_basic():
  """Get TTF Basic

  returns an array of locations for the basic TTF font files
  """
  basic_ttf_path = relative_path_to('fonts', 'ttf-filesamples-com')
  return files_in_dir(basic_ttf_path)

def say_hi():
  print(get_ttf_basic())
  print('hello')
