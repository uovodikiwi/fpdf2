# Links #

`fpdf2` can generate both **internal** links (to other pages in the document)
& **hyperlinks** (links to external URLs that will be opened in a browser).


## Internal links ##

_TODO: work in progress_


## Hyperlink with FPDF.cell ##

This method makes the whole cell clickable (not only the text):

```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=24)
pdf.cell(w=40, h=10, txt="Cell link", border=1, align="C", link="https://github.com/PyFPDF/fpdf2")
pdf.output("hyperlink.pdf")
```


## Hyperlink with FPDF.link ##

The `FPDF.link` is a low-level method that defines a rectangular clickable area.

There is an example showing how to place such rectangular link over some text:

```python
from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("helvetica", size=36)
line_height = 10
text = "Text link"
pdf.text(x=0, y=line_height, txt=text)
width = pdf.get_string_width(text)
pdf.link(x=0, y=0, w=width, h=line_height, link="https://github.com/PyFPDF/fpdf2")
pdf.output("hyperlink.pdf")
```


## Hyperlink with write_html ##

An alternative method using [`fpdf.HTMLMixin`](HTML.html):

```python
from fpdf import FPDF, HTMLMixin

class PDF(FPDF, HTMLMixin):
    pass

pdf = PDF()
pdf.set_font_size(16)
pdf.add_page()
pdf.write_html('<a href="https://github.com/PyFPDF/fpdf2">Link defined as HTML</a>')
pdf.output('hyperlink.pdf')
```

The hyperlinks defined this way will be rendered in blue with underline.
