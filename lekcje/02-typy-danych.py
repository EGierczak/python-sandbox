# Lekcja 02 — Typy danych (12.09.2026)

# CZTERY PODSTAWOWE TYPY
# int   - liczba całkowita
# float - liczba z kropką
# str   - string/text
# bool  - True/False - pisze się z dużej litery!

print(type(5))
print(type("5"))
print(type(3.14))
print(type(True))

# PLUS DZIAŁA RÓŻNIE ZALEŻNIE OD TYPU
print(5 + 5)
print("5" + "5")

# KONWERSJE — to ja decyduję, w którą stronę
print(5 + int("5"))
print(str(5) + "5")

# BŁĘDY (odkomentuj, żeby zobaczyć)
# 5 + "5"        -> TypeError: różne typy po dwóch stronach działania
# int("pięć")    -> ValueError: w środku nie ma czegoś co da się zamienić na liczbę wg pythona

# FLOAT BYWA NIEŚCISŁY
print(0.1 + 0.2)
print(0.1 + 0.2 == 0.3)
# dlaczego: bo suma wartości leżących najbliżej 0.1 i 0.2 nie jest taka sama jak wartość leżącą najbliżej 0.3