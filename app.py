from flask import Flask, render_template, request
from typing import List, Tuple

app = Flask(__name__)

# Data
hotel = [
        ("Abadan", 1136000, 0, 2274000, 607300, 0), ("Abadeh", 0, 0, 0, 566000, 515000), ("Arak", 824000, 0, 1957000, 0, 1339000), ("Ardabil", 580000, 0, 3770000, 327000, 1635000), ("Ardakan", 0, 0, 0, 797000, 741600), ("Esfahan", 780000, 2100000, 3660000, 417000, 773000), ("Ahvaz", 741600, 2950000, 2873700, 978000, 0), ("Bandar Abbas", 2276000, 2718000, 2900000, 1485000, 0), ("Bandar Anzali", 1275000, 2750000, 0, 618000, 1545000), ("Bojnurd", 830000, 1405000, 0, 0, 0), ("Birjand", 1263600, 1093000, 0, 520000, 0), ("Babol", 0, 0, 0, 742000, 0), ("Tabriz", 853000, 2142400, 2595000, 1479000, 1030000), ("Tehran", 1267000, 3090000, 3420000, 430000, 1030000), ("Jiroft", 927000, 0, 0, 0, 0), ("Kerman", 824000, 2260000, 2171000, 592000, 927000), ("Kermanshah", 0, 1610000, 1720000, 1166000, 1312200), ("Kashan", 1564000, 0, 0, 813000, 510000), ("Qazvin", 1905000, 1500000, 0, 310000, 1854000), ("Mashhad", 826000, 1744000, 2300000, 1072000, 1410000), ("Shiraz", 794000, 1152000, 1855000, 288000, 536000), ("Yazd", 325000, 1348000, 2110000, 380000, 310000), ("Qom", 1312000, 927000, 0, 713000, 445000), ("Sanandaj", 2120000, 1826000, 0, 0, 418000), ("Sari", 1045000, 824000, 0, 721000, 2400000), ("Hamedan", 918000, 1590000, 0, 650000, 577000), ("Gorgan", 1345000, 1500000, 2100000, 618000, 927000), ("Rasht", 1900000, 3250000, 2377000, 1236000, 412000), ("Zanjan", 709000, 3100000, 0, 578000, 1442000), ("Urmia", 1228000, 766000, 4400000, 1260000, 0), ("Qeshm", 721000, 1700000, 4220000, 650000, 618000), ("Sabzevar", 900000, 0, 0, 870000, 0), ("Nishapur", 0, 1820000, 0, 735000, 1545000), ("Kazerun", 0, 0, 0, 0, 0), ("Kish", 740000, 860000, 1854000, 834000, 0), ("Ilam", 1770000, 0, 0, 0, 0), ("Bushehr", 1300000, 0, 3368000, 740000, 780000), ("Bam", 0, 1761300, 0, 934000, 0), ("Bandar Lengeh", 0, 0, 0, 0, 0), ("Zabol", 0, 0, 0, 515000, 0), ("Karaj", 1800000, 0, 0, 810000, 1030000), ("Khorramabad", 1340000, 0, 0, 0, 1854000), ("Shahr-e Kord", 1300000, 2140000, 0, 470000, 0), ("Yasuj", 1567000, 1528000, 0, 0, 1140000), ("Ramsar", 1630000, 3400000, 0, 0, 722000), ("Najafabad", 0, 1820000, 0, 1130000, 1546000), ("Zarand", 1100000, 1875000, 0, 700000, 0), ("Maku", 0, 0, 0, 556000, 0), ("Dezful", 1340000, 0, 0, 1400000, 0), ("Mahabad", 800000, 0, 0, 0, 970000), ("Gonbad Kavus", 0, 0, 0, 566000, 1610000), ("Quchan", 0, 0, 0, 0, 0), ("Khoy", 1244000, 0, 0, 1020000, 0), ("Kashmar", 0, 0, 0, 0, 0), ("Lahijan", 1370000, 1920000, 2200000, 1140000, 2780000), ("Malayer", 0, 0, 0, 740000, 0), ("Maragheh", 0, 0, 0, 862000, 773000), ("Minab", 0, 0, 0, 1120000, 0), ("Nahavand", 0, 0, 0, 0, 0), ("Saveh", 0, 1100000, 0, 544000, 0), ("Shushtar", 773000, 0, 0, 741600, 700000), ("Susa", 0, 0, 0, 0, 0), ("Varamin", 785000, 0, 0, 0, 1468000)

]

