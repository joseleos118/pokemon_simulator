class Pokemon:
    _contador_pokemons = 0

    def __init__(self, nombre, ataque, defensa, salud):
        if not self.validar_estadistica(ataque):
            raise ValueError("El ataque debe ser un número positivo.")

        if not self.validar_estadistica(defensa):
            raise ValueError("La defensa debe ser un número positivo.")

        if not self.validar_estadistica(salud):
            raise ValueError("La salud debe ser un número positivo.")

        self.nombre = nombre
        self.nivel = 1
        self.ataque = ataque
        self.defensa = defensa
        self.salud = salud
        self.salud_maxima = salud

        self._tipo = "Desconocido"

        Pokemon._contador_pokemons += 1

        print(f"¡{self.nombre} ha sido capturado!")

    def __del__(self):
        """
        Destructor.
        Disminuye el contador cuando el objeto es eliminado.
        """
        try:
            Pokemon._contador_pokemons -= 1
            print(f"{self.nombre} ha sido liberado.")
        except AttributeError:
            pass

    def entrenar(self, stat1=None, stat2=None, stat3=None):
        """
        Entrena al Pokémon y aumenta su nivel.

        Si no se proporcionan estadísticas:
        - Ataque aumenta 5
        - Defensa aumenta 5
        - Salud máxima aumenta 10
        - Salud actual aumenta 10

        También permite proporcionar incrementos
        personalizados mediante stat1, stat2 y stat3.
        """

        self.subir_nivel()

        if stat1 is None and stat2 is None and stat3 is None:
            print(f"\n{self.nombre} está entrenando...")

            self.ataque += 5
            self.defensa += 5
            self.salud_maxima += 10
            self.salud += 10

            print(f"¡{self.nombre} subió al nivel {self.nivel}!")
            print("Ataque +5")
            print("Defensa +5")
            print("Salud +10")

        else:
            if stat1 is not None:
                if not self.validar_estadistica(stat1):
                    raise ValueError(
                        "El incremento de ataque debe ser positivo."
                    )
                self.ataque += stat1

            if stat2 is not None:
                if not self.validar_estadistica(stat2):
                    raise ValueError(
                        "El incremento de defensa debe ser positivo."
                    )
                self.defensa += stat2

            if stat3 is not None:
                if not self.validar_estadistica(stat3):
                    raise ValueError(
                        "El incremento de salud debe ser positivo."
                    )

                self.salud_maxima += stat3
                self.salud += stat3

            print(f"\n¡{self.nombre} subió al nivel {self.nivel}!")

    def atacar(self, objetivo):
        """
        Ataque básico.
        El daño se calcula como:
        ataque - defensa del objetivo.

        El daño mínimo siempre será 1.
        """

        if objetivo.salud <= 0:
            print(
                f"{objetivo.nombre} está debilitado "
                "y no puede recibir ataques."
            )
            return

        daño = max(1, self.ataque - objetivo.defensa)

        print(
            f"\n{self.nombre} ataca a {objetivo.nombre} "
            f"y causa {daño} puntos de daño."
        )

        objetivo.recibir_dano(daño)

    def recibir_dano(self, cantidad):
        """
        Reduce la salud del Pokémon.
        Si llega a 0, el Pokémon queda debilitado.
        """

        if cantidad <= 0:
            return

        self.salud -= cantidad

        if self.salud < 0:
            self.salud = 0

        print(
            f"{self.nombre} recibió {cantidad} puntos de daño. "
            f"Salud: {self.salud}/{self.salud_maxima}"
        )

        if self.salud == 0:
            print(f"¡{self.nombre} se ha debilitado!")

    def mostrar_info(self):
        """
        Muestra toda la información del Pokémon.
        """

        print("\n" + "-" * 40)
        print("INFORMACIÓN DEL POKÉMON")
        print("-" * 40)
        print(f"Nombre: {self.nombre}")
        print(f"Tipo: {self._tipo}")
        print(f"Nivel: {self.nivel}")
        print(f"Ataque: {self.ataque}")
        print(f"Defensa: {self.defensa}")
        print(f"Salud: {self.salud}/{self.salud_maxima}")
        print("-" * 40)

    def subir_nivel(self):
        """
        Aumenta el nivel y mejora las estadísticas base.
        """

        self.nivel += 1
        self.ataque += 2
        self.defensa += 2
        self.salud_maxima += 5
        self.salud += 5

    @classmethod
    def total_pokemons(cls):
        """
        Devuelve el número total de Pokémon activos.
        """

        return cls._contador_pokemons

    @staticmethod
    def validar_estadistica(valor):
        """
        Verifica que una estadística sea un número positivo.
        """

        return isinstance(valor, (int, float)) and valor > 0


