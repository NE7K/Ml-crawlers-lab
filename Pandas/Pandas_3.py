import pandas as pd

# info xlsx file open = read_excel, engine='openpyxl'
save = pd.read_excel('product.xlsx', engine='openpyxl')

print(save)