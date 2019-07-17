#Calculating the onbase plus slugging percentage of two Braves hitters

onBasePlusSlugging = {'Ronald Acuna Jr': [.373, .509], 'Freddie Freeman': [.388, .582]}

oBPS = {k: sum(v) for k, v in onBasePlusSlugging.items()}

print(oBPS)
