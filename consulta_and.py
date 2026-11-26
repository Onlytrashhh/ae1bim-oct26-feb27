"""Consulta con and_(): filtra historias clínicas por fecha y diagnóstico."""

from datetime import date

from sqlalchemy import and_
from sqlalchemy.orm import sessionmaker

from crear_base_entidades import HistoriaClinica, engine


def consultar_historias_and():
    """Obtiene historias clínicas desde noviembre de 2026 con diagnóstico de dermatitis."""
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        historias = (
            session.query(HistoriaClinica)
            .filter(
                and_(
                    HistoriaClinica.fecha_atencion >= date(2026, 11, 1),
                    HistoriaClinica.diagnostico.ilike("%dermatitis%"),
                )
            )
            .all()
        )

        print("=== Historias Clínicas desde 2026-11-01 con Dermatitis (uso de and_) ===")
        for historia in historias:
            vet = historia.veterinario
            print(
                f"Fecha: {historia.fecha_atencion} | "
                f"Mascota: {historia.nombre_mascota} | "
                f"Diagnóstico: {historia.diagnostico} | "
                f"Tratamiento: {historia.tratamiento} | "
                f"Veterinario: {vet.nombres} {vet.apellidos}"
            )
    finally:
        session.close()


if __name__ == "__main__":
    consultar_historias_and()