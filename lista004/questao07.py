a = {"x": 1, "y": 2}
b = {"y": 20, "z": 3}

z = a.copy() 
z.update(b) 

print("Método 1 (update):", z)