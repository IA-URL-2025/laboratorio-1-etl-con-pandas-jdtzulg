import pandas as pd

ruta = "data/citas_clinica.csv"

def run_etl():
    df = pd.read_csv(ruta)
    
    df = df[df['telefono'].isna()].copy()
    df['paciente'] = df['paciente'].str.title()
    df['especialidad'] = df['especialidad'].str.upper()

    df['fecha_cita'] = pd.to_datetime(df['fecha_cita'], errors='coerce')
    
    df = df.dropna(subset=['fecha_cita'])

    df = df[df['estado'] == 'CONFIRMADA']
    df = df[df['costo'] > 0]

    df['telefono'] = df['telefono'].fillna('NO REGISTRA')
    
    # Guardar resultado
    df.to_csv("data/output.csv", index=False)

if __name__ == "__main__":
    run_etl()
