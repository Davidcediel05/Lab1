## Analisis estadistico de señal EMG
### Describcion 
<p>
Este proyecto analiza señales de electromiografía (EMG) utilizando algoritmos de programación. Se emplean herramientas de procesamiento de señales para leer, visualizar y analizar datos provenientes de registros EMG.
</p>

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

### Análisis Estadístico de la Señal

<p>
El análisis estadístico de la señal EMG permite extraer información relevante sobre su comportamiento, lo que es fundamental para diversas aplicaciones biomédicas. Algunos de los aspectos analizados incluyen:
</p>

- **Media:**  La media de una señal es una medida fundamental que proporciona información sobre el valor promedio de los datos. 
- **Desviación estándar:** La desviación estándar de una señal es una medida de variabilidad de los datos.

#### Estas medidas en señales EMG, nos permite:
- Evaluar la amplitud de la señal.
- Detectar ruido o artefactos.
- Comparar la actividad muscular entre diferentes canales o condiciones.
- Analizar la calidad de la señal.

-**Histograma:** Es una herramienta grafica que nos permite analizar las propiedades estadísticas y visuales de una señal, para su procesamiento y mejora.
Visualizar la distribución de amplitudes
Identificar características estadísticas
Detectar ruido o anomalías
Análisis de contraste en imágenes
Compresión de datos
Diseño de filtros

  
