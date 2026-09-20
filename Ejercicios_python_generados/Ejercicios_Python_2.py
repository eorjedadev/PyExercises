# ============================================================
# CURSO COMPLETO DE PYTHON - PARTE 2
# EJERCICIOS 85-200 (Nivel Básico-Intermedio)
# ============================================================

# ============================================================
#        EJERCICIOS 85-120: PROGRAMACIÓN ORIENTADA A OBJETOS
# ============================================================

"""
────────────────────────────────
EJERCICIO 85 - CLASE BÁSICA
────────────────────────────────
Descripción: Crea tu primera clase en Python.

Concepto: Una clase es un plano para crear objetos.
         Los objetos tienen atributos (datos) y métodos (funciones).

Código:
"""
class Persona:
    """Clase que representa una persona"""
    
    # Constructor - inicializa el objeto
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo
    
    # Método - función dentro de la clase
    def saludar(self):
        return f"Hola, soy {self.nombre} y tengo {self.edad} años"
    
    def cumpleanos(self):
        self.edad += 1
        return f"¡Feliz cumpleaños! Ahora tengo {self.edad} años"

# Crear objetos (instancias)
persona1 = Persona("Juan", 25)
persona2 = Persona("María", 30)

print(persona1.nombre)
print(persona1.saludar())
print(persona2.cumpleanos())

"""
────────────────────────────────
EJERCICIO 86 - ATRIBUTOS DE CLASE VS INSTANCIA
────────────────────────────────
Descripción: Diferencia entre atributos de clase e instancia.

Concepto: Atributos de clase compartidos por todas las instancias.
         Atributos de instancia únicos para cada objeto.

Código:
"""
class Coche:
    # Atributo de clase (compartido)
    ruedas = 4
    tipo = "automóvil"
    
    def __init__(self, marca, modelo):
        # Atributos de instancia (únicos)
        self.marca = marca
        self.modelo = modelo
        self.encendido = False
    
    def arrancar(self):
        self.encendido = True
        return f"{self.marca} {self.modelo} arrancó"
    
    def __str__(self):
        return f"{self.marca} {self.modelo}"

# Uso
coche1 = Coche("Toyota", "Corolla")
coche2 = Coche("Honda", "Civic")

print(f"{coche1} tiene {Coche.ruedas} ruedas")
print(f"{coche2} tiene {Coche.ruedas} ruedas")

# Modificar atributo de clase
Coche.ruedas = 3  # ¡Afecta a todos!
print(f"{coche1} tiene {coche1.ruedas} ruedas")

# Modificar atributo de instancia
coche1.ruedas = 4  # Solo afecta a coche1
print(f"{coche1} tiene {coche1.ruedas} ruedas")
print(f"{coche2} tiene {coche2.ruedas} ruedas")

"""
────────────────────────────────
EJERCICIO 87 - MÉTODOS ESPECIALES (DUNDER)
────────────────────────────────
Descripción: Métodos especiales con doble guión bajo.

Concepto: __init__, __str__, __repr__, __len__, etc.

Código:
"""
class Libro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    
    # Representación legible
    def __str__(self):
        return f"'{self.titulo}' por {self.autor}"
    
    # Representación técnica (para desarrolladores)
    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}', {self.paginas})"
    
    # Longitud
    def __len__(self):
        return self.paginas
    
    # Comparación
    def __eq__(self, otro):
        return self.titulo == otro.titulo
    
    def __lt__(self, otro):
        return self.paginas < otro.paginas

libro1 = Libro("1984", "Orwell", 328)
libro2 = Libro(" Fahrenheit 451", "Bradbury", 256)

print(str(libro1))
print(repr(libro1))
print(len(libro1))
print(libro1 < libro2)  # Por número de páginas

"""
────────────────────────────────
EJERCICIO 88 - HERENCIA BÁSICA
────────────────────────────────
Descripción: Crea clases que heredan de otras.

Concepto: La herencia permite reutilizar código.
         La clase hija hereda atributos y métodos del padre.

Código:
"""
# Clase padre
class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def hacer_sonido(self):
        return "Sonido genérico"
    
    def __str__(self):
        return f"{self.nombre}, {self.edad} años"

# Clase hija
class Perro(Animal):
    def __init__(self, nombre, edad, raza):
        super().__init__(nombre, edad)  # Llamar al constructor padre
        self.raza = raza
    
    # Sobreescribir método
    def hacer_sonido(self):
        return "¡Guau!"
    
    def ladrar(self):
        return f"{self.nombre} está ladrando"

class Gato(Animal):
    def hacer_sonido(self):
        return "¡Miau!"
    
    def maullar(self):
        return f"{self.nombre} está maullando"

# Uso
perro = Perro("Max", 3, "Labrador")
gato = Gato("Whiskers", 2)

print(perro)              # Heredado de Animal
print(perro.hacer_sonido())  # Sobreescrito
print(perro.ladrar())     # Método propio

print(gato)
print(gato.hacer_sonido())

"""
────────────────────────────────
EJERCICIO 89 - HERENCIA MÚLTIPLE
────────────────────────────────
Descripción: Una clase puede heredar de varias clases.

Concepto: Python soporta herencia múltiple.
         El orden de herencia afecta el MRO (Method Resolution Order).

Código:
"""
class Volador:
    def __init__(self):
        self.altitud = 0
    
    def volar(self, metros):
        self.altitud += metros
        return f"Vola a {self.altitud}m de altura"

class Nadador:
    def __init__(self):
        self.profundidad = 0
    
    def nadar(self, metros):
        self.profundidad += metros
        return f"Nada a {self.profundidad}m de profundidad"

class Pato(Volador, Nadador):
    def __init__(self, nombre):
        self.nombre = nombre
        Volador.__init__(self)
        Nadador.__init__(self)
    
    def description(self):
        return f"{self.nombre} puede volar y nadar"

pato = Pato("Donald")
print(pato.volar(100))
print(pato.nadar(50))
print(pato.description())

# MRO - Orden de resolución de métodos
print(Pato.mro())

"""
────────────────────────────────
EJERCICIO 90 - POLIMORFISMO
────────────────────────────────
Descripción: Objetos de diferentes clases se usan de forma interchangeable.

Concepto: El mismo método se comporta diferente en cada clase.

Código:
"""
class Figura:
    def area(self):
        pass
    
    def perimetro(self):
        pass

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return (self.base * self.altura) / 2
    
    def perimetro(self):
        # Triángulo equilátero
        return 3 * self.base

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        return 3.14159 * self.radio ** 2
    
    def perimetro(self):
        return 2 * 3.14159 * self.radio

# Polimorfismo: misma interfaz, diferentes implementaciones
figuras = [
    Rectangulo(10, 5),
    Triangulo(6, 4),
    Circulo(3)
]

for figura in figuras:
    print(f"Área: {figura.area():.2f}, Perímetro: {figura.perimetro():.2f}")

"""
────────────────────────────────
EJERCICIO 91 - ENCAPSULAMIENTO
────────────────────────────────
Descripción: Protege los datos con modificadores de acceso.

Concepto: 
- _protegido: Convention (no forzado)
- __privado: Name mangling (改名)
- _atributo: acceso directo no recomendado

Código:
"""
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial):
        self.titular = titular
        self.__saldo = saldo_inicial  # Privado (name mangling)
        self._historial = []  # Protegido (convención)
    
    # Getter
    def get_saldo(self):
        return self.__saldo
    
    # Setter con validación
    def set_saldo(self, nuevo_saldo):
        if nuevo_saldo >= 0:
            self.__saldo = nuevo_saldo
        else:
            raise ValueError("El saldo no puede ser negativo")
    
    def depositar(self, monto):
        if monto > 0:
            self.__saldo += monto
            self._historial.append(f"Depósito: +{monto}")
            return True
        return False
    
    def retirar(self, monto):
        if monto > 0 and monto <= self.__saldo:
            self.__saldo -= monto
            self._historial.append(f"Retiro: -{monto}")
            return True
        return False
    
    def __str__(self):
        return f"Cuenta de {self.titular}: ${self.__saldo}"

cuenta = CuentaBancaria("Juan", 1000)
print(cuenta)
print(f"Saldo: {cuenta.get_saldo()}")
cuenta.depositar(500)
print(f"Saldo después de depósito: {cuenta.get_saldo()}")
cuenta.retirar(200)
print(f"Saldo después de retiro: {cuenta.get_saldo()}")

