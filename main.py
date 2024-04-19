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
        
        print(data_frame)
    
    except Exception as e:

        print(f"Error: la columna '{e.args[0]}' no existe en el data_frame")
        return None

data_frame = pd.read_csv("edad.csv", delimiter=";")
   
analisis_estadistico(data_frame)

