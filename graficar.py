import os

class Reportes:
    def graficar(lista_circular):
        with open("Matriz.dot", "w") as archivo:
            nodo_actual = lista_circular.inicio
            matrix_count = 0
            archivo.write('digraph G {\n')
            archivo.write('    rankdir=TB;\n')
            archivo.write('    node [shape=ellipse];\n')
            archivo.write('    edge [dir=none];\n')
            archivo.write(f'    Matrices -> {nodo_actual.nombre};\n')
            
            while nodo_actual is not None:
                n = nodo_actual.n + 1 
                m = nodo_actual.m + 1
                matriz = nodo_actual.matriz
                
                archivo.write(f'     {{\n')
                archivo.write(f'        n{matrix_count} [label="n= {n}"];\n')
                archivo.write(f'        m{matrix_count} [label="m= {m}"];\n')
                
                for i in range(m):
                    for j in range(n):
                        dato = matriz.obtener_elemento(i, j)
                        cell_id = f'cell_{matrix_count}_{i}_{j}'
                        archivo.write(f'        {cell_id} [label="{dato}"];\n')
                
                for j in range(n):
                    for i in range(m - 1):
                        current_cell = f'cell_{matrix_count}_{i}_{j}'
                        next_cell = f'cell_{matrix_count}_{i+1}_{j}'
                        archivo.write(f'        {current_cell} -> {next_cell} [constraint=true];\n')
                
                for j in range(n):
                    initial_cell = f'cell_{matrix_count}_0_{j}'
                    archivo.write(f'    {nodo_actual.nombre} -> {initial_cell};\n')
                
                archivo.write('    }\n')
                
                archivo.write(f'    {nodo_actual.nombre} -> n{matrix_count};\n')
                archivo.write(f'    {nodo_actual.nombre} -> m{matrix_count};\n')
                
                if nodo_actual.siguiente == lista_circular.inicio:
                    break
                nodo_actual = nodo_actual.siguiente
                matrix_count += 1
            
            archivo.write('}')
        
        os.system('dot -Tpng Matriz.dot -o Matriz.png')

    

