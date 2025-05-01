import pandas as pd

save = pd.read_excel('product.xlsx', engine='openpyxl')

print(save)