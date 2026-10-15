from src.calculos import sumar, media, contar_prioridades, es_urgente


def main():
    prioridades = [1, 2, 1, 3, 2]
    incidencias = [
        {"id": 1, "prioridad": 1},
        {"id": 2, "prioridad": 2},
        {"id": 3, "prioridad": 1},
        {"id": 4, "prioridad": 3},
    ]

    print("Suma:", sumar(4, 6))
    print("Media:", media(prioridades))
    print("Incidencias por prioridad:", contar_prioridades(incidencias))
    print("Urgentes:", [i["id"] for i in incidencias if es_urgente(i["prioridad"])])


if __name__ == "__main__":
    main()
