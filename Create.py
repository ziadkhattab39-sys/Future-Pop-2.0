import pandas as pd
Data = pd.read_excel("Unified_Form_Formatted.xlsx")
from Governorate import Governorate
Govs = []

for index, row in Data.iterrows() :
    name = row["Governorate"]
    capital = row["Capital"]
    type = row["Type"]
    pop2018 = row[2018]
    pop2020 = row[2020]
    pop2022 = row[2022]
    pop2024 = row[2024]
    pop2026 = row[2026]
    area = row["Area"]
    Gov = Governorate(name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area)
    Govs.append(Gov)

Govs[0].Calc_Pop_Growth_Rate()
Govs[0].Calc_Pop_Density()
Govs[0].Calc_Growth_Rate_Drop()
Govs[0].Calc_Pred_Growth_Rate()
Govs[0].Calc_Pred_Pop_Count()
print(Govs[0].Pop_Growth_Rate)
print(Govs[0].Pop_Density)
print(Govs[0].Growth_Rate_Drop)
print(Govs[0].Pred_Growth_Rate)
print(Govs[0].Pred_Pop_Count)
print()
Govs[1].Calc_Pop_Growth_Rate()
Govs[1].Calc_Pop_Density()
Govs[1].Calc_Growth_Rate_Drop()
Govs[1].Calc_Pred_Growth_Rate()
Govs[1].Calc_Pred_Pop_Count()
print(Govs[1].Pop_Growth_Rate)
print(Govs[1].Pop_Density)
print(Govs[1].Growth_Rate_Drop)
print(Govs[1].Pred_Growth_Rate)
print(Govs[1].Pred_Pop_Count)