# Intentar acceso directo a __saldo (genera error)
# print(cuenta.__saldo)  # AttributeError

# Acceso mediante name mangling
print(cuenta._CuentaBancaria__saldo)  # Funciona pero no recomendado

"""
────────────────────────────────
EJERCICIO 92 - @PROPERTY
────────────────────────────────
Descripción: Crea getters, setters y deleteters controlados.

Concepto: property() o decorador @property para acceso controlado.

Código:
"""
class Temperatura:
    def __init__(self):
        self._celsius = 0
    
    # Getter
    @property
    def celsius(self):
        return self._celsius
    
    # Setter
    @celsius.setter
    def celsius(self, valor):
        if valor < -273.15:
            raise ValueError("Temperatura menor al cero absoluto")
        self._celsius = valor
    
    # Deleter
    @celsius.deleter
    def celsius(self):
        print("Temperatura reiniciada a 0")
        self._celsius = 0
    
    # Propiedades calculadas
    @property
    def fahrenheit(self):
        return self._celsius * 9/5 + 32
    
    @property
    def kelvin(self):
        return self._celsius + 273.15

# Uso
temp = Temperatura()
temp.celsius = 25  # Usa el setter
print(temp.celsius)  # Usa el getter
print(temp.fahrenheit)  # Propiedad calculada
print(temp.kelvin)

# Delet
# del temp.celsius

# Intentar temperatura inválida
try:
    temp.celsius = -300
except ValueError as e:
    print(f"Error: {e}")

"""
────────────────────────────────
EJERCICIO 93 - CLASES ABSTRACTAS
────────────────────────────────
Descripción: Define interfaces que las subclases deben implementar.

Concepto: ABC (Abstract Base Class), @abstractmethod

Código:
"""
from abc import ABC, abstractmethod

class Figura(ABC):
    """Clase abstracta para figuras geométricas"""
    
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimetro(self):
        pass
    
    def descripcion(self):
        return f"Soy un {self.__class__.__name__}"

class Rectangulo(Figura):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    def area(self):
        return self.ancho * self.alto
    
    def perimetro(self):
        return 2 * (self.ancho + self.alto)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
    
    def area(self):
        import math
        return math.pi * self.radio ** 2
    
    def perimetro(self):
        import math
        return 2 * math.pi * self.radio

# Uso
figuras = [Rectangulo(10, 5), Circulo(3)]

for figura in figuras:
    print(f"{figura.descripcion()}")
    print(f"  Área: {figura.area():.2f}")
    print(f"  Perímetro: {figura.perimetro():.2f}")

# No se puede instanciar clase abstracta
# fig = Figura()  # TypeError

"""
────────────────────────────────
EJERCICIO 94 - DATA CLASSES
────────────────────────────────
Descripción: Simplifica la creación de clases para datos.

Concepto: @dataclass genera __init__, __repr__, __eq__ automáticamente

Código:
"""
from dataclasses import dataclass, field

@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int = 0  # Valor por defecto
    
    @property
    def total(self):
        return self.precio * self.cantidad

# Uso simplificado
p1 = Producto("Laptop", 999.99, 5)
p2 = Producto("Laptop", 999.99, 5)

print(p1)  # Producto(nombre='Laptop', ...)
print(p1 == p2)  # True (compara todos los campos)
print(p1.total)  # 4999.95

# Data class con métodos
@dataclass
class Persona:
    nombre: str
    edad: int
    email: str = ""
    
    def es_mayor(self):
        return self.edad >= 18

persona = Persona("Juan", 25, "juan@email.com")
print(persona.es_mayor())

# Con field y factory
@dataclass
class Carrito:
    productos: list = field(default_factory=list)
    
    def agregar(self, producto, cantidad):
        self.productos.append({"producto": producto, "cantidad": cantidad})
    
    def total(self):
        return sum(p["producto"].precio * p["cantidad"] for p in self.productos)

"""
────────────────────────────────
EJERCICIO 95 - COMPOSICIÓN
────────────────────────────────
Descripción: Una clase contiene objetos de otras clases.

Concepto: "Tiene un" vs "Es un" (herencia)

Código:
"""
class Motor:
    def __init__(self, tipo, potencia):
        self.tipo = tipo
        self.potencia = potencia
    
    def start(self):
        return "Motor arrancado"
    
    def stop(self):
        return "Motor detenido"

class Rueda:
    def __init__(self, tamaño):
        self.tamaño = tamaño
    
    def inflar(self):
        return "Rueda inflada"

class Coche:
    def __init__(self, marca, modelo, motor_tipo, potencia):
        self.marca = marca
        self.modelo = modelo
        self.motor = Motor(motor_tipo, potencia)
        self.ruedas = [Rueda(17) for _ in range(4)]
    
    def arrancar(self):
        return self.motor.start()
    
    def conducir(self):
        return f"{self.marca} {self.modelo} está conduciendo"
    
    def __str__(self):
        return f"{self.marca} {self.modelo} con motor {self.motor.tipo}"

# Uso
coche = Coche("Tesla", "Model 3", "Eléctrico", 450)
print(coche)
print(coche.arrancar())
print(coche.conducir())

"""
────────────────────────────────
EJERCICIO 96 - CLASES SINGLETON
────────────────────────────────
Descripción: Asegura que una clase tenga una sola instancia.

Concepto: Útil para configuraciones, conexiones, etc.

Código:
"""
class Configuracion:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.config = {}
        return cls._instancia
    
    def set(self, clave, valor):
        self.config[clave] = valor
    
    def get(self, clave):
        return self.config.get(clave)

# Uso
config1 = Configuracion()
config2 = Configuracion()

config1.set("theme", "dark")
print(config2.get("theme"))  # Misma instancia

print(config1 is config2)  # True

# Con decorador
def singleton(cls):
    instances = {}
    
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    
    return get_instance

@singleton
class Database:
    def __init__(self):
        self.connection = "Conectado"
    
    def query(self, sql):
        return f"Ejecutando: {sql}"

db1 = Database()
db2 = Database()
print(db1 is db2)  # True

"""
────────────────────────────────
EJERCICIO 97 - CLASES NESTED (ANIDADAS)
────────────────────────────────
Descripción: Clases definidas dentro de otras clases.

Concepto: Útil para estructuras complejas o privacidad.

Código:
"""
class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self._empleados = []
    
    class Empleado:
        def __init__(self, nombre, cargo, salario):
            self.nombre = nombre
            self.cargo = cargo
            self.salario = salario
        
        def __str__(self):
            return f"{self.nombre} - {self.cargo}"
    
    def agregar_empleado(self, nombre, cargo, salario):
        emp = self.Empleado(nombre, cargo, salario)
        self._empleados.append(emp)
        return emp
    
    def listar_empleados(self):
        return [str(e) for e in self._empleados]

# Uso
empresa = Empresa("TechCorp")
emp1 = empresa.agregar_empleado("Juan", "Desarrollador", 50000)
emp2 = empresa.agregar_empleado("Ana", "Diseñadora", 45000)

print(empresa.listar_empleados())

# ============================================================
#        EJERCICIOS 121-160: MÓDULOS Y PAQUETES
# ============================================================

"""
────────────────────────────────
EJERCICIO 98 - IMPORTAR MÓDULOS
────────────────────────────────
Descripción: Usa módulos externos y del estándar.

Concepto: import, from ... import, as ...

Código:
"""
# Importar módulo completo
import math
print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.14159...

# Importar funciones específicas
from math import sqrt, pi
print(sqrt(25))
print(pi)

# Importar con alias
import datetime as dt
from collections import Counter as Contador

# Módulos comunes del estándar
import random
import json
import os
import sys
from datetime import datetime, timedelta

# Uso de random
print(random.randint(1, 10))
print(random.choice(["a", "b", "c"]))
print(random.sample([1,2,3,4,5], 2))

# Uso de datetime
ahora = datetime.now()
print(ahora)
print(ahora.strftime("%Y-%m-%d %H:%M:%S"))

"""
────────────────────────────────
EJERCICIO 99 - CREAR MÓDULOS PROPIOS
────────────────────────────────
Descripción: Crea y usa tus propios módulos.

Concepto: Un archivo .py es un módulo.

Código:
"""
# Supongamos que tenemos un archivo llamado 'mi_modulo.py'
"""
# mi_modulo.py
def saludar(nombre):
    return f"Hola {nombre}"

def sumar(a, b):
    return a + b

CONSTANTE = 42
"""

