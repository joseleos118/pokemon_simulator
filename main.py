from clases.pokemon import (
    Pokemon,
    PokemonFuego,
    PokemonAgua,
    PokemonPlanta
)


# VARIABLES DEL PROGRAMA

equipo = []


# FUNCIONES AUXILIARES

def mostrar_menu():
    """
    Muestra el menú principal del programa.
    """

    print("\n")
    print("-" * 50)
    print("        SIMULADOR DE ENTRENAMIENTO POKÉMON")
    print("-" * 50)
    print("1. Capturar Pokémon")
    print("2. Entrenar Pokémon")
    print("3. Atacar")
    print("4. Ver información")
    print("5. Total de Pokémon")
    print("6. Liberar Pokémon")
    print("7. Salir")
    print("-" * 50)


def seleccionar_pokemon(mensaje):
    """
    Permite seleccionar un Pokémon del equipo
    mediante su número.
    """

    if len(equipo) == 0:
        print("\nNo hay Pokémon en el equipo.")
        return None

    print("\n" + "-" * 40)
    print("POKÉMON DISPONIBLES")
    print("-" * 40)

    for i, pokemon in enumerate(equipo, start=1):
        estado = "DEBILITADO" if pokemon.salud <= 0 else "Activo"

        print(
            f"{i}. {pokemon.nombre} "
            f"({pokemon._tipo}) - "
            f"Nivel {pokemon.nivel} - "
            f"Salud {pokemon.salud}/{pokemon.salud_maxima} "
            f"- {estado}"
        )

    print("-" * 40)

    while True:
        try:
            opcion = int(input(mensaje))

            if opcion < 1 or opcion > len(equipo):
                print("Selecciona un número válido.")
                continue

            return equipo[opcion - 1]

        except ValueError:
            print("Debes introducir un número.")


# OPCIÓN 1: CAPTURAR

def capturar_pokemon():
    """
    Captura un nuevo Pokémon y lo agrega al equipo.
    """

    print("\n" + "-" * 50)
    print("             CAPTURAR POKÉMON")
    print("-" * 50)

    try:
        nombre = input("Nombre del Pokémon: ").strip()

        if not nombre:
            print("El nombre no puede estar vacío.")
            return

        print("\nTipos disponibles:")
        print("1. Fuego")
        print("2. Agua")
        print("3. Planta")

        tipo = input("Selecciona el tipo: ").strip().lower()

        tipos = {
            "1": "Fuego",
            "2": "Agua",
            "3": "Planta",
            "fuego": "Fuego",
            "agua": "Agua",
            "planta": "Planta"
        }

        if tipo not in tipos:
            print("Tipo de Pokémon no válido.")
            print("Debes elegir Fuego, Agua o Planta.")
            return

        tipo = tipos[tipo]

        ataque = float(input("Ataque: "))
        defensa = float(input("Defensa: "))
        salud = float(input("Salud: "))

        if ataque.is_integer():
            ataque = int(ataque)

        if defensa.is_integer():
            defensa = int(defensa)

        if salud.is_integer():
            salud = int(salud)

        # Validar estadísticas

        if not Pokemon.validar_estadistica(ataque):
            print("El ataque debe ser positivo.")
            return

        if not Pokemon.validar_estadistica(defensa):
            print("La defensa debe ser positiva.")
            return

        if not Pokemon.validar_estadistica(salud):
            print("La salud debe ser positiva.")
            return

        # Crear el Pokémon correspondiente

        if tipo == "Fuego":
            nuevo_pokemon = PokemonFuego(
                nombre,
                ataque,
                defensa,
                salud
            )

        elif tipo == "Agua":
            nuevo_pokemon = PokemonAgua(
                nombre,
                ataque,
                defensa,
                salud
            )

        else:
            nuevo_pokemon = PokemonPlanta(
                nombre,
                ataque,
                defensa,
                salud
            )

        equipo.append(nuevo_pokemon)

        print(f"{nombre} fue agregado a tu equipo.")

    except ValueError:
        print("Error: introduce valores numéricos válidos.")


# OPCIÓN 2: ENTRENAR

