szamlak = [
    {"partner": "Kovacs Bt.", "email": "info@kovacsbt.hu", "sorszam": "2026/0142", "osszeg": 340000, "hatarido": "2026-08-10", "kifizetve": False},
    {"partner": "Kovacs Bt.", "email": "info@kovacsbt.hu", "sorszam": "2026/0151", "osszeg": 125000, "hatarido": "2026-08-25", "kifizetve": False},
    {"partner": "Nagy Kft.", "email": "penzugy@nagykft.hu", "sorszam": "2026/0147", "osszeg": 780000, "hatarido": "2026-08-15", "kifizetve": True},
    {"partner": "Szabo Zrt.", "email": "szamla@szabozrt.hu", "sorszam": "2026/0155", "osszeg": 95000, "hatarido": "2026-09-20", "kifizetve": False},
]
for szamla in szamlak:
    if szamla["kifizetve"] == False:
        print(szamla["partner"], szamla["sorszam"], szamla["osszeg"])