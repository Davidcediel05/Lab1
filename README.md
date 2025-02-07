## Analisis estadistico de señal EMG
### Describcion 
<p>
Este proyecto analiza señales de electromiografía (EMG) utilizando algoritmos de programación. Se emplean herramientas de procesamiento de señales para leer, visualizar y analizar datos provenientes de registros EMG.
</p>.
### Caracteristicas principales
- Lectura de señales EMG: Utiliza la biblioteca wfdb para leer señales EMG desde un archivo.
-	Visualización de señales: Grafica las señales EMG en el dominio del tiempo.
- Cálculo de métricas estadísticas: Calcula la media, desviación estándar, coeficiente de variación y genera histogramas con funciones de densidad de probabilidad (PDF).
- Agregar ruido: Permite agregar ruido gaussiano, ruido de impulso y ruido tipo artefacto a la señal.
- Cálculo de SNR: Calcula la relación señal-ruido (SNR) después de agregar ruido.
### Estructura del proyecto
- Lab1.py: Lee y visualiza la señal EMG desde un archivo
- LABfinal.py: Versión optimizada del procesamiento de señales EMG.
- Pruebaruido.py: Genera ruido aleatorio y analiza su comportamiento en el dominio de la frecuencia.
- emg_healthy.dat y emg_healthy.hea: Archivos de datos de la señal EMG.
- Lab1s.docx: Documento con información del laboratorio.
###Análisis Estadístico de la Señal
<p>
El análisis estadístico de la señal EMG permite extraer información relevante sobre su comportamiento, lo que es fundamental para diversas aplicaciones biomédicas. Algunos de los aspectos analizados incluyen:
</p>
- Media y Varianza: Para conocer el nivel de actividad muscular y su variabilidad
- Distribución de la Señal: Se utiliza la estimación de densidad de probabilidad para comprender la distribución de amplitudes.
- Transformada de Fourier: Permite analizar la frecuencia dominante y evaluar la presencia de ruido.
- Detección de Patrones: Ayuda en la identificación de fatiga muscular o anomalías en la actividad neuromuscular.
