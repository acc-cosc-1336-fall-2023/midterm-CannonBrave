from question_a import get_fahrenheit

print('C\tF')

for celsius in range(0,21):
    fahrenheit = get_fahrenheit(celsius)
    print(f"{celsius}\t{fahrenheit}")