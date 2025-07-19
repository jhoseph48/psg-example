habitats_peligro = {"polo norte": {"especies": {"oso polar", "morsa", "ballena"}},
                    "amazonas": {"especies": {"tigre", "mono", "guacamayo"}}}
print(habitats_peligro)

habitats_peligro.update({"barrera de coral": {"especies": {"tortuga marina", "pez payaso"}},
                         "madagascar": {"especies": {"lemur", "fosa"}}})
print(habitats_peligro)

existe_amazonas = 'amazonas' in habitats_peligro
print("¿Existe el hábitat 'amazonas'?", existe_amazonas)

habitats_peligro['amazonas']['especies'].add('anaconda')
print(habitats_peligro)