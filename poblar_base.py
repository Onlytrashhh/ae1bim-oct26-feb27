"""Script para poblar la base de datos con datos de ejemplo."""

from datetime import date

from sqlalchemy.orm import sessionmaker

from crear_base_entidades import (
    Base,
    Clinica,
    Consultorio,
    HistoriaClinica,
    Veterinario,
    engine,
)


def poblar():
    """Inserta clínicas, consultorios, veterinarios e historias clínicas."""
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        if session.query(Clinica).count() > 0:
            print("La base de datos ya contiene registros. No se insertaron duplicados.")
            return

        # 1. Clínicas
        clinica_norte = Clinica(
            nombre_comercial="VetVida Norte",
            direccion="Av. Amazonas N45-120, Quito",
            veterinario_responsable="Dr. Carlos Mendoza",
        )
        clinica_sur = Clinica(
            nombre_comercial="Huellas Saludables",
            direccion="Av. 9 de Octubre 812, Guayaquil",
            veterinario_responsable="Dra. Valeria Paredes",
        )
        clinica_andes = Clinica(
            nombre_comercial="Clínica Veterinaria Los Andes",
            direccion="Calle Bolívar 14-35, Cuenca",
            veterinario_responsable="Dr. Andrés Villavicencio",
        )

        # 2. Consultorios (asociados obligatoriamente a una sola clínica)
        cons_101 = Consultorio(
            nombre_numero="Consultorio 101",
            especialidad="Medicina General",
            clinica=clinica_norte,
        )
        cons_102 = Consultorio(
            nombre_numero="Consultorio 102",
            especialidad="Cirugía",
            clinica=clinica_norte,
        )
        cons_201 = Consultorio(
            nombre_numero="Consultorio 201",
            especialidad="Dermatología",
            clinica=clinica_sur,
        )
        cons_202 = Consultorio(
            nombre_numero="Consultorio 202",
            especialidad="Cirugía",
            clinica=clinica_sur,
        )
        cons_301 = Consultorio(
            nombre_numero="Consultorio A1",
            especialidad="Medicina General",
            clinica=clinica_andes,
        )
        cons_302 = Consultorio(
            nombre_numero="Consultorio A2",
            especialidad="Dermatología",
            clinica=clinica_andes,
        )

        # 3. Veterinarios (cada uno con nombre y apellido, en un único consultorio)
        vet_1 = Veterinario(
            nombres="Carlos",
            apellidos="Mendoza",
            correo="carlos.mendoza@vetvida.ec",
            numero_licencia="VET-EC-1001",
            consultorio=cons_101,
        )
        vet_2 = Veterinario(
            nombres="Sofía",
            apellidos="Benítez",
            correo="sofia.benitez@vetvida.ec",
            numero_licencia="VET-EC-1002",
            consultorio=cons_102,
        )
        vet_3 = Veterinario(
            nombres="Diego",
            apellidos="Salazar",
            correo="diego.salazar@vetvida.ec",
            numero_licencia="VET-EC-1003",
            consultorio=cons_102,
        )
        vet_4 = Veterinario(
            nombres="Valeria",
            apellidos="Paredes",
            correo="valeria.paredes@huellas.ec",
            numero_licencia="VET-EC-2001",
            consultorio=cons_201,
        )
        vet_5 = Veterinario(
            nombres="Mateo",
            apellidos="Ortega",
            correo="mateo.ortega@huellas.ec",
            numero_licencia="VET-EC-2002",
            consultorio=cons_202,
        )
        vet_6 = Veterinario(
            nombres="Andrés",
            apellidos="Villavicencio",
            correo="andres.villavicencio@losandesvet.ec",
            numero_licencia="VET-EC-3001",
            consultorio=cons_301,
        )
        vet_7 = Veterinario(
            nombres="Camila",
            apellidos="Cordero",
            correo="camila.cordero@losandesvet.ec",
            numero_licencia="VET-EC-3002",
            consultorio=cons_302,
        )

        # 4. Historias Clínicas (enfermedades y tratamientos comunes)
        historias = [
            # VetVida Norte -> 4 historias clínicas
            HistoriaClinica(
                fecha_atencion=date(2026, 10, 5),
                diagnostico="Infección estomacal",
                tratamiento="Suero oral, dieta blanda y amoxicilina por 5 días",
                nombre_mascota="Max",
                veterinario=vet_1,
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 10, 12),
                diagnostico="Vacunación anual",
                tratamiento="Vacuna antirrábica y vacuna múltiple",
                nombre_mascota="Luna",
                veterinario=vet_1,
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 10, 18),
                diagnostico="Fractura en pata delantera",
                tratamiento="Inmovilización con yeso y meloxicam para el dolor",
                nombre_mascota="Rocky",
                veterinario=vet_2,
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 2),
                diagnostico="Esterilización",
                tratamiento="Cirugía de rutina, amoxicilina y reposo por 7 días",
                nombre_mascota="Mía",
                veterinario=vet_3,
            ),
            # Huellas Saludables -> 3 historias clínicas
            HistoriaClinica(
                fecha_atencion=date(2026, 10, 20),
                diagnostico="Dermatitis por pulgas",
                tratamiento="Pipeta antipulgas y champú medicado semanal",
                nombre_mascota="Toby",
                veterinario=vet_4,
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 5),
                diagnostico="Dermatitis alérgica",
                tratamiento="Crema con cortisona y antihistamínico oral por 7 días",
                nombre_mascota="Nala",
                veterinario=vet_4,
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 10),
                diagnostico="Infección en herida",
                tratamiento="Limpieza con clorhexidina, puntos y amoxicilina",
                nombre_mascota="Bruno",
                veterinario=vet_5,
            ),
            # Clínica Veterinaria Los Andes -> 2 historias clínicas
            HistoriaClinica(
                fecha_atencion=date(2026, 10, 28),
                diagnostico="Infección de oído (otitis)",
                tratamiento="Gotas óticas antibióticas y limpieza diaria por 7 días",
                nombre_mascota="Kira",
                veterinario=vet_6,
            ),
            HistoriaClinica(
                fecha_atencion=date(2026, 11, 14),
                diagnostico="Dermatitis por hongos",
                tratamiento="Crema antimicótica (ketoconazol) y baño medicado",
                nombre_mascota="Simba",
                veterinario=vet_7,
            ),
        ]

        session.add_all(
            [
                clinica_norte,
                clinica_sur,
                clinica_andes,
                cons_101,
                cons_102,
                cons_201,
                cons_202,
                cons_301,
                cons_302,
                vet_1,
                vet_2,
                vet_3,
                vet_4,
                vet_5,
                vet_6,
                vet_7,
                *historias,
            ]
        )
        session.commit()
        print("Datos insertados correctamente en la base de datos.")
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()


if __name__ == "__main__":
    poblar()