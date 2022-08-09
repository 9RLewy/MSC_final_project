

import pandas as pd


table = pd.read_csv('testset-levelc.tsv', sep='\t')
table.to_csv('testset-levelc.csv', index=False)
