import numpy as np
import pandas as pd
from matplotlib import pyplot
file="C:/Users/KHAN/Desktop/Skin_Care.xlsx"
df=pd.read_excel(file)
df.head()
df["Do you think there's need of Burn medication betterment in Pakistan"].value_counts().plot(kind='bar')
df["Do you think it can revolutionize the Health Care?"].value_counts().plot(kind='bar',color=['b','r','g'])
df["If you find a device that can identify the degree of burn and provide you with first aid treatment, would you invest in purchasing the smart device "].value_counts().plot(kind='bar',color=['b','r','g','y'])
