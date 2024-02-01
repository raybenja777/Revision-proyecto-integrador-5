mapa = """..###################
....#...............#
#.#.#####.#########.#
#.#...........#.#.#.#
#.#####.#.###.#.#.#.#
#...#.#.#.#.....#...#
#.#.#.#######.#.#####
#.#...#.....#.#...#.#
#####.#####.#.#.###.#
#.#.#.#.......#...#.#
#.#.#.#######.#####.#
#...#...#...#.#.#...#
###.#.#####.#.#.###.#
#.#...#.......#.....#
#.#.#.###.#.#.###.#.#
#...#.#...#.#.....#.#
###.#######.###.###.#
#.#.#.#.#.#...#.#...#
#.#.#.#.#.#.#.#.#.#.#
#.....#.....#.#.#.#.#
###################.."""

mapa = [
    
    ['#', '#', '.', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '.', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '.', '#', '#', '#', '#',],
    ['#', '#', '#', '.', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],
    ['#', '#', '#', '#', '#', '#', '#', '#', '#',],

]




import os
import random

class Juego:
  def __init__(self, mapa, posicion_inicial, posicion_final):
    self.mapa = mapa
    self.posicion_inicial = posicion_inicial
    self.posicion_final = posicion_final
    self.posicion_actual = posicion_inicial

  def mover(self, direccion):
    px, py = self.posicion_actual
    
    if direccion == 'arriba' and py > 0 and self.mapa[py - 1][px] != '#':
      py -= 1
    elif direccion == 'abajo' and py < len(self.mapa) - 1 and self.mapa[py + 1][px] != '#':
      py += 1
    elif direccion == 'izquierda' and px > 0 and self.mapa[py][px - 1][px] != '#':
      px -= 1 
    elif direccion == 'derecha' and px < len(self.mapa[0]) - 1 and self.mapa[py][px + 1] != '#':
      px += 1

    self.posicion_actual = (px, py)

  def mostrar_mapa(self):
    os.system( 'cls' if os.name == 'nt' else 'clear')
    for fila in self.mapa:
      print(''.join(fila))

  def victoria(self):
    return self.posicion_actual == self.posicion_final

class JuegoArchivo(Juego):
  def __init__(self, path_mapas, nombre):
    archivo_elegido = self.elegir_archivo(path_mapas)
    mapa, posicion_inicial, posicion_final = self.leer_mapa(archivo_elegido)
    super().__init__(mapa, posicion_inicial, posicion_final)
    self.nombre = nombre

  def elegir_archivo(self, path_mapas):
    archivos = os.listdir(path_mapas)
    nombre_archivo = random.choice(archivos)
    return os.path.join(path_mapas, nombre_archivo)

  def leer_mapa(self, path_archivo):
    with open(path_archivo, 'r', encoding='utf-8') as archivo:
      contenido = archivo.readlines()

      coordenadas = list(map(int, contenido[0].split()))
      posicion_inicial = (coordenadas[0], coordenadas[1])
      posicion_final = (coordenadas[2], coordenadas[3])

        
      mapa = [list(linea.strip()) for linea in contenido[1:]]


    return mapa, posicion_inicial, posicion_final


    return mapa, posicion_inicial, posicion_final

if __name__ == '__main__':
  nombre = input('Ingrese su nombre: ')

  juego = JuegoArchivo(path_mapas=r'C:\Users\HP\Documents\Proyecto integrador 5', nombre=nombre)

  while not juego.victoria():
    juego.mostrar_mapa()
    direccion = input('Ingresar(abajo, arriba, derecha, izquierda): ').lower()
    juego.mover(direccion)

    print(f'Felicitaciones, {nombre}! Has ganado, campeon.')






