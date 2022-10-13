### CURSO DE PYTHON - RAFA
### PANDAS

import numpy as np
import  pandas as pd

country = ['Mexico', 'Spain', 'Colombia', 'Peru']
day = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']
gender = ['F', 'M']

n=10000
mu = 10
sigma = 2

# Simulating the sell of a product to a one person:

np.random.seed(1235)
sim_gen = np.random.choice(gender, size=n )
sim_age = np.random.binomial(60, 0.5, size=n)   # valores alrededor de 30
sim_country = np.random.choice(country, p=[0.0, 0.5, 0.0, 0.5])    # p = sum(i) = 1
sim_spent = np.round(np.random.normal(loc=mu, scale=sigma, size=n), 2)
sim_day = np.random.choice(day, size=n)


dictionary_sim = dict(gender=sim_gen,
                      age = sim_age,
                      country=sim_country,
                      sim_spent=sim_spent,
                      day=sim_day)

# To create the DF
sales_df = pd.DataFrame(dictionary_sim)
print(sales_df.head())

# Export to a file
sales_df.to_csv('sales_online.csv', index=False)

# To load the file

sales_df2 = pd.read_csv('sales_online.csv')

print(sales_df2.head())
