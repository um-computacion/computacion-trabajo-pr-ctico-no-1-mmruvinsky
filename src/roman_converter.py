
def decimal_to_roman(decimal):
    valores = [
        (1000, "M"),
        (900, "CM"),
        (500, "D"),
        (400, "CD"),
        (100, "C"),
        (90, "XC"),
        (50, "L"),
        (40, "XL"),
        (10, "X"),
        (9, "IX"),
        (5, "V"),
        (4, "IV"),
        (1, "I")
    ]
    
    if not 1 <= decimal <= 3999:
        return "Número fuera del rango (1-3999)"
    
    result = ""
    for valor, simbolo in valores:
        while decimal >= valor:
            result += simbolo
            decimal -= valor
    
    return result