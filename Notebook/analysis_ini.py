# Telco customer churn problem

import pandas as pd
import matplotlib.pyplot as plt

churn_df = pd.read_csv('../Data/WA_Fn-UseC_-Telco-Customer-Churn.csv')
"""
# Basic information:
print(churn_df.head(10))
print('shape (rows, columns) = ', churn_df.shape)
# print(churn_df.dtypes)
"""
churn_df.info()

# EDA
# print(churn_df['Churn'].head(10))
q_churn = churn_df.groupby('Churn')['customerID'].count().reset_index()
print('q_churn: ',q_churn)
# print(type(q_churn))
# x = q_churn.size
# y= len(q_churn)
# print(x,y)

plt.pie(q_churn['customerID'],labels=q_churn['Churn'] ,autopct='%1.1f%%')
plt.title('Churn', loc='center', fontsize=30)
plt.show()




q_churn_no   = q_churn.loc[0,'customerID']
q_churn_yes  = q_churn.loc[1,'customerID']
q_churn_no_p = q_churn_no /(q_churn_no + q_churn_yes)
q_churn_yes_p = q_churn_yes /(q_churn_no + q_churn_yes)

print('Customers losses:     ',q_churn_no,  format(q_churn_no_p, '.1%') )
print('Customers retentions: ',q_churn_yes, format(q_churn_yes_p,'.1%') )



label = ['Retentions','Losses']
plt.pie(q_churn['customerID'],
        labels=label,
        colors=['g','r'],
        autopct='%1.1f%%'
        )
plt.show()


def fast_view(df1,col):
        colum_to_view = df1.groupby(col)['customerID'].count().reset_index()
        print('Column: ',colum_to_view)
        plt.pie(colum_to_view['customerID'],labels=colum_to_view[col] ,autopct='%1.1f%%')
        plt.title(col, loc='center', fontsize=30)
        plt.show()
        return len(colum_to_view['customerID'])

# fast_view(churn_df,'Churn')
# fast_view(churn_df,'gender')

q_var = []
for col in churn_df:
        if col == 'customerID':
                continue
        elif col == 'tenure':
                continue
        elif col == 'MonthlyCharges':
                continue
        elif col == 'TotalCharges':
                continue
        else:
                print(col)
                q_var.append(fast_view(churn_df, col))

print('Variables: ')
print(q_var)
