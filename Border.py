from Governorate import Governorate


class Border(Governorate):
    def __init__(self, name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area):
        super().__init__(name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area)

        self.School_Ratio = 3500.0
        self.Hospital_Ratio = 30000.0
        self.Police_Ratio = 20000.0
        self.Ambulance_Ratio = 40000.0
        self.Fire_Station_Ratio = 45000.0

    def Service_Ratio(self):
        latest_pop = self.Pop_Count[4]

        self.School_Number = int(latest_pop / self.School_Ratio)
        self.Hospital_Number = int(latest_pop / self.Hospital_Ratio)
        self.Police_Number = int(latest_pop / self.Police_Ratio)
        self.Ambulance_Number = int(latest_pop / self.Ambulance_Ratio)
        self.Fire_Station_Number = int(latest_pop / self.Fire_Station_Ratio)

    def Future_Service(self):
        if not self.Pred_Pop_Count:
            raise ValueError("Predicted population has not been calculated yet.")

        self.Future_School_Number = []
        self.Future_Hospital_Number = []
        self.Future_Police_Number = []
        self.Future_Ambulance_Number = []
        self.Future_Fire_Station_Number = []

        for future_pop in self.Pred_Pop_Count:
            self.Future_School_Number.append(int(future_pop / self.School_Ratio))
            self.Future_Hospital_Number.append(int(future_pop / self.Hospital_Ratio))
            self.Future_Police_Number.append(int(future_pop / self.Police_Ratio))
            self.Future_Ambulance_Number.append(int(future_pop / self.Ambulance_Ratio))
            self.Future_Fire_Station_Number.append(int(future_pop / self.Fire_Station_Ratio))