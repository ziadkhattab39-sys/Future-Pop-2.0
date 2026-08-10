from Governorate import Governorate


class Border(Governorate):
    def __init__(
        self,
        name: str,
        capital: str,
        pop0: int,
        pop1: int,
        pop2: int,
        pop3: int,
        pop4: int,
        area: int,
        type_: str,
    ):
        super().__init__(name=name, capital=capital, area=area, type_=type_)
        self.pop_count[0] = pop0
        self.pop_count[1] = pop1
        self.pop_count[2] = pop2
        self.pop_count[3] = pop3
        self.pop_count[4] = pop4
        self.school_ratio = 3500.0
        self.hospital_ratio = 30000.0
        self.police_ratio = 20000.0
        self.ambulance_ratio = 40000.0
        self.fire_station_ratio = 45000.0

    def service_ratio(self) -> None:
        border_school = self.pop_count[4] / self.school_ratio
        self.school_number = int(border_school)

        border_hospital = self.pop_count[4] / self.hospital_ratio
        self.hospital_number = int(border_hospital)

        border_police = self.pop_count[4] / self.police_ratio
        self.police_number = int(border_police)

        border_ambulance = self.pop_count[4] / self.ambulance_ratio
        self.ambulance_number = int(border_ambulance)

        border_fire = self.pop_count[4] / self.fire_station_ratio
        self.fire_station_number = int(border_fire)