import pandas as pd
import numpy as np
import math
from pandas import DataFrame, read_csv
from orm.models import Kelas,Siswa,HasilTes,Karakter,NilaiAkademik,Plomba,Bobot
from io import BytesIO
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa 


#reportPDF
def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='apllication/pdf')
    return None


