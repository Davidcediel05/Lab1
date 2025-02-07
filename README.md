## Analisis estadistico de señal EMG
### Descripcion 
<p>
En este proyecto se busca identificar los estadísticos que describen una señal biomédica, obtenerlos a partir de algoritmos de programación y mostrarlas, además se procesara una señal de electromiografía (EMG) y se les añade diferentes tipos de ruidos (gaussiano, de impulso y artefacto), posterior a eso calcular SNR y se graficaran las señales resultantes
Al trabajar con señales biomédicas como las de EMG, nos podemos encontrar con ruidos dentro de las mediciones, El ruido se puede crear por diversos motivos como interferencias eléctricas, movimientos involuntarios o alguna daño e interferencia en los electrodos.
En este proyecto analizamos la señal y 3 tipos de ruidos:

-	Señal sin ruido
-	Ruido gaussiano
-	Ruido impulso
-	Ruido tipo Artefacto
  
Además, se mide la relación Señal-Ruido (SNR), con lo cual cuantificar la calidad de la señal después de contaminarla de ruido
</p>

#### Señal sin ruido


Se elige una señal original sin ninguna alteración, muestra un comportamiento real de una señal EMG, donde se evidencia picos normales de la actividad muscular

![Señalsinruido](https://github.com/user-attachments/assets/286d7f53-465d-4017-aac7-89b0e850f3fb)

#### Ruido gaussiano
<p>
Se comprende como un ruido estadístico, se caracteriza por su curva en forma de campana, simétricamente alrededor de su valor medio, nos representa variaciones aleatorias que ocurren en los datos del mundo real, se caracteriza por su media y varianza, donde su media indica la tendencia central de ruido y la variancia mide la dispersión de los valores de ruido, dentro de nuestro enfoque este tipo de ruido se puede generar a partir de imperfecciones del sensor o factores ambientales.
    
![RuidoG](https://github.com/user-attachments/assets/1a95ec67-f2e6-4396-a05a-0f5dd530546f)

Como se puede observar en la imagen se muestra la señal original(azul) y la señal con ruido gaussiano (naranja) en ella notamos como el ruido afecta su claridad sin embargo su SNR (10.01dB) al ser un numero positivo nos permite inferir que sigue siendo predominante la señal.
</p>


#### Ruido impulso
<P>
Este tipo de ruido se caracteriza por sonidos de corta duración y alguna presión sonora por picos repentinos, por parte del entorno en el que analizamos este tipo de ruido se puede deber por algún error en los electrodos o movimientos bruscos dentro de la medición de EMG.
    
![RuidoImpulso](https://github.com/user-attachments/assets/e07570ae-6fe2-4447-aefe-063385692ccf)

En la grafica se logra observar la aparición de picos abruptos que ocurren de manera constante a lo largo de la señal, su SNR (-9.73dB) nos indica que el ruido influye en la claridad de la señal original.
</p>

#### Ruido tipo Artefacto
<p>
Un ruido tipo de Artefacto se puede definir como una distorsión o error, lo cual puede alterar la interpretación de la medición viéndose como un señal senoidal , simulando alguna patología, sin embargo, este tipo de ruido nos puede hablar de mal funcionamiento de los electrodos o algún contacto indebido dentro de la medición.
    
![RuidoA](https://github.com/user-attachments/assets/e36e59ec-b294-47ad-a48c-3c02790b749a)

En la grafica podemos observar como este tipo de ruido introduce una señal undilatoria que esta superpuesta a la señal original, su SNR(-13.67) lo cual nos indica que el ruido es mas fuerte que la señal original.
</p>

### Análisis Estadístico de la Señal

<p>
El análisis estadístico de la señal EMG permite extraer información relevante sobre su comportamiento, lo que es fundamental para diversas aplicaciones biomédicas. Algunos de los aspectos analizados incluyen:
</p>

- **La Media:**  De una señal es una medida fundamental que proporciona información sobre el valor promedio de los datos. 
- **Desviación estándar:** La desviación estándar de una señal es una medida de variabilidad de los datos.
  
![Metricas](https://github.com/user-attachments/assets/d5c5d173-16dc-4a44-a0e9-88008b335190)

#### Estas medidas en señales EMG, nos permite:
- Evaluar la amplitud de la señal.
- Detectar ruido o artefactos.
- Comparar la actividad muscular entre diferentes canales o condiciones.
- Analizar la calidad de la señal.

**Histograma:** Es una herramienta grafica que nos permite analizar las propiedades estadísticas y visuales de una señal, para su procesamiento y mejora.
- Visualizar la distribución de amplitudes
- Identificar características estadísticas
- Detectar ruido o anomalías
- Análisis de contraste en imágenes
- Compresión de datos
- Diseño de filtros

![Histograma](https://github.com/user-attachments/assets/8c307ff4-5c97-4711-aa62-69623eccfd08)

<p>
  En la grafica podemos observar que en la actividad muscular se presentan valores positivos mas frecuentes lo cual sugiere que hubo contracción muscular durante la medición, es evidente que el pico es muy pronunciado, lo cual indica que la señal tiene una buena calidad.
</p>

### Relacion señal-ruido
<p>
La relación señal-ruido es una métrica fundamental en el procesamiento de señales, puesto que permite evaluar la calidad de una señal en presencia de ruido, esta medida  compara la potencia de la señal útil con la potencia del ruido presente en un sistema.
    
</p>

### Requisitos
<p>
Para ejecutar el código, es necesario instalar Python y las siguientes librerías:
- wfdb
- numpy
- matplotlib
- scipy
Tener instalado un compilador, que para este caso se utilizo spyder.  
</p>

### Caracteristicas principales
- Lectura de señales EMG: Utiliza la biblioteca wfdb para leer señales EMG desde un archivo.
- Visualización de señales: Grafica las señales EMG en el dominio del tiempo.
- Cálculo de métricas estadísticas: Calcula la media, desviación estándar, coeficiente de variación y genera histogramas con funciones de densidad de probabilidad (PDF).
- Agregar ruido: Permite agregar ruido gaussiano, ruido de impulso y ruido tipo artefacto a la señal.
- Cálculo de SNR: Calcula la relación señal-ruido (SNR) después de agregar ruido.

### Estructura del proyecto
- Lab1.py: Lee y visualiza la señal EMG desde un archivo
- LABfinal.py: Versión optimizada del procesamiento de señales EMG.
- Pruebaruido.py: Genera ruido aleatorio y analiza su comportamiento en el dominio de la frecuencia.
- emg_healthy.dat y emg_healthy.hea: Archivos de datos de la señal EMG.
- Lab1s.docx: Documento con información del laboratorio.

### Ejecución

- Asegúrate de que los archivos de datos están en la misma carpeta que los scripts.
-	Ejecuta Lab1.py o LABfinal.py para analizar la señal:
- python Lab1.py
  Para probar la simulación de ruido, ejecuta:
  
`python Pruebaruido.py`


### Conclusión
<p>
Este proyecto nos permite identificar las métricas estadísticas de una señal de EMG en condiciones normales, para posteriormente analizar el comportamiento de esta señal agregando diferentes tipos de ruidos y con ello calcular su SNR lo cual nos ayuda a comprender el fundamento y el impacto de estos ruido.
</p>

### Licencia

Este proyecto es de uso académico y educativo.

### Contacto
<p>
Si tienes alguna pregunta o sugerencia, no dudes en contactarme:
</p>

- **Nombre:** [Juan David Cediel Farfan]
- **Email:** [Juandacedielfarfan2@gmail.com]
- **GitHub:** [David05Cediel]  

