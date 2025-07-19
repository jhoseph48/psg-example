jhon_autos = {'Ferrari', 'Lamborghini', 'Porsche', 'Bugatti', 'McLaren'}
jess_autos = {'Ferrari', 'Lamborghini', 'Tesla', 'Ford', 'Chevrolet'}

autos_comun = jhon_autos.intersection(jess_autos)


if autos_comun:
    print("Jhon y Jess tienen autos en común")
    print(autos_comun)
else:
    print("No, Jhon y Jess no tienen autos en común en sus colecciones.")