# POKÉMON DE FUEGO

class PokemonFuego(Pokemon):

    def __init__(self, nombre, ataque, defensa, salud):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Fuego"

    def atacar(self, objetivo):
        """
        Fuego:
        - Fuerte contra Planta: daño x2
        - Débil contra Agua: daño /2
        """

        if objetivo.salud <= 0:
            print(
                f"{objetivo.nombre} está debilitado "
                "y no puede recibir ataques."
            )
            return

        daño_base = max(1, self.ataque - objetivo.defensa)

        if objetivo._tipo == "Planta":
            daño = daño_base * 2
            print("Es muy efectivo contra Planta.")

        elif objetivo._tipo == "Agua":
            daño = max(1, daño_base // 2)
            print("No es muy efectivo contra Agua.")

        else:
            daño = daño_base

        print(
            f"\n{self.nombre} ataca a {objetivo.nombre} "
            f"y causa {daño} puntos de daño."
        )

        objetivo.recibir_dano(daño)

    def mostrar_info(self):
        super().mostrar_info()
        print("Arde con pasión.")


# POKÉMON DE AGUA

class PokemonAgua(Pokemon):

    def __init__(self, nombre, ataque, defensa, salud):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Agua"

    def atacar(self, objetivo):
        """
        Agua:
        - Fuerte contra Fuego: daño x2
        - Débil contra Planta: daño /2
        """

        if objetivo.salud <= 0:
            print(
                f"{objetivo.nombre} está debilitado "
                "y no puede recibir ataques."
            )
            return

        daño_base = max(1, self.ataque - objetivo.defensa)

        if objetivo._tipo == "Fuego":
            daño = daño_base * 2
            print("Es muy efectivo contra Fuego.")

        elif objetivo._tipo == "Planta":
            daño = max(1, daño_base // 2)
            print("No es muy efectivo contra Planta.")

        else:
            daño = daño_base

        print(
            f"\n{self.nombre} ataca a {objetivo.nombre} "
            f"y causa {daño} puntos de daño."
        )

        objetivo.recibir_dano(daño)

    def mostrar_info(self):
        super().mostrar_info()
        print("Fluye como el río.")


# POKÉMON DE PLANTA

class PokemonPlanta(Pokemon):

    def __init__(self, nombre, ataque, defensa, salud):
        super().__init__(nombre, ataque, defensa, salud)
        self._tipo = "Planta"

    def atacar(self, objetivo):
        """
        Planta:
        - Fuerte contra Agua: daño x2
        - Débil contra Fuego: daño /2
        """

        if objetivo.salud <= 0:
            print(
                f"{objetivo.nombre} está debilitado "
                "y no puede recibir ataques."
            )
            return

        daño_base = max(1, self.ataque - objetivo.defensa)

        if objetivo._tipo == "Agua":
            daño = daño_base * 2
            print("Es muy efectivo contra Agua.")

        elif objetivo._tipo == "Fuego":
            daño = max(1, daño_base // 2)
            print("No es muy efectivo contra Fuego.")

        else:
            daño = daño_base

        print(
            f"\n{self.nombre} ataca a {objetivo.nombre} "
            f"y causa {daño} puntos de daño."
        )

        objetivo.recibir_dano(daño)

    def mostrar_info(self):
        super().mostrar_info()
        print("Crece con fuerza.")