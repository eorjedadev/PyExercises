# ============================================================
# CURSO COMPLETO DE PYTHON - PARTE 3
# EJERCICIOS 201-350 (Nivel Intermedio-Avanzado)
# ============================================================

# ============================================================
#        EJERCICIOS 201-250: COLECCIONES AVANZADAS
# ============================================================

"""
────────────────────────────────
EJERCICIO 201 - defaultdict
────────────────────────────────
Descripción:Diccionario con valores por defecto.

Concepto: defaultdictint crea valores 0 automáticamente

Código:
"""
from collections import defaultdict, Counter, OrderedDict, deque

# defaultdict - valor por defecto
palabras = ["hola", "mundo", "hola", "python", "mundo", "hola"]

contador = defaultdict(int)
for palabra in palabras:
    contador[palabra] += 1

print(dict(contador))  # {'hola': 3, 'mundo': 2, 'python': 1}

# defaultdict con list
frutas_por_letra = defaultdict(list)
for fruta in ["manzana", "banano", "cereza", "uva"]:
    frutas_por_letra[fruta[0]].append(fruta)

print(dict(frutas_por_letra))

# defaultdict con set
palabras_repetidas = ["el", "el", "sol", "sol", "sol", "la"]
conjuntos = defaultdict(set)
for palabra in palabras_repetidas:
    conjuntos[palabra[0]].add(palabra)

print(dict(conjuntos))

"""
────────────────────────────────
EJERCICIO 202 - COUNTER
────────────────────────────────
Descripción: Cuenta elementos en iterables.

Concepto: Counter es como un diccionario especializado

Código:
"""
# Contar elementos
contador = Counter("abracadabra")
print(contador)  # Counter({'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1})

# Métodos útiles
print(contador.most_common(3))  # [('a', 5), ('b', 2), ('r', 2)]
print(list(contador.elements()))  # ['a', 'a', 'a', 'a', 'a', 'b', 'b', ...]

# Operaciones de conjuntos
c1 = Counter([1, 2, 3, 4])
c2 = Counter([3, 4, 5, 6])

print(c1 + c2)  # Suma
print(c1 - c2)  # Diferencia (solo positivos)
print(c1 & c2)  # Intersección
print(c1 | c2)  # Unión

# Actualizar
contador = Counter()
contador.update("hello")
print(contador)

"""
────────────────────────────────
EJERCICIO 203 - OrderedDict
────────────────────────────────
Descripción: Diccionario que mantiene orden (pre-Python 3.7).

Concepto: Útil para versiones antiguas o cuando se necesita control explícito

Código:
"""
# OrderedDict (ahora dict mantiene orden, pero OrderedDict tiene métodos extra)
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3

print(od)
print(list(od.keys()))
print(list(od.values()))

# Mover elemento al final
od.move_to_end('a')
print(list(od.keys()))

# Mover al principio
od.move_to_end('c', last=False)
print(list(od.keys()))

# popitem con comportamiento específico
print(od.popitem(last=True))  # Elimina último
print(od.popitem(last=False))  # Elimina primero

"""
────────────────────────────────
EJERCICIO 204 - DEQUE
────────────────────────────────
Descripción: Cola doblemente terminada.

Concepto: Rápido agregar/quitar de ambos extremos

Código:
"""
# Crear deque
d = deque([1, 2, 3])
print(d)

# Agregar extremos
d.append(4)        # derecha
d.appendleft(0)    # izquierda
print(d)

# Remover extremos
d.pop()           # derecha
d.popleft()       # izquierda
print(d)

# Rotar
d = deque([1, 2, 3, 4, 5])
d.rotate(1)       # Rota a la derecha
print(d)  # [5, 1, 2, 3, 4]
d.rotate(-1)      # Rota a la izquierda
print(d)  # [1, 2, 3, 4, 5]

# Extender
d.extend([6, 7])
print(d)

# Maxlen
d = deque(maxlen=3)
d.extend([1, 2, 3, 4, 5])  # Mantiene solo últimos 3
print(d)  # deque([3, 4, 5], maxlen=3)

# Usar como cola circular
def ventana_deslizante(lista, tamano):
    resultado = deque(maxlen=tamano)
    for elem in lista:
        resultado.append(elem)
        if len(resultado) == tamano:
            yield tuple(resultado)

print(list(ventana_deslizante([1,2,3,4,5,6], 3)))

"""
────────────────────────────────
EJERCICIO 205 - NAMEDTUPLE
────────────────────────────────
Descripción: Tuplas con nombres de campo.

Concepto: Acceso por índice o por nombre

Código:
"""
from collections import namedtuple

# Definir namedtuple
Punto = namedtuple('Punto', ['x', 'y'])
Punto3D = namedtuple('Punto3D', 'x y z')

# Crear instancias
p = Punto(10, 20)
p3d = Punto3D(1, 2, 3)

# Acceso por nombre
print(p.x, p.y)
print(p3d.x, p3d.y, p3d.z)

# Acceso por índice
print(p[0], p[1])

# Como diccionario
print(p._asdict())

# Reemplazar campos
p2 = p._replace(x=30)
print(p2)

# Crear desde iterable
p_from_list = Punto._make([100, 200])
print(p_from_list)

# Herencia
PuntoConColor = namedtuple('PuntoConColor', Punto._fields + ('color',))
pc = PuntoConColor(1, 2, 'rojo')
print(pc)

"""
────────────────────────────────
EJERCICIO 206 - CHAINMAP
────────────────────────────────
Descripción: Agrupa múltiples diccionarios.

Concepto: Busca en orden, no fusiona

Código:
"""
from collections import ChainMap

# Crear ChainMap
dic1 = {'a': 1, 'b': 2}
dic2 = {'b': 3, 'c': 4}
dic3 = {'c': 5, 'd': 6}

cm = ChainMap(dic1, dic2, dic3)

# Búsqueda en orden
print(cm['a'])  # 1 (en dic1)
print(cm['b'])  # 2 (en dic1, no busca en dic2)
print(cm['c'])  # 4 (en dic2)
print(cm['d'])  # 6 (en dic3)

# Keys, values, items
print(list(cm.keys()))
print(list(cm.values()))
print(list(cm.maps))  # Ver diccionarios individuales

# Modificar afecta el primer diccionario
cm['a'] = 10
print(dic1)  # {'a': 10, 'b': 2}

# Agregar nuevo diccionario
cm.maps.insert(0, {'z': 99})
print(cm['z'])  # 99

# Crear nuevo child (con ámbito local)
child = cm.new_child({'a': 100})
print(child['a'])  # 100 (local)
print(child.maps[1]['a'])  # 10 (padre)

"""
────────────────────────────────
EJERCICIO 207 - HEAPQ (COLAS PRIORIDAD)
────────────────────────────────
Descripción: Implementa colas de prioridad.

Concepto: El elemento menor siempre está en la cima

Código:
"""
import heapq

# Crear heap
heap = []
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 8)
print(heap)  # [2, 5, 8]

# Extraer mínimo
print(heapq.heappop(heap))  # 2
print(heapq.heappop(heap))  # 5

# Convertir lista a heap
numeros = [5, 2, 8, 1, 9]
heapq.heapify(numeros)
print(numeros)  # [1, 2, 8, 5, 9]

# nlargest y nsmallest
print(heapq.nlargest(3, [5, 2, 8, 1, 9]))  # [9, 8, 5]
print(heapq.nsmallest(3, [5, 2, 8, 1, 9]))  # [1, 2, 5]

# Implementar cola de prioridad
class ColaPrioridad:
    def __init__(self):
        self.heap = []
    
    def push(self, prioridad, elemento):
        heapq.heappush(self.heap, (prioridad, elemento))
    
    def pop(self):
        return heapq.heappop(self.heap)[1]
    
    def is_empty(self):
        return len(self.heap) == 0

cola = ColaPrioridad()
cola.push(2, "Baja prioridad")
cola.push(1, "Alta prioridad")
cola.push(3, "Muy baja")

print(cola.pop())  # Alta prioridad

# ============================================================
#        EJERCICIOS 251-300: HERRAMIENTAS AVANZADAS
# ============================================================

"""
────────────────────────────────
EJERCICIO 208 - itertools
────────────────────────────────
Descripción: Herramientas para iteradores.

Concepto: count, cycle, repeat, chain, islice, product

Código:
"""
import itertools

# count(inicio, paso) - infinito
contador = itertools.count(1, 2)
print([next(contador) for _ in range(5)])  # [1, 3, 5, 7, 9]

