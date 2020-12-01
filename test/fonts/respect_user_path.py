"""respect_user_path.py"""

import fpdf
import os
import pathlib
import six
import shutil
import sys
import traceback
import unittest


# python -m unittest test.fonts.respect_user_path.UserPathTest

from test.utilities import relative_path_to, set_doc_date_0

@unittest.skip("skip while under development")
class UserPathTest(unittest.TestCase):
  def test_regular_add_font_dir(self):
    pdf = fpdf.FPDF()
    set_doc_date_0(pdf)
    pdf.add_page()
    
    with self.assertRaises(fpdf.errors.FPDFUndefinedFontException) as raised:
      pdf.set_font('abc')

    ex = raised.exception
    self.assertEqual(str(ex), 'Undefined font: abc')
    self.assertEqual(repr(ex), "FPDFUndefinedFontException('abc', '')")

  def test_regular_add_font_dir(self):
    # where fpdf will try to look
    dn, join = os.path.dirname, os.path.join
    font_tests = dn(os.path.abspath(__file__))
    repo = dn(dn(font_tests))
    regular_folder = join(repo, 'fpdf', 'font')

    os.mkdir(regular_folder)
    testing_output = relative_path_to('test_regular_add_font_dir.pdf')

    def cp_to_regular_folder(f):
      shutil.copyfile(join(font_tests, f), join(regular_folder, f))
      

    try:
      cp_to_regular_folder('slick.ttf')
      pdf = fpdf.FPDF()
      pdf.set_font('arial', '', 12)
      set_doc_date_0(pdf)
      pdf.add_page()
      pdf.add_font('slick', '', 'slick.ttf', True)
      pdf.set_font('slick', '', 12)
      pdf.write(12, 'hello world hello world hello world hello world')
      pdf.output(testing_output)

      try:
        os.system('ls -la ' + regular_folder)
        os.system('file ' + regular_folder)
        os.system('evince {}'.format(testing_output))
      except Exception as e:
        print('os system errors')
    except Exception as e:
      traceback.print_exc()
      # (''.join(traceback.format_stack()))
    finally:
      try:
        shutil.rmtree(regular_folder)
        os.unlink(testing_output)
      except Exception as e:
        print('\n\nproblems unlinking\n\n')


    os.system('ls -la ' + regular_folder)

