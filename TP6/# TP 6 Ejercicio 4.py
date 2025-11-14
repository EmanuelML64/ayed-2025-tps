# TP 6 Ejercicio 4
def eliminar_comentarios(nombre_archivo):
    try:
        with open(nombre_archivo, 'r', encoding='utf-8') as f_in, \
             open("sin_comentarios.py", 'w', encoding='utf-8') as f_out:
            
            dentro_docstring = False
            tipo_doc = None  

            for linea in f_in:
                l = linea.strip()

                
                if not dentro_docstring:
                    if l.startswith("'''") or l.startswith('"""'):
                        if l.count("'''") == 2 or l.count('"""') == 2:
                            continue
                        dentro_docstring = True
                        tipo_doc = l[:3]
                        continue
                else:
                    if tipo_doc in l:
                        dentro_docstring = False
                        tipo_doc = None
                    continue  

                
                nueva_linea = ""
                dentro_comillas = False
                tipo_comilla = None

                for i, c in enumerate(linea):
                    if c in ('"', "'"):
                        
                        if not dentro_comillas:
                            dentro_comillas = True
                            tipo_comilla = c
                        elif tipo_comilla == c:
                            dentro_comillas = False

                    
                    if c == '#' and not dentro_comillas:
                        break

                    nueva_linea += c

                
                if nueva_linea.strip():
                    f_out.write(nueva_linea.rstrip() + '\n')

        print("Archivo generado: sin_comentarios.py")

    except FileNotFoundError:
        print("Error: No se encontró el archivo.")
    except Exception as e:
        print("Error inesperado:", e)


nombre = input("Ingrese el nombre del archivo Python a limpiar: ")
eliminar_comentarios(nombre)
