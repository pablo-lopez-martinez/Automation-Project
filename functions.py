import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, Spacer, LongTable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import os 





def create_pdf(dataframe: pd.DataFrame, path_dest: str):
    

    head = dataframe.head(1)

    elements = []
    zona = head["zona"].values[0]
    fecha = str(head["fecha"].values[0])
    empresa = head["empresa"].values[0]
    usuario = head["usuario"].values[0]
    ref = str(head["nuestra ref"].values[0])
    nro_solicitud = str(head["nro solicitud"].values[0])
    
    #Creación de la imagen
    logo_path = 'logo.jpg'

    #Agregar el logo
    logo = Image(logo_path, width=100, height=50)
    elements.append(logo)
    elements.append(Spacer(0,50))
    elements.append(Paragraph(f"Zona: {zona}"))
    elements.append(Paragraph(f"Fecha: {fecha}"))
    elements.append(Paragraph(f"Usuario: {usuario}"))
    elements.append(Paragraph(f"Referencia: {ref}"))
    elements.append(Paragraph(f"Nro solicitud: {nro_solicitud}"))
    elements.append(Spacer(0,20))
    
    
    #Generación tabla de precios e items 
    info = dataframe[['cantidad', 'desc larga', 'precio total cot', 'precio prov', 'tiempo entrega']]

    #Procesado para crear la tabla 
    info['desc larga'] = info['desc larga'].astype(str).replace(';','\n');
    info['desc larga'] = info['desc larga'].apply(lambda x: Paragraph(x, None))

    info['tiempo entrega'] = info['tiempo entrega'].astype(str);
    info['tiempo entrega'] = info['tiempo entrega'].apply(lambda x: Paragraph(x, None))
    
    pdf = SimpleDocTemplate(path_dest, pagesize=letter)
    
    column_widths = [50, 200, 80, 80, 80]
    table_info = [info.columns] + info.values.tolist()
    table = Table(table_info , column_widths)
   
    style = [('BACKGROUND', (0, 0), (-1, 0), (0.7, 0.7, 0.7)),
             ('TEXTCOLOR', (0, 0), (-1, 0), (1, 1, 1)),
             ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
             ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
             ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
             ('BACKGROUND', (0, 1), (-1, -1), (0.9, 0.9, 0.9)),
             ('GRID', (0, 0), (-1, -1), 1, (0, 0, 0)),
             ('VALIGN', (0, 0), (-1, -1), 'MIDDLE')]
    
    table.setStyle(style)

    elements.append(table)

    pdf.build(elements)
