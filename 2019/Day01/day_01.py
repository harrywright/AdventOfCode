def fuel_from_mass(mass: int) -> int:
    fuel = (mass // 3) - 2
    if fuel < 0:
        return 0
    fuel += fuel_from_mass(fuel)
    return fuel


total_fuel = 0

with open("input.txt") as f:
    for line in f:
        total_fuel += fuel_from_mass(int(line))

print(f'Total fuel required: {total_fuel}')
