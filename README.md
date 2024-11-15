
# Proyecto de Extracción de Texto de Imagen

Este proyecto permite procesar imágenes mediante la librería `Pillow` para manipular imágenes y `pytesseract` para realizar el Reconocimiento Óptico de Caracteres (OCR). El flujo del código realiza los siguientes pasos:

1. Amplifica la resolución de una imagen.
2. Divide la imagen amplificada en bloques de un tamaño específico.
3. Extrae texto de cada bloque usando OCR.
4. Guarda bloques donde no se pudo extraer texto.
5. Muestra el texto extraído por consola y guarda el texto completo si es válido.

## ¿Cómo funciona?

### 1. **Abrir la imagen**

El script comienza abriendo una imagen llamada `bis.jpg` desde el directorio de trabajo actual. Utiliza `Pillow` para cargar la imagen en un objeto `Image`.

### 2. **Ampliar la imagen**

Después de abrir la imagen, se amplifica. Esto se logra multiplicando las dimensiones (ancho y alto) de la imagen por un factor de amplificación, que está configurado como `2` en el código por defecto. El tamaño de la imagen se ajusta utilizando el filtro de redimensionado `Image.LANCZOS` para mantener la calidad de la imagen.

### 3. **Dividir la imagen en bloques**

Una vez que la imagen está ampliada, se divide en bloques de 100 píxeles de altura, de acuerdo con el valor de `linea_altura`. Esto permite procesar partes más pequeñas de la imagen de manera más eficiente, facilitando la extracción de texto de áreas específicas.

### 4. **Extracción de texto con OCR**

Para cada bloque de imagen, el código utiliza la librería `pytesseract` para extraer el texto. Si un bloque contiene texto legible, el texto se guarda en una lista `texto_extraido`. Si un bloque no contiene texto, se guarda la imagen del bloque en un archivo con un nombre como `captura_bloque_X.jpg` (donde `X` es el número del bloque).

### 5. **Mostrar y guardar resultados**

Después de procesar todos los bloques, el script imprime el texto extraído de cada bloque en la consola. Al final, si se extrajo algún texto, se concatena todo el texto en una sola cadena y se imprime por completo. Si no se extrajo ningún texto, el código muestra un mensaje de advertencia.

## Requisitos

Este proyecto depende de las siguientes librerías de Python:

- **Pillow**: Para la manipulación de imágenes, como abrir, redimensionar y dividir la imagen en bloques.
- **pytesseract**: Para extraer texto de las imágenes mediante el motor OCR Tesseract.
- **tesseract-ocr**: Es el motor OCR que utiliza `pytesseract` para hacer la extracción de texto.

## Instalación

1. **Instalar dependencias de Python**:
   Crea un entorno virtual (opcional pero recomendado) e instala las dependencias necesarias con el siguiente comando:

   ```bash
   pip install -r requirements.txt

2. **Instalar Tesseract-OCR**: 

    Asegúrate de tener instalado Tesseract-OCR en tu sistema. Este es el motor que pytesseract utiliza para hacer OCR.

    En Linux:

        sudo apt install tesseract-ocr

    Asegúrate de agregar Tesseract al PATH de tu sistema para que pytesseract pueda encontrarlo.

## Uso

Asegúrate de tener la imagen bis.jpg en el mismo directorio que el script de Python. Si la imagen tiene otro nombre, modifica el nombre del archivo en el código o coloca la imagen correcta en el mismo directorio.

Ejecuta el script para redimensionar la imagen, dividirla en bloques y extraer el texto:

            python script.py

El script generará un archivo copia_mejorada.jpg con la imagen ampliada y guardará cualquier bloque de imagen sin texto extraído como archivos .jpg (por ejemplo, captura_bloque_1.jpg).

El texto extraído de cada bloque será mostrado en la consola, y el texto completo extraído se imprimirá al final.

## Archivos generados

* copia_mejorada.jpg: La imagen ampliada y redimensionada.

* captura_bloque_X.jpg: Archivos de imagen de cualquier bloque donde no se pudo extraer texto (si corresponde).

## Notas

Si no se puede extraer texto de ningún bloque, el código mostrará un mensaje indicando que no se pudo extraer texto de la imagen.

Si el bloque contiene texto, el texto se imprime en la consola y se guarda en la variable texto_completo.

Si usas un entorno virtual, asegúrate de activarlo antes de ejecutar el script