def entrenar_pokemon():
    """
    Permite seleccionar y entrenar un Pokémon.
    """

    print("\n" + "-" * 50)
    print("             ENTRENAR POKÉMON")
    print("-" * 50)

    pokemon = seleccionar_pokemon(
        "Selecciona el número del Pokémon que deseas entrenar: "
    )

    if pokemon is None:
        return

    if pokemon.salud <= 0:
        print(
            f"{pokemon.nombre} está debilitado "
            "y no puede entrenar."
        )
        return

    try:
        pokemon.entrenar()

        print("\nEntrenamiento completado.")
        print(f"Nivel actual: {pokemon.nivel}")

    except ValueError as error:
        print(f"Error durante el entrenamiento: {error}")


# OPCIÓN 3: ATACAR

def atacar_pokemon():
    """
    Permite seleccionar un atacante y un objetivo.
    """

    print("\n" + "-" * 50)
    print("                ATAQUE")
    print("-" * 50)

    if len(equipo) < 2:
        print("Necesitas al menos 2 Pokémon para atacar.")
        return

    atacante = seleccionar_pokemon(
        "Selecciona el número del Pokémon atacante: "
    )

    if atacante is None:
        return

    if atacante.salud <= 0:
        print(
            f"{atacante.nombre} está debilitado "
            "y no puede atacar."
        )
        return

    objetivo = seleccionar_pokemon(
        "Selecciona el número del Pokémon objetivo: "
    )

    if objetivo is None:
        return

    if atacante is objetivo:
        print("Un Pokémon no puede atacarse a sí mismo.")
        return

    if objetivo.salud <= 0:
        print(
            f"{objetivo.nombre} ya está debilitado "
            "y no puede recibir otro ataque."
        )
        return

    print(
        f"\n{atacante.nombre} ({atacante._tipo}) "
        f"vs {objetivo.nombre} ({objetivo._tipo})"
    )

    atacante.atacar(objetivo)


# OPCIÓN 4: INFORMACIÓN

def mostrar_informacion():
    """
    Muestra la información de todos los Pokémon.
    """

    print("\n" + "-" * 50)
    print("             INFORMACIÓN DEL EQUIPO")
    print("-" * 50)

    if len(equipo) == 0:
        print("No tienes Pokémon capturados.")
        return

    for pokemon in equipo:
        pokemon.mostrar_info()


# OPCIÓN 5: TOTAL

def mostrar_total():
    """
    Muestra el total de Pokémon activos.
    """

    print("\n" + "-" * 50)
    print("             TOTAL DE POKÉMON")
    print("-" * 50)

    total = Pokemon.total_pokemons()

    print(f"Pokémon activos: {total}")


# OPCIÓN 6: LIBERAR

def liberar_pokemon():
    """
    Permite eliminar un Pokémon del equipo.
    """

    print("\n" + "-" * 50)
    print("             LIBERAR POKÉMON")
    print("-" * 50)

    pokemon = seleccionar_pokemon(
        "Selecciona el número del Pokémon que deseas liberar: "
    )

    if pokemon is None:
        return

    print(
        f"\n¿Estás seguro de que deseas liberar a "
        f"{pokemon.nombre}?"
    )

    confirmacion = input(
        "Escribe 'si' para confirmar: "
    ).strip().lower()

    if confirmacion == "si":
        posicion = equipo.index(pokemon)

        pokemon_liberado = equipo.pop(posicion)

        del pokemon_liberado

        print("Pokémon liberado correctamente.")

    else:
        print("Operación cancelada.")


# PROGRAMA PRINCIPAL

def main():
    """
    Función principal del programa.
    """

    print("\n")
    print("-" * 50)
    print("BIENVENIDO AL SIMULADOR DE ENTRENAMIENTO POKÉMON")
    print("-" * 50)

    while True:

        mostrar_menu()

        try:
            opcion = input(
                "Selecciona una opción: "
            ).strip()

            if opcion == "1":
                capturar_pokemon()

            elif opcion == "2":
                entrenar_pokemon()

            elif opcion == "3":
                atacar_pokemon()

            elif opcion == "4":
                mostrar_informacion()

            elif opcion == "5":
                mostrar_total()

            elif opcion == "6":
                liberar_pokemon()

            elif opcion == "7":
                print("\nGracias por usar el Simulador Pokémon.")
                print("Hasta pronto.")
                break

            else:
                print("Opción no válida.")
                print("Selecciona una opción del 1 al 7.")

        except Exception as error:
            print(f"\nOcurrió un error: {error}")


# INICIO DEL PROGRAMA

if __name__ == "__main__":
    main()