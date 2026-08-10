from pathlib import Path

try:
    import pandas as pd
except ImportError:  # pragma: no cover - fallback for minimal environments
    pd = None

excel_path = Path(__file__).resolve().parent / "Unified_Form_Formatted.xlsx"

if pd is not None:
    try:
        Data = pd.read_excel(excel_path)
    except Exception:
        Data = None
else:
    Data = None


class Governorate:
    def __init__(self, name: str = "", capital: str = "", area: int = 0, type_: str = ""):
        self.name = name
        self.capital = capital
        self.area = area
        self.type = type_
        self.pop_count = [0] * 5
        self.school_number = 0
        self.hospital_number = 0
        self.police_number = 0

    def service_ratio(self):
        raise NotImplementedError("Subclasses must implement service_ratio()")