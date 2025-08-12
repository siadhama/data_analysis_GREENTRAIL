import pandas as pd  
import numpy as np  

df=pd.read_csv("store_data.csv")
print(df.describe())
print(df.head(1))
for col in ["Weekly Sales During Promotion", "Weekly Sales Before Promotion","Average Daily Visits During Promotion","Average Daily Visits Before Promotion"]:
    df[col] ==pd.to_numeric(df[col],errors='coerce')
print(df.dtypes)

for cols in ["Weekly Sales During Promotion","Weekly Sales Before Promotion","Weekly Sales After Promotion"]:
    df[cols]=pd.to_numeric(df[cols].astype(str).str.strip(),errors='coerce')



print(df.dtypes)  
types=["Discount","Buy-One-Get-One","Special Event"]


for i in types:
    new_part=df[df["Type of Promotion"]==i]
    Sales_Uplift = ((new_part["Weekly Sales During Promotion"] - new_part["Weekly Sales Before Promotion"]) / new_part["Weekly Sales Before Promotion"]) * 100   
    print("the sales uplift for the promotion ",i,Sales_Uplift.mean())
    Visit_Uplift = ((new_part["Average Daily Visits During Promotion"] - new_part["Average Daily Visits Before Promotion"])/new_part["Average Daily Visits Before Promotion"]) * 100
    print("the visits uplift for the promotion ",i,Visit_Uplift.mean())



print("average analysis")
df["Sales Uplift (%)"] = ((df["Weekly Sales During Promotion"] - df["Weekly Sales Before Promotion"])
                           / df["Weekly Sales Before Promotion"]) * 100

df["Visit Uplift (%)"] = ((df["Average Daily Visits During Promotion"] - df["Average Daily Visits Before Promotion"])
                           / df["Average Daily Visits Before Promotion"]) * 100
average_sales_uplift = df["Sales Uplift (%)"].mean()
average_visit_uplift = df["Visit Uplift (%)"].mean()
print(f"📈 Average Sales Uplift: {average_sales_uplift:.2f}%")
print(f"👣 Average Visit Uplift: {average_visit_uplift:.2f}%")