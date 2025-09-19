import time
import matplotlib.pyplot as plt

alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:',.<>/?\\|`~\""
contraseña  = "ABC1"

def fuerza_bruta(contraseña, alfabeto):
    intentos = 0
    tiempos = []      # Lista para guardar tiempo por longitud
    longitudes = []   # Lista para guardar la longitud actual
    inicio_total = time.time()
    
    longitud = 1
    while True:
        max_num = len(alfabeto) ** longitud
        inicio = time.time()  # Tiempo al iniciar esta longitud
        
        for num in range(max_num):
            intento = ""
            temp = num
            for _ in range(longitud):
                intento = alfabeto[temp % len(alfabeto)] + intento
                temp //= len(alfabeto)
            intentos += 1
            
            if intento == contraseña:
                fin_total = time.time()
                print(f"Contraseña encontrada: {intento}")
                print(f"Intentos necesarios: {intentos}")
                print(f"Tiempo total de ejecución: {fin_total - inicio_total:.4f} segundos")
                
                # Graficar
                plt.plot(longitudes, tiempos, marker='o')
                plt.xlabel("Longitud de intento")
                plt.ylabel("Tiempo (segundos)")
                plt.title("Tiempo de fuerza bruta por longitud de contraseña")
                plt.grid(True)
                plt.show()
                return

        fin = time.time()
        tiempos.append(fin - inicio)  # Tiempo tomado para esta longitud
        longitudes.append(longitud)   # Registrar la longitud
        longitud += 1
        
        if longitud > len(contraseña):
            print("Contraseña no encontrada")
            return

if __name__ == "__main__":
    fuerza_bruta(contraseña, alfabeto)
