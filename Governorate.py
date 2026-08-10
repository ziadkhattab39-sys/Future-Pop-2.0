<<<<<<< HEAD
from pathlib import Path

try:
    import pandas as pd
except ImportError:  # pragma: no cover - fallback for minimal environments
    pd = None

excel_path = Path(__file__).resolve().parent / "Unified_Form_Formatted.xlsx"

if pd is not None:
    try:
        Data = pd.read_excel(excel_path)
    except Exception:
        Data = None
else:
    Data = None


class Governorate:
    def __init__(self, name: str = "", capital: str = "", area: int = 0, type_: str = ""):
        self.name = name
        self.capital = capital
        self.area = area
        self.type = type_
        self.pop_count = [0] * 5
        self.school_number = 0
        self.hospital_number = 0
        self.police_number = 0

    def service_ratio(self):
        raise NotImplementedError("Subclasses must implement service_ratio()")
=======
class Governorate :
    def __init__(self, name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area):
        ### INPUTS
        self.Gov_Name = name
        self.Gov_Capital = capital
        self.Gov_Type = type
        self.Pop_Count = [pop2018, pop2020, pop2022, pop2024 ,pop2026]
        self.Area = area

        ### Calculated
        self.Pop_Density = []
        self.Pop_Growth_Rate = []
        self.Growth_Rate_Drop = []
        self.Avg_Growth_Rate_Drop = 0
        self.Pred_Growth_Rate = []
        self.Pred_Pop_Count = []

    def Calc_Pop_Density (self) :
        for i in range(5) :
            Density = self.Pop_Count[i] / self.Area
            self.Pop_Density.append(int(Density))

    def Calc_Pop_Growth_Rate (self) :
        for i in  range(4) :
            Growth_Rate = (self.Pop_Count[i+1] - self.Pop_Count[i]) / self.Pop_Count[i]
            self.Pop_Growth_Rate.append(Growth_Rate)

    def Calc_Growth_Rate_Drop (self) :
        for i in range(len(self.Pop_Growth_Rate) - 1) :
            Drop = self.Pop_Growth_Rate[i+1] - self.Pop_Growth_Rate[i]
            self.Growth_Rate_Drop.append(Drop)
        self.Avg_Growth_Rate_Drop = sum(self.Growth_Rate_Drop) / len(self.Growth_Rate_Drop)

    def Calc_Pred_Growth_Rate (self) :
        New2028 = self.Pop_Growth_Rate[3] + self.Avg_Growth_Rate_Drop
        New2030 = New2028 + self.Avg_Growth_Rate_Drop
        New2032 = New2030 + self.Avg_Growth_Rate_Drop
        self.Pred_Growth_Rate = [New2028, New2030, New2032]

    def Calc_Pred_Pop_Count (self) :
        Pop2028 = (1 + self.Pred_Growth_Rate[0]) * self.Pop_Count[4]
        Pop2030 = (1 + self.Pred_Growth_Rate[1]) * Pop2028
        Pop2032 = (1 + self.Pred_Growth_Rate[2]) * Pop2030
        self.Pred_Pop_Count = [int(Pop2028), int(Pop2030), int(Pop2032)]
>>>>>>> 9b0ac3bfb0b5ab7bede03a7ffc964483ce766222
