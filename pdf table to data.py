import pandas as pd
from tabula.io import read_pdf
path = "/Users/goldenhuang/Documents/analysis/Apple Reports.pdf"
df = read_pdf(path, pages = 'all', multiple_tables = True)
print(df)