import pandas as pd

def analisis_estadistico(data_frame):
    try:
        df = pd.DataFrame(data_frame, columns=['edad', 'fi'])

        #  calcula la frecuencias acumulas
        df["Fi"] = df["fi"].cumsum()

        # calcula la frecuencias relativas
        df["ri"] = df["fi"] / df["fi"].sum()
      
        # calcula la frecuencias relaativaws acumuladas
        df["Ri"] = df['ri'].cumsum()
        
        # calcula la probabilidades en porcentaje
        df["pi%"] =df["ri"] * 100
        
        # calcula la probabilidades de acumuladas en porcentaje
        df["Pi%"] =df["Ri"] * 100
        
        print(df)

        df.to_csv('edad.csv', index=False)
    
    except Exception as e:

        print(f"Error:{e}")
        return None



data_frame = [

            [19,2],
            [20,2],
            [21,1],
            [22,2],
            [23,2],
            [24,2],
            [25,1],
            [26,2],
            [27,2],
            [28,2],
            [29,1],
            [30,2],
            [31,2],
            [32,2],
            [33,2],
            [34,2],  
            [35,1],
]



analisis_estadistico(data_frame)

