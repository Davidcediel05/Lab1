import wfdb
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import gaussian_kde

ruta_señal= r"C:\Users\juany\OneDrive\Escritorio\LabSeñales\Lab1\emg_healthy"
#1.Extraer la señal con wfdb(datos y frecuencia de muestreo) 
record= wfdb.rdrecord(ruta_señal)
señal = record.p_signal #Datos de la señal
fs = record.fs  #Frecuencia de muestreo
n_canales = record.sig_name #numero de canales EMG siempre tiene varios canales de donde se extraen datos
#Creamos un vector de cero hasta el numero de muestras de la señal
tiempo= np.arange(0,len(señal))/fs #Se divide por fs para convertir las muestras en tiempo(segundos)
#2.Grafica de la señal sin ruido
plt.figure(figsize=(10,6))
for i, nombre in enumerate(n_canales):
    plt.plot(tiempo, señal[:, i], label=nombre)
plt.title("Señal EMG")
plt.xlabel("Tiempo [s]")
plt.ylabel("Voltaje [V]")
plt.legend()
plt.grid()
plt.show()
#3. Metricas estadisticas
def calcular_con_funciones(tiempo, señal, n_canales):
    for i, nombre in enumerate(n_canales):
        canal = señal[:, i]  

       
        media = np.mean(canal)

        
        desviacion_estandar = np.std(canal)

        
        coeficiente_variacion = (desviacion_estandar / media) * 100

        print(f"Canal {nombre}:")
        print(f"  - Media: {media:.4f}")
        print(f"  - Desviación estándar: {desviacion_estandar:.4f}")
        print(f"  - Coeficiente de variación: {coeficiente_variacion:.4f}%\n")

        
        pdf = gaussian_kde(canal)
        x = np.linspace(min(canal), max(canal), 1000)
        y = pdf(x)

        plt.figure(figsize=(4, 4))
        plt.hist(canal, bins=50, density=True, alpha=0.7, color='blue', edgecolor='black', label="Histograma")
        plt.plot(x, y, color='yellow', label='PDF')
        plt.title(f"Histograma del canal {nombre}")
        plt.xlabel("Voltaje [mV]")
        plt.ylabel("Densidad de probabilidad")
        plt.legend()
        plt.grid()
def calcular_manual(tiempo, señal, n_canales):
    for i, nombre in enumerate(n_canales):
        canal = señal[:, i]
        suma = 0
        for valor in canal:
            suma += valor #Media
        media = suma / len(canal)
        suma_= 0
        
        for valor in canal:
            suma_ += (valor - media) ** 2 
        desviacion_estandar = (suma_ / len(canal)) ** 0.5
        
        coeficiente_v = (desviacion_estandar / media) * 100 if media != 0 else 0
        
        print(f"Canal {nombre}:")
        print(f"  - Media: {media:.4f}")
        print(f"  - Desviación estándar: {desviacion_estandar:.4f}")
        print(f"  - Coeficiente de variación: {coeficiente_v:.4f}%\n")
           
        pdf = gaussian_kde(canal)
        x = np.linspace(min(canal), max(canal), 1000)
        y = pdf(x)

    
        plt.figure(figsize=(4, 4))
        plt.hist(canal, bins=50, alpha=0.7, color='blue', edgecolor='black', label="Histograma")
        plt.plot(x, y, color='yellow', label='PDF')
        plt.title(f"Histograma del canal {nombre}Manual")
        plt.xlabel("Voltaje [V]")
        plt.ylabel("Frecuencia")
        plt.legend()
        plt.grid()
        plt.show()
#4.agregaremos ruido y calcularemos SNR
def calcular_snr(señal_ori, señal_ruido):
    potencia_señal = np.mean(señal_ori ** 2)
    ruido = señal_ruido - señal_ori
    potencia_ruido = np.mean(ruido ** 2)
    snr = 10 * np.log10(potencia_señal / potencia_ruido)
    return snr

def ruido_gaussiano(señal, snr_objetivo):
    ruido = np.random.normal(0, np.std(señal) / (10 ** (snr_objetivo / 20)), señal.shape)
    señal_ruidosa = señal + ruido
    snr = calcular_snr(señal, señal_ruidosa)
    
        
    plt.figure(figsize=(10, 5))
    plt.plot(tiempo, señal, label="Señal original", alpha=0.7)
    plt.plot(tiempo, señal_ruidosa, label=f"Ruido Gaussiano (SNR: {snr:.2f} dB)", alpha=0.7)
    plt.title("Señal con Ruido Gaussiano")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Voltaje [V]")
    plt.legend()
    plt.grid()
    plt.show()
    
    return señal_ruidosa, snr
def ruido_impulso(señal, porcentaje=0.05):
    señal_ruidosa = señal.copy()
    num_muestras = int(len(señal) * porcentaje)
    indices = np.random.choice(len(señal), num_muestras, replace=False)
    señal_ruidosa[indices] = np.max(señal) * np.random.choice([-1, 1], size=num_muestras)
    snr = calcular_snr(señal, señal_ruidosa)
    
    
    plt.figure(figsize=(10, 5))
    plt.plot(tiempo, señal, label="Señal original", alpha=0.7)
    plt.plot(tiempo, señal_ruidosa, label=f"Ruido de Impulso (SNR: {snr:.2f} dB)", alpha=0.7)
    plt.title("Señal con Ruido de Impulso")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Voltaje [V]")
    plt.legend()
    plt.grid()
    plt.show()
    
    return señal_ruidosa, snr
def ruido_artefacto(señal, frecuencia=2, amplitud_factor=0.5):
    tiempo = np.arange(len(señal))
    ruido = amplitud_factor * np.max(señal) * np.sin(2 * np.pi * frecuencia * tiempo / len(señal))
    señal_ruidosa = señal + ruido
    snr = calcular_snr(señal, señal_ruidosa)
    
   
    plt.figure(figsize=(10, 5))
    plt.plot(tiempo, señal, label="Señal original", alpha=0.7)
    plt.plot(tiempo, señal_ruidosa, label=f"Ruido Tipo Artefacto (SNR: {snr:.2f} dB)", alpha=0.7)
    plt.title("Señal con Ruido Tipo Artefacto")
    plt.xlabel("Tiempo [s]")
    plt.ylabel("Voltaje [V]")
    plt.legend()
    plt.grid()
    plt.show()
    
    return señal_ruidosa, snr
        
print("\n--- METRICAS CON FUNCIONES ---")
calcular_con_funciones(tiempo, señal, n_canales)

print("\n--- METRICAS MANUALES ---")
calcular_manual(tiempo, señal, n_canales)


canal = señal[:, 0]


ruido_gaussiano(canal, snr_objetivo=10)
ruido_impulso(canal, porcentaje=0.05)
ruido_artefacto(canal, frecuencia=2)
