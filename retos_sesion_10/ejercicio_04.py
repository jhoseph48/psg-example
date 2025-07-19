jane_postres = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
jhon_postres = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}

postres_en_comun = jane_postres.intersection(jhon_postres)

cantidad_comun = len(postres_en_comun)

total_postres_jane = len(jane_postres)

porcentaje_comun = (cantidad_comun / total_postres_jane) * 100
print(porcentaje_comun)

compatibilidad = porcentaje_comun > 50
print("son compatibles:" , compatibilidad)