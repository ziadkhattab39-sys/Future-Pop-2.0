from Urban import Urban
from Border import Border

cairo = Urban(
    name="Cairo", capital="Cairo",
    pop0=9500000, pop1=9850000, pop2=10200000, pop3=10560000, pop4=10920000,
    area=3085, type_="Urban"
)
cairo.service_ratio()
print("Cairo school number:", cairo.school_number)
print("Cairo hospital number:", cairo.hospital_number)
print("Cairo fire station number:", cairo.fire_station_number)

sinai = Border(
    name="North Sinai", capital="Arish",
    pop0=450000, pop1=451000, pop2=448000, pop3=447000, pop4=447500,
    area=27564, type_="Border"
)
sinai.service_ratio()
print("\nNorth Sinai school number:", sinai.school_number)
print("North Sinai hospital number:", sinai.hospital_number)
print("North Sinai fire station number:", sinai.fire_station_number)