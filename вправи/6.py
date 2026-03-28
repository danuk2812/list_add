hardware = ("Monitor", "CPU", "Keyboard", "Mouse")

software = ["Windows", "Python", "Browser", "Linux"]

print("Hardware:")
for item in hardware:
    print(f"- {item}")

print("\nSoftware:")
for item in software:
    print(f"- {item}")
software[1] = "Photoshop"
print(f"\nОновлений список Software: {software}")

try:
    hardware[1] = "GPU"
except TypeError as e:
    print(f"\nПомилка при зміні кортежу: {e}")