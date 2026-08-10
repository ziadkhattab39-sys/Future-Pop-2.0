from Urban import Urban
from Border import Border

cairo = Urban("Cairo", "Cairo", "Urban", 9500000, 9850000, 10200000, 10560000, 10920000, 3085)
cairo.Calc_Pop_Density()
cairo.Calc_Pop_Growth_Rate()
cairo.Service_Ratio()
print("Cairo schools:", cairo.School_Number)
print("Cairo hospitals:", cairo.Hospital_Number)

sinai = Border("North Sinai", "Arish", "Border", 450000, 451000, 448000, 447000, 447500, 27564)
sinai.Calc_Pop_Density()
sinai.Calc_Pop_Growth_Rate()
sinai.Service_Ratio()
print("\nSinai schools:", sinai.School_Number)
print("Sinai hospitals:", sinai.Hospital_Number)