from Governorate import Governorate


class Mixed(Governorate):
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
        self.school_ratio = 7500.0
        self.hospital_ratio = 42500.0
        self.police_ratio = 31000.0
        self.ambulance_ratio = 55000.0

    def service_ratio(self) -> None:
        mixed_school = self.pop_count[4] / self.school_ratio
        self.school_number = int(mixed_school)

        mixed_hospital = self.pop_count[4] / self.hospital_ratio
        self.hospital_number = int(mixed_hospital)

        mixed_police = self.pop_count[4] / self.police_ratio
        self.police_number = int(mixed_police)

        mixed_ambulance = self.pop_count[4] / self.ambulance_ratio
        self.ambulance_number = int(mixed_ambulance)
