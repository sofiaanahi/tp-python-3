import pandas as pd

def analisis_estadistico(data_frame):
    try:
        #  calcula la frecuencias acumulas
        data_frame["Fi"] = data_frame["fi"].cumsum()

        # calcula la frecuencias relativas
        data_frame["ri"] = data_frame["fi"] / data_frame["fi"].sum()
      
        # calcula la frecuencias relaativaws acumuladas
        data_frame["Ri"] = data_frame['ri'].cumsum()
        
        # calcula la probabilidades en porcentaje
        data_frame["pi%"] = data_frame["ri"] * 100
        
        # calcula la probabilidades de acumuladas en porcentaje
        data_frame["Pi%"] = data_frame["Ri"] * 100
        
        estadistica = {
            'fi': data_frame['fi'].tolist(),
            'Fi': data_frame['Fi'].tolist(),
            'ri': data_frame['ri'].tolist(),
            'Ri': data_frame['Ri'].tolist(),
            'pi%': data_frame['pi%'].tolist(),
            'Pi%': data_frame['Ri'].tolist()

        }

        return estadistica
       
    except Exception as e:

        print(f"Error: la columna '{e.args[0]}' no existe en el data_frame")
        return None

data_frame = pd.read_csv("edad.csv", delimiter=";")
   
resultado = analisis_estadistico(data_frame)

if resultado is not None:
    print("Resultado:" )
    for key, value in resultado.items():
        print(f"{key}:{value}")
   
else:
    print("No funciona")