# Desde otro archivo:
# import mi_modulo
# print(mi_modulo.saludar("Juan"))
# print(mi_modulo.sumar(3, 4))

# O import específico:
# from mi_modulo import saludar, CONSTANTE
# print(saludar("Mundo"))

# Demo con __name__ == "__main__"
def funcion_principal():
    print("Esta función se ejecuta solo cuando el archivo es principal")

if __name__ == "__main__":
    funcion_principal()

"""
────────────────────────────────
EJERCICIO 100 - PAQUETES
────────────────────────────────
Descripción: Organiza módulos en paquetes (directorios).

Concepto: Un paquete es un directorio con __init__.py

Código:
"""
# Estructura de paquete:
# mi_paquete/
#   __init__.py
#   modulo1.py
#   modulo2.py
#   subpaquete/
#     __init__.py
#     modulo3.py

# En __init__.py (opcional):
"""
from . import modulo1
from .subpaquete import modulo3
"""

# Importar
# from mi_paquete import modulo1
# from mi_paquete.subpaquete import modulo3
# from mi_paquete.modulo1 import funcion

# __all__ define qué se exporta con *
__all__ = ['funcion1', 'Clase1']

def funcion1():
    pass

def funcion_interna():
    pass

class Clase1:
    pass

# ============================================================
#        EJERCICIOS 161-200: FUNCIONES AVANZADAS
# ============================================================

"""
────────────────────────────────
EJERCICIO 101 - DECORADORES BÁSICOS
────────────────────────────────
Descripción: Modifica el comportamiento de funciones.

Concepto: Un decorador es una función que envuelve otra función.

Código:
"""
def mi_decorador(funcion):
    """Decorador que ejecuta código antes y después de la función"""
    def wrapper(*args, **kwargs):
        print("=== Antes de la función ===")
        resultado = funcion(*args, **kwargs)
        print("=== Después de la función ===")
        return resultado
    return wrapper

@mi_decorador
def saludar():
    print("¡Hola!")

saludar()

# Equivalente a:
# saludar = mi_decorador(saludar)

# Con parámetros
def decorador_con_parametros(param):
    def decorador(funcion):
        def wrapper(*args, **kwargs):
            print(f"Parámetro: {param}")
            return funcion(*args, **kwargs)
        return wrapper
    return decorador

@decorador_con_parametros("mi valor")
def ejemplo():
    print("Función ejecutada")

ejemplo()

"""
────────────────────────────────
EJERCICIO 102 - @FUNCTOOLS.WRAPS
────────────────────────────────
Descripción: Preserva la metadata de la función original.

Concepto: @wraps copia __name__, __doc__, etc.

Código:
"""
import functools

def mi_decorador(funcion):
    @functools.wraps(funcion)
    def wrapper(*args, **kwargs):
        """Documentación del wrapper"""
        print("Ejecutando...")
        return funcion(*args, **kwargs)
    return wrapper

@mi_decorador
def saludar():
    """Documentación de saludar"""
    return "¡Hola!"

print(saludar.__name__)  # saludar (no wrapper)
print(saludar.__doc__)   # Documentación de saludar

# Sin @wraps:
# print(saludar.__name__)  # wrapper (incorrecto)

"""
────────────────────────────────
EJERCICIO 103 - GENERADORES
────────────────────────────────
Descripción: Crea iteradores de forma eficiente.

Concepto: yield pa returns values sin terminar la función

Código:
"""
# Función normal
def numeros_hasta(n):
    lista = []
    for i in range(1, n + 1):
        lista.append(i)
    return lista

# Generador
def generador_numeros(n):
    for i in range(1, n + 1):
        yield i

# Uso
print(numeros_hasta(5))  # [1, 2, 3, 4, 5] (lista completa en memoria)

for num in generador_numeros(5):
    print(num)  # Uno a la vez (memoria eficiente)

# Crear generador con expresión
cuadrados_gen = (x**2 for x in range(5))
print(list(cuadrados_gen))

