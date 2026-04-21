import pandas as pd
data = pd.read_csv("C:/Users/G SHIVAPRAKASH/OneDrive/Desktop/python/10prog_4laptops - 10prog_4laptops.csv")  
print(data) 
q3 = data['Weight_kg'].quantile(0.75)  
q1 = data['Weight_kg'].quantile(0.25) 
iqr = q3 - q1 
lower_bound = q1 - 1.5*iqr  
upper_bound = q3 + 1.5*iqr 
outliers = data[(data['Weight_kg'] < lower_bound) | (data['Weight_kg'] >  upper_bound)] 
print('lower bound, upper bound and iqr values are: ',lower_bound, upper_bound,  iqr) 
print('No.of outliers are: ', outliers.shape[0])
