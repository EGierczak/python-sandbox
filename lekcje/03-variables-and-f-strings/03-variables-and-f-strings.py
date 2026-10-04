name = input("What is your name? ") # standardowy input
age = int(input("How old are you? ")) # input zawsze jest stringiem, trzeba przekonwertować na int
current_year = 2026 # zmienna, przypisanie wartości, nie trzeba deklarować rodzaju zmiennej
birth_year = current_year - age
print(f"Hello, {name}! Next year you will be {age + 1}, and you were born around {birth_year}.") #print(f"Hello, {name}") pozwala na Łatwiejszą obsługę print ze zmiennymi. Zmienne Możemy Podać w {} zamiast rozdzielać wszystko "+"

# BŁĘDY (moje z dzisiaj)
# SyntaxError - nic się nie wykonało, błąd składni
# NameError   - nazwa zmiennej nie istnieje
# TypeError   - 5 + "5" działanie zawiera po dwóch stronach różne typy
# ValueError  - int("five") wpisana wartość nie jest intem i python nie potrafi jej odczytać i zamienić na int