havapeyma = [
        ("Abadan", "Esfahan", 2110000),("Abadan", "Mashhad", 1450000),("Abadan", "Shiraz", 2100000),("Abadan", "Kermanshah", 2350000),("Abadan", "Bandar Abbas", 2800000),("Abadan", "Tehran", 1500000),("Arak", "Mashhad", 1900000),("Arak", "Tehran", 850000),("Ardabil", "Tehran", 2100000),("Ardabil", "Mashhad", 2700000),("Esfahan", "Tabriz", 2250000),("Esfahan", "Mashhad", 2900000),("Esfahan", "Bandar Abbas", 2700000),("Esfahan", "Ahvaz", 2500000),("Esfahan", "Gorgan", 2000000),("Esfahan", "Kerman", 2400000),("Esfahan", "Kermanshah", 2300000),("Esfahan", "Kish", 3900000),("Esfahan", "Rasht", 2400000),("Esfahan", "Shiraz", 2100000),("Esfahan", "Tehran", 2200000),("Esfahan", "Zahedan", 2600000),("Esfahan", "Abadan", 2110000),("Esfahan", "Ramsar", 2500000),("Esfahan", "Qeshm", 2700000),("Esfahan", "Sari", 2100000),("Esfahan", "Yazd", 1800000),("Ahvaz", "Esfahan", 2500000),("Ahvaz", "Yazd", 1900000),("Ahvaz", "Shiraz", 2120000),("Ahvaz", "Rasht", 3570000),("Ahvaz", "Tabriz", 3125000),("Ahvaz", "Mashhad", 2800000),("Ahvaz", "Kish", 2000000),("Ahvaz", "Kermanshah", 2350000),("Ahvaz", "Bandar Abbas", 3570000),("Ahvaz", "Sari", 2600000),("Ahvaz", "Tehran", 2400000),("Bandar Abbas", "Tehran", 3250000),("Bandar Abbas", "Shiraz", 2200000),("Bandar Abbas", "Esfahan", 2700000),("Bandar Abbas", "Tabriz", 3600000),("Bandar Abbas", "Yazd", 1950000),("Bandar Abbas", "Rasht", 3520000),("Bandar Abbas", "Abadan", 2800000),("Bandar Abbas", "Kermanshah", 2500000),("Bandar Abbas", "Ahvaz", 3100000),("Bandar Abbas", "Mashhad", 2500000),("Bandar Abbas", "Sari", 3300000),("Bandar Abbas", "Bushehr", 2000000),("Bandar Abbas", "Kish", 2000000),("Bandar Abbas", "Gorgan", 2700000),("Bojnurd", "Tehran", 2500000),("Birjand", "Tehran", 2800000),("Birjand", "Mashhad", 1800000),("Tabriz", "Tehran", 2400000),("Tabriz", "Mashhad", 3000000),("Tabriz", "Esfahan", 2700000),("Tabriz", "Shiraz", 3300000),("Tabriz", "Ahvaz", 3120000),("Tabriz", "Bandar Abbas", 3600000),("Tabriz", "Kish", 3200000),("Tabriz", "Qeshm", 2800000),("Tabriz", "Rasht", 2500000),("Tabriz", "Sari", 2500000),("Tabriz", "Kermanshah", 2300000),("Tehran", "Mashhad", 2500000),("Tehran", "Bandar Abbas", 3300000),("Tehran", "Khorramabad", 2000000),("Tehran", "Tabriz", 2400000),("Tehran", "Kish", 3300000),("Tehran", "Qeshm", 3200000),("Tehran", "Abadan", 2560000),("Tehran", "Chabahar", 3200000),("Tehran", "Ahvaz", 2400000),("Tehran", "Shiraz", 2600000),("Tehran", "Sirjan", 2800000),("Tehran", "Sanandaj", 2100000),("Tehran", "Esfahan", 2000000),("Tehran", "Birjand", 2800000),("Tehran", "Bojnurd", 2500000),("Tehran", "Zahedan", 3300000),("Tehran", "Yazd", 2300000),("Tehran", "Ilam", 2300000),("Tehran", "Kerman", 2800000),("Tehran", "Ardabil", 2100000),("Tehran", "Gorgan", 2000000),("Tehran", "Kermanshah", 2100000),("Tehran", "Urmia", 2500000),("Tehran", "Dezful", 2200000),("Tehran", "Jahrom", 2700000),("Tehran", "Bandar Lengeh", 2500000),("Tehran", "Rasht", 2000000),("Tehran", "Yasuj", 2400000),("Tehran", "Bushehr", 2500000),("Tehran", "Arak", 850000),("Tehran", "Nowshahr", 1900000),("Tehran", "Ramsar", 2000000),("Tehran", "Sari", 770000),("Tehran", "Shahr-e Kord", 1900000),("Tehran", "Maragheh", 2300000),("Tehran", "Jiroft", 3100000),("Tehran", "Zabol", 3150000),("Tehran", "Sabzevar", 2500000),("Tehran", "Rafsanjan", 2450000),("Tehran", "Khoy", 2560000),("Tehran", "Hamedan", 1850000),("Tehran", "Karaj", 1200000),("Tehran", "Zanjan", 1950000),("Tehran", "Kashan", 1500000),("Jiroft", "Tehran", 3100000),("Kerman", "Tehran", 2700000),("Kerman", "Mashhad", 2500000),("Kerman", "Shiraz", 2100000),("Kerman", "Esfahan", 2400000),("Kerman", "Tabriz", 2800000),("Kerman", "Kish", 2900000),("Kerman", "Zahedan", 2700000),("Kerman", "Ahvaz", 2500000),("Kerman", "Kermanshah", 2300000),("Kerman", "Abadan", 2100000),("Kermanshah", "Tehran", 2100000),("Kermanshah", "Esfahan", 2300000),("Kermanshah", "Tabriz", 2500000),("Kermanshah", "Ahvaz", 2400000),("Kermanshah", "Shiraz", 2300000),("Kermanshah", "Kerman", 2300000),("Kermanshah", "Gorgan", 2400000),("Kermanshah", "Bandar Abbas", 2800000),("Kermanshah", "Urmia", 2500000),("Kermanshah", "Dezful", 2200000),("Kermanshah", "Sirjan", 2600000),("Kermanshah", "Ilam", 2400000),("Kermanshah", "Bushehr", 2500000),("Kermanshah", "Chabahar", 2700000),("Kermanshah", "Zahedan", 2600000),("Kermanshah", "Kish", 2800000),("Kermanshah", "Mashhad", 2500000),("Kermanshah", "Abadan", 2300000),("Kermanshah", "Qeshm", 2800000),("Kashan", "Tehran", 1500000),("Kashan", "Kish", 2000000),("Kashan", "Qeshm", 2100000),("Mashhad", "Abadan", 1450000),("Mashhad", "Ardabil", 2700000),("Mashhad", "Urmia", 2500000),("Mashhad", "Esfahan", 2900000),("Mashhad", "Ahvaz", 2800000),("Mashhad", "Ilam", 2500000),("Mashhad", "Bandar Abbas", 2500000),("Mashhad", "Bushehr", 2000000),("Mashhad", "Birjand", 1800000),("Mashhad", "Tabriz", 3000000),("Mashhad", "Tehran", 2500000),("Mashhad", "Chabahar", 2800000),("Mashhad", "Rasht", 2400000),("Mashhad", "Zabol", 2600000),("Mashhad", "Zahedan", 2700000),("Mashhad", "Zanjan", 2500000),("Mashhad", "Sari", 2600000),("Mashhad", "Shiraz", 2400000),("Mashhad", "Qeshm", 2800000),("Mashhad", "Kashan", 1800000),("Mashhad", "Kerman", 2500000),("Mashhad", "Kermanshah", 2500000),("Mashhad", "Kish", 2700000),("Mashhad", "Gorgan", 2600000),("Mashhad", "Nowshahr", 1900000),("Mashhad", "Mahshahr", 2600000),("Mashhad", "Hamedan", 2100000),("Mashhad", "Yazd", 2200000),("Mashhad", "Jahrom", 2600000),("Mashhad", "Khorramabad", 2200000),("Mashhad", "Ramsar", 2300000),("Shiraz", "Tehran", 2600000),("Shiraz", "Tabriz", 3300000),("Shiraz", "Mashhad", 2100000),("Shiraz", "Ahvaz", 2200000),("Shiraz", "Esfahan", 2100000),("Shiraz", "Sari", 2200000),("Shiraz", "Nowshahr", 2500000),("Shiraz", "Abadan", 2100000),("Shiraz", "Bushehr", 2000000),("Shiraz", "Bandar Abbas", 2200000),("Shiraz", "Kerman", 2100000),("Shiraz", "Kermanshah", 2300000),("Shiraz", "Kish", 2400000),("Shiraz", "Chabahar", 2800000),("Shiraz", "Qeshm", 2500000),("Shiraz", "Rasht", 2200000),("Yazd", "Tehran", 2300000),("Yazd", "Mashhad", 2200000),("Yazd", "Ahvaz", 2100000),("Yazd", "Kish", 2300000),("Yazd", "Bandar Abbas", 2200000),("Yazd", "Karaj", 1800000),("Sanandaj", "Tehran", 2100000),("Sanandaj", "Kish", 2500000),("Sari", "Tehran", 770000),("Sari", "Esfahan", 2100000),("Sari", "Mashhad", 2600000),("Sari", "Ahvaz", 2500000),("Sari", "Shiraz", 2500000),("Sari", "Tabriz", 2600000),("Sari", "Bandar Abbas", 3300000),("Sari", "Kish", 2700000),("Hamedan", "Mashhad", 2100000),("Hamedan", "Tehran", 1850000),("Hamedan", "Kish", 2500000),("Gorgan", "Mashhad", 2500000),("Gorgan", "Tehran", 2000000),("Gorgan", "Kish", 2400000),("Gorgan", "Qeshm", 2500000),("Gorgan", "Zabol", 2500000),("Gorgan", "Zahedan", 2600000),("Rasht", "Tehran", 2000000),("Rasht", "Mashhad", 2400000),("Rasht", "Kish", 2600000),("Rasht", "Shiraz", 2400000),("Rasht", "Bandar Abbas", 3500000),("Rasht", "Tabriz", 2500000),("Rasht", "Ahvaz", 2500000),("Rasht", "Esfahan", 2400000),("Zanjan", "Mashhad", 2600000),("Zanjan", "Kish", 2400000),("Urmia", "Tehran", 2500000),("Urmia", "Mashhad", 2600000),("Urmia", "Kish", 2600000),("Qeshm", "Tehran", 3200000),("Qeshm", "Mashhad", 2800000),("Qeshm", "Shiraz", 2500000),("Qeshm", "Esfahan", 2700000),("Qeshm", "Gorgan", 2500000),("Qeshm", "Tabriz", 3000000),("Qeshm", "Kermanshah", 2800000),("Sabzevar", "Tehran", 2500000),("Kish", "Tehran", 3300000),("Kish", "Shiraz", 2400000),("Kish", "Mashhad", 2700000),("Kish", "Esfahan", 2500000),("Kish", "Bandar Abbas", 2200000),("Kish", "Kerman", 2900000),("Kish", "Ahvaz", 2200000),("Kish", "Tabriz", 3200000),("Kish", "Yazd", 2300000),("Kish", "Hamedan", 2600000),("Kish", "Bushehr", 2500000),("Kish", "Rasht", 2600000),("Kish", "Kermanshah", 2800000),("Kish", "Sari", 2700000),("Kish", "Kashan", 2000000),("Kish", "Gorgan", 2500000),("Kish", "Urmia", 2600000),("Kish", "Sanandaj", 2800000),("Kish", "Nowshahr", 2400000),("Ilam", "Tehran", 2300000),("Ilam", "Mashhad", 2500000),("Bushehr", "Tehran", 2500000),("Bushehr", "Esfahan", 2100000),("Bushehr", "Mashhad", 2000000),("Bushehr", "Kish", 2000000),("Bushehr", "Ahvaz", 2300000),("Bushehr", "Shiraz", 2000000),("Bam", "Tehran", 3000000),("Bandar Lengeh", "Shiraz", 2400000),("Bandar Lengeh", "Tehran", 2800000),("Zabol", "Tehran", 2500000),("Zabol", "Mashhad", 2600000),("Karaj", "Kish", 1900000),("Karaj", "Ahvaz", 1800000),("Karaj", "Mashhad", 1700000),("Karaj", "Yazd", 1900000),("Khorramabad", "Tehran", 2000000),("Khorramabad", "Mashhad", 2200000),("Shahr-e Kord", "Tehran", 1900000),("Shahr-e Kord", "Mashhad", 2200000),("Yasuj", "Tehran", 2400000),("Ramsar", "Tehran", 2000000),("Ramsar", "Mashhad", 2300000),("Ramsar", "Esfahan", 2400000)

]

def calculate_costs(noe_safar: str, noe_haml: str, nafarat: int, chan_shab: int, bodje: int, mabda: str) -> List[str]:
    mazhabi = [
        "Abadeh", "Arak", "Ardabil", "Ardakan", "Esfahan", "Ahvaz",
        "Bojnurd", "Birjand", "Tabriz", "Tehran", "Kerman", "Kermanshah",
        "Kashan", "Qazvin", "Mashhad", "Shiraz", "Yazd", "Qom", "Sanandaj",
        "Hamedan", "Zanjan", "Urmia", "Sabzevar", "Nishapur", "Kazerun",
        "Ilam", "Zabol", "Khorramabad", "Shahr-e Kord", "Yasuj",
        "Najafabad", "Zarand", "Maku", "Dezful", "Mahabad",
        "Gonbad Kavus", "Quchan", "Khoy", "Kashmar", "Malayer",
        "Maragheh", "Minab", "Nahavand", "Saveh", "Shushtar",
        "Susa", "Varamin"
    ]
    
    tarikhi = [
        "Esfahan", "Shiraz", "Tehran", "Yazd", "Kerman", "Kashan", "Hamedan", "Tabriz", "Qazvin", "Shush",
        "Kermanshah", "Semnan", "Zanjan", "Ardabil", "Shushtar", "Neyshabur", "Gorgan", "Kashmar", "Sirjan",
        "Bam", "Bandar Anzali", "Shahr-e Kord"
    ]

    tafrehi = [
        "Esfahan", "Shiraz", "Tehran", "Yazd", "Kerman", "Kashan", "Hamedan", "Tabriz", "Qazvin",
        "Kermanshah", "Ardabil", "Gorgan", "Bandar Anzali", "Ramsar", "Kish", "Qeshm", "Mashhad",
        "Rasht", "Abadan", "Ahvaz", "Bushehr", "Bandar Abbas", "Dezful", "Urmia", "Sari"
    ]

    select_1 = []
    select_2 = []
    nahaee = []

    if noe_safar == "Mazhabi":
        cities = mazhabi
    elif noe_safar == "Tarikhi":
        cities = tarikhi
    elif noe_safar == "Tafrehi":
        cities = tafrehi
    else:
        return []

    if noe_haml == "Havapeyma":
        for flight in havapeyma:
            if flight[0] == mabda and flight[1] in cities:
                flight_cost = 2 * (flight[2] * nafarat)
                select_1.append((flight[0], flight[1], flight_cost))

        for flight in select_1:
            for room in hotel:
                if room[0] == flight[1]:
                    hotel_cost = sum(price for price in room[1:] if price > 0)
                    total_cost = (hotel_cost + flight[2]) * chan_shab
                    if nafarat > 2:
                        total_cost += ((nafarat - 2) * 500000) * chan_shab
                    if 0 < total_cost <= bodje:
                        nahaee.append(room[0])

    elif noe_haml in ["Khodro", "Otobos"]:
        transport_cost = 500000 if noe_haml == "Khodro" else 600000 * nafarat
        for room in hotel:
            if room[0] in cities:
                hotel_cost = sum(price for price in room[1:] if price > 0)
                total_cost = (hotel_cost + transport_cost) * chan_shab
                if nafarat > 2:
                    total_cost += ((nafarat - 2) * 500000) * chan_shab
                if 0 < total_cost <= bodje:
                    nahaee.append(room[0])

    return nahaee

