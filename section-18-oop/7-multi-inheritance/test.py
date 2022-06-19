from digital_clock import DigitalClock

complete_clock = DigitalClock(8, 30, 54, 7, 4, 2021)

print(f"Hora: {complete_clock.get_hour()}")
print(f"Fecha: {complete_clock.get_data()}")
print(f"Hora / Fecha: {complete_clock}")

print(DigitalClock.__mro__)