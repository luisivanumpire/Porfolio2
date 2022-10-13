# Working with gapminder files

import pandas as pd
gap_df = pd.read_csv('../gapminder_full.csv')
print(gap_df.head(10))
