from Urban import Urban
from Border import Border

cairo = Urban("Cairo", "Cairo", "Urban", 9500000, 9850000, 10200000, 10560000, 10920000, 3085)
cairo.Calc_Pop_Density()
cairo.Calc_Pop_Growth_Rate()
cairo.Calc_Density_Classification()
cairo.Calc_Growth_Rate_Classification()
cairo.Calc_Risk_Analysis()
print("Cairo:", cairo.Density_State, cairo.Growth_Rate_State, cairo.Risk_State)

sinai = Border("North Sinai", "Arish", "Border", 450000, 451000, 448000, 447000, 447500, 27564)
sinai.Calc_Pop_Density()
sinai.Calc_Pop_Growth_Rate()
sinai.Calc_Density_Classification()
sinai.Calc_Growth_Rate_Classification()
sinai.Calc_Risk_Analysis()
print("Sinai:", sinai.Density_State, sinai.Growth_Rate_State, sinai.Risk_State)