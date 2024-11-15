from PIL import Image
import pytesseract

imagen_original = Image.open("bis.jpg")

factor_amplificacion = 2
ancho,alto   = imagen_original.size
nuevo_ancho = ancho * factor_amplificacion
nuevo_alto = alto * factor_amplificacion


aumentar_imagen = imagen_original.resize((nuevo_ancho,nuevo_alto), Image.LANCZOS)

aumentar_imagen.save("copia_mejorada.jpg")
print("Copia guarda Exitosamente!")


bloques=[]


linea_altura = 100
for i in range(0,aumentar_imagen.height, linea_altura):
    region = (0, i,aumentar_imagen.width, i + linea_altura)
    bloques.append(aumentar_imagen.crop(region))



texto_extraido=[]

for idx, bloque in enumerate(bloques):
    texto = pytesseract.image_to_string(bloque)
    texto_extraido.append(texto)
    print(f"texto extraido del bloque {idx + 1}: ")
    print(texto)

    if not texto.strip():
        print(f"No se pudo extraer bloque de {idx + 1} ... Tomando captura de imagen")
        bloque.save(f"captura_bloque_{idx + 1}.jpg")
        print(f"Se ha guardado la captura del bloque {idx + 1} como 'captura_bloque_{idx + 1}.jpg'.")


texto_completo = "\n".join(texto_extraido)
if not texto_completo.strip():
    print("No se pudo extraer el texto de ninguna parte de la imagen....")
else:
    print("Texto extraido de toda la imagen")
    print("Texto completo")


