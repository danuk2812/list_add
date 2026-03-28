
professions = ['Doctor', 'Engineer', 'Artist', 'Teacher', 'Pilot']
print(f"Оригінальний список: {professions}")

sorted_professions = sorted(professions)
print(f"\nРезультат sorted(): {sorted_professions}")
print(f"Оригінальний список після sorted() (не змінився): {professions}")

# Цей метод змінює ОРИГІНАЛЬНИЙ список, розгортаючи його задом наперед (не за алфавітом).
professions.reverse()
print(f"\nОригінальний список після .reverse(): {professions}")

professions.sort()
print(f"\nОригінальний список після .sort(): {professions}")

professions.sort(reverse=True)
print(f"Після .sort(reverse=True): {professions}")