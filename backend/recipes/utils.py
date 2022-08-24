import io
import os

from django.http import FileResponse
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

FONTS_ROOT = os.path.dirname(os.path.abspath(__file__))


def header(doc, title, size, space, ta):
    doc.append(Spacer(1, 20))
    doc.append(Paragraph(title, ParagraphStyle(
        name='name', fontName='arial', fontSize=size, alignment=ta
    )))
    doc.append(Spacer(1, space))
    return doc


def body(doc, text, size):
    for line in text:
        doc.append(Paragraph(line, ParagraphStyle(
            name='line', fontName='arial', fontSize=size, alignment=TA_LEFT
        )))
        doc.append(Spacer(1, 12))
    return doc


def download_pdf(data):
    buffer = io.BytesIO()
    font_path = os.path.join(FONTS_ROOT, 'fonts/', 'arial.ttf')
    pdfmetrics.registerFont(TTFont('arial', font_path))
    doc = header([], 'Список покупок', 28, 35, TA_CENTER)
    pdf = SimpleDocTemplate(
        buffer, pagesize=A4, topMargin=10, bottomMargin=12, rightMargin=12,
        leftMargin=50,
    )
    pdf.build(body(doc, data, 14))
    buffer.seek(0)
    return FileResponse(
        buffer, as_attachment=True, filename='shopping_list.pdf'
    )
