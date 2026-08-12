import pandas as pd

Data = pd.read_excel("Unified_Form_Formatted.xlsx")

from Governorate import Governorate
from Urban import Urban
from Rural import Rural
from Mixed import Mixed
from Border import Border
Govs = []
print(len(Govs))
for index, row in Data.iterrows() :
    name = row["Governorate"]
    capital = row["Capital"]
    type = row["Type"].strip()
    pop2018 = row[2018]
    pop2020 = row[2020]
    pop2022 = row[2022]
    pop2024 = row[2024]
    pop2026 = row[2026]
    area = row["Area"]
    if type == "Urban" :
        Gov = Urban(name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area)
    elif type == "Rural" :
        Gov = Rural(name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area)
    elif type == "Mixed" :
        Gov = Mixed(name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area)
    elif type == "Border" :
        Gov = Border(name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area)
    Govs.append(Gov)

for i in  Govs :
    i.Calc_Pop_Growth_Rate()
    i.Calc_Pop_Density()
    i.Calc_Growth_Rate_Drop()
    i.Calc_Pred_Growth_Rate()
    i.Calc_Pred_Pop_Count()
    i.Service_Ratio()
    i.Show_Info()
    print(i.Pop_Growth_Rate)
    print(i.Pop_Density)
    print(i.Growth_Rate_Drop)
    print(i.Pred_Growth_Rate)
    print(i.Pred_Pop_Count)
    print(i.School_Number)
    print(i.Hospital_Number)
    print(i.Police_Number)
    print(i.Ambulance_Number)
    print(i.Fire_Station_Number)
    print("\n_______________________________________________\n")
