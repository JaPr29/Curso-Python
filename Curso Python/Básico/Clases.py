class Persona:
    def __init__(self, nombre: str, apellido: str, edad: int, país: str = "Desconocido"):
        self.nombre_completo = nombre + " " + apellido
        self.edad = edad
        self.país = país
        self.nombre = nombre
        self.apellido = apellido
    

    def estudiar(self, asignatura: str):
        print(f"{self.nombre} esta estudiando {asignatura}")

def print_persona_info(persona: Persona):
    if persona.país == "Desconocido":
        print(f"{persona.nombre_completo} tiene {persona.edad} años")
        return
    print(f"{persona.nombre_completo} tiene {persona.edad} años y es de {persona.país}")

