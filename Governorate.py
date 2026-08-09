class Governorate :
    def __init__(self, name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area):
        self.Gov_Name = name
        self.Gov_Capital = capital
        self.Gov_Type = type
        self.Pop_Count = [pop2018, pop2020, pop2022, pop2024 ,pop2026]
        self.Area = area

    Pop_Density = []
    def Calc_Pop_Density (self) :
        for i in range(5) :
            Density = self.Pop_Count[i] / self.Area
            self.Pop_Density.append(Density)

    Pop_Growth_Rate = []
    def Calc_Pop_Growth_Rate (self) :
        for i in  range(4) :
            Growth_Rate = (self.Pop_Count[i+1] - self.Pop_Count[i]) / self.Pop_Count[i]
            self.Pop_Growth_Rate.append(Growth_Rate)

    Pred_Pop_Growth_Rate = []
    Growth_Rate_Drop = []
    def Calc_Growth_Rate_Drop (self) :
        Total_Growth_Rate = self.Pop_Growth_Rate + self.Pred_Pop_Growth_Rate
        for i in range(len(self.Pop_Growth_Rate) + len(self.Pred_Pop_Growth_Rate) - 1) :
            Drop = Total_Growth_Rate[i+1] - Total_Growth_Rate[i]
            self.Growth_Rate_Drop.append(Drop)