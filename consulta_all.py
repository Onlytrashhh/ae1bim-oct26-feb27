"""Consulta con all(): presenta cada Clínica y el número de Historias Clínicas asociadas."""

from sqlalchemy.orm import sessionmaker

from crear_base_entidades import Clinica, engine


def consultar_clinicas_y_historias():
    """Obtiene todas las clínicas usando all() y cuenta sus historias clínicas."""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        clinicas = session.query(Clinica).all()

        print("=== Clínicas y número de Historias Clínicas asociadas (uso de all) ===")
        for clinica in clinicas:
            total_historias = sum(
                len(veterinario.historias_clinicas)
                for consultorio in clinica.consultorios
                for veterinario in consultorio.veterinarios
            )
            print(
                f"Clínica: {clinica.nombre_comercial} | "
                f"Dirección: {clinica.direccion} | "
                f"Responsable: {clinica.veterinario_responsable} | "
                f"Historias Clínicas asociadas: {total_historias}"
            )
    finally:
        session.close()


if __name__ == "__main__":
    consultar_clinicas_y_historias()