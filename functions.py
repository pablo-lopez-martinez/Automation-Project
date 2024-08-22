import pandas as pd
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Image, Paragraph, Spacer, LongTable
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import letter
import os 



def create_pdf(dataframe: pd.DataFrame, path_dest: str):
    

    head = dataframe.head(1)

    elements = []
    zona = head["zona"].values[0]
    fecha_datetime = pd.to_datetime(head["fecha"].values[0])
    if pd.isna(fecha_datetime): 
        fecha = "Fecha no Disponible"
    else:
        fecha =  fecha_datetime.strftime('%d-%m-%Y')
    empresa = head["empresa"].values[0]
    usuario = head["usuario"].values[0]
    ref = str(head["nuestra ref"].values[0])
    nro_solicitud = str(head["nro solicitud"].values[0])
    validez = str(head["validez de la oferta"].values[0])
    forma_pago = str(head["forma de pago"].values[0])
    tasa_cambio = str(head["tasa cambio"].values[0])
    
    #Creación de la imagen
    logo_path = 'logo.jpg'

    #Agregar el logo
    logo = Image(logo_path, width=100, height=50)
    elements.append(logo)
    elements.append(Spacer(0,50))
    elements.append(Paragraph(f"<b>Zona</b>: {zona}"))
    elements.append(Paragraph(f"<b>Fecha</b>: {fecha}"))
    elements.append(Paragraph(f"<b>Usuario</b>: {usuario}"))
    elements.append(Paragraph(f"<b>Referencia</b>: {ref}"))
    elements.append(Paragraph(f"<b>Nro solicitud</b>: {nro_solicitud}"))
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

    elements.append(Spacer(0,50))
    elements.append(Paragraph(f"<b>Validez de la oferta</b>: {validez}"))
    elements.append(Paragraph(f"<b>Forma de pago</b>: {forma_pago}"))
    elements.append(Paragraph(f"<b>Tasa de cambio</b>: {tasa_cambio} Bs/US$"))
    elements.append(Spacer(0,20))

    pdf.build(elements)
