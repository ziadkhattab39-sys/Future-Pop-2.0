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

        ### Services (يتحدد في كل subclass)
        self.School_Number = 0
        self.Hospital_Number = 0
        self.Police_Number = 0
        self.Ambulance_Number = 0
        self.Fire_Station_Number = 0

        ### Risk Analysis
        self.DENSITY_RISK_THRESHOLD = 2500
        self.GROWTH_RISK_THRESHOLD = 0.02
        self.Density_State = ""
        self.Growth_Rate_State = ""
        self.Risk_State = ""

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

    def Calc_Density_Classification(self):
            # Classifies the latest population density into one of five categories.
            if not self.Pop_Density:
                raise ValueError("Population density has not been calculated yet.")
            # [-1] gets the last value in the list, which represents the latest year.
            Last_Density = self.Pop_Density[-1]
            # Make sure the latest density is actually a number.
            if not isinstance(Last_Density, (int, float)) or isinstance(Last_Density, bool):
                raise TypeError("The latest population density must be a number.")

            if 0 < Last_Density < 100:
                self.Density_State = "Sparse"
            elif Last_Density < 1000:
                self.Density_State = "Low"
            elif Last_Density < 2500:
                self.Density_State = "Moderate"
            elif Last_Density < 4000:
                self.Density_State = "High"
            else:
                self.Density_State = "Very High"

    def Calc_Growth_Rate_Classification(self):
            # Classifies the latest population growth rate into one of four categories.
            if not self.Pop_Growth_Rate:
                raise ValueError("Population growth rate has not been calculated yet.")
            # [-1] gets the latest growth rate.
            Last_Growth_Rate = self.Pop_Growth_Rate[-1]
            # Make sure the latest growth rate is actually a number.
            if not isinstance(Last_Growth_Rate, (int, float)) or isinstance(Last_Growth_Rate, bool):
                raise TypeError("The latest population growth rate must be a number.")
    
            if Last_Growth_Rate < 0.01:
                self.Growth_Rate_State = "Stable"
            elif Last_Growth_Rate < 0.02:
                self.Growth_Rate_State = "Moderate"
            elif Last_Growth_Rate < 0.03:
                self.Growth_Rate_State = "High"
            else:
                self.Growth_Rate_State = "Explosive"

    def Calc_Risk_Analysis(self):
            # Combines the latest density and growth rate to determine the overall risk.
            if not self.Pop_Density:
                raise ValueError("Population density has not been calculated yet.")
            if not self.Pop_Growth_Rate:
                raise ValueError("Population growth rate has not been calculated yet.")
            # Get the latest density and growth rate.
            Last_Density = self.Pop_Density[-1]
            Last_Growth_Rate = self.Pop_Growth_Rate[-1]
            # Check that both values are numbers.
            if not isinstance(Last_Density, (int, float)) or isinstance(Last_Density, bool):
                raise TypeError("The latest population density must be a number.")
            if not isinstance(Last_Growth_Rate, (int, float)) or isinstance(Last_Growth_Rate, bool):
                raise TypeError("The latest population growth rate must be a number.")
    
            # True means the value has reached its risk threshold.
            Density_Risk = Last_Density >= self.DENSITY_RISK_THRESHOLD
            Growth_Risk = Last_Growth_Rate >= self.GROWTH_RISK_THRESHOLD
    
            if not Density_Risk and not Growth_Risk:
                self.Risk_State = "Stable"
            elif not Density_Risk and Growth_Risk:
                self.Risk_State = "Growing"
            elif Density_Risk and not Growth_Risk:
                self.Risk_State = "Crowded"
            else:
                self.Risk_State = "Critical"

    def Show_Info (self) :
        print(f"""
Governorate Name: {self.Gov_Name}
Governorate Type: {self.Gov_Type}
Governorate Area: {self.Area}
""")