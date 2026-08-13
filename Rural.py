from Governorate import Governorate

class Rural(Governorate):
    def __init__(self, name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area):
        super().__init__(name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area)

        self.School_Ratio = 4500.0
        self.Hospital_Ratio = 65000.0
        self.Police_Ratio = 35000.0
        self.Ambulance_Ratio = 50000.0
        self.Fire_Station_Ratio = 25000.0

    def Service_Ratio(self) -> None:
        rural_school = self.Pop_Count[4] / self.School_Ratio
        self.School_Number = int(rural_school)

        rural_hospital = self.Pop_Count[4] / self.Hospital_Ratio
        self.Hospital_Number = int(rural_hospital)

        rural_police = self.Pop_Count[4] / self.Police_Ratio
        self.Police_Number = int(rural_police)

        rural_ambulance = self.Pop_Count[4] / self.Ambulance_Ratio
        self.Ambulance_Number = int(rural_ambulance)

        rural_fire_Stations = self.Pop_Count[4] / self.Fire_Station_Ratio
        self.Fire_Station_Number = int(rural_fire_Stations)

    def Future_Service(self):
        if not self.Pred_Pop_Count:
            raise ValueError("Predicted population has not been calculated yet.")

        for future_pop in self.Pred_Pop_Count:
            self.Future_School_Number.append(int(future_pop / self.School_Ratio))
            self.Future_Hospital_Number.append(int(future_pop / self.Hospital_Ratio))
            self.Future_Police_Number.append(int(future_pop / self.Police_Ratio))
            self.Future_Ambulance_Number.append(int(future_pop / self.Ambulance_Ratio))
            self.Future_Fire_Station_Number.append(int(future_pop / self.Fire_Station_Ratio))