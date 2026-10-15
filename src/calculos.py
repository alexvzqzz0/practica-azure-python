def sumar(a, b):
    return a + b


def media(numeros):
    if not numeros:
        raise ValueError("La lista no puede estar vacía")
    return sum(numeros) / len(numeros)


def contar_prioridades(incidencias):
    resultado = {}
    for incidencia in incidencias:
        prioridad = incidencia["prioridad"]
        resultado[prioridad] = resultado.get(prioridad, 0) + 1
    return resultado


def es_urgente(prioridad):
    return prioridad == 1
