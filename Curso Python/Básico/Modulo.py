from Clases import Clases

persona = Clases.Persona("Jano", "Juarez", 18)

persona.estudiar("Python")

persona.país = "Argentina"

Clases.print_persona_info(persona)
# Excepciones
try :
    print(persona.arriba)
except Exception as e:
    print("Ha habido un error:", e)
finally:
    print("La ejecución continua")