def filter_cities(cities: List[str], fasl: str, ab_hava: str, khared: str, tabeyat: str) -> List[str]:
    seasons = {
        "bahar": {
            "sard": ["Ardabil", "Tabriz", "Hamedan", "Zanjan", "Urmia", "Shahr-e Kord"],
            "garm": ["Abadan", "Ahvaz", "Bandar Abbas", "Kashan", "Yazd", "Qom", "Qeshm", "Kish", "Bushehr", "Bam", "Dezful", "Shushtar"],
            "sharge": ["Abadan", "Ahvaz", "Bandar Abbas", "Bandar Anzali", "Sari", "Gorgan", "Rasht", "Qeshm", "Kish", "Bushehr", "Ramsar", "Lahijan"],
            "motadel": ["Arak", "Esfahan", "Bandar Anzali", "Tehran", "Kerman", "Kermanshah", "Qazvin", "Mashhad", "Shiraz", "Sari", "Gorgan", "Rasht", "Nishapur", "Ramsar", "Kashmar", "Lahijan"]
        },
        "tabastan": {
            "sard": ["Ardabil", "Hamedan"],
            "garm": ["Abadan", "Arak", "Esfahan", "Ahvaz", "Bandar Abbas", "Bandar Anzali", "Tehran", "Kerman", "Kermanshah", "Kashan", "Qazvin", "Mashhad", "Shiraz", "Yazd", "Qom", "Sari", "Gorgan", "Rasht", "Qeshm", "Nishapur", "Kish", "Bushehr", "Bam", "Ramsar", "Dezful", "Kashmar", "Lahijan", "Shushtar"],
            "sharge": ["Abadan", "Ahvaz", "Bandar Abbas", "Bandar Anzali", "Gorgan", "Rasht", "Qeshm", "Kish", "Bushehr", "Ramsar", "Lahijan"],
            "motadel": ["Tabriz", "Zanjan", "Urmia", "Shahr-e Kord"]
        },
        "paiez": {
            "sard": ["Arak", "Ardabil", "Esfahan", "Tabriz", "Tehran", "Kerman", "Kermanshah", "Kashan", "Qazvin", "Mashhad", "Shiraz", "Yazd", "Qom", "Hamedan", "Zanjan", "Urmia", "Nishapur", "Bam", "Shahr-e Kord", "Kashmar"],
            "garm": ["Abadan", "Ahvaz", "Bandar Abbas", "Qeshm", "Kish", "Bushehr", "Dezful", "Shushtar"],
            "sharge": ["Abadan", "Ahvaz", "Bandar Abbas", "Sari", "Gorgan", "Rasht", "Qeshm", "Kish", "Bushehr", "Ramsar", "Lahijan"],
            "motadel": ["Bandar Anzali", "Sari", "Gorgan", "Rasht", "Ramsar", "Lahijan"]
        },
        "zemestan": {
            "sard": ["Arak", "Ardabil", "Esfahan", "Tabriz", "Tehran", "Kerman", "Kermanshah", "Kashan", "Qazvin", "Mashhad", "Shiraz", "Yazd", "Qom", "Sari", "Hamedan", "Gorgan", "Rasht", "Zanjan", "Urmia", "Nishapur", "Bam", "Shahr-e Kord", "Ramsar", "Kashmar", "Lahijan"],
            "garm": [],
            "sharge": ["Abadan", "Ahvaz", "Bandar Abbas", "Bandar Anzali", "Sari", "Gorgan", "Rasht", "Qeshm", "Kish", "Bushehr", "Ramsar", "Lahijan"],
            "motadel": ["Abadan", "Ahvaz", "Bandar Abbas", "Qeshm", "Kish", "Bushehr", "Dezful", "Shushtar"]
        }
    }

    filtered_cities = [city for city in cities if city in seasons[fasl][ab_hava]]

    if khared == "bale":
        shopping_cities = ["Esfahan", "Tehran", "Shiraz", "Mashhad", "Tabriz", "Kish", "Qeshm", "Bandar Abbas", "Ahvaz", "Rasht", "Bandar Anzali", "Ardabil", "Yazd", "Kerman", "Sari", "Bushehr", "Abadan"]
        filtered_cities = [city for city in filtered_cities if city in shopping_cities]

    if tabeyat == "bale":
        nature_cities = ["Ardabil", "Tabriz", "Tehran", "Kerman", "Kermanshah", "Sari", "Hamedan", "Gorgan", "Rasht", "Zanjan", "Urmia", "Qeshm", "Kish", "Bandar Abbas", "Bandar Anzali", "Ramsar", "Shahr-e Kord", "Lahijan", "Mashhad", "Shiraz", "Esfahan", "Ahvaz", "Kashan", "Bushehr", "Nishapur", "Bam", "Yazd", "Abadan", "Arak", "Dezful"]
        filtered_cities = [city for city in filtered_cities if city in nature_cities]

    return filtered_cities

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result')
def result():
    noe_safar = request.args.get('trip-type')
    noe_haml = request.args.get('transport')
    nafarat = int(request.args.get('passengers'))
    chan_shab = int(request.args.get('nights'))
    bodje = int(request.args.get('budget'))
    mabda = request.args.get('origin')
    fasl = request.args.get('fasl')
    ab_hava = request.args.get('ab_hava')
    khared = request.args.get('khared')
    tabeyat = request.args.get('tabeyat')

    recommended_cities = calculate_costs(noe_safar, noe_haml, nafarat, chan_shab, bodje, mabda)
    filtered_cities = filter_cities(recommended_cities, fasl, ab_hava, khared, tabeyat)
    return render_template('result.html', cities=filtered_cities)

if __name__ == '__main__':
    app.run(debug=True)