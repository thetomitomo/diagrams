SGD_TO_ID = 11348.9

TOTAL_INCLUDING_FEES = 857
# FX_FEE = 5.82

KATHERIN_BASE = 4220000
KENTHER_BASE = 4220000
TOMY_BASE = 1220000
SUM = KATHERIN_BASE+KENTHER_BASE+TOMY_BASE

KatherinPays = KATHERIN_BASE/SUM * TOTAL_INCLUDING_FEES
KentherPays = KENTHER_BASE/SUM * TOTAL_INCLUDING_FEES
TomyPays = TOMY_BASE/SUM * TOTAL_INCLUDING_FEES
sum = KatherinPays+KentherPays+TomyPays

TomyPaysRobo = 3000000/SGD_TO_ID

messages = [
    f'Total transfer of Rp {SUM:.2f} is SGD {TOTAL_INCLUDING_FEES:.2f}',
    f'Assuming SGD to ID rate at {SGD_TO_ID:.2f}',
    f'Katherin pays Tomy SGD {KatherinPays:.2f} (Rp {KATHERIN_BASE})',
    f'Kenther pays Tomy SGD {KentherPays:.2f} (Rp{KENTHER_BASE})',
    f"Tomy's payment portion is SGD {TomyPays:.2f} (Rp{TOMY_BASE})",
    f"Tomy will transfer SGD {TomyPaysRobo:.2f} to RoboInvestment"
]
messages = "\n".join(messages)
print(messages)