# next() y iter()
gen = generador_numeros(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# print(next(gen))  # StopIteration

"""
────────────────────────────────
EJERCICIO 104 - GENERADORES CON YIELD FROM
────────────────────────────────
Descripción: Delega a otro generador.

Concepto: yield from itera sobre un iterable y yield c/u

Código:
"""
def generar_hasta(n):
    for i in range(1, n + 1):
        yield i

def generar_pares(n):
    for i in generar_hasta(n):
        if i % 2 == 0:
            yield i

# Con yield from
def generar_pares_from(n):
    yield from (i for i in range(1, n + 1) if i % 2 == 0)

# Aplanar generadores
def aplanar(lista):
    for sublist in lista:
        yield from sublist

matriz = [[1, 2], [3, 4], [5, 6]]
print(list(aplanar(matriz)))  # [1, 2, 3, 4, 5, 6]

# Gen coroutine
def coroutine():
    while True:
        valor = yield
        print(f"Recibido: {valor}")

co = coroutine()
next(co)  # Iniciar
co.send("Hola")
co.send("Mundo")

"""
────────────────────────────────
EJERCICIO 105 - ITERADORES CUSTOM
────────────────────────────────
Descripción: Crea tus propios iteradores.

Concepto: Implementa __iter__ y __next__

Código:
"""
class Contador:
    def __init__(self, inicio, fin):
        self.actual = inicio
        self.fin = fin
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.actual >= self.fin:
            raise StopIteration
        valor = self.actual
        self.actual += 1
        return valor

# Uso
for num in Contador(1, 5):
    print(num)  # 1, 2, 3, 4

# Iterador que itera sobre archivo
class IteradorLineas:
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    
    def __iter__(self):
        self.file = open(self.filename, 'r')
        return self
    
    def __next__(self):
        linea = self.file.readline()
        if not linea:
            self.file.close()
            raise StopIteration
        return linea.strip()
    
    def __del__(self):
        if self.file:
            self.file.close()

# ============================================================
#        EJERCICIOS 201-250: APLICACIONES PRÁCTICAS
# ============================================================

"""
────────────────────────────────
EJERCICIO 106 - MANEJO DE EXCEPCIONES PERSONALIZADAS
────────────────────────────────
Descripción: Crea tus propias excepciones.

Concepto: Hereda de Exception o sus subclases

Código:
"""
class ErrorPersonalizado(Exception):
    """Excepción base personalizada"""
    pass

class ErrorValidacion(ErrorPersonalizado):
    def __init__(self, campo, mensaje):
        self.campo = campo
        self.mensaje = mensaje
        super().__init__(f"Error en {campo}: {mensaje}")

class ErrorEdadInvalida(ErrorValidacion):
    def __init__(self, edad):
        super().__init__("edad", f"Edad inválida: {edad}")

def validar_edad(edad):
    if edad < 0:
        raise ErrorEdadInvalida(edad)
    if edad > 150:
        raise ErrorValidacion("edad", "Parece irreal")
    return True

# Uso
try:
    validar_edad(-5)
except ErrorEdadInvalida as e:
    print(f"Error específico: {e}")
except ErrorValidacion as e:
    print(f"Error de validación: {e}")
except ErrorPersonalizado as e:
    print(f"Error personalizado: {e}")

"""
────────────────────────────────
EJERCICIO 107 - CONTEXT MANAGERS
────────────────────────────────
Descripción: Gestiona recursos con 'with'.

Concepto: Implementa __enter__ y __exit__

Código:
"""
class GestorArchivos:
    def __init__(self, nombre, modo):
        self.nombre = nombre
        self.modo = modo
        self.archivo = None
    
    def __enter__(self):
        self.archivo = open(self.nombre, self.modo)
        return self.archivo
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.archivo:
            self.archivo.close()
        return False  # No suprimir excepciones

# Uso
with GestorArchivos("prueba.txt", "w") as f:
    f.write("Hola mundo")

# Con contextmanager
from contextlib import contextmanager

@contextmanager
def temporizador():
    import time
    inicio = time.time()
    try:
        yield
    finally:
        fin = time.time()
        print(f"Tiempo: {fin - inicio:.2f}s")

with temporizador():
    suma = sum(range(1000000))

"""
────────────────────────────────
EJERCICIO 108 - TYPING BÁSICO
────────────────────────────────
Descripción: Anota tipos para mejor documentación y tooling.

Concepto: type hints con : tipo

Código:
"""
from typing import List, Dict, Tuple, Optional, Union

# Funciones con tipos
def saludar(nombre: str) -> str:
    return f"Hola {nombre}"

def sumar(a: int, b: int) -> int:
    return a + b

# Tipos compuestos
def procesar_datos(datos: List[int]) -> Dict[str, int]:
    return {
        "suma": sum(datos),
        "promedio": sum(datos) / len(datos),
        "cantidad": len(datos)
    }

# Tipos opcionales
def buscarUsuario(id: int) -> Optional[dict]:
    # Retorna dict o None
    pass

# Tipos union
def procesar(valor: Union[int, str]) -> str:
    return str(valor)

# Alias de tipos
Matriz = List[List[int]]
Coordenada = Tuple[float, float]

def mover(punto: Coordenada, movimiento: Coordenada) -> Coordenada:
    return (punto[0] + movimiento[0], punto[1] + movimiento[1])

"""
────────────────────────────────
EJERCICIO 109 - UNITTEST BÁSICO
────────────────────────────────
Descripción: Escribe pruebas unitarias.

Concepto: unittest module de la biblioteca estándar

Código:
"""
import unittest

class TestMatematicas(unittest.TestCase):
    
    def test_sumar(self):
        self.assertEqual(1 + 1, 2)
        self.assertEqual(0 + 0, 0)
    
    def test_dividir(self):
        self.assertEqual(10 / 2, 5)
        with self.assertRaises(ZeroDivisionError):
            1 / 0
    
    def test_palindromo(self):
        self.assertTrue("radar"[::-1] == "radar")
        self.assertFalse("python"[::-1] == "python")

# Pruebas para funciones propias
class TestFunciones(unittest.TestCase):
    
    def test_fibonacci(self):
        # Asumiendo función fibonacci definida
        # from modulo import fibonacci
        # self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        pass
    
    def test_validar_email(self):
        # Asumiendo función validar_email
        # self.assertTrue(validar_email("test@test.com"))
        # self.assertFalse(validar_email("invalid"))
        pass

# if __name__ == "__main__":
#     unittest.main()

# Ejemplo ejecutable
class TestSimple(unittest.TestCase):
    def test_suma(self):
        self.assertEqual(2 + 2, 4)

print("Pruebas unitarias definidas")

"""
────────────────────────────────
EJERCICIO 110 - LOGGER BÁSICO
────────────────────────────────
Descripción: Registra eventos de la aplicación.

Concepto: Módulo logging

Código:
"""
import logging

# Configuración básica
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Diferentes niveles
logger.debug("Mensaje de debug")
logger.info("Mensaje informativo")
logger.warning("Advertencia")
logger.error("Error")
logger.critical("Error crítico")

# En funciones
def dividir(a, b):
    try:
        resultado = a / b
        logger.info(f"División exitosa: {a}/{b} = {resultado}")
        return resultado
    except ZeroDivisionError as e:
        logger.error(f"División por cero: {a}/{b}")
        raise

# Con archivos
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Configuración por lingkungan
import os
nivel = os.getenv('LOG_LEVEL', 'INFO')
logging.basicConfig(level=getattr(logging, nivel))

print("Logging configurado")

# ============================================================
#        EJERCICIOS 251-300: ALGORITMOS Y ESTRUCTURAS
# ============================================================

"""
────────────────────────────────
EJERCICIO 111 - BÚSQUEDA LINEAL
────────────────────────────────
Descripción: Busca un elemento en una lista secuencialmente.

Concepto: O(n) - Compara cada elemento

Código:
"""
def busqueda_lineal(lista, objetivo):
    """
    Busca objetivo en lista
    Retorna índice si encuentra, -1 si no
    """
    for i, elemento in enumerate(lista):
        if elemento == objetivo:
            return i
    return -1

# Pruebas
numeros = [4, 2, 7, 1, 9, 3]
print(busqueda_lineal(numeros, 7))  # 2
print(busqueda_lineal(numeros, 5))  # -1

# Con sorted (búsqueda binaria automática)
import bisect
lista_ordenada = [1, 2, 3, 4, 5, 6, 7]
indice = bisect.bisect_left(lista_ordenada, 4)
print(f"Índice de 4: {indice}")

"""
────────────────────────────────
EJERCICIO 112 - BÚSQUEDA BINARIA
────────────────────────────────
Descripción: Busca en listas ordenadas eficientemente.

Concepto: O(log n) - Divide el espacio de búsqueda

Código:
"""
def busqueda_binaria(lista, objetivo):
    """Busca en lista ORDENADA"""
    izquierda, derecha = 0, len(lista) - 1
    
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        
        if lista[medio] == objetivo:
            return medio
        elif lista[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    
    return -1

# Pruebas
ordenada = [1, 3, 5, 7, 9, 11, 13, 15]
print(busqueda_binaria(ordenada, 7))  # 3
print(busqueda_binaria(ordenada, 6))  # -1

# Recursiva
def busqueda_binaria_rec(lista, objetivo, izquierda=None, derecha=None):
    if izquierda is None:
        izquierda, derecha = 0, len(lista) - 1
    
    if izquierda > derecha:
        return -1
    
    medio = (izquierda + derecha) // 2
    
    if lista[medio] == objetivo:
        return medio
    elif lista[medio] < objetivo:
        return busqueda_binaria_rec(lista, objetivo, medio + 1, derecha)
    else:
        return busqueda_binaria_rec(lista, objetivo, izquierda, medio - 1)

print(busqueda_binaria_rec(ordenada, 9))

"""
────────────────────────────────
EJERCICIO 113 - ORDENAMIENTO RÁPIDO (QUICKSORT)
────────────────────────────────
Descripción: Algoritmo de ordenamiento eficiente.

Concepto: O(n log n) promedio, divide y conquistás

Código:
"""
def quicksort(lista):
    """Ordena lista usando quicksort"""
    if len(lista) <= 1:
        return lista
    
    pivote = lista[len(lista) // 2]
    menores = [x for x in lista if x < pivote]
    iguales = [x for x in lista if x == pivote]
    mayores = [x for x in lista if x > pivote]
    
    return quicksort(menores) + iguales + quicksort(mayores)

# Pruebas
desordenada = [3, 6, 8, 10, 1, 2, 1]
print(quicksort(desordenada))

# In-place
def quicksort_inplace(lista, inicio=0, fin=None):
    if fin is None:
        fin = len(lista) - 1
    
    if inicio < fin:
        pivote = particionar(lista, inicio, fin)
        quicksort_inplace(lista, inicio, pivote - 1)
        quicksort_inplace(lista, pivote + 1, fin)
    
    return lista

def particionar(lista, inicio, fin):
    pivote = lista[fin]
    i = inicio - 1
    
    for j in range(inicio, fin):
        if lista[j] <= pivote:
            i += 1
            lista[i], lista[j] = lista[j], lista[i]
    
    lista[i + 1], lista[fin] = lista[fin], lista[i + 1]
    return i + 1

print(quicksort_inplace([3, 6, 8, 10, 1, 2, 1]))

"""
────────────────────────────────
EJERCICIO 114 - ORDENAMIENTO POR MEZCLA (MERGESORT)
────────────────────────────────
Descripción: Algoritmo estable y eficiente.

Concepto: O(n log n) - Divide, ordena, mezcla

Código:
"""
def mergesort(lista):
    """Ordena lista usando mergesort"""
    if len(lista) <= 1:
        return lista
    
    medio = len(lista) // 2
    izquierda = mergesort(lista[:medio])
    derecha = mergesort(lista[medio:])
    
    return merge(izquierda, derecha)

def merge(izq, der):
    """Mezcla dos listas ordenadas"""
    resultado = []
    i = j = 0
    
    while i < len(izq) and j < len(der):
        if izq[i] <= der[j]:
            resultado.append(izq[i])
            i += 1
        else:
            resultado.append(der[j])
            j += 1
    
    resultado.extend(izq[i:])
    resultado.extend(der[j:])
    
    return resultado

# Pruebas
desordenada = [38, 27, 43, 3, 9, 82, 10]
print(mergesort(desordenada))

"""
────────────────────────────────
EJERCICIO 115 - PILA (STACK)
────────────────────────────────
Descripción: Estructura LIFO (Last In, First Out).

Concepto: push (apilar), pop (desapilar), peek (ver cima)

Código:
"""
class Pila:
    def __init__(self):
        self.elementos = []
    
    def push(self, elemento):
        """Agrega elemento a la cima"""
        self.elementos.append(elemento)
    
    def pop(self):
        """Retorna y remueve el elemento superior"""
        if self.esta_vacia():
            return None
        return self.elementos.pop()
    
    def peek(self):
        """Retorna el elemento superior sin remover"""
        if self.esta_vacia():
            return None
        return self.elementos[-1]
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def tamaño(self):
        return len(self.elementos)
    
    def __str__(self):
        return str(self.elementos)

# Uso
pila = Pila()
pila.push(1)
pila.push(2)
pila.push(3)
print(pila)  # [1, 2, 3]
print(pila.pop())  # 3
print(pila.peek())  # 2
print(pila.esta_vacia())  # False

# Verificar paréntesis
def verificar_parentesis(expr):
    pila = Pila()
    pares = {')': '(', ']': '[', '}': '{'}
    
    for char in expr:
        if char in '([{':
            pila.push(char)
        elif char in ')]}':
            if pila.esta_vacia() or pila.pop() != pares[char]:
                return False
    
    return pila.esta_vacia()

print(verificar_parentesis("({[]})"))  # True
print(verificar_parentesis("({)}"))   # False

"""
────────────────────────────────
EJERCICIO 116 - COLA (QUEUE)
────────────────────────────────
Descripción: Estructura FIFO (First In, First Out).

Concepto: enqueue (agregar), dequeue (remover), front (ver frente)

Código:
"""
from collections import deque

class Cola:
    def __init__(self):
        self.elementos = deque()
    
    def enqueue(self, elemento):
        """Agrega al final"""
        self.elementos.append(elemento)
    
    def dequeue(self):
        """Retorna y remueve del frente"""
        if self.esta_vacia():
            return None
        return self.elementos.popleft()
    
    def front(self):
        """Ver elemento del frente"""
        if self.esta_vacia():
            return None
        return self.elementos[0]
    
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def tamaño(self):
        return len(self.elementos)
    
    def __str__(self):
        return str(list(self.elementos))

# Uso
cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
print(cola)  # [1, 2, 3]
print(cola.dequeue())  # 1
print(cola.front())  # 2

# Simulación de cola de打印
def simular_cola_tareas(tareas):
    cola = Cola()
    for tarea in tareas:
        cola.enqueue(tarea)
    
    while not cola.esta_vacia():
        tarea = cola.dequeue()
        print(f"Procesando: {tarea}")

simular_cola_tareas(["Task1", "Task2", "Task3"])

"""
────────────────────────────────
EJERCICIO 117 - ÁRBOL BINARIO BÁSICO
────────────────────────────────
Descripción: Estructura jerárquica con nodos.

Concepto: root (raíz), branch (rama), leaf (hoja)

Código:
"""
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None
    
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_rec(self.raiz, valor)
    
    def _insertar_rec(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_rec(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_rec(nodo.derecho, valor)
    
    def buscar(self, valor):
        return self._buscar_rec(self.raiz, valor)
    
    def _buscar_rec(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.valor:
            return True
        elif valor < nodo.valor:
            return self._buscar_rec(nodo.izquierdo, valor)
        else:
            return self._buscar_rec(nodo.derecho, valor)
    
    def inorden(self):
        """Recorrido inorden: izq - raíz - der"""
        return self._inorden_rec(self.raiz, [])
    
    def _inorden_rec(self, nodo, resultado):
        if nodo:
            resultado = self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            resultado = self._inorden_rec(nodo.derecho, resultado)
        return resultado

# Uso
arbol = ArbolBinario()
for valor in [50, 30, 70, 20, 40, 60, 80]:
    arbol.insertar(valor)

print("Inorden (ordenado):",arbol.inorden())
print("Buscar 40:",arbol.buscar(40))
print("Buscar 90:",arbol.buscar(90))

"""
────────────────────────────────
EJERCICIO 118 - GRAFOS CON ADYACENCIA
────────────────────────────────
Descripción: Representa grafos con listas de adyacencia.

Concepto: Vértices y aristas, dirigido/no dirigido

Código:
"""
class Grafo:
    def __init__(self, dirigido=False):
        self.dirigido = dirigido
        self.adyacencia = {}
    
    def agregar_vertice(self, vertice):
        if vertice not in self.adyacencia:
            self.adyacencia[vertice] = []
    
    def agregar_arista(self, origen, destino):
        self.agregar_vertice(origen)
        self.agregar_vertice(destino)
        
        self.adyacencia[origen].append(destino)
        
        if not self.dirigido:
            self.adyacencia[destino].append(origen)
    
    def adyacentes(self, vertice):
        return self.adyacencia.get(vertice, [])
    
    def __str__(self):
        resultado = []
        for vertice, adyacentes in self.adyacencia.items():
            resultado.append(f"{vertice} -> {adyacentes}")
        return "\n".join(resultado)

# Uso
grafo = Grafo()
grafo.agregar_arista("A", "B")
grafo.agregar_arista("A", "C")
grafo.agregar_arista("B", "D")
grafo.agregar_arista("C", "D")
grafo.agregar_arista("D", "E")

print(grafo)
print("Adyacentes de A:", grafo.adyacentes("A"))

# BFS
from collections import deque

def bfs(grafo, inicio):
    visitados = set()
    cola = deque([inicio])
    visitados.add(inicio)
    
    while cola:
        vertice = cola.popleft()
        print(vertice, end=" ")
        
        for adyacente in grafo.adyacentes(vertice):
            if adyacente not in visitados:
                visitados.add(adyacente)
                cola.append(adyacente)

print("\nBFS desde A:")
bfs(grafo, "A")

"""
────────────────────────────────
EJERCICIO 119 - TABLA HASH
────────────────────────────────
Descripción: Estructura clave-valor con acceso rápido.

Concepto: O(1) promedio - Hash function + manejo de colisiones

Código:
"""
class TablaHash:
    def __init__(self, tamaño=10):
        self.tamaño = tamaño
        self.tabla = [[] for _ in range(tamaño)]
    
    def _hash(self, clave):
        """Función hash simple"""
        return hash(clave) % self.tamaño
    
    def insertar(self, clave, valor):
        indice = self._hash(clave)
        # Buscar si existe
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                self.tabla[indice][i] = (clave, valor)
                return
        # Agregar nuevo
        self.tabla[indice].append((clave, valor))
    
    def obtener(self, clave):
        indice = self._hash(clave)
        for k, v in self.tabla[indice]:
            if k == clave:
                return v
        return None
    
    def eliminar(self, clave):
        indice = self._hash(clave)
        for i, (k, v) in enumerate(self.tabla[indice]):
            if k == clave:
                del self.tabla[indice][i]
                return True
        return False
    
    def __str__(self):
        resultado = []
        for i, bucket in enumerate(self.tabla):
            if bucket:
                resultado.append(f"{i}: {bucket}")
        return "\n".join(resultado)

# Uso
tabla = TablaHash(5)
tabla.insertar("nombre", "Juan")
tabla.insertar("edad", 25)
tabla.insertar("ciudad", "Madrid")

print(tabla)
print("nombre:", tabla.obtener("nombre"))
print("edad:", tabla.obtener("edad"))
tabla.eliminar("edad")
print("edad después de eliminar:", tabla.obtener("edad"))

"""
────────────────────────────────
EJERCICIO 120 - PROGRAMACIÓN DINÁMICA - FIBONACCI
────────────────────────────────
Descripción: Optimiza recursion con memorización.

Concepto: Guardar resultados ya calculados para evitar recomputación

Código:
"""
# Sin optimización - O(2^n)
def fib_recursivo(n):
    if n <= 1:
        return n
    return fib_recursivo(n-1) + fib_recursivo(n-2)

# Con memorización - O(n)
from functools import lru_cache

@lru_cache(maxsize=None)
def fib_memo(n):
    if n <= 1:
        return n
    return fib_memo(n-1) + fib_memo(n-2)

# Con tabulación - O(n)
def fib_tabulacion(n):
    if n <= 1:
        return n
    
    tabla = [0] * (n + 1)
    tabla[1] = 1
    
    for i in range(2, n + 1):
        tabla[i] = tabla[i-1] + tabla[i-2]
    
    return tabla[n]

# Comparación
import time

n = 35

start = time.time()
result1 = fib_memo(n)
print(f"Memo: {time.time() - start:.4f}s - Result: {result1}")

start = time.time()
result2 = fib_tabulacion(n)
print(f"Tabla: {time.time() - start:.4f}s - Result: {result2}")

# ============================================================
#        EJERCICIOS 301-400: NIVEL INTERMEDIO-INTERMEDIO AVANZADO
# ============================================================

"""
────────────────────────────────
EJERCICIO 121 - DECORADORES CON ARGUMENTOS
────────────────────────────────
Descripción: Decoradores que aceptan parámetros.

Concepto: Factory de decoradores

Código:
"""
import functools
import time

def retry(max_intentos=3, delay=1):
    """Decorador que reintenta función en caso de error"""
    def decorador(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for intento in range(max_intentos):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if intento == max_intentos - 1:
                        raise
                    print(f"Intento {intento + 1} falló: {e}")
                    time.sleep(delay)
            return wrapper
        return decorador
    return decorador

@retry(max_intentos=3, delay=2)
def conectar_api():
    import random
    if random.random() < 0.7:
        raise ConnectionError("Conexión fallida")
    return "Conectado"

# Probar (comenta para evitar espera)
# print(conectar_api())

"""
────────────────────────────────
EJERCICIO 122 - PROPIEDADES CON DESCRIPTORS
────────────────────────────────
Descripción: Crea descriptores para validar atributos.

Concepto: Clases con __get__, __set__, __delete__

Código:
"""
class Descriptor:
    def __init__(self, default=None):
        self.default = default
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name, self.default)
    
    def __set__(self, obj, value):
        setattr(obj, self.name, value)

class Rango(Descriptor):
    def __init__(self, minimo=None, maximo=None, default=None):
        super().__init__(default)
        self.minimo = minimo
        self.maximo = maximo
    
    def __set__(self, obj, value):
        if value is not None:
            if self.minimo is not None and value < self.minimo:
                raise ValueError(f"Mínimo es {self.minimo}")
            if self.maximo is not None and value > self.maximo:
                raise ValueError(f"Máximo es {self.maximo}")
        super().__set__(obj, value)

class Persona:
    edad = Rango(minimo=0, maximo=150, default=0)
    altura = Rango(minimo=0.5, maximo=3.0, default=1.70)

p = Persona()
p.edad = 25
print(p.edad)

# p.edad = 200  # ValueError

"""
────────────────────────────────
EJERCICIO 123 - META CLASES BÁSICAS
────────────────────────────────
Descripción: Clases que crean clases.

Concepto: metaclass define el comportamiento de clases

Código:
"""
class Meta(type):
    def __new__(cls, name, bases, namespace):
        # Agregar método automático
        namespace["descripcion"] = lambda self: f"Soy {name}"
        
        # Validar que exista ciertos atributos
        if "saludar" not in namespace and "despedir" not in namespace:
            print(f"Advertencia: {name} no tiene saludar ni despedir")
        
        return super().__new__(cls, name, bases, namespace)

class MiClase(metaclass=Meta):
    def saludar(self):
        return "Hola"

# Uso
obj = MiClase()
print(obj.descripcion())

# Registro automático
class Registro(type):
    clases = {}
    
    def __new__(cls, name, bases, namespace):
        nueva_clase = super().__new__(cls, name, bases, namespace)
        cls.clases[name] = nueva_clase
        return nueva_clase

class PluginBase(metaclass=Registro):
    pass

class Plugin1(PluginBase):
    def ejecutar(self):
        return "Plugin 1"

class Plugin2(PluginBase):
    def ejecutar(self):
        return "Plugin 2"

print(list(Registro.clases.keys()))

"""
────────────────────────────────
EJERCICIO 124 - EJECUTOR DE COMANDOS
────────────────────────────────
Descripción: Sistema que ejecuta comandos desde entrada.

Concepto: Patrón Command,反射

Código:
"""
class Comando:
    def __init__(self, receptor):
        self.receptor = receptor
    
    def ejecutar(self):
        pass

class Receptor:
    def accion_a(self):
        return "Acción A ejecutada"
    
    def accion_b(self):
        return "Acción B ejecutada"

class ComandoA(Comando):
    def ejecutar(self):
        return self.receptor.accion_a()

class ComandoB(Comando):
    def ejecutar(self):
        return self.receptor.accion_b()

class Invocador:
    def __init__(self):
        self.comandos = {}
    
    def registrar(self, nombre, comando):
        self.comandos[nombre] = comando
    
    def ejecutar(self, nombre):
        if nombre in self.comandos:
            return self.comandos[nombre].ejecutar()
        return "Comando no encontrado"

# Uso
receptor = Receptor()
invocador = Invocador()

invocador.registrar("a", ComandoA(receptor))
invocador.registrar("b", ComandoB(receptor))

print(invocador.ejecutar("a"))
print(invocador.ejecutar("b"))

"""
────────────────────────────────
EJERCICIO 125 - OBSERVER PATTERN
────────────────────────────────
Descripción: Sistema de suscripción y notificaciones.

Concepto: Sujeto notifica a observadores cuando cambia

Código:
"""
class Observador:
    def actualizar(self, mensaje):
        pass

class Sujeto:
    def __init__(self):
        self._observadores = []
    
    def agregar_observador(self, observador):
        self._observadores.append(observador)
    
    def eliminar_observador(self, observador):
        self._observadores.remove(observador)
    
    def notificar(self, mensaje):
        for observador in self._observadores:
            observador.actualizar(mensaje)

class Usuario(Observador):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def actualizar(self, mensaje):
        print(f"{self.nombre} recibió: {mensaje}")

# Uso
sujeto = Sujeto()

u1 = Usuario("Juan")
u2 = Usuario("María")

sujeto.agregar_observador(u1)
sujeto.agregar_observador(u2)

sujeto.notificar("Nuevo mensaje")

sujeto.eliminar_observador(u1)
sujeto.notificar("Segundo mensaje")

"""
────────────────────────────────
EJERCICIO 126 - FACTORY PATTERN
────────────────────────────────
Descripción: Crea objetos sin especificar clase exacta.

Concepto: Factory method crea instancias según parámetros

Código:
"""
class Producto:
    def operacion(self):
        pass

class ProductoConcretoA(Producto):
    def operacion(self):
        return "Producto A"

class ProductoConcretoB(Producto):
    def operacion(self):
        return "Producto B"

class Factory:
    @staticmethod
    def crear_producto(tipo):
        if tipo == "A":
            return ProductoConcretoA()
        elif tipo == "B":
            return ProductoConcretoB()
        raise ValueError(f"Tipo {tipo} no válido")

# Uso
producto = Factory.crear_producto("A")
print(producto.operacion())

# Con registro
class FactoryRegistro:
    _productos = {}
    
    @classmethod
    def registrar(cls, tipo, clase):
        cls._productos[tipo] = clase
    
    @classmethod
    def crear(cls, tipo):
        if tipo not in cls._productos:
            raise ValueError(f"Tipo {tipo} no registrado")
        return cls._productos[tipo]()

FactoryRegistro.registrar("A", ProductoConcretoA)
FactoryRegistro.registrar("B", ProductoConcretoB)

print(FactoryRegistro.crear("B").operacion())

"""
────────────────────────────────
EJERCICIO 127 - SERIALIZACIÓN JSON
────────────────────────────────
Descripción: Convierte objetos a/de JSON.

Concepto: json.dumps(), json.loads()

Código:
"""
import json

# Serialización básica
datos = {
    "nombre": "Juan",
    "edad": 30,
    "ciudad": "Madrid",
    "hobbies": ["lectura", "deporte"]
}

# A JSON string
json_str = json.dumps(datos)
print(json_str)

# A diccionario
datos2 = json.loads(json_str)
print(datos2)

# Con archivo
with open("datos.json", "w") as f:
    json.dump(datos, f, indent=2)

with open("datos.json", "r") as f:
    datos3 = json.load(f)
print(datos3)

# Custom encoder para clases
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class PersonaEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Persona):
            return {"nombre": obj.nombre, "edad": obj.edad}
        return super().default(obj)

p = Persona("Juan", 30)
print(json.dumps(p, cls=PersonaEncoder))

# Con __dict__ y @property
class Persona2:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def to_dict(self):
        return self.__dict__

print(json.dumps(p.to_dict()))

"""
────────────────────────────────
EJERCICIO 128 - PERSISTENCIA CON PICKLE
────────────────────────────────
Descripción: Serializa objetos Python complejos.

Concepto: pickle.dumps(), pickle.loads() - solo Python

Código:
"""
import pickle

class Usuario:
    def __init__(self, nombre, permisos):
        self.nombre = nombre
        self.permisos = permisos
    
    def __str__(self):
        return f"{self.nombre} ({', '.join(self.permisos)})"

# Serializar
usuario = Usuario("admin", ["leer", "escribir", "eliminar"])
datos = pickle.dumps(usuario)
print(f"Tamaño: {len(datos)} bytes")

# Deserializar
usuario2 = pickle.loads(datos)
print(usuario2)

# Con archivo
with open("usuario.pkl", "wb") as f:
    pickle.dump(usuario, f)

with open("usuario.pkl", "rb") as f:
    usuario3 = pickle.load(f)
print(usuario3)

# Advertencia: ¡No unpickle código no confiable!
# pickle.loads(datos_no_confiables)  # Peligroso

"""
────────────────────────────────
EJERCICIO 129 - EXPRESIONES REGULARES BÁSICAS
────────────────────────────────
Descripción: Busca patrones en texto.

Concepto: re module, patrones, grupos

Código:
"""
import re

# Basic matching
texto = "Mi email es juan@ejemplo.com"
patron = r"\w+@\w+\.\w+"
match = re.search(patron, texto)
print(match.group() if match else "No encontrado")

# Metacaracteres
# .  - cualquier carácter
# \d - dígito
# \w - palabra (letra, número, _)
# \s - espacio
# ^  - inicio
# $  - fin
# *  - 0 o más
# +  - 1 o más
# ?  - 0 o 1
# [] - clase de caracteres

# Validar email
def validar_email(email):
    patron = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(patron, email) is not None

print(validar_email("juan@email.com"))
print(validar_email("juan@email"))

# Extracción
texto = "Tel: 123-456-7890"
patron = r"\d{3}-\d{3}-\d{4}"
print(re.findall(patron, texto))

# Grupos
patron = r"(\w+)@(\w+)\.(\w+)"
match = re.search(patron, "juan@gmail.com")
if match:
    print(match.group(0))  # Todo
    print(match.group(1))  # juan
    print(match.group(2))  # gmail
    print(match.group(3))  # com

# Reemplazar
texto = "Hola Juan, saludos Juan"
print(re.sub(r"Juan", "Pedro", texto))

# ============================================================
#        EJERCICIOS 401-500: NIVEL AVANZADO
# ============================================================

"""
────────────────────────────────
EJERCICIO 130 - ASYNCIO BÁSICO
────────────────────────────────
Descripción: Programación asíncrona con asyncio.

Concepto: async/await, event loop, corrutinas

Código:
"""
import asyncio

async def tarea(nombre, delay):
    print(f"{nombre} iniciando...")
    await asyncio.sleep(delay)
    print(f"{nombre} completado después de {delay}s")
    return f"{nombre} listo"

async def main():
    # Ejecutar concurrentemente
    resultados = await asyncio.gather(
        tarea("Tarea 1", 2),
        tarea("Tarea 2", 1),
        tarea("Tarea 3", 3)
    )
    print(resultados)

# asyncio.run(main())

# Con create_task
async def main2():
    tarea1 = asyncio.create_task(tarea("A", 2))
    tarea2 = asyncio.create_task(tarea("B", 1))
    
    print("Esperando tareas...")
    await tarea1
    await tarea2
    print("Todas completadas")

# asyncio.run(main2())

# Semaphore
async def tarea_con_limite(semaphore, nombre):
    async with semaphore:
        print(f"{nombre} trabajando")
        await asyncio.sleep(1)
        return nombre

async def main3():
    semaphore = asyncio.Semaphore(2)  # Máx 2 concurrentes
    tareas = [tarea_con_limite(semaphore, f"Tarea {i}") for i in range(5)]
    await asyncio.gather(*tareas)

# asyncio.run(main3())

print("async/asyncio configurado")

"""
────────────────────────────────
EJERCICIO 131 - THREADING BÁSICO
────────────────────────────────
Descripción: Hilos para concurrencia.

Concepto: threading.Thread, run(), start(), join()

Código:
"""
import threading
import time

def tarea(nombre, delay):
    print(f"{nombre} iniciando")
    time.sleep(delay)
    print(f"{nombre} completado")

# Crear hilo
hilo1 = threading.Thread(target=tarea, args=("Hilo 1", 2))
hilo2 = threading.Thread(target=tarea, args=("Hilo 2", 1))

# Iniciar
hilo1.start()
hilo2.start()

# Esperar
hilo1.join()
hilo2.join()

print("Todos los hilos terminados")

# Con clase
class MiHilo(threading.Thread):
    def __init__(self, nombre, delay):
        super().__init__()
        self.nombre = nombre
        self.delay = delay
    
    def run(self):
        print(f"{self.nombre} ejecutando")
        time.sleep(self.delay)
        print(f"{self.nombre} terminado")

hilo = MiHilo("MiHilo", 1)
hilo.start()
hilo.join()

# Variables compartidas (con lock)
contador = 0
lock = threading.Lock()

def incrementar():
    global contador
    for _ in range(100000):
        with lock:
            contador += 1

hilos = [threading.Thread(target=incrementar) for _ in range(10)]
for h in hilos:
    h.start()
for h in hilos:
    h.join()

print(f"Contador final: {contador}")  # 1000000

"""
────────────────────────────────
EJERCICIO 132 - multiprocessing
────────────────────────────────
Descripción: Procesos paralelos (para CPU-bound).

Concepto: Proceso separado con su propio GIL

Código:
"""
from multiprocessing import Process, Pool
import time

def proceso_pesado(n):
    # Simular trabajo CPU-bound
    resultado = sum(i**2 for i in range(n))
    return resultado

# Con Process
if __name__ == "__main__":
    procesos = []
    for i in range(4):
        p = Process(target=proceso_pesado, args=(1000000,))
        procesos.append(p)
        p.start()
    
    for p in procesos:
        p.join()
    
    print("Procesos terminados")

# Con Pool
def cuadrado(x):
    return x**2

with Pool(4) as pool:
    resultados = pool.map(cuadrado, range(10))
    print(resultados)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

"""
────────────────────────────────
EJERCICIO 133 - ANOTACIONES TIPO AVANZADAS
────────────────────────────────
Descripción: Type hints avanzados.

Concepto: Generics, Protocol, TypeVar

Código:
"""
from typing import TypeVar, Generic, List, Dict, Optional, Protocol, Callable

T = TypeVar('T')

class Pila(Generic[T]):
    def __init__(self):
        self.elementos: List[T] = []
    
    def push(self, item: T) -> None:
        self.elementos.append(item)
    
    def pop(self) -> T:
        return self.elementos.pop()
    
    def peek(self) -> T:
        return self.elementos[-1]
    
    def is_empty(self) -> bool:
        return len(self.elementos) == 0

# Uso
pila: Pila[int] = Pila()
pila.push(1)
pila.push(2)
print(pila.pop())

# Protocol (structural subtyping)
class Runnable(Protocol):
    def run(self) -> None: ...

class MiClase:
    def run(self) -> None:
        print("Ejecutando")

def iniciar(r: Runnable) -> None:
    r.run()

iniciar(MiClase())  # Sin herencia explícita

# Callable
def aplicar_funcion(func: Callable[[int], int], valor: int) -> int:
    return func(valor)

print(aplicar_funcion(lambda x: x * 2, 5))

"""
────────────────────────────────
EJERCICIO 134 - ATRIBUTOS DE CLASE DINÁMICOS
────────────────────────────────
Descripción: Crear atributos en tiempo de ejecución.

Concepto: __getattr__, __setattr__, __getattribute__

Código:
"""
class ObjetoDinamico:
    def __init__(self):
        self._datos = {}
    
    def __getattr__(self, nombre):
        if nombre.startswith('_'):
            raise AttributeError(nombre)
        return self._datos.get(nombre, f"Attr '{nombre}' no existe")
    
    def __setattr__(self, nombre, valor):
        if nombre.startswith('_'):
            super().__setattr__(nombre, valor)
        else:
            self._datos[nombre] = valor
    
    def __delattr__(self, nombre):
        if nombre in self._datos:
            del self._datos[nombre]
    
    def __dir__(self):
        return list(super().__dir__()) + list(self._datos.keys())

obj = ObjetoDinamico()
obj.nombre = "Juan"
print(obj.nombre)
print(obj.edad)  # No existe, retorna mensaje

# Proxy dinámico
class Proxy:
    def __init__(self, objeto):
        self._objeto = objeto
    
    def __getattr__(self, nombre):
        return getattr(self._objeto, nombre)
    
    def __setattr__(self, nombre, valor):
        if nombre.startswith('_'):
            super().__setattr__(nombre, valor)
        else:
            setattr(self._objeto, nombre, valor)

class Real:
    def saludar(self):
        return "Hola"

proxy = Proxy(Real())
print(proxy.saludar())

"""
────────────────────────────────
EJERCICIO 135 - METACLASES AVANZADAS
────────────────────────────────
Descripción: Metaclasses con validación y transformación.

Concepto: Validar y transformar clases al crearlas

Código:
"""
class ValidarAtributos(type):
    """Metaclase que valida que las clases tengan ciertos atributos"""
    
    def __new__(cls, name, bases, namespace):
        # Agregar método para obtener atributos requeridos
        if "obtener_info" not in namespace:
            namespace["obtener_info"] = lambda self: f"{name}: {self.__dict__}"
        
        return super().__new__(cls, name, bases, namespace)

class ClaseValidada(metaclass=ValidarAtributos):
    pass

# Validar métodos requeridos
class RequiereMetodos(type):
    _metodos_requeridos = []
    
    def __new__(cls, name, bases, namespace):
        namespace["_metodos_requeridos"] = cls._metodos_requeridos
        return super().__new__(cls, name, bases, namespace)

# Mixin para validación
class ValidableMixin:
    def validar(self):
        for metodo in getattr(self.__class__, "_metodos_requeridos", []):
            if not hasattr(self, metodo):
                raise NotImplementedError(f"Debe implementar {metodo}")

# Registry de clases
class Registry(type):
    registro = {}
    
    def __new__(cls, name, bases, namespace):
        nueva_clase = super().__new__(cls, name, bases, namespace)
        cls.registro[name] = nueva_clase
        return nueva_clase

class Plugin(metaclass=Registry):
    pass

class PluginA(Plugin):
    def ejecutar(self):
        return "A"

class PluginB(Plugin):
    def ejecutar(self):
        return "B"

print(list(Registry.registro.keys()))

"""
────────────────────────────────
EJERCICIO 136 - DESCRIPTORES AVANZADOS
────────────────────────────────
Descripción: Descriptores con validación compleja.

Código:
"""
class DescriptorValidado:
    def __init__(self, validador):
        self.validador = validador
        self.name = None
    
    def __set_name__(self, owner, name):
        self.name = f"_{name}"
    
    def __get__(self, obj, objtype=None):
        return getattr(obj, self.name)
    
    def __set__(self, obj, value):
        if not self.validador(value):
            raise ValueError(f"Valor inválido: {value}")
        setattr(obj, self.name, value)

# Validadores
def es_positivo(x):
    return x > 0

def rango(minimo, maximo):
    def validar(x):
        return minimo <= x <= maximo
    return validar

def longitud_maxima(n):
    def validar(s):
        return len(s) <= n
    return validar

class Persona:
    edad = DescriptorValidado(lambda x: x > 0 and x < 150)
    altura = DescriptorValidado(rango(0.5, 3.0))
    nombre = DescriptorValidado(longitud_maxima(50))

p = Persona()
p.edad = 25
print(p.edad)

# p.edad = 200  # ValueError

"""
────────────────────────────────
EJERCICIO 137 - GENERADORES CON ESTADO
────────────────────────────────
Descripción: Generadores que mantienen estado.

Código:
"""
class IteradorEstado:
    """Iterador con estado complejo"""
    
    def __init__(self, datos):
        self.datos = datos
        self.indice = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.indice >= len(self.datos):
            raise StopIteration
        valor = self.datos[self.indice]
        self.indice += 1
        return valor

# Generador de Fibonacci con control
def fibonacci_generator(limite=None):
    a, b = 0, 1
    contador = 0
    while limite is None or contador < limite:
        yield a
        a, b = b, a + b
        contador += 1

# Generador con memoria
def generador_ventana(secuencia, tamano):
    ventana = []
    for elemento in secuencia:
        ventana.append(elemento)
        if len(ventana) == tamano:
            yield tuple(ventana)
            ventana.pop(0)

numeros = [1, 2, 3, 4, 5, 6, 7]
for ventana in generador_ventana(numeros, 3):
    print(ventana)

# Generador infinito
def generador_infinio():
    n = 0
    while True:
        yield n
        n += 1

# Usar con islice
from itertools import islice
gen = generador_infinio()
print(list(islice(gen, 10)))

"""
────────────────────────────────
EJERCICIO 138 - CONTEXT MANAGERS PERSONALIZADOS
────────────────────────────────
Descripción: Crea context managers con clase o función.

Código:
"""
# Con clase
class Temporizador:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def __enter__(self):
        import time
        self.inicio = time.time()
        print(f"Iniciando {self.nombre}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        import time
        tiempo = time.time() - self.inicio
        print(f"{self.nombre} tomó {tiempo:.2f}s")
        return False  # No suprimir excepciones

with Temporizador("Operación"):
    suma = sum(range(1000000))

# Con función (contextlib)
from contextlib import contextmanager

@contextmanager
def abrir_archivo(nombre, modo):
    archivo = open(nombre, modo)
    try:
        yield archivo
    finally:
        archivo.close()

# Uso
# with abrir_archivo("prueba.txt", "w") as f:
#     f.write("Hola")

# Timer decorator
import functools
import time

def tiempo_ejecucion(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = func(*args, **kwargs)
        print(f"{func.__name__} tardó {time.time() - inicio:.4f}s")
        return resultado
    return wrapper

@tiempo_ejecucion
def operacion_lenta():
    time.sleep(0.5)

operacion_lenta()

"""
────────────────────────────────
EJERCICIO 139 - PROPAGACIÓN DE EXCEPCIONES
────────────────────────────────
Descripción: Manejo avanzado de excepciones.

Concepto: raise from, encadenamiento, custom

Código:
"""
class MiError(Exception):
    def __init__(self, mensaje, codigo=None):
        super().__init__(mensaje)
        self.codigo = codigo

def funcion1():
    raise ValueError("Error en función 1")

def funcion2():
    try:
        funcion1()
    except ValueError as e:
        # Encadenar excepciones
        raise MiError("Error en función 2", codigo=500) from e

try:
    funcion2()
except MiError as e:
    print(f"Error: {e}")
    print(f"Causado por: {e.__cause__}")
    print(f"Código: {e.codigo}")

# Re-lanzar excepción original
def funcion3():
    try:
        funcion1()
    except ValueError:
        raise  # Re-lanza la excepción original

#traceback
import traceback

try:
    funcion1()
except Exception:
    traceback.print_exc()

"""
────────────────────────────────
EJERCICIO 140 - SOBRECARGA DE OPERADORES
────────────────────────────────
Descripción: Personaliza operadores para clases.

Concepto: __add__, __sub__, __eq__, __lt__, etc.

Código:
"""
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, otro):
        return Vector(self.x + otro.x, self.y + otro.y)
    
    def __sub__(self, otro):
        return Vector(self.x - otro.x, self.y - otro.y)
    
    def __mul__(self, escalar):
        return Vector(self.x * escalar, self.y * escalar)
    
    def __rmul__(self, escalar):
        return self.__mul__(escalar)
    
    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __len__(self):
        return 2
    
    def __getitem__(self, indice):
        if indice == 0:
            return self.x
        elif indice == 1:
            return self.y
        raise IndexError()

v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  # (4, 6)
print(v1 - v2)  # (-2, -2)
print(v1 * 3)   # (3, 6)
print(3 * v1)   # (3, 6)
print(-v1)      # (-1, -2)
print(v1 == v2)  # False
print(v1[0])    # 1

# Matriz
class Matriz:
    def __init__(self, datos):
        self.datos = datos
        self.filas = len(datos)
        self.columnas = len(datos[0]) if datos else 0
    
    def __mul__(self, otra):
        if self.columnas != otra.filas:
            raise ValueError("Dimensiones incompatibles")
        
        resultado = []
        for i in range(self.filas):
            fila = []
            for j in range(otra.columnas):
                suma = sum(self.datos[i][k] * otra.datos[k][j] 
                          for k in range(self.columnas))
                fila.append(suma)
            resultado.append(fila)
        
        return Matriz(resultado)
    
    def __str__(self):
        return "\n".join(str(fila) for fila in self.datos)

m1 = Matriz([[1, 2], [3, 4]])
m2 = Matriz([[5, 6], [7, 8]])
print(m1 * m2)

# ============================================================
#        CONTINÚA EN ARCHIVO SIGUIENTE...
# ============================================================

print("\n" + "="*60)
print("FIN DE LA PARTE 2 - EJERCICIOS 85-200")
print("Continúa en: Ejercicios_Python_3.py")
print("="*60)
