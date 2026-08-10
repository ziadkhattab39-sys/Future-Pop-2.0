from Governorate import Governorate


class Mixed(Governorate):
    def __init__(self, name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area):
        super().__init__(name, capital, type, pop2018, pop2020, pop2022, pop2024, pop2026, area)

        self.School_Ratio = 4000.0
        self.Hospital_Ratio = 70000.0
        self.Police_Ratio = 40000.0
        self.Ambulance_Ratio = 55000.0
        self.Fire_Station_Ratio = 20000.0

    def Service_Ratio(self) -> None:
        mixed_school = self.Pop_Count[4] / self.School_Ratio
        self.School_Number = int(mixed_school)

        mixed_hospital = self.Pop_Count[4] / self.Hospital_Ratio
        self.Hospital_Number = int(mixed_hospital)

        mixed_police = self.Pop_Count[4] / self.Police_Ratio
        self.Police_Number = int(mixed_police)

        mixed_ambulance = self.Pop_Count[4] / self.Ambulance_Ratio
        self.Ambulance_Number = int(mixed_ambulance)

        mixed_fire_Stations = self.Pop_Count[4] / self.Fire_Station_Ratio
        self.Fire_Station_Number = int(mixed_fire_Stations)
