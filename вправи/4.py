def things(list_things):
    rain = list_things[-1]
    print(rain.title())
    print(list_things)
    list_things[-1]=rain.upper()
    print(list_things)
    print(list_things[:-1])
things(['wallet', 'mirror', 'umbrella'])