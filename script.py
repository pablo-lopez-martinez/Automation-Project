import pandas as pd 
from functions import create_pdf
import os 



count = 1

df = pd.read_excel('cotizaciones.xlsx', dtype={'item': int, 'cantidad': int})
df['precio']= df['precio'].round(2)
df['precio total cot'] = df['precio total cot'].round(2)

unique_column = 'nro solicitud'

groups = df.groupby(unique_column)
#Por cada grupo se realiza una factura 
for group_name, group in groups:
    path_dest = os.path.join("C:/Users/Pablo/OneDrive/Escritorio/Claudia/facturas", f"factura{count}.pdf")
    create_pdf(group, path_dest)
    count+=1


print("\n\n\n\n\nHa salido todo bien")
