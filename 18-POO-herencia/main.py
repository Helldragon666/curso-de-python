
import clases

persona = clases.Persona()
persona.setNombre('Yon')
persona.setApellido('Cervantes')
persona.setAltura('163cm')
persona.setEdad('20 años')

print(f'La persona es: {persona.getNombre()} {persona.getApellido()}')
print(persona.hablar())



informatico = clases.Informatico()

informatico.setNombre('Yonatan')
informatico.setApellido('Cervantes')

print(f'El informático es: {informatico.getNombre()} {informatico.getApellido()}')
print(informatico.getLenguajes())
print(informatico.caminar())
print(informatico.experiencia)


tecnico = clases.TecnicoRedes()
print(tecnico.auditarRedes, tecnico.getLenguajes())
