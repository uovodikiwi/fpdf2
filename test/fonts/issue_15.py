import unittest
import sys
import os
# from . import * as fonts
# import self as fonts
# import __init__ as fonts

from . import get_ttf_basic

# from . import say_hi
# class THING(object):
#   """docstring for THING"""
#   def __init__(self, say_hi):
#     super(THING, self).__init__()
#     self.say_hi = say_hi
# fonts = THING(say_hi)

sys.path.insert(0,
  os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    os.path.join('..', '..')
  )
)

import fpdf
import test
from test.utilities import relative_path_to, \
                           set_doc_date_0, \
                           calculate_hash_of_file

# python -m unittest test.fonts.issue_15.Issue15

class Issue15(unittest.TestCase):
  def test_issue_15(self):

    basic_ttfs = get_ttf_basic()
    basic_ttf = basic_ttfs[4]
    print(basic_ttf)

    example_name_ac = 'HELLO WORLD'
    example_name_example = example_name_ac
    pdf = fpdf.FPDF('L', 'pt', 'A4')
    pdf.add_font('Bookman Old Style', '', basic_ttf, uni=True)
    pdf.add_font('Bookman Old Style', 'B', basic_ttf, uni=True)

    pdf.add_page()
    # pdf.image(example_background, x=0, y=0, h=200, w=200)
    pdf.ln(10)
    pdf.set_font('Bookman Old Style', 'B', 45)
    pdf.cell(100, 47, example_name_example, ln=2, align="C")

    outfile = relative_path_to('line_output1.pdf')
    pdf.output(outfile)
    # print(calculate_hash_of_file(outfile))
    # known_good_hash = "4cf8faa9baf3f1835c03fa4ac1e6eb29"
    # self.assertEqual(known_good_hash, calculate_hash_of_file(outfile))
    # os.system('evince ' + outfile)
    os.unlink(outfile)


if __name__ == '__main__':
  unittest.main()

## Development of demo mostly done as written above.
    # self.assertEqual(known_good_hash, calculate_hash_of_file(outfile))
    # os.unlink(outfile)