# cycle - repite infinitamente
ciclador = itertools.cycle([1, 2, 3])
print([next(ciclador) for _ in range(7)])  # [1, 2, 3, 1, 2, 3, 1]

# repeat - repite valor
repetidor = itertools.repeat("hola", 3)
print(list(repetidor))  # ['hola', 'hola', 'hola']

# chain - concatenar iterables
print(list(itertools.chain([1, 2], [3, 4], [5])))  # [1, 2, 3, 4, 5]

# islice - cortar iterable
print(list(itertools.islice(range(10), 2, 8, 2)))  # [2, 4, 6]

# product - producto cartesiano
print(list(itertools.product([1, 2], ['a', 'b'])))
# [(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]

# permutations - permutaciones
print(list(itertools.permutations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]

# combinations - combinaciones
print(list(itertools.combinations([1, 2, 3], 2)))
# [(1, 2), (1, 3), (2, 3)]

# groupby - agrupar
datos = [('a', 1), ('a', 2), ('b', 3), ('b', 4)]
for clave, grupo in itertools.groupby(datos, lambda x: x[0]):
    print(clave, list(grupo))

"""
────────────────────────────────
EJERCICIO 209 - functools
────────────────────────────────
Descripción: Herramientas de programación funcional.

Concepto: lru_cache, partial, reduce, wraps

Código:
"""
import functools
import time

# lru_cache - memorización
@functools.lru_cache(maxsize=128)
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

start = time.time()
print(fibonacci(100))
print(f"Tiempo: {time.time() - start:.4f}s")

# partial - crear funciones parcialmente aplicadas
from functools import partial

def potencia(base, exponente):
    return base ** exponente

cuadrado = partial(potencia, exponente=2)
cubo = partial(potencia, exponente=3)
print(cuadrado(5))  # 25
print(cubo(5))      # 125

# reduce (ya vimos)
from functools import reduce
print(reduce(lambda x, y: x + y, [1, 2, 3, 4]))  # 10

# singledispatch - sobrecarga de funciones
@functools.singledispatch
def procesar(dato):
    print(f"Default: {dato}")

@procesar.register(int)
def _(dato):
    print(f"Entero: {dato * 2}")

@procesar.register(str)
def _(dato):
    print(f"String: {dato.upper()}")

procesar(5)    # Entero: 10
procesar("hi") # String: HI
procesar(3.14) # Default: 3.14

# cmp_to_key - comparar para sorted
from functools import cmp_to_key

def comparar(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    return 0

print(sorted([3, 1, 4, 1, 5], key=cmp_to_key(comparar)))

"""
────────────────────────────────
EJERCICIO 210 - OPERATOR
────────────────────────────────
Descripción: Operadores como funciones.

Concepto: itemgetter, attrgetter, methodcaller

Código:
"""
import operator

# itemgetter - acceder items
personas = [
    {'nombre': 'Juan', 'edad': 30},
    {'nombre': 'Ana', 'edad': 25},
    {'nombre': 'Luis', 'edad': 35}
]

# Ordenar por edad
print(sorted(personas, key=operator.itemgetter('edad')))

# Múltiples niveles
data = [(1, (5, 2)), (2, (1, 3))]
print(sorted(data, key=operator.itemgetter(1, 0)))

# attrgetter - acceder atributos
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def __repr__(self):
        return f"Persona({self.nombre}, {self.edad})"

personas = [Persona('Juan', 30), Persona('Ana', 25)]
print(sorted(personas, key=operator.attrgetter('edad')))

# methodcaller - llamar métodos
palabras = ['hola', 'mundo', 'python']
print(sorted(palabras, key=operator.methodcaller('upper')))

# Operaciones
print(operator.add(2, 3))       # 5
print(operator.mul(2, 3))       # 6
print(operator.getitem([1,2,3], 1))  # 2
print(operator.setitem([1,2,3], 0, 10))  # [10, 2, 3]
print(operator.not_(False))     # True

"""
────────────────────────────────
EJERCICIO 211 - dataclasses AVANZADO
────────────────────────────────
Descripción: Data classes con funcionalidades avanzadas.

Concepto: field, frozen, slots

Código:
"""
from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class Estudiante:
    nombre: str
    edad: int
    cursos: List[str] = field(default_factory=list)
    activo: bool = True

# Uso
e = Estudiante("Juan", 20, ["Python", "Java"])
print(e)

# field con comparador personalizado
@dataclass(order=True)
class PersonaOrdenada:
    nombre: str
    edad: int

p1 = PersonaOrdenada("Juan", 30)
p2 = PersonaOrdenada("Ana", 25)
print(sorted([p1, p2]))  # Ordena por edad

# frozen - inmutable
@dataclass(frozen=True)
class Configuracion:
    puerto: int = 8080
    host: str = "localhost"

config = Configuracion()
# config.puerto = 3000  # FrozenInstanceError

# slots (Python 3.10+)
@dataclass(slots=True)
class Usuario:
    nombre: str
    email: str

# Post-init
@dataclass
class Rectangulo:
    ancho: float
    alto: float
    area: float = field(init=False)
    
    def __post_init__(self):
        self.area = self.ancho * self.alto

r = Rectangulo(10, 5)
print(r.area)

# with dict
@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int = 0

p = Producto("Laptop", 999)
print(asdict(p))
print(astuple(p))
print(p.__dict__)

"""
────────────────────────────────
EJERCICIO 212 - ENUM
────────────────────────────────
Descripción: Enumeraciones con tipos definidos.

Concepto: Enum, IntEnum, Flag

Código:
"""
from enum import Enum, IntEnum, Flag, auto

# Enum básico
class Color(Enum):
    ROJO = 1
    VERDE = 2
    AZUL = 3

print(Color.ROJO)  # Color.ROJO
print(Color.ROJO.value)  # 1
print(Color['ROJO'])  # Color.ROJO

# Iterar
for color in Color:
    print(color.name, color.value)

# IntEnum (se comporta como int)
class Nivel(IntEnum):
    BAJO = 1
    MEDIO = 2
    ALTO = 3

print(Nivel.MEDIO + 1)  # 4
print(Nivel.BAJO < Nivel.ALTO)  # True

# Flag (para组合)
class Permisos(Flag):
    LEER = auto()
    ESCRIBIR = auto()
    EJECUTAR = auto()

LECTURA_Y_ESCRITURA = Permisos.LEER | Permisos.ESCRIBIR
print(LECTURA_Y_ESCRITURA)
print(bool(LECTURA_Y_ESCRITURA & Permisos.LEER))  # True

# Enum con métodos
class Estado(Enum):
    PENDIENTE = "pendiente"
    PROCESANDO = "procesando"
    COMPLETADO = "completado"
    ERROR = "error"
    
    @property
    def es_final(self):
        return self in (self.COMPLETADO, self.ERROR)
    
    def __str__(self):
        return self.value

print(Estado.COMPLETADO.es_final)

"""
────────────────────────────────
EJERCICIO 213 - SLOTS OPTIMIZACIÓN
────────────────────────────────
Descripción: Optimiza memoria con __slots__.

Concepto: Evita __dict__ por instancia

Código:
"""
import sys

class SinSlots:
    def __init__(self, x):
        self.x = x

class ConSlots:
    __slots__ = ['x']
    def __init__(self, x):
        self.x = x

# Comparar tamaño
s1 = SinSlots(1)
s2 = ConSlots(1)

print(f"Sin slots: {sys.getsizeof(s1.__dict__)} bytes")
# Con slots no tiene __dict__
try:
    print(sys.getsizeof(s2.__dict__))
except:
    print("Con slots: no tiene __dict__")

# Agregar atributos dinámicamente
# s2.y = 2  # Error: no tiene 'y' en __slots__

# Slots con property
class ConSlotsProperty:
    __slots__ = ['_x']
    
    @property
    def x(self):
        return self._x
    
    @x.setter
    def x(self, valor):
        self._x = valor

obj = ConSlotsProperty()
obj.x = 10
print(obj.x)

# Slots y herencia
class Base:
    __slots__ = ['a']

class Derivada(Base):
    __slots__ = ['b']  # Combina con los del padre

d = Derivada()
d.a = 1
d.b = 2
# d.c = 3  # Error

"""
────────────────────────────────
EJERCICIO 214 - WEAKREF
────────────────────────────────
Descripción: Referencias débiles que no previenen garbage collection.

Concepto: Útil para cachés y callbacks

Código:
"""
import weakref

class MiClase:
    def __init__(self, nombre):
        self.nombre = nombre
    def __repr__(self):
        return f"MiClase({self.nombre})"

# Crear referencia débil
obj = MiClase("Referencia")
ref = weakref.ref(obj)

print(ref())  # MiClase(Referencia)

# Eliminar referencia fuerte
del obj
print(ref())  # None (objeto recolectado)

# WeakSet
ws = weakref.WeakSet()
obj1 = MiClase("A")
obj2 = MiClase("B")
ws.add(obj1)
ws.add(obj2)
print(list(ws))

del obj1
print(list(ws))  # Solo obj2

# WeakKeyDictionary
wd = weakref.WeakKeyDictionary()
obj = MiClase("Test")
wd[obj] = "valor"
print(wd[obj])

# Callback al eliminar
class ReferenciaConCallback:
    def __init__(self, nombre, callback):
        self.ref = weakref.ref(self, callback)
        self.nombre = nombre
    
    def __repr__(self):
        return f"Objeto({self.nombre})"

def cuando_se_borre(ref):
    print("Objeto eliminado!")

obj = ReferenciaConCallback("Temp", cuando_se_borra)
del obj  # Imprime "Objeto eliminado!"

"""
────────────────────────────────
EJERCICIO 215 - ABC AVANZADO
────────────────────────────────
Descripción: Clases abstractas avanzadas.

Concepto: register, abstractmethod, ABC

Código:
"""
from abc import ABC, abstractmethod

# ABC con abstractmethod
class Figura(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    # Método no abstracto
    def descripcion(self):
        return f"Figura con área {self.area()}"

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
    
    def area(self):
        return self.lado ** 2
    
    def perimetro(self):
        return 4 * self.lado

# No se puede instanciar Figura
# f = Figura()  # TypeError

# Se puede crear Cuadrado
c = Cuadrado(5)
print(c.area())
print(c.descripcion())

# Registrar clases (sin herencia)
class Triangulo:
    def area(self):
        return 0.5 * 3 * 4
    def perimetro(self):
        return 3 + 4 + 5

# Registrar como implementación
Figura.register(Triangulo)
t = Triangulo()
print(isinstance(t, Figura))  # True

# Propiedades abstractas
class Vehiculo(ABC):
    @property
    @abstractmethod
    def velocidad_maxima(self):
        pass

class Coche(Vehiculo):
    @property
    def velocidad_maxima(self):
        return 200

print(Coche().velocidad_maxima)

# ============================================================
#        EJERCICIOS 301-350: PATRONES DE DISEÑO
# ============================================================

"""
────────────────────────────────
EJERCICIO 216 - PATRÓN STRATEGY
────────────────────────────────
Descripción: Define familia de algoritmos intercambiables.

Concepto: Interfaz común para diferentes estrategias

Código:
"""
from abc import ABC, abstractmethod

class EstrategiaOrdenamiento(ABC):
    @abstractmethod
    def ordenar(self, datos):
        pass

class OrdenamientoBurbuja(EstrategiaOrdenamiento):
    def ordenar(self, datos):
        datos = datos.copy()
        n = len(datos)
        for i in range(n):
            for j in range(0, n - i - 1):
                if datos[j] > datos[j + 1]:
                    datos[j], datos[j + 1] = datos[j + 1], datos[j]
        return datos

class OrdenamientoRapido(EstrategiaOrdenamiento):
    def ordenar(self, datos):
        return sorted(datos)  # Usar sorted para simplificar

class Contexto:
    def __init__(self, estrategia):
        self.estrategia = estrategia
    
    def ejecutar(self, datos):
        return self.estrategia.ordenar(datos)
    
    def cambiar_estrategia(self, estrategia):
        self.estrategia = estrategia

datos = [5, 2, 8, 1, 9]

contexto = Contexto(OrdenamientoBurbuja())
print(contexto.ejecutar(datos))

contexto.cambiar_estrategia(OrdenamientoRapido())
print(contexto.ejecutar(datos))

"""
────────────────────────────────
EJERCICIO 217 - PATRÓN DECORATOR
────────────────────────────────
Descripción: Agrega funcionalidad dinámicamente.

Concepto: Envolver objetos sin modificar su clase

Código:
"""
# Decorator pattern real
class Cafe:
    def costo(self):
        return 5
    
    def descripcion(self):
        return "Café básico"

class DecoratorCafe(ABC):
    @abstractmethod
    def costo(self):
        pass
    
    @abstractmethod
    def descripcion(self):
        pass

class ConLeche(DecoratorCafe):
    def __init__(self, cafe):
        self._cafe = cafe
    
    def costo(self):
        return self._cafe.costo() + 1.5
    
    def descripcion(self):
        return self._cafe.descripcion() + ", leche"

class ConAzucar(DecoratorCafe):
    def __init__(self, cafe):
        self._cafe = cafe
    
    def costo(self):
        return self._cafe.costo() + 0.5
    
    def descripcion(self):
        return self._cafe.descripcion() + ", azúcar"

# Uso
cafe = Cafe()
cafe = ConLeche(cafe)
cafe = ConAzucar(cafe)
print(f"{cafe.descripcion()}: ${cafe.costo()}")

"""
────────────────────────────────
EJERCICIO 218 - PATRÓN ADAPTER
────────────────────────────────
Descripción: Convierte interfaz de una clase en otra.

Concepto: Hacer compatible lo incompatible

Código:
"""
# Clase existente con interfaz diferente
class SistemaLegacy:
    def procesar_datos_legacy(self, datos):
        return f"Procesado: {datos.upper()}"

# Nueva interfaz esperada
class InterfazNueva:
    def procesar(self, datos):
        pass

# Adapter
class Adapter(InterfazNueva):
    def __init__(self):
        self._legacy = SistemaLegacy()
    
    def procesar(self, datos):
        return self._legacy.procesar_datos_legacy(datos)

# Uso
nueva_interfaz = Adapter()
print(nueva_interfaz.procesar("hello"))

# Multiple inheritance adapter
class InterfazA:
    def metodo_a(self):
        pass

class InterfazB:
    def metodo_b(self):
        pass

class AdapterMultiple(InterfazA, InterfazB):
    def metodo_a(self):
        return "A"
    
    def metodo_b(self):
        return "B"

"""
────────────────────────────────
EJERCICIO 219 - PATRÓN FACADE
────────────────────────────────
Descripción: Interfaz simplificada para sistema complejo.

Concepto: Ocultar complejidad detrás de interfaz simple

Código:
"""
# Subsistemas complejos
class CPU:
    def freeze(self): pass
    def jump(self, posicion): pass
    def execute(self): pass

class Memoria:
    def load(self, posicion, datos): pass

class Disco:
    def read(self, sector, tamaño): pass

# Facade
class Computadora:
    def __init__(self):
        self.cpu = CPU()
        self.memoria = Memoria()
        self.disco = Disco()
    
    def iniciar(self):
        self.cpu.freeze()
        self.memoria.load(0, self.disco.read(0, 1024))
        self.cpu.jump(0)
        self.cpu.execute()
        print("Computadora iniciada")
    
    def apagar(self):
        print("Computadora apagada")

# Uso simple
computadora = Computadora()
computadora.iniciar()
computadora.apagar()

"""
────────────────────────────────
EJERCICIO 220 - PATRÓN BUILDER
────────────────────────────────
Descripción: Construye objetos complejos paso a paso.

Concepto: Separa construcción de representación

Código:
"""
class ConstructorPizza:
    def __init__(self):
        self.pizza = Pizza()
    
    def set_tamaño(self, tamaño):
        self.pizza.tamaño = tamaño
        return self
    
    def set_masa(self, masa):
        self.pizza.masa = masa
        return self
    
    def agregar_ingrediente(self, ingrediente):
        self.pizza.ingredientes.append(ingrediente)
        return self
    
    def build(self):
        return self.pizza

class Pizza:
    def __init__(self):
        self.tamaño = None
        self.masa = None
        self.ingredientes = []
    
    def __str__(self):
        return f"Pizza {self.tamaño} con masa {self.masa}: {', '.join(self.ingredientes)}"

# Uso
pizza = (PizzaBuilder()
    .set_tamaño("grande")
    .set_masa("integral")
    .agregar_ingrediente("queso")
    .agregar_ingrediente("tomate")
    .agregar_ingrediente("jamón")
    .build())

print(pizza)

# Director (opcional)
class Director:
    def construir_pizza_clasica(self):
        return (PizzaBuilder()
            .set_tamaño("mediana")
            .set_masa("tradicional")
            .agregar_ingrediente("queso")
            .agregar_ingrediente("tomate")
            .build())

director = Director()
print(director.construir_pizza_clasica())

"""
────────────────────────────────
EJERCICIO 221 - PATRÓN PROTOTYPE
────────────────────────────────
Descripción: Crea objetos clonando prototipos.

Concepto: Clonar en lugar de crear nuevo

Código:
"""
import copy

class Prototipo(ABC):
    def __init__(self):
        pass
    
    @abstractmethod
    def clonar(self):
        pass

class Documento(Prototipo):
    def __init__(self, titulo, contenido):
        self.titulo = titulo
        self.contenido = contenido
    
    def clonar(self):
        return copy.deepcopy(self)
    
    def __str__(self):
        return f"Documento: {self.titulo}"

# Registro de prototipos
class RegistroPrototipos:
    def __init__(self):
        self._prototipos = {}
    
    def registrar(self, nombre, prototipo):
        self._prototipos[nombre] = prototipo
    
    def clonar(self, nombre):
        return self._prototipos[nombre].clonar()

# Uso
original = Documento("Original", "Contenido original")
registro = RegistroPrototipos()
registro.registrar("doc1", original)

clon = registro.clonar("doc1")
clon.titulo = "Clon"

print(original)
print(clon)

"""
────────────────────────────────
EJERCICIO 222 - PATRÓN STATE
────────────────────────────────
Descripción: Objeto cambia comportamiento según estado.

Concepto: Máquina de estados

Código:
"""
class Estado(ABC):
    @abstractmethod
    def manejar(self, contexto):
        pass

class EstadoEncendido(Estado):
    def manejar(self, contexto):
        print("El sistema ya estáendido")
        contexto.estado = EstadoApagado()

class EstadoApagado(Estado):
    def manejar(self, contexto):
        print("Encendiendo sistema...")
        contexto.estado = EstadoEncendido()

class Contexto:
    def __init__(self):
        self.estado = EstadoApagado()
    
    def pulsar_boton(self):
        self.estado.manejar(self)

contexto = Contexto()
contexto.pulsar_boton()  # Encendiendo
contexto.pulsar_boton()  # Ya estáendido
contexto.pulsar_boton()  # Apagando

# Ejemplo más completo: Reproductor
class EstadoReproduciendo:
    def play(self, reproductor):
        print("Ya está reproduciendo")
    
    def pause(self, reproductor):
        print("Pausando")
        reproductor.estado = reproductor.estado_pausa
    
    def stop(self, reproductor):
        print("Deteniendo")
        reproductor.estado = reproductor.estado_detenido

class EstadoPausa:
    def play(self, reproductor):
        print("Reproduciendo")
        reproductor.estado = reproductor.estado_reproduciendo
    
    def pause(self, reproductor):
        print("Ya está en pausa")
    
    def stop(self, reproductor):
        print("Deteniendo")
        reproductor.estado = reproductor.estado_detenido

class EstadoDetenido:
    def play(self, reproductor):
        print("Iniciando reproducción")
        reproductor.estado = reproductor.estado_reproduciendo
    
    def pause(self, reproductor):
        print("No hay nada en pausa")
    
    def stop(self, reproductor):
        print("Ya está detenido")

class Reproductor:
    def __init__(self):
        self.estado_reproduciendo = EstadoReproduciendo()
        self.estado_pausa = EstadoPausa()
        self.estado_detenido = EstadoDetenido()
        self.estado = self.estado_detenido
    
    def play(self):
        self.estado.play(self)
    
    def pause(self):
        self.estado.pause(self)
    
    def stop(self):
        self.estado.stop(self)

reproductor = Reproductor()
reproductor.play()  # Iniciando
reproductor.pause()  # Pausando
reproductor.play()  # Reproduciendo

"""
────────────────────────────────
EJERCICIO 223 - PATRÓN TEMPLATE METHOD
────────────────────────────────
Descripción: Define esqueleto de algoritmo.

Concepto: subclases redefinen pasos específicos

Código:
"""
class Abstracta(ABC):
    def template_method(self):
        self.paso1()
        self.paso2()
        self.paso3()
    
    def paso1(self):
        pass
    
    @abstractmethod
    def paso2(self):
        pass
    
    @abstractmethod
    def paso3(self):
        pass

class Concreta(Abstracta):
    def paso2(self):
        print("Implementación paso 2")
    
    def paso3(self):
        print("Implementación paso 3")

# Uso
c = Concreta()
c.template_method()

# Ejemplo: Preparar bebidas
class BebidaCaliente:
    def preparar(self):
        self.hervir_agua()
        self.agregar_ingrediente()
        self.verter_en_taza()
        self.agregar_extras()
    
    def hervir_agua(self):
        print("Hirviendo agua")
    
    @abstractmethod
    def agregar_ingrediente(self):
        pass
    
    def verter_en_taza(self):
        print("Vertiendo en taza")
    
    def agregar_extras(self):
        pass

class Cafe(BebidaCaliente):
    def agregar_ingrediente(self):
        print("Agregando café")

class Te(BebidaCaliente):
    def agregar_ingrediente(self):
        print("Agregando té")
    
    def agregar_extras(self):
        print("Agregando limón")

Cafe().preparar()
print()
Te().preparar()

"""
────────────────────────────────
EJERCICIO 224 - PATRÓN VISITOR
────────────────────────────────
Descripción: Separa algoritmos de objetos.

Concepto: Visitar elementos y realizar operaciones

Código:
"""
# Elementos
class Elemento(ABC):
    @abstractmethod
    def aceptar(self, visitor):
        pass

class ElementoA(Elemento):
    def aceptar(self, visitor):
        return visitor.visitar_elemento_a(self)
    
    def operacion_a(self):
        return "ElementoA"

class ElementoB(Elemento):
    def aceptar(self, visitor):
        return visitor.visitar_elemento_b(self)
    
    def operacion_b(self):
        return "ElementoB"

# Visitor
class Visitor(ABC):
    @abstractmethod
    def visitar_elemento_a(self, elemento):
        pass
    
    @abstractmethod
    def visitar_elemento_b(self, elemento):
        pass

class ConcreteVisitor(Visitor):
    def visitar_elemento_a(self, elemento):
        return f"Visitor procesa {elemento.operacion_a()}"
    
    def visitar_elemento_b(self, elemento):
        return f"Visitor procesa {elemento.operacion_b()}"

# Uso
elementos = [ElementoA(), ElementoB()]
visitor = ConcreteVisitor()

for elemento in elementos:
    print(elemento.aceptar(visitor))

"""
────────────────────────────────
EJERCICIO 225 - PATRÓN INTERPRETER
────────────────────────────────
Descripción: Interpreta lenguaje o expresiones.

Concepto: Representar gramática y evaluar

Código:
"""
# Expresión base
class Expresion(ABC):
    @abstractmethod
    def interpretar(self, contexto):
        pass

class Numero(Expresion):
    def __init__(self, valor):
        self.valor = int(valor)
    
    def interpretar(self, contexto):
        return self.valor

class Sumar(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha
    
    def interpretar(self, contexto):
        return self.izquierda.interpretar(contexto) + self.derecha.interpretar(contexto)

class Restar(Expresion):
    def __init__(self, izquierda, derecha):
        self.izquierda = izquierda
        self.derecha = derecha
    
    def interpretar(self, contexto):
        return self.izquierda.interpretar(contexto) - self.derecha.interpretar(contexto)

# "(5 + 3) - 2"
expresion = Restar(
    Sumar(Numero(5), Numero(3)),
    Numero(2)
)

print(expresion.interpretar({}))  # 6

# ============================================================
#        EJERCICIOS 351-400: CASOS DE USO AVANZADOS
# ============================================================

"""
────────────────────────────────
EJERCICIO 226 - CLASEGENÉRICA CON BOUNDS
────────────────────────────────
Descripción: Genéricos con restricciones.

Concepto: TypeVar con bound

Código:
"""
from typing import TypeVar, Generic

# TypeVar básico
T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: list[T] = []
    
    def push(self, item: T):
        self.elementos.append(item)
    
    def pop(self) -> T:
        return self.elementos.pop()

pila_int: Pila[int] = Pila()
pila_int.push(1)

pila_str: Pila[str] = Pila()
pila_str.push("hola")

# Con bound (restricción)
Num = TypeVar('Num', int, float)

class Calculadora(Generic[Num]):
    def __init__(self, valor: Num):
        self.valor = valor
    
    def duplicar(self) -> Num:
        return self.valor * 2

calc_int = Calculadora(5)
print(calc_int.duplicar())

calc_float = Calculadora(3.5)
print(calc_float.duplicar())

# Multiple TypeVars
K = TypeVar('K')
V = TypeVar('V')

class Diccionario(Generic[K, V]):
    def __init__(self):
        self.datos: dict[K, V] = {}
    
    def set(self, key: K, value: V):
        self.datos[key] = value
    
    def get(self, key: K) -> V:
        return self.datos[key]

d: Diccionario[str, int] = Diccionario()
d.set("edad", 30)

"""
────────────────────────────────
EJERCICIO 227 - CONTEXTLIB AVANZADO
────────────────────────────────
Descripción: Utilidades de contexto avanzadas.

Concepto: @contextmanager, closing, suppress

Código:
"""
from contextlib import contextmanager, suppress, closing, nullcontext

# @contextmanager
@contextmanager
def transaccion(db):
    print("Iniciando transacción")
    try:
        yield "conexión"
        print("Confirmando")
    except Exception:
        print("Revirtiendo")
        raise
    finally:
        print("Cerrando")

with transaccion() as conn:
    print(f"Usando {conn}")

# suppress - ignora excepciones específicas
with suppress(FileNotFoundError):
    open("noexiste.txt").read()

# closing
with closing(open("test.txt", "w")) as f:
    f.write("test")

# nullcontext
valor = nullcontext(42).enter_context()
print(valor)

# redirect_stdout
from contextlib import redirect_stdout
import io

f = io.StringIO()
with redirect_stdout(f):
    print("Hola")
print(f.getvalue())

"""
────────────────────────────────
EJERCICIO 228 - CALLABLE Y METACLASES
────────────────────────────────
Descripción: Objetos callable y metaclases.

Concepto: __call__, metaclass

Código:
"""
# Callable - hacer que objeto se llame como función
class Multiplicador:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, valor):
        return valor * self.factor

x = Multiplicador(3)
print(x(10))  # 30
print(callable(x))  # True

# Crear callable con lambda
class Sumador:
    def __init__(self, inicial):
        self.total = inicial
    
    def __call__(self, valor):
        self.total += valor
        return self.total

sumador = Sumador(10)
print(sumador(5))  # 15
print(sumador(3))  # 18

# Metaclase que hace todas las clases callable
class CallableMeta(type):
    def __call__(cls, *args, **kwargs):
        print(f"Creando instancia de {cls.__name__}")
        return super().__call__(*args, **kwargs)

class MiClase(metaclass=CallableMeta):
    def __init__(self, valor):
        self.valor = valor

obj = MiClase(42)
print(obj.valor)

"""
────────────────────────────────
EJERCICIO 229 - IMPORLIB Y DYNAMIC IMPORT
────────────────────────────────
Descripción: Importar módulos dinámicamente.

Concepto: importlib, __import__

Código:
"""
import importlib

# Importar por nombre de string
modulo = importlib.import_module("math")
print(modulo.sqrt(16))

# Importar desde subpaquete
import json
# equivalente a: from json import loads
loads = importlib.import_module("json").loads

# Recargar módulo
import time
importlib.reload(time)

# Obtener atributos
math = importlib.import_module("math")
print(getattr(math, 'pi'))

# Intentar importar (manejar errores)
def importar_seguro(nombre):
    try:
        return importlib.import_module(nombre)
    except ImportError as e:
        print(f"No se pudo importar {nombre}: {e}")
        return None

math = importar_seguro("math")
numpy = importar_seguro("numpy")

# Dynamic import con from
spec = importlib.util.find_spec("os")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
print(module.getcwd())

"""
────────────────────────────────
EJERCICIO 230 - INSPECT MODULE
────────────────────────────────
Descripción: Inspectionar código en tiempo de ejecución.

Concepto: introspección de funciones, clases, módulos

Código:
"""
import inspect

def mi_funcion(a, b, c=10):
    """Función de ejemplo"""
    return a + b + c

# Información de función
print(inspect.signature(mi_funcion))
print(mi_funcion.__doc__)
print(inspect.getsource(mi_funcion))

# Ver parámetros
sig = inspect.signature(mi_funcion)
for nombre, param in sig.parameters.items():
    print(f"{nombre}: {param.default}")

# Clases
class MiClase:
    def __init__(self, x):
        self.x = x
    
    def metodo(self):
        pass

print(inspect.getmembers(MiClase, inspect.isfunction))
print(inspect.getmembers(MiClase, inspect.ismethod))

# Verificar si es generador
def gen():
    yield 1

print(inspect.isgeneratorfunction(gen))

# Stack y frame
def funcion_a():
    return funcion_b()

def funcion_b():
    for frame_info in inspect.stack():
        print(frame_info.function)

funcion_a()

# ============================================================
#        EJERCICIOS 401-450: PRACTICA INTEGRADORA
# ============================================================

"""
────────────────────────────────
EJERCICIO 231 - CRUD COMPLETO CON CLASES
────────────────────────────────
Descripción: Sistema CRUD completo.

Concepto: Create, Read, Update, Delete

Código:
"""
from dataclasses import dataclass, field
from typing import Optional, List
from datetime import datetime
import json

@dataclass
class Entidad:
    id: int
    
class Persona(Entidad):
    def __init__(self, id: int, nombre: str, email: str):
        super().__init__(id)
        self.nombre = nombre
        self.email = email
    
    def to_dict(self):
        return {"id": self.id, "nombre": self.nombre, "email": self.email}

class Repositorio:
    def __init__(self):
        self._datos: dict[int, Persona] = {}
        self._next_id = 1
    
    def crear(self, nombre: str, email: str) -> Persona:
        persona = Persona(self._next_id, nombre, email)
        self._datos[self._next_id] = persona
        self._next_id += 1
        return persona
    
    def leer(self, id: int) -> Optional[Persona]:
        return self._datos.get(id)
    
    def leer_todos(self) -> List[Persona]:
        return list(self._datos.values())
    
    def actualizar(self, id: int, nombre: str = None, email: str = None) -> Optional[Persona]:
        persona = self._datos.get(id)
        if persona:
            if nombre:
                persona.nombre = nombre
            if email:
                persona.email = email
        return persona
    
    def eliminar(self, id: int) -> bool:
        if id in self._datos:
            del self._datos[id]
            return True
        return False
    
    def guardar_archivo(self, filename: str):
        with open(filename, 'w') as f:
            json.dump([p.to_dict() for p in self._datos.values()], f)
    
    def cargar_archivo(self, filename: str):
        with open(filename, 'r') as f:
            datos = json.load(f)
            self._datos = {d['id']: Persona(d['id'], d['nombre'], d['email']) for d in datos}
            self._next_id = max(self._datos.keys()) + 1 if self._datos else 1

# Uso
repo = Repositorio()
repo.crear("Juan", "juan@email.com")
repo.crear("Ana", "ana@email.com")

print(repo.leer_todos())
repo.actualizar(1, email="juan@nuevo.com")
print(repo.leer(1))
repo.eliminar(2)
print(repo.leer_todos())

"""
────────────────────────────────
EJERCICIO 232 - PIPELINE DE DATOS
────────────────────────────────
Descripción: Pipeline de procesamiento de datos.

Concepto: Chain de transformaciones

Código:
"""
from typing import Callable, Any, List
from dataclasses import dataclass

@dataclass
class Dato:
    valor: Any
    metadatos: dict = field(default_factory=dict)

class Pipeline:
    def __init__(self):
        self.pasos: List[Callable] = []
    
    def agregar_paso(self, funcion: Callable):
        self.pasos.append(funcion)
        return self  # Para encadenar
    
    def ejecutar(self, dato: Dato) -> Dato:
        resultado = dato
        for paso in self.pasos:
            resultado = paso(resulto)
        return resultado

# Definir pasos
def validar(dato: Dato) -> Dato:
    if not dato.valor:
        raise ValueError("Valor no puede ser vacío")
    return dato

def normalizar(dato: Dato) -> Dato:
    if isinstance(dato.valor, str):
        dato.valor = dato.valor.strip().lower()
    return dato

def agregar_timestamp(dato: Dato) -> Dato:
    from datetime import datetime
    dato.metadatos['timestamp'] = datetime.now()
    return dato

def enriquecer(dato: Dato) -> Dato:
    if isinstance(dato.valor, str):
        dato.metadatos['longitud'] = len(dato.valor)
    return dato

# Ejecutar pipeline
pipeline = Pipeline()
pipeline.agregar_paso(validar).agregar_paso(normalizar).agregar_paso(agregar_timestamp).agregar_paso(enriquecer)

dato = Dato("  Hola Mundo  ")
resultado = pipeline.ejecutar(dato)

print(f"Valor: {resultado.valor}")
print(f"Metadatos: {resultado.metadatos}")

"""
────────────────────────────────
EJERCICIO 233 - CACHE CON LRU
────────────────────────────────
Descripción: Sistema de caché con LRU.

Concepto: Least Recently Used

Código:
"""
from collections import OrderedDict
from typing import Any, Optional
import time

class CacheLRU:
    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.cache: OrderedDict = OrderedDict()
    
    def get(self, clave: str) -> Optional[Any]:
        if clave not in self.cache:
            return None
        # Mover al final (más reciente)
        self.cache.move_to_end(clave)
        return self.cache[clave]
    
    def put(self, clave: str, valor: Any):
        if clave in self.cache:
            self.cache.move_to_end(clave)
        else:
            if len(self.cache) >= self.capacidad:
                # Eliminar el menos reciente (primero)
                self.cache.popitem(last=False)
        
        self.cache[clave] = valor
    
    def __contains__(self, clave: str) -> bool:
        return clave in self.cache
    
    def __len__(self):
        return len(self.cache)

# Uso
cache = CacheLRU(3)
cache.put("a", 1)
cache.put("b", 2)
cache.put("c", 3)

print(cache.get("a"))  # 1
cache.put("d", 4)  # Expulsa "b"
print(cache.get("b"))  # None

# Decorador con caché
def memoize(func):
    cache = CacheLRU(100)
    
    def wrapper(*args):
        clave = str(args)
        resultado = cache.get(clave)
        if resultado is None:
            resultado = func(*args)
            cache.put(clave, resultado)
        return resultado
    
    return wrapper

@memoize
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Rápido por memoización

"""
────────────────────────────────
EJERCICIO 234 - VALIDATOR GENÉRICO
────────────────────────────────
Descripción: Validador genérico de datos.

Concepto: Chain de validadores

Código:
"""
from typing import Callable, Any, List
from dataclasses import dataclass, field

@dataclass
class ResultadoValidacion:
    valido: bool
    errores: List[str] = field(default_factory=list)

class Validador:
    def __init__(self):
        self.validadores: List[Callable] = []
    
    def agregar(self, validador: Callable[[Any], bool], mensaje: str):
        def wrapper(valor):
            return(validador(valor), mensaje)
        self.validadores.append(wrapper)
        return self
    
    def validar(self, valor: Any) -> ResultadoValidacion:
        errores = []
        for validador in self.validadores:
            es_valido, mensaje = validador(valor)
            if not es_valido:
                errores.append(mensaje)
        
        return ResultadoValidacion(len(errores) == 0, errores)

# Validadores predefinidos
class Validators:
    @staticmethod
    def no_vacio(valor):
        return valor is not None and valor != "", "No puede estar vacío"
    
    @staticmethod
    def min_longitud(n):
        def validator(valor):
            return len(str(valor)) >= n, f"Mínimo {n} caracteres"
        return validator
    
    @staticmethod
    def max_longitud(n):
        def validator(valor):
            return len(str(valor)) <= n, f"Máximo {n} caracteres"
        return validator
    
    @staticmethod
    def rango(minimo, maximo):
        def validator(valor):
            return minimo <= valor <= maximo, f"Debe estar entre {minimo} y {maximo}"
        return validator
    
    @staticmethod
    def email(valor):
        import re
        patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(patron, valor), "Email inválido"

# Uso
validador = Validador()
validador.agregar(Validators.no_vacio, "Nombre requerido")
validador.agregar(Validators.min_longitud(3), "Nombre muy corto")
validador.agregar(Validators.max_longitud(50), "Nombre muy largo")

resultado = validador.validar("")
print(resultado.valido, resultado.errores)

resultado = validador.validar("Jo")
print(resultado.valido, resultado.errores)

resultado = validador.validar("Juan Pérez")
print(resultado.valido, resultado.errores)

"""
────────────────────────────────
EJERCICIO 235 - EVENT EMITTER
────────────────────────────────
Descripción: Sistema de eventos.

Concepto: Pub/Sub con manejo de eventos

Código:
"""
from typing import Callable, List, Dict
from dataclasses import dataclass, field

@dataclass
class Evento:
    nombre: str
    datos: dict = field(default_factory=dict)

class EventEmitter:
    def __init__(self):
        self._events: Dict[str, List[Callable]] = {}
    
    def on(self, evento: str, callback: Callable):
        if evento not in self._events:
            self._events[evento] = []
        self._events[evento].append(callback)
        return self
    
    def once(self, evento: str, callback: Callable):
        def wrapper(*args, **kwargs):
            callback(*args, **kwargs)
            self.off(evento, wrapper)
        return self.on(evento, wrapper)
    
    def off(self, evento: str, callback: Callable):
        if evento in self._events:
            self._events[evento] = [cb for cb in self._events[evento] if cb != callback]
    
    def emit(self, evento: str, **datos):
        if evento in self._events:
            evento_obj = Evento(evento, datos)
            for callback in self._events[evento]:
                callback(evento_obj)
    
    def remove_all_listeners(self, evento: str = None):
        if evento:
            self._events[evento] = []
        else:
            self._events = {}

# Uso
emisor = EventEmitter()

def on_usuario_creado(evento):
    print(f"Usuario creado: {evento.datos['nombre']}")

def on_login(evento):
    print(f"Login: {evento.datos['usuario']}")

emisor.on("usuario.creado", on_usuario_creado).on("login", on_login)

emisor.emit("usuario.creado", nombre="Juan")
emisor.emit("login", usuario="juan@email.com")

# Uno solo
emisor.once("visita", lambda e: print(f"Primera visita: {e.datos}"))
emisor.emit("visita", pagina="/home")
emisor.emit("visita", pagina="/about")

"""
────────────────────────────────
EJERCICIO 236 - PATRÓN REPOSITORY
────────────────────────────────
Descripción: Abstrae acceso a datos.

Concepto: Interfaz entre lógica de negocio y datos

Código:
"""
from abc import ABC, abstractmethod
from typing import List, Optional, Any
from dataclasses import dataclass

@dataclass
class Entidad:
    id: int

# Entidad concreta
class Producto(Entidad):
    def __init__(self, id: int, nombre: str, precio: float):
        super().__init__(id)
        self.nombre = nombre
        self.precio = precio

# Interfaz repositorio
class Repositorio(ABC):
    @abstractmethod
    def obtener_todos(self) -> List[Entidad]:
        pass
    
    @abstractmethod
    def obtener_por_id(self, id: int) -> Optional[Entidad]:
        pass
    
    @abstractmethod
    def guardar(self, entidad: Entidad) -> Entidad:
        pass
    
    @abstractmethod
    def eliminar(self, id: int) -> bool:
        pass

# Implementación en memoria
class RepositorioMemoria(Repositorio):
    def __init__(self):
        self._datos: dict[int, Entidad] = {}
        self._next_id = 1
    
    def obtener_todos(self) -> List[Entidad]:
        return list(self._datos.values())
    
    def obtener_por_id(self, id: int) -> Optional[Entidad]:
        return self._datos.get(id)
    
    def guardar(self, entidad: Entidad) -> Entidad:
        if entidad.id == 0:
            entidad.id = self._next_id
            self._next_id += 1
        self._datos[entidad.id] = entidad
        return entidad
    
    def eliminar(self, id: int) -> bool:
        if id in self._datos:
            del self._datos[id]
            return True
        return False

# Servicio que usa repositorio
class ServicioProducto:
    def __init__(self, repositorio: Repositorio):
        self._repo = repositorio
    
    def listar_productos(self):
        return self._repo.obtener_todos()
    
    def buscar_producto(self, id: int):
        return self._repo.obtener_por_id(id)
    
    def crear_producto(self, nombre: str, precio: float):
        producto = Producto(0, nombre, precio)
        return self._repo.guardar(producto)

# Uso
repo = RepositorioMemoria()
servicio = ServicioProducto(repo)

servicio.crear_producto("Laptop", 999)
servicio.crear_producto("Mouse", 25)

print(servicio.listar_productos())

"""
────────────────────────────────
EJERCICIO 237 - SERIALIZACIÓN CUSTOM
────────────────────────────────
Descripción: Serialización personalizada de objetos.

Concepto: JSONEncoder, __getstate__, __setstate__

Código:
"""
import json
from datetime import datetime, date

# JSON Encoder personalizado
class CustomEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return {"__datetime__": obj.isoformat()}
        if isinstance(obj, date):
            return {"__date__": obj.isoformat()}
        if isinstance(obj, set):
            return {"__set__": list(obj)}
        return super().default(obj)

def custom_decoder(dct):
    if "__datetime__" in dct:
        return datetime.fromisoformat(dct["__datetime__"])
    if "__date__" in dct:
        return date.fromisoformat(dct["__date__"])
    if "__set__" in dct:
        return set(dct["__set__"])
    return dct

# Uso
data = {
    "nombre": "Juan",
    "fecha": datetime.now(),
    "etiquetas": {"python", "programación"}
}

json_str = json.dumps(data, cls=CustomEncoder)
print(json_str)

data_decoded = json.loads(json_str, object_hook=custom_decoder)
print(data_decoded)

# Con pickle y __getstate__/__setstate__
class MiObjeto:
    def __init__(self, valor):
        self.valor = valor
        self._cache = {}
    
    def __getstate__(self):
        # Solo serializar lo necesario
        return {"valor": self.valor}
    
    def __setstate__(self, state):
        self.valor = state["valor"]
        self._cache = {}  # Inicializar cache

import pickle
obj = MiObjeto(42)
pickle_str = pickle.dumps(obj)
obj2 = pickle.loads(pickle_str)
print(obj2.valor)

"""
────────────────────────────────
EJERCICIO 238 - PATRÓN CHAIN OF RESPONSIBILITY
────────────────────────────────
Descripción: Pasa solicitud por cadena de manejadores.

Concepto: Cada manejador decide procesar o pasar

Código:
"""
from abc import ABC, abstractmethod
from typing import Any

class Manejador(ABC):
    def __init__(self):
        self.siguiente: Manejador = None
    
    def set_siguiente(self, manejador):
        self.siguiente = manejador
        return manejador
    
    def manejar(self, solicitud):
        if self.puede_manejar(solicitud):
            return self.procesar(solicitud)
        elif self.siguiente:
            return self.siguiente.manejar(solicitud)
        return None
    
    @abstractmethod
    def puede_manejar(self, solicitud) -> bool:
        pass
    
    @abstractmethod
    def procesar(self, solicitud):
        pass

class ManejadorAutenticacion(Manejador):
    def puede_manejar(self, solicitud):
        return "token" in solicitud
    
    def procesar(self, solicitud):
        return f"Autenticado: {solicitud['token']}"

class ManejadorAutorizacion(Manejador):
    def puede_manejar(self, solicitud):
        return "permiso" in solicitud
    
    def procesar(self, solicitud):
        return f"Autorizado: {solicitud['permiso']}"

class ManejadorValidacion(Manejador):
    def puede_manejar(self, solicitud):
        return "datos" in solicitud
    
    def procesar(self, solicitud):
        return f"Datos validados: {solicitud['datos']}"

# Uso
cadena = ManejadorAutenticacion()
cadena.set_siguiente(ManejadorValidacion()).set_siguiente(ManejadorAutorizacion())

print(cadena.manejar({"token": "abc123"}))
print(cadena.manejar({"datos": "información"}))
print(cadena.manejar({"permiso": "admin"}))

"""
────────────────────────────────
EJERCICIO 239 - FÁBRICA ABSTRACTA
────────────────────────────────
Descripción: Crea familias de objetos relacionados.

Concepto: Interfaz para crear familias de objetos

Código:
"""
from abc import ABC, abstractmethod

# Productos abstractos
class Boton(ABC):
    @abstractmethod
    def render(self):
        pass

class Input(ABC):
    @abstractmethod
    def render(self):
        pass

# Productos concretos - Windows
class WindowsBoton(Boton):
    def render(self):
        return "Boton estilo Windows"

class WindowsInput(Input):
    def render(self):
        return "Input estilo Windows"

# Productos concretos - Mac
class MacBoton(Boton):
    def render(self):
        return "Boton estilo Mac"

class MacInput(Input):
    def render(self):
        return "Input estilo Mac"

# Fabrica abstracta
class FabricaUI(ABC):
    @abstractmethod
    def crear_boton(self) -> Boton:
        pass
    
    @abstractmethod
    def crear_input(self) -> Input:
        pass

# Fabricas concretas
class FabricaWindows(FabricaUI):
    def crear_boton(self) -> Boton:
        return WindowsBoton()
    
    def crear_input(self) -> Input:
        return WindowsInput()

class FabricaMac(FabricaUI):
    def crear_boton(self) -> Boton:
        return MacBoton()
    
    def crear_input(self) -> Input:
        return MacInput()

# Cliente
def crear_ui(fabrica: FabricaUI):
    boton = fabrica.crear_boton()
    input = fabrica.crear_input()
    return {"boton": boton.render(), "input": input.render()}

# Uso
print(crear_ui(FabricaWindows()))
print(crear_ui(FabricaMac()))

"""
────────────────────────────────
EJERCICIO 240 - PROXY
────────────────────────────────
Descripción: Controla acceso a objeto.

Concepto: Surrogate o placeholder

Código:
"""
from abc import ABC, abstractmethod

class Recurso(ABC):
    @abstractmethod
    def acceder(self):
        pass

class RecursoReal(Recurso):
    def __init__(self, archivo):
        self.archivo = archivo
        print(f"Cargando recurso: {archivo}")
    
    def acceder(self):
        return f"Contenido de {self.archivo}"

class ProxyRecurso(Recurso):
    def __init__(self, archivo):
        self.archivo = archivo
        self._recurso_real = None
    
    def acceder(self):
        if not self._recurso_real:
            self._recurso_real = RecursoReal(self.archivo)
        return self._recurso_real.acceder()

# Proxy con control de acceso
class RecursoProtegido(Recurso):
    def __init__(self, archivo, usuario):
        self.archivo = archivo
        self.usuario = usuario
        self._recurso = None
    
    def _verificar_permisos(self):
        return self.usuario in ["admin", "propietario"]
    
    def acceder(self):
        if self._verificar_permisos():
            if not self._recurso:
                self._recurso = RecursoReal(self.archivo)
            return self._recurso.acceder()
        return "Acceso denegado"

# Uso
proxy = ProxyRecurso("documento.txt")
print(proxy.acceder())
print(proxy.acceder())  # No vuelve a cargar

print(RecursoProtegido("secreto.txt", "admin").acceder())
print(RecursoProtegido("secreto.txt", "invitado").acceder())

# ============================================================
#        EJERCICIOS 450-500: PROYECTOS INTEGRADORES
# ============================================================

"""
────────────────────────────────
EJERCICIO 241 - MICROSERVICIO SIMPLE
────────────────────────────────
Descripción: Estructura básica de microservicio.

Concepto: API con endpoints

Código:
"""
from http.server import HTTPServer, BaseHTTPRequestHandler
import json
from urllib.parse import urlparse

#simulación de base de datos
usuarios_db = {}

class MicroservicioHandler(BaseHTTPRequestHandler):
    def _send_json(self, status, data):
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())
    
    def do_GET(self):
        parsed = urlparse(self.path)
        
        if parsed.path == '/usuarios':
            self._send_json(200, {"usuarios": list(usuarios_db.values())})
        elif parsed.path.startswith('/usuarios/'):
            id = parsed.path.split('/')[-1]
            if id in usuarios_db:
                self._send_json(200, usuarios_db[id])
            else:
                self._send_json(404, {"error": "No encontrado"})
        else:
            self._send_json(404, {"error": "Ruta no encontrada"})
    
    def do_POST(self):
        if self.path == '/usuarios':
            length = int(self.headers['Content-Length'])
            body = self.rfile.read(length)
            data = json.loads(body)
            
            id = str(len(usuarios_db) + 1)
            data['id'] = id
            usuarios_db[id] = data
            
            self._send_json(201, data)
        else:
            self._send_json(404, {"error": "Ruta no encontrada"})
    
    def do_PUT(self):
        if self.path.startswith('/usuarios/'):
            id = self.path.split('/')[-1]
            if id in usuarios_db:
                length = int(self.headers['Content-Length'])
                body = self.rfile.read(length)
                data = json.loads(body)
                data['id'] = id
                usuarios_db[id] = data
                self._send_json(200, data)
            else:
                self._send_json(404, {"error": "No encontrado"})
    
    def do_DELETE(self):
        if self.path.startswith('/usuarios/'):
            id = self.path.split('/')[-1]
            if id in usuarios_db:
                del usuarios_db[id]
                self._send_json(200, {"mensaje": "Eliminado"})
            else:
                self._send_json(404, {"error": "No encontrado"})

# Iniciar servidor (descomenta para probar)
# server = HTTPServer(('localhost', 8080), MicroservicioHandler)
# print("Servidor en puerto 8080")
# server.serve_forever()

print("Microservicio definido")

"""
────────────────────────────────
EJERCICIO 242 - GAME LOOP BÁSICO
────────────────────────────────
Descripción: Motor de juego básico.

Concepto: Update, Draw, FPS control

Código:
"""
import time
from typing import Callable, List, Any
from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class Entidad:
    x: float = 0
    y: float = 0
    
    def update(self, dt: float):
        pass
    
    def draw(self):
        pass

@dataclass
class Jugador(Entidad):
    velocidad: float = 100
    
    def update(self, dt: float):
        # Simular movimiento
        self.x += self.velocidad * dt
    
    def draw(self):
        return f"Jugador en ({self.x:.1f}, {self.y:.1f})"

class MotorJuego:
    def __init__(self):
        self.entidades: List[Entidad] = []
        self.ejecutando = False
        self.fps = 60
        self.dt = 1.0 / self.fps
    
    def agregar_entidad(self, entidad: Entidad):
        self.entidades.append(entidad)
    
    def iniciar(self):
        self.ejecutando = True
    
    def detener(self):
        self.ejecutando = False
    
    def actualizar(self):
        for entidad in self.entidades:
            entidad.update(self.dt)
    
    def dibujar(self):
        resultados = []
        for entidad in self.entidades:
            resultados.append(entidad.draw())
        return resultados
    
    def ciclo_principal(self):
        ultimo_tiempo = time.time()
        cuadros = 0
        inicio = time.time()
        
        while self.ejecutando:
            tiempo_actual = time.time()
            self.dt = tiempo_actual - ultimo_tiempo
            ultimo_tiempo = tiempo_actual
            
            self.actualizar()
            resultados = self.dibujar()
            
            # Mostrar FPS cada segundo
            cuadros += 1
            if tiempo_actual - inicio >= 1.0:
                print(f"FPS: {cuadros}")
                cuadros = 0
                inicio = time.time()
            
            # Controlar FPS
            tiempo_procesamiento = time.time() - tiempo_actual
            if tiempo_procesamiento < self.dt:
                time.sleep(self.dt - tiempo_procesamiento)

# Uso
juego = MotorJuego()
juego.agregar_entidad(Jugador(x=10))
juego.iniciar()

print("Entidades:", juego.dibujar())

"""
────────────────────────────────
EJERCICIO 243 - ADMINISTRADOR DE TAREAS ASYNC
────────────────────────────────
Descripción: Gestor de tareas asíncronas.

Concepto: asyncio con múltiples tareas

Código:
"""
import asyncio
import random
from dataclasses import dataclass
from typing import List
from datetime import datetime
import uuid

@dataclass
class Tarea:
    id: str
    nombre: str
    duracion: int  # segundos
    completada: bool = False
    
    async def ejecutar(self):
        print(f"Iniciando: {self.nombre}")
        await asyncio.sleep(self.duracion)
        self.completada = True
        print(f"Completada: {self.nombre}")

class GestorTareas:
    def __init__(self, max_concurrentes: int = 3):
        self.tareas: List[Tarea] = []
        self.max_concurrentes = max_concurrentes
        self.semaforo = asyncio.Semaphore(max_concurrentes)
    
    def agregar(self, nombre: str, duracion: int):
        tarea = Tarea(str(uuid.uuid4())[:8], nombre, duracion)
        self.tareas.append(tarea)
        return tarea
    
    async def ejecutar_tarea(self, tarea: Tarea):
        async with self.semaforo:
            await tarea.ejecutar()
    
    async def ejecutar_todas(self):
        await asyncio.gather(*[self.ejecutar_tarea(t) for t in self.tareas])
    
    def tareas_pendientes(self):
        return [t for t in self.tareas if not t.completada]
    
    def tareas_completadas(self):
        return [t for t in self.tareas if t.completada]

# Uso
async def main():
    gestor = GestorTareas(max_concurrentes=2)
    
    gestor.agregar("Descargar archivo", 3)
    gestor.agregar("Procesar datos", 2)
    gestor.agregar("Enviar email", 1)
    gestor.agregar("Generar reporte", 2)
    
    print("Iniciando tareas...")
    await gestor.ejecutar_todas()
    
    print(f"Tareas completadas: {len(gestor.tareas_completadas())}")

# asyncio.run(main())

print("Gestor de tareas async configurado")

"""
────────────────────────────────
EJERCICIO 244 - ADMINISTRADOR DE CONFIGURACIÓN
────────────────────────────────
Descripción: Manejo centralizado de configuración.

Concepto: Singleton, patrones, validación

Código:
"""
from dataclasses import dataclass, field
from typing import Any, Dict, Optional
import json
import os

@dataclass
class Configuracion:
    debug: bool = False
    puerto: int = 8080
    host: str = "localhost"
    max_conexiones: int = 100
    timeout: int = 30
    base_datos: Dict[str, Any] = field(default_factory=dict)
    logging: Dict[str, Any] = field(default_factory=dict)

class GestorConfiguracion:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._config = Configuracion()
        return cls._instancia
    
    def cargar_desde_dict(self, config: dict):
        for clave, valor in config.items():
            if hasattr(self._config, clave):
                setattr(self._config, clave, valor)
    
    def cargar_desde_json(self, archivo: str):
        if os.path.exists(archivo):
            with open(archivo, 'r') as f:
                config = json.load(f)
                self.cargar_desde_dict(config)
    
    def cargar_desde_env(self):
        if 'DEBUG' in os.environ:
            self._config.debug = os.environ['DEBUG'].lower() == 'true'
        if 'PORT' in os.environ:
            self._config.puerto = int(os.environ['PORT'])
        if 'HOST' in os.environ:
            self._config.host = os.environ['HOST']
    
    def get(self, clave: str, default: Any = None) -> Any:
        return getattr(self._config, clave, default)
    
    def set(self, clave: str, valor: Any):
        if hasattr(self._config, clave):
            setattr(self._config, clave, valor)
    
    @property
    def config(self):
        return self._config

# Uso
config = GestorConfiguracion()
config.cargar_desde_dict({
    "debug": True,
    "puerto": 3000,
    "base_datos": {"host": "localhost", "nombre": "mydb"}
})

print(config.config.debug)
print(config.config.puerto)
print(config.config.base_datos)

"""
────────────────────────────────
EJERCICIO 245 - MANEJADOR DE PLUGINS
────────────────────────────────
Descripción: Sistema extensible de plugins.

Concepto: Registro dinámico, hooks

Código:
"""
from abc import ABC, abstractmethod
from typing import Dict, List, Callable, Any

class Plugin(ABC):
    @property
    @abstractmethod
    def nombre(self) -> str:
        pass
    
    @property
    @abstractmethod
    def version(self) -> str:
        pass
    
    @abstractmethod
    def inicializar(self):
        pass
    
    @abstractmethod
    def ejecutar(self, contexto: Any):
        pass

class PluginLogger(Plugin):
    @property
    def nombre(self) -> str:
        return "logger"
    
    @property
    def version(self) -> str:
        return "1.0.0"
    
    def inicializar(self):
        print(f"Plugin {self.nombre} inicializado")
    
    def ejecutar(self, contexto):
        print(f"Logging: {contexto}")

class GestorPlugins:
    def __init__(self):
        self._plugins: Dict[str, Plugin] = {}
        self._hooks: Dict[str, List[Callable]] = {}
    
    def registrar_plugin(self, plugin: Plugin):
        self._plugins[plugin.nombre] = plugin
        plugin.inicializar()
    
    def desregistrar_plugin(self, nombre: str):
        if nombre in self._plugins:
            del self._plugins[nombre]
    
    def obtener_plugin(self, nombre: str) -> Plugin:
        return self._plugins.get(nombre)
    
    def agregar_hook(self, evento: str, callback: Callable):
        if evento not in self._hooks:
            self._hooks[evento] = []
        self._hooks[evento].append(callback)
    
    def ejecutar_hook(self, evento: str, contexto: Any = None):
        if evento in self._hooks:
            for callback in self._hooks[evento]:
                callback(contexto or {})
    
    def ejecutar_todos(self, contexto: Any = None):
        for plugin in self._plugins.values():
            plugin.ejecutar(contexto)

# Uso
gestor = GestorPlugins()
gestor.registrar_plugin(PluginLogger())

gestor.agregar_hook("inicio", lambda ctx: print("Inicio:", ctx))
gestor.ejecutar_hook("inicio", {"tiempo": "ahora"})

print("\nPlugins registrados:", list(gestor._plugins.keys()))

# ============================================================
#        CONTINÚA EN ARCHIVO SIGUIENTE...
# ============================================================

print("\n" + "="*60)
print("FIN DE LA PARTE 3 - EJERCICIOS 201-350")
print("Continúa en: Ejercicios_Python_4.py")
print("="*60)
