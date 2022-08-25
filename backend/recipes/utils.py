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
HEADER_FONT_SIZE = 28
HEADER_TOP_MARGIN = 20
HEADER_BOTTOM_MARGIN = 35
BODY_FONT_SIZE = 14
BODY_LINE_SPACING = 12
TEXT_TOP_MARGIN = 10
TEXT_BOTTOM_MARGIN = 12
TEXT_RIGHT_MARGIN = 12
TEXT_LEFT_MARGIN = 50
SPACER = 1
STREAM_POSITION = 0


def header(doc, title, size, space, ta):
    doc.append(Spacer(SPACER, HEADER_TOP_MARGIN))
    doc.append(Paragraph(title, ParagraphStyle(
        name='name', fontName='arial', fontSize=size, alignment=ta
    )))
    doc.append(Spacer(SPACER, space))
    return doc


def body(doc, text, size):
    for line in text:
        doc.append(Paragraph(line, ParagraphStyle(
            name='line', fontName='arial', fontSize=size, alignment=TA_LEFT
        )))
        doc.append(Spacer(SPACER, BODY_LINE_SPACING))
    return doc


def download_pdf(data):
    buffer = io.BytesIO()
    font_path = os.path.join(FONTS_ROOT, 'fonts/', 'arial.ttf')
    pdfmetrics.registerFont(TTFont('arial', font_path))
    doc = header(
        [], 'Список покупок', HEADER_FONT_SIZE, HEADER_BOTTOM_MARGIN, TA_CENTER
    )
    pdf = SimpleDocTemplate(
        buffer,
        pagesize=A4,
        topMargin=TEXT_TOP_MARGIN,
        bottomMargin=TEXT_BOTTOM_MARGIN,
        rightMargin=TEXT_RIGHT_MARGIN,
        leftMargin=TEXT_LEFT_MARGIN,
    )
    pdf.build(body(doc, data, BODY_FONT_SIZE))
    buffer.seek(STREAM_POSITION)
    return FileResponse(
        buffer, as_attachment=True, filename='shopping_list.pdf'
    )
