from Governorate import Governorate
 
 
class Urban(Governorate):
    def __init__(self, name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area):
        super().__init__(name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area)
 
        self.School_Ratio = 9000.0
        self.Hospital_Ratio = 55000.0
        self.Police_Ratio = 35000.0
        self.Ambulance_Ratio = 60000.0
        self.Fire_Station_Ratio = 70000.0
 
    def Service_Ratio(self):
        latest_pop = self.Pop_Count[4]
 
        self.School_Number = int(latest_pop / self.School_Ratio)
        self.Hospital_Number = int(latest_pop / self.Hospital_Ratio)
        self.Police_Number = int(latest_pop / self.Police_Ratio)
        self.Ambulance_Number = int(latest_pop / self.Ambulance_Ratio)
        self.Fire_Station_Number = int(latest_pop / self.Fire_Station_Ratio)
 