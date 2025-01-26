def nombres_ciudad(city,country):
    info=f"{city}, {country}"
    return info.title()

cl=nombres_ciudad("santiago","chile")
arg=nombres_ciudad("buenos aires","argentina")
cr=nombres_ciudad("san josé", "costa rica")

print(cl)
print(arg)
print(cr)