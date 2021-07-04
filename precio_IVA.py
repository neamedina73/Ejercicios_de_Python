"""Programa que agraga el IVA al precio de un producto
Programa Elaborado por Nelson Acuña Medina"""
IVA = 0.19
precio_Base = 8000
precio_Final = precio_Base + (precio_Base*IVA)
print(f"El precio final es de : ${precio_Final}")