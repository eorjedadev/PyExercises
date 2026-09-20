# ============================================================
# CURSO COMPLETO DE PYTHON - PARTE 4
# EJERCICIOS 351-500 (Nivel Avanzado)
# ============================================================

# ============================================================
#        EJERCICIOS 351-400: PATRONES AVANZADOS
# ============================================================

"""
────────────────────────────────
EJERCICIO 351 - PATRÓN MVC SIMPLE
────────────────────────────────
Descripción: Implementa el patrón Modelo-Vista-Controlador.

Concepto: Separación de responsabilidades

Código:
"""
# Modelo
class Modelo:
    def __init__(self):
        self._datos = []
    
    def agregar(self, item):
        self._datos.append(item)
    
    def obtener_todos(self):
        return self._datos.copy()
    
    def buscar(self, indice):
        if 0 <= indice < len(self._datos):
            return self._datos[indice]
        return None

# Vista
class Vista:
    @staticmethod
    def mostrar_menu():
        print("1. Agregar item")
        print("2. Ver todos")
        print("3. Buscar")
        print("4. Salir")
    
    @staticmethod
    def mostrar_items(items):
        for i, item in enumerate(items):
            print(f"{i}: {item}")
    
    @staticmethod
    def mostrar_error(mensaje):
        print(f"ERROR: {mensaje}")
    
    @staticmethod
    def mostrar_exito(mensaje):
        print(f"ÉXITO: {mensaje}")

# Controlador
class Controlador:
    def __init__(self):
        self.modelo = Modelo()
        self.vista = Vista()
    
    def ejecutar(self):
        while True:
            self.vista.mostrar_menu()
            opcion = input("Opción: ")
            
            if opcion == "1":
                item = input("Item a agregar: ")
                self.modelo.agregar(item)
                self.vista.mostrar_exito("Item agregado")
            
            elif opcion == "2":
                items = self.modelo.obtener_todos()
                self.vista.mostrar_items(items)
            
            elif opcion == "3":
                indice = int(input("Índice: "))
                item = self.modelo.buscar(indice)
                if item:
                    print(f"Item: {item}")
                else:
                    self.vista.mostrar_error("No encontrado")
            
            elif opcion == "4":
                break

# Uso
# controlador = Controlador()
# controlador.ejecutar()

print("Patrón MVC definido")

"""
────────────────────────────────
EJERCICIO 352 - PATRÓN CQRS SIMPLIFICADO
────────────────────────────────
Descripción: Separa lectura y escritura.

Concepto: Command Query Responsibility Segregation

Código:
"""
from dataclasses import dataclass
from typing import List, Any

# Eventos
class Evento:
    pass

@dataclass
class ItemCreado(Evento):
    id: int
    nombre: str

@dataclass
class ItemActualizado(Evento):
    id: int
    nuevo_nombre: str

@dataclass
class ItemEliminado(Evento):
    id: int

# Command (escritura)
class CommandHandler:
    def __init__(self):
        self.eventos = []
        self.items = {}
        self.next_id = 1
    
    def crear_item(self, nombre):
        evento = ItemCreado(self.next_id, nombre)
        self._aplicar(evento)
        self.eventos.append(evento)
        return self.next_id - 1
    
    def actualizar_item(self, id, nombre):
        if id in self.items:
            evento = ItemActualizado(id, nombre)
            self._aplicar(evento)
            self.eventos.append(evento)
            return True
        return False
    
    def eliminar_item(self, id):
        if id in self.items:
            evento = ItemEliminado(id)
            self._aplicar(evento)
            self.eventos.append(evento)
            return True
        return False
    
    def _aplicar(self, evento):
        if isinstance(evento, ItemCreado):
            self.items[evento.id] = evento.nombre
            self.next_id += 1
        elif isinstance(evento, ItemActualizado):
            self.items[evento.id] = evento.nuevo_nombre
        elif isinstance(evento, ItemEliminado):
            del self.items[evento.id]

# Query (lectura)
class QueryHandler:
    def __init__(self, command_handler):
        self.command_handler = command_handler
    
    def obtener_item(self, id):
        return self.command_handler.items.get(id)
    
    def obtener_todos(self):
        return list(self.command_handler.items.items())
    
    def contar(self):
        return len(self.command_handler.items)

# Uso
cmd = CommandHandler()
qry = QueryHandler(cmd)

cmd.crear_item("Item 1")
cmd.crear_item("Item 2")
cmd.actualizar_item(1, "Item 1 Actualizado")

print("Items:", qry.obtener_todos())
print("Total:", qry.contar())

"""
────────────────────────────────
EJERCICIO 353 - PATRÓN SPECIFICATION
────────────────────────────────
Descripción: Criterios de filtrado reutilizables.

Concepto: Specification pattern

Código:
"""
from abc import ABC, abstractmethod

class Especificacion(ABC):
    @abstractmethod
    def es_satisfecho(self, item) -> bool:
        pass
    
    def and_(self, other):
        return AndEspecificacion(self, other)
    
    def or_(self, other):
        return OrEspecificacion(self, other)
    
    def not_(self):
        return NotEspecificacion(self)

class AndEspecificacion(Especificacion):
    def __init__(self, izq, der):
        self.izq = izq
        self.der = der
    
    def es_satisfecho(self, item) -> bool:
        return self.izq.es_satisfecho(item) and self.der.es_satisfecho(item)

class OrEspecificacion(Especificacion):
    def __init__(self, izq, der):
        self.izq = izq
        self.der = der
    
    def es_satisfecho(self, item) -> bool:
        return self.izq.es_satisfecho(item) or self.der.es_satisfecho(item)

class NotEspecificacion(Especificacion):
    def __init__(self, spec):
        self.spec = spec
    
    def es_satisfecho(self, item) -> bool:
        return not self.spec.es_satisfecho(item)

# Especificaciones concretas
class EsPrecioMayor(Especificacion):
    def __init__(self, precio):
        self.precio = precio
    
    def es_satisfecho(self, item) -> bool:
        return item['precio'] > self.precio

class EsCategoria(Especificacion):
    def __init__(self, categoria):
        self.categoria = categoria
    
    def es_satisfecho(self, item) -> bool:
        return item['categoria'] == self.categoria

# Uso
productos = [
    {"nombre": "Laptop", "precio": 1000, "categoria": "electronics"},
    {"nombre": "Mouse", "precio": 25, "categoria": "electronics"},
    {"nombre": "Camisa", "precio": 50, "categoria": "clothing"},
]

# Filtrar: electronics con precio > 30
especificacion = EsCategoria("electronics").and_(EsPrecioMayor(30))

for p in productos:
    if especificacion.es_satisfecho(p):
        print(f"{p['nombre']}: ${p['precio']}")

"""
────────────────────────────────
EJERCICIO 354 - REPOSITORY CON CACHÉ
────────────────────────────────
Descripción: Repositorio con capa de caché.

Concepto: Cache aside pattern

Código:
"""
from typing import TypeVar, Generic, Optional, List
from dataclasses import dataclass
import time

T = TypeVar('T')

@dataclass
class Entidad:
    id: int

class RepositorioMemoria(Generic[T]):
    def __init__(self):
        self._store: dict[int, T] = {}
        self._next_id = 1
    
    def guardar(self, item: T) -> T:
        if hasattr(item, 'id') and item.id == 0:
            item.id = self._next_id
            self._next_id += 1
        self._store[item.id] = item
        return item
    
    def buscar(self, id: int) -> Optional[T]:
        return self._store.get(id)
    
    def todos(self) -> List[T]:
        return list(self._store.values())

class CacheLRU:
    def __init__(self, capacidad: int):
        self.capacidad = capacidad
        self.cache = {}
    
    def get(self, key) -> Optional[any]:
        if key in self.cache:
            # Mover al final
            self.cache[key] = self.cache.pop(key)
            return self.cache[key]
        return None
    
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacidad:
            # Eliminar el primero (menos reciente)
            oldest = next(iter(self.cache))
            del self.cache[oldest]
        self.cache[key] = value

class RepositorioConCache(RepositorioMemoria):
    def __init__(self, capacidad_cache: int = 100):
        super().__init__()
        self.cache = CacheLRU(capacidad_cache)
    
    def buscar(self, id: int) -> Optional[T]:
        # Buscar en caché primero
        item = self.cache.get(id)
        if item is not None:
            return item
        
        # Si no está en caché, buscar en store
        item = super().buscar(id)
        if item:
            self.cache.put(id, item)
        return item
    
    def guardar(self, item: T) -> T:
        # Invalidar caché al guardar
        if hasattr(item, 'id'):
            self.cache.cache.pop(item.id, None)
        return super().guardar(item)

# Uso
repo = RepositorioConCache()

class Producto(Entidad):
    def __init__(self, id, nombre, precio):
        self.id = id
        self.nombre = nombre
        self.precio = precio

p1 = Producto(0, "Laptop", 1000)
repo.guardar(p1)

# Primera búsqueda - va a DB
print(repo.buscar(1))
# Segunda búsqueda - va a caché
print(repo.buscar(1))

"""
────────────────────────────────
EJERCICIO 355 - EVENT SOURCING BÁSICO
────────────────────────────────
Descripción: Almacena eventos en lugar de estado.

Concepto: Guardar todos los eventos

Código:
"""
from dataclasses import dataclass, field
from typing import List, Callable
from datetime import datetime

@dataclass
class Evento:
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class CuentaCreada(Evento):
    id: int
    nombre: str

@dataclass
class Deposito(Evento):
    cuenta_id: int
    monto: float

@dataclass
class Retiro(Evento):
    cuenta_id: int
    monto: float

class EventStore:
    def __init__(self):
        self._eventos: List[Evento] = []
    
    def append(self, evento: Evento):
        self._eventos.append(evento)
    
    def get_events(self, cuenta_id: int = None) -> List[Evento]:
        if cuenta_id is None:
            return self._eventos.copy()
        return [e for e in self._eventos 
                if hasattr(e, 'cuenta_id') and e.cuenta_id == cuenta_id]

class CuentaBancaria:
    def __init__(self, id: int, nombre: str, event_store: EventStore):
        self.id = id
        self.nombre = nombre
        self.saldo = 0
        self.event_store = event_store
    
    def crear(self):
        self.event_store.append(CuentaCreada(self.id, self.nombre))
    
    def depositar(self, monto: float):
        if monto <= 0:
            raise ValueError("Monto debe ser positivo")
        self.event_store.append(Deposito(self.id, monto))
        self.saldo += monto
    
    def retirar(self, monto: float):
        if monto <= 0:
            raise ValueError("Monto debe ser positivo")
        if monto > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.event_store.append(Retiro(self.id, monto))
        self.saldo -= monto
    
    @staticmethod
    def reconstruir(id: int, nombre: str, eventos: List[Evento]) -> 'CuentaBancaria':
        cuenta = CuentaBancaria(id, nombre, EventStore())
        for evento in eventos:
            if isinstance(evento, Deposito):
                cuenta.saldo += evento.monto
            elif isinstance(evento, Retiro):
                cuenta.saldo -= evento.monto
        return cuenta

# Uso
event_store = EventStore()
cuenta = CuentaBancaria(1, "Juan", event_store)
cuenta.crear()
cuenta.depositar(1000)
cuenta.retirar(250)

print(f"Saldo actual: {cuenta.saldo}")
print(f"Eventos almacenados: {len(event_store.get_events(1))}")

# Reconstruir desde eventos
cuenta2 = CuentaBancaria.reconstruir(1, "Juan", event_store.get_events(1))
print(f"Saldo reconstruido: {cuenta2.saldo}")

"""
────────────────────────────────
EJERCICIO 356 - DECORADOR DE MEMOIZACIÓN AVANZADO
────────────────────────────────
Descripción: Memoización con diferentes estrategias.

Concepto: Cache con LRU, TTL, etc.

Código:
"""
from functools import wraps
from collections import OrderedDict
import time
import hashlib
import pickle

def memoize_lru(maxsize=128):
    cache = OrderedDict()
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Crear clave
            key = (args, tuple(sorted(kwargs.items())))
            
            if key in cache:
                cache.move_to_end(key)
                return cache[key]
            
            result = func(*args, **kwargs)
            
            if len(cache) >= maxsize:
                cache.popitem(last=False)
            
            cache[key] = result
            return result
        
        wrapper.cache = cache
        wrapper.cache_clear = lambda: cache.clear()
        return wrapper
    return decorator

def memoize_ttl(ttl_seconds=60):
    cache = {}
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = (args, tuple(sorted(kwargs.items())))
            now = time.time()
            
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < ttl_seconds:
                    return result
            
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        
        wrapper.cache = cache
        wrapper.cache_clear = lambda: cache.clear()
        return wrapper
    return decorator

def memoize_disk(filename):
    cache = {}
    try:
        with open(filename, 'rb') as f:
            cache = pickle.load(f)
    except:
        pass
    
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = hashlib.md5(pickle.dumps((args, kwargs))).hexdigest()
            
            if key in cache:
                return cache[key]
            
            result = func(*args, **kwargs)
            cache[key] = result
            
            with open(filename, 'wb') as f:
                pickle.dump(cache, f)
            
            return result
        
        return wrapper
    return decorator

# Uso
@memoize_lru(maxsize=3)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(100))  # Rápido

@memoize_ttl(ttl_seconds=5)
def obtener_datos():
    return time.time()

print(obtener_datos())

"""
────────────────────────────────
EJERCICIO 357 - WORKFLOW ENGINE
────────────────────────────────
────────────────────────────────
Descripción: Motor de flujos de trabajo.

Concepto: Ejecutar pasos en secuencia

Código:
"""
from typing import Callable, Any, Dict, List
from dataclasses import dataclass
from enum import Enum

class Estado(Enum):
    PENDIENTE = "pendiente"
    EN_PROCESO = "en_proceso"
    COMPLETADO = "completado"
    FALLIDO = "fallido"

@dataclass
class Paso:
    nombre: str
    accion: Callable
    requiere: List[str] = None
    
    def __post_init__(self):
        if self.requiere is None:
            self.requiere = []

class Workflow:
    def __init__(self, nombre: str):
        self.nombre = nombre
        self.pasos: Dict[str, Paso] = {}
        self.resultados: Dict[str, Any] = {}
        self.estado = Estado.PENDIENTE
    
    def agregar_paso(self, paso: Paso):
        self.pasos[paso.nombre] = paso
    
    def ejecutar(self) -> bool:
        self.estado = Estado.EN_PROCESO
        ejecutados = set()
        
        while len(ejecutados) < len(self.pasos):
            # Buscar paso ejecutable
            ejecutable = None
            for nombre, paso in self.pasos.items():
                if nombre in ejecutados:
                    continue
                
                # Verificar requisitos
                requisitos_cumplidos = all(r in ejecutados for r in paso.requiere)
                
                if requisitos_cumplidos:
                    ejecutable = nombre
                    break
            
            if ejecutable is None:
                self.estado = Estado.FALLIDO
                return False
            
            # Ejecutar paso
            try:
                paso = self.pasos[ejecutable]
                resultado = paso.accion(self.resultados)
                self.resultados[ejecutable] = resultado
                ejecutados.add(ejecutable)
            except Exception as e:
                print(f"Error en paso {ejecutable}: {e}")
                self.estado = Estado.FALLIDO
                return False
        
        self.estado = Estado.COMPLETADO
        return True

# Uso
wf = Workflow("Preparar Café")

wf.agregar_paso(Paso("hervir_agua", lambda r: "agua caliente"))
wf.agregar_paso(Paso("moler_cafe", lambda r: "cafe molido"))
wf.agregar_paso(Paso("mezclar", ["hervir_agua", "moler_cafe"], 
                     lambda r: f"cafe preparado con {r['hervir_agua']} y {r['moler_cafe']}"))

if wf.ejecutar():
    print(f"Workflow completado: {wf.estado}")
    print(f"Resultados: {wf.resultados}")

"""
────────────────────────────────
EJERCICIO 358 - STATE MACHINE
────────────────────────────────
Descripción: Máquina de estados genérica.

Concepto: Transiciones entre estados

Código:
"""
from typing import Callable, Dict, Set
from abc import ABC, abstractmethod

class EstadoMaquina(ABC):
    @abstractmethod
    def entrar(self):
        pass
    
    @abstractmethod
    def salir(self):
        pass

class MaquinaEstados:
    def __init__(self, estado_inicial):
        self.estados: Dict[str, EstadoMaquina] = {}
        self.estado_actual = estado_inicial
        self.transiciones: Dict[tuple, Callable] = {}
    
    def agregar_estado(self, nombre: str, estado: EstadoMaquina):
        self.estados[nombre] = estado
    
    def agregar_transicion(self, desde: str, hacia: str, callback: Callable = None):
        self.transiciones[(desde, hacia)] = callback
    
    def cambiar_estado(self, hacia: str):
        if (self.estado_actual, hacia) not in self.transiciones:
            raise ValueError(f"Transición {self.estado_actual} -> {hacia} no existe")
        
        # Ejecutar callbacks
        callback = self.transiciones[(self.estado_actual, hacia)]
        if callback:
            callback()
        
        # Cambiar estado
        self.estados[self.estado_actual].salir()
        self.estado_actual = hacia
        self.estados[self.estado_actual].entrar()
    
    def get_estado(self):
        return self.estado_actual

# Implementación concreta
class EstadoInactivo(EstadoMaquina):
    def entrar(self):
        print("-> Inactivo")
    
    def salir(self):
        print("Saliendo de Inactivo")

class EstadoActivo(EstadoMaquina):
    def entrar(self):
        print("-> Activo")
    
    def salir(self):
        print("Saliendo de Activo")

class EstadoPausado(EstadoMaquina):
    def entrar(self):
        print("-> Pausado")
    
    def salir(self):
        print("Saliendo de Pausado")

maquina = MaquinaEstados("inactivo")
maquina.agregar_estado("inactivo", EstadoInactivo())
maquina.agregar_estado("activo", EstadoActivo())
maquina.agregar_estado("pausado", EstadoPausado())

maquina.agregar_transicion("inactivo", "activo", lambda: print("Iniciando..."))
maquina.agregar_transicion("activo", "pausado", lambda: print("Pausando..."))
maquina.agregar_transicion("pausado", "activo", lambda: print("Reanudando..."))
maquina.agregar_transicion("activo", "inactivo", lambda: print("Deteniendo..."))

maquina.cambiar_estado("activo")
maquina.cambiar_estado("pausado")
maquina.cambiar_estado("activo")
maquina.cambiar_estado("inactivo")

"""
────────────────────────────────
EJERCICIO 359 - SCHEDULER
────────────────────────────────
Descripción: Programador de tareas.

Concepto: Ejecutar tareas en intervalos

Código:
"""
import time
import threading
from typing import Callable, List
from dataclasses import dataclass
from datetime import datetime, timedelta

@dataclass
class TareaProgramada:
    nombre: str
    funcion: Callable
    intervalo: float  # segundos
    ultima_ejecucion: float = 0
    activa: bool = True

class Scheduler:
    def __init__(self):
        self.tareas: List[TareaProgramada] = []
        self.ejecutando = False
        self.hilo = None
    
    def agregar(self, nombre: str, funcion: Callable, intervalo: float):
        tarea = TareaProgramada(nombre, funcion, intervalo)
        self.tareas.append(tarea)
        return tarea
    
    def iniciar(self):
        self.ejecutando = True
        self.hilo = threading.Thread(target=self._ciclo, daemon=True)
        self.hilo.start()
    
    def detener(self):
        self.ejecutando = False
        if self.hilo:
            self.hilo.join()
    
    def _ciclo(self):
        while self.ejecutando:
            ahora = time.time()
            for tarea in self.tareas:
                if tarea.activa and ahora - tarea.ultima_ejecucion >= tarea.intervalo:
                    try:
                        tarea.funcion()
                    except Exception as e:
                        print(f"Error en tarea {tarea.nombre}: {e}")
                    finally:
                        tarea.ultima_ejecucion = ahora
            time.sleep(0.1)
    
    def pausar(self, nombre: str):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                tarea.activa = False
    
    def reanudar(self, nombre: str):
        for tarea in self.tareas:
            if tarea.nombre == nombre:
                tarea.activa = True

# Uso
contador = [0]

def tarea1():
    contador[0] += 1
    print(f"Tarea 1 ejecutada: {contador[0]}")

def tarea2():
    print(f"Tarea 2: {datetime.now()}")

scheduler = Scheduler()
scheduler.agregar("contador", tarea1, 1.0)  # cada segundo
scheduler.agregar("reloj", tarea2, 3.0)      # cada 3 segundos

scheduler.iniciar()
time.sleep(5)
scheduler.detener()

print("Scheduler detenido")

"""
────────────────────────────────
EJERCICIO 360 - MÓDULO CLI
────────────────────────────────
Descripción: Crear interfaz de línea de comandos.

Concepto: argparse, click

Código:
"""
# Usando argparse
import argparse

def main():
    parser = argparse.ArgumentParser(description="Mi aplicación CLI")
    
    # Argumentos posicionales
    parser.add_argument("nombre", help="Nombre del usuario")
    
    # Opciones
    parser.add_argument("-e", "--edad", type=int, help="Edad del usuario")
    parser.add_argument("-c", "--ciudad", default="Madrid", help="Ciudad")
    parser.add_argument("-v", "--verbose", action="store_true", help="Modo verbose")
    
    # Flags
    parser.add_argument("--debug", action="store_true", help="Modo debug")
    
    args = parser.parse_args()
    
    if args.verbose:
        print("Modo verbose activado")
    
    print(f"Hola {args.nombre}")
    if args.edad:
        print(f"Tienes {args.edad} años")
    print(f"Ciudad: {args.ciudad}")
    
    if args.debug:
        print(f"Argumentos: {args}")

# Ejecutar: python app.py Juan -e 25 -c Barcelona -v --debug

# Usando click (alternativa más simple)
"""
import click

@click.command()
@click.argument("nombre")
@click.option("-e", "--edad", type=int, prompt=True)
@click.option("-c", "--ciudad", default="Madrid")
@click.option("-v", "--verbose", is_flag=True)
def cli(nombre, edad, ciudad, verbose):
    click.echo(f"Hola {nombre}")
    if verbose:
        click.echo("Modo verbose")
    click.echo(f"Edad: {edad}")
    click.echo(f"Ciudad: {ciudad}")

if __name__ == "__main__":
    cli()
"""

# Ejecutar con click: python app.py Juan --edad 25 --ciudad Barcelona -v

print("CLI configurado")

# ============================================================
#        EJERCICIOS 401-450: INTEGRACIÓN Y APIS
# ============================================================

"""
────────────────────────────────
EJERCICIO 361 - API REST SIMPLE CON FLASK
────────────────────────────────
Descripción: Crear API REST básica.

Concepto: Flask, rutas, JSON

Código:
"""
# archivo: app.py
"""
from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos en memoria
productos = []
next_id = 1

# GET todos
@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos)

# GET uno
@app.route('/productos/<int:id>', methods=['GET'])
def obtener_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if producto:
        return jsonify(producto)
    return jsonify({'error': 'No encontrado'}), 404

# POST crear
@app.route('/productos', methods=['POST'])
def crear_producto():
    global next_id
    data = request.get_json()
    producto = {
        'id': next_id,
        'nombre': data.get('nombre'),
        'precio': data.get('precio')
    }
    productos.append(producto)
    next_id += 1
    return jsonify(producto), 201

# PUT actualizar
@app.route('/productos/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    producto = next((p for p in productos if p['id'] == id), None)
    if not producto:
        return jsonify({'error': 'No encontrado'}), 404
    
    data = request.get_json()
    producto['nombre'] = data.get('nombre', producto['nombre'])
    producto['precio'] = data.get('precio', producto['precio'])
    return jsonify(producto)

# DELETE eliminar
@app.route('/productos/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    global productos
    productos = [p for p in productos if p['id'] != id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True, port=5000)
"""

print("API REST con Flask configurada (descomenta para usar)")

"""
────────────────────────────────
EJERCICIO 362 - WEBSOCKET SERVER
────────────────────────────────
Descripción: Servidor de WebSocket simple.

Concepto: ws, comunicación bidireccional

Código:
"""
"""
# Servidor WebSocket simple
import asyncio
import websockets

clientes = set()

async def manejar_cliente(websocket, path):
    clientes.add(websocket)
    try:
        async for mensaje in websocket:
            # Broadcast a todos los clientes
            for cliente in clientes:
                if cliente != websocket:
                    await cliente.send(f"Echo: {mensaje}")
    finally:
        clientes.remove(websocket)

async def main():
    async with websockets.serve(manejar_cliente, "localhost", 8765):
        print("Servidor WebSocket en puerto 8765")
        await asyncio.Future()  # Ejecutar forever

asyncio.run(main())

# Cliente
"""
import asyncio
import websockets

async def cliente():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        await websocket.send("Hola servidor")
        respuesta = await websocket.recv()
        print(respuesta)

asyncio.run(cliente())
"""

print("WebSocket configurado")

"""
────────────────────────────────
EJERCICIO 363 - GRPC CLIENTE-SERVIDOR
────────────────────────────────
────────────────────────────────
Descripción: gRPC básico.

Concepto: Protocol Buffers + HTTP/2

Código:
"""
# archivo: service.proto
"""
syntax = "proto3";

service Calculator {
    rpc Add(AddRequest) returns (AddResponse);
    rpc Multiply(MultiplyRequest) returns (MultiplyResponse);
    rpc StreamNumbers(StreamRequest) returns (stream StreamResponse);
}

message AddRequest {
    int32 a = 1;
    int32 b = 2;
}

message AddResponse {
    int32 result = 1;
}

message MultiplyRequest {
    int32 a = 1;
    int32 b = 2;
}

message MultiplyResponse {
    int32 result = 1;
}

message StreamRequest {
    int32 count = 1;
}

message StreamResponse {
    int32 number = 1;
}
"""

# servidor.py
"""
from concurrent import futures
import grpc
import service_pb2
import service_pb2_grpc

class Calculadora(service_pb2_grpc.CalculatorServicer):
    def Add(self, request, context):
        return service_pb2.AddResponse(result=request.a + request.b)
    
    def Multiply(self, request, context):
        return service_pb2.MultiplyResponse(result=request.a * request.b)
    
    def StreamNumbers(self, request, context):
        for i in range(request.count):
            yield service_pb2.StreamResponse(number=i+1)

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    service_pb2_grpc.add_CalculatorServicer_to_server(
        Calculadora(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
"""

# cliente.py
"""
import grpc
import service_pb2
import service_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = service_pb2_grpc.CalculatorStub(channel)
    
    # Simple
    response = stub.Add(service_pb2.AddRequest(a=10, b=20))
    print(f"Add: {response.result}")
    
    # Streaming
    for resp in stub.StreamNumbers(service_pb2.StreamRequest(count=5)):
        print(f"Number: {resp.number}")

if __name__ == '__main__':
    run()
"""

print("gRPC configurado")

"""
────────────────────────────────
EJERCICIO 364 - CONSUMIR API EXTERNA
────────────────────────────────
Descripción: Hacer requests a APIs.

Concepto: requests, manejo de errores

Código:
"""
import requests
from typing import Optional
import json

class ClienteAPI:
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json',
            'User-Agent': 'PythonAPIClient/1.0'
        })
    
    def get(self, endpoint: str, params: Optional[dict] = None) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.get(url, params=params, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
    
    def post(self, endpoint: str, data: dict) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.post(url, json=data, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
    
    def put(self, endpoint: str, data: dict) -> dict:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.put(url, json=data, timeout=self.timeout)
        response.raise_for_status()
        return response.json()
    
    def delete(self, endpoint: str) -> bool:
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        response = self.session.delete(url, timeout=self.timeout)
        return response.status_code == 204

# Uso
try:
    api = ClienteAPI("https://jsonplaceholder.typicode.com")
    
    # GET
    usuarios = api.get("/users")
    print(f"Usuarios: {len(usuarios)}")
    
    # POST
    nuevo = api.post("/posts", {
        "title": "Título",
        "body": "Contenido",
        "userId": 1
    })
    print(f"Nuevo post: {nuevo['id']}")
    
except requests.exceptions.RequestException as e:
    print(f"Error de conexión: {e}")

"""
────────────────────────────────
EJERCICIO 365 - OAUTH2 SIMPLE
────────────────────────────────
Descripción: Flujo OAuth2 básico.

Concepto: Autorización, tokens

Código:
"""
import secrets
import time
from dataclasses import dataclass
from typing importimport hashlib

 Dict, Optional
@dataclass
class Usuario:
    id: str
    nombre: str

class OAuth2Server:
    def __init__(self):
        self.clientes: Dict[str, dict] = {}
        self.codes: Dict[str, dict] = {}
        self.tokens: Dict[str, dict] = {}
    
    def registrar_cliente(self, cliente_id: str, redirect_uri: str):
        self.clientes[cliente_id] = {
            'redirect_uri': redirect_uri,
            'client_secret': secrets.token_urlsafe(32)
        }
    
    def generar_authorization_url(self, cliente_id: str, redirect_uri: str, 
                                   state: str) -> str:
        code = secrets.token_urlsafe(32)
        self.codes[code] = {
            'cliente_id': cliente_id,
            'redirect_uri': redirect_uri,
            'state': state,
            'expira': time.time() + 600
        }
        return f"{redirect_uri}?code={code}&state={state}"
    
    def intercambiar_code_por_token(self, code: str, cliente_id: str, 
                                   client_secret: str) -> Optional[dict]:
        code_data = self.codes.get(code)
        
        if not code_data:
            return None
        
        if code_data['expira'] < time.time():
            del self.codes[code]
            return None
        
        if code_data['cliente_id'] != cliente_id:
            return None
        
        cliente = self.clientes.get(cliente_id)
        if not cliente or cliente['client_secret'] != client_secret:
            return None
        
        # Generar token
        access_token = secrets.token_urlsafe(32)
        refresh_token = secrets.token_urlsafe(32)
        
        self.tokens[access_token] = {
            'refresh_token': refresh_token,
            'expira': time.time() + 3600,
            'usuario': 'user_123'
        }
        
        return {
            'access_token': access_token,
            'token_type': 'Bearer',
            'expires_in': 3600,
            'refresh_token': refresh_token
        }

# Uso
oauth = OAuth2Server()
oauth.registrar_cliente('mi_app', 'https://miapp.com/callback')

# Paso 1: Redirect a autorización
auth_url = oauth.generar_authorization_url('mi_app', 'https://miapp.com/callback', 'xyz')
print(f"URL autorización: {auth_url}")

# Paso 2: Intercambiar código por token
token = oauth.intercambiar_code_por_token(
    code='codigo_del_url',
    cliente_id='mi_app',
    client_secret='secreto'
)
print(f"Token: {token}")

"""
────────────────────────────────
EJERCICIO 366 - WEBSCRAPING
────────────────────────────────
Descripción: Extraer datos de páginas web.

Concepto: BeautifulSoup, requests

Código:
"""
import requests
from bs4 import BeautifulSoup

def extraer_titulos(url: str) -> list[str]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    titulos = []
    for titulo in soup.find_all('h2'):
        titulos.append(tulo.get_text(strip=True))
    
    return titulos

def extraer_tablas(url: str, indice_tabla: int = 0) -> list[dict]:
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    tablas = soup.find_all('table')
    
    if indice_tabla >= len(tablas):
        return []
    
    tabla = tablas[indice_tabla]
    headers = [th.get_text(strip=True) for th in tabla.find_all('th')]
    filas = []
    
    for tr in tabla.find_all('tr')[1:]:
        celdas = [td.get_text(strip=True) for td in tr.find_all('td')]
        if celdas:
            filas.append(dict(zip(headers, celdas)))
    
    return filas

# Ejemplo con Wikipedia
# url = "https://es.wikipedia.org/wiki/Python"
# titulos = extraer_titulos(url)
# print(titulos)

# Scraping ético
"""
- Respetar robots.txt
- No hacer demasiadas requests
- Identificarse con User-Agent
- No evadir autenticación
"""

print("Web scraping configurado")

"""
────────────────────────────────
EJERCICIO 367 - TESTING AVANZADO CON MOCKS
────────────────────────────────
Descripción: Pruebas con objetos simulados.

Concepto: unittest.mock, patch

Código:
"""
import unittest
from unittest.mock import Mock, patch, MagicMock

# Ejemplo: Probar código que hace requests
class ClienteServidor:
    def __init__(self, api_url):
        self.api_url = api_url
    
    def obtener_usuario(self, id):
        import requests
        response = requests.get(f"{self.api_url}/users/{id}")
        return response.json()

# Test con mock
class TestClienteServidor(unittest.TestCase):
    @patch('requests.get')
    def test_obtener_usuario(self, mock_get):
        # Configurar mock
        mock_response = Mock()
        mock_response.json.return_value = {'id': 1, 'name': 'John'}
        mock_get.return_value = mock_response
        
        # Ejecutar
        cliente = ClienteServidor("https://api.example.com")
        resultado = cliente.obtener_usuario(1)
        
        # Verificar
        self.assertEqual(resultado['name'], 'John')
        mock_get.assert_called_once_with("https://api.example.com/users/1")
    
    @patch('requests.get')
    def test_obtener_usuario_error(self, mock_get):
        mock_get.side_effect = Exception("Network error")
        
        with self.assertRaises(Exception):
            cliente = ClienteServidor("https://api.example.com")
            cliente.obtener_usuario(1)

# Test con MagicMock (más flexible)
class TestMagicMock(unittest.TestCase):
    def testMagicMock(self):
        mock = MagicMock()
        
        # Configurar retorno
        mock.method.return_value = "valor"
        mock.method("arg")
        
        # Verificar llamada
        mock.method.assert_called_with("arg")

print("Testing con mocks configurado")

# ============================================================
#        EJERCICIOS 451-500: PROYECTOS FINALES
# ============================================================

"""
────────────────────────────────
EJERCICIO 368 - CHAT EN TIEMPO REAL
────────────────────────────────
Descripción: Sistema de chat básico.

Concepto: WebSocket, rooms

Código:
"""
"""
# Servidor de chat con Flask-SocketIO
from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('join')
def on_join(data):
    room = data['room']
    join_room(room)
    send({'message': f'Usuario joined {room}'}, room=room)

@socketio.on('leave')
def on_leave(data):
    room = data['room']
    leave_room(room)
    send({'message': f'Usuario left {room}'}, room=room)

@socketio.on('message')
def on_message(data):
    room = data['room']
    message = data['message']
    send({'message': message}, room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True)
"""

# Cliente JavaScript (index.html)
"""
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.socket.io/4.0.0/socket.io.min.js"></script>
</head>
<body>
    <input id="room" placeholder="Room">
    <input id="message" placeholder="Message">
    <button onclick="send()">Send</button>
    <div id="messages"></div>
    
    <script>
        const socket = io();
        
        function join() {
            socket.emit('join', {room: document.getElementById('room').value});
        }
        
        function send() {
            socket.emit('message', {
                room: document.getElementById('room').value,
                message: document.getElementById('message').value
            });
        }
        
        socket.on('message', function(msg) {
            document.getElementById('messages').innerHTML += '<p>' + msg.message + '</p>';
        });
    </script>
</body>
</html>
"""

print("Chat en tiempo real configurado")

"""
────────────────────────────────
EJERCICIO 369 - SISTEMA DE NOTIFICACIONES
────────────────────────────────
Descripción: Sistema de notificaciones multi-canal.

Concepto: Push, Email, SMS

Código:
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List
import time

@dataclass
class Notificacion:
    destinatario: str
    titulo: str
    mensaje: str
    canal: str = "email"

class CanalNotificacion(ABC):
    @abstractmethod
    def enviar(self, notificacion: Notificacion) -> bool:
        pass

class EmailChannel(CanalNotificacion):
    def enviar(self, notificacion: Notificacion) -> bool:
        print(f"[EMAIL] Enviando a {notificacion.destinatario}: {notificacion.titulo}")
        time.sleep(0.1)  # Simular delay
        return True

class SMSChannel(CanalNotificacion):
    def enviar(self, notificacion: Notificacion) -> bool:
        print(f"[SMS] Enviando a {notificacion.destinatario}: {notificacion.mensaje}")
        time.sleep(0.1)
        return True

class PushChannel(CanalNotificacion):
    def enviar(self, notificacion: Notificacion) -> bool:
        print(f"[PUSH] Enviando a {notificacion.destinatario}: {notificacion.mensaje}")
        time.sleep(0.1)
        return True

class GestorNotificaciones:
    def __init__(self):
        self.canales: dict[str, CanalNotificacion] = {}
    
    def registrar_canal(self, nombre: str, canal: CanalNotificacion):
        self.canales[nombre] = canal
    
    def enviar(self, notificacion: Notificacion) -> bool:
        canal = self.canales.get(notificacion.canal)
        if canal:
            return canal.enviar(notificacion)
        return False
    
    def enviar_multi_canal(self, notificacion: Notificacion, canales: List[str]) -> dict:
        resultados = {}
        for canal in canales:
            resultados[canal] = self.enviar(notificacion)
        return resultados

# Uso
gestor = GestorNotificaciones()
gestor.registrar_canal("email", EmailChannel())
gestor.registrar_canal("sms", SMSChannel())
gestor.registrar_canal("push", PushChannel())

notif = Notificacion("user@example.com", "Bienvenido", "Gracias por registrarte")
gestor.enviar(notif)

gestor.enviar_multi_canal(notif, ["email", "push"])

"""
────────────────────────────────
EJERCICIO 370 - SISTEMA DE AUTENTICACIÓN JWT
────────────────────────────────
Descripción: Autenticación con JSON Web Tokens.

Concepto: JWT, tokens, refresh

Código:
"""
import jwt
import time
import secrets
from dataclasses import dataclass
from typing import Optional

@dataclass
class TokenPayload:
    usuario_id: str
    email: str
    exp: int
    iat: int

class GestorJWT:
    def __init__(self, secret: str, algoritmo: str = "HS256"):
        self.secret = secret
        self.algoritmo = algoritmo
    
    def crear_token(self, usuario_id: str, email: str, expira_en: int = 3600) -> str:
        ahora = int(time.time())
        payload = {
            'usuario_id': usuario_id,
            'email': email,
            'iat': ahora,
            'exp': ahora + expira_en
        }
        return jwt.encode(payload, self.secret, algorithm=self.algoritmo)
    
    def verificar_token(self, token: str) -> Optional[TokenPayload]:
        try:
            payload = jwt.decode(token, self.secret, algorithms=[self.algoritmo])
            return TokenPayload(**payload)
        except jwt.ExpiredSignatureError:
            print("Token expirado")
            return None
        except jwt.InvalidTokenError:
            print("Token inválido")
            return None
    
    def refresh_token(self, token: str, expira_en: int = 3600) -> Optional[str]:
        payload = self.verificar_token(token)
        if payload:
            return self.crear_token(payload.usuario_id, payload.email, expira_en)
        return None

# Uso
gestor = GestorJWT(secrets.token_urlsafe(32))

# Crear token
token = gestor.crear_token("user123", "user@example.com")
print(f"Token: {token[:50]}...")

# Verificar
payload = gestor.verificar_token(token)
if payload:
    print(f"Usuario: {payload.usuario_id}, Email: {payload.email}")

# Refresh
nuevo_token = gestor.refresh_token(token)
print(f"Nuevo token: {nuevo_token[:50] if nuevo_token else 'None'}...")

"""
────────────────────────────────
EJERCICIO 371 - CARGO MANAGER
────────────────────────────────
────────────────────────────────
Descripción: Gestor de carga de archivos.

Concepto: Upload, procesamiento

Código:
"""
import os
import hashlib
import time
from dataclasses import dataclass
from typing import Optional

@dataclass
class Archivo:
    nombre: str
    tamano: int
    hash: str
    ruta: str
    timestamp: float

class GestorArchivos:
    def __init__(self, directorio_subidas: str = "uploads"):
        self.directorio = directorio_subidas
        os.makedirs(directorio_subidas, exist_ok=True)
    
    def guardar(self, nombre: str, contenido: bytes) -> Archivo:
        # Generar nombre único
        timestamp = time.time()
        hash_contenido = hashlib.md5(contenido).hexdigest()
        
        # Nombre con hash para evitar colisiones
        nombre_final = f"{timestamp}_{hash_contenido[:8]}_{nombre}"
        ruta = os.path.join(self.directorio, nombre_final)
        
        with open(ruta, 'wb') as f:
            f.write(contenido)
        
        return Archivo(
            nombre=nombre,
            tamano=len(contenido),
            hash=hashlib.sha256(contenido).hexdigest(),
            ruta=ruta,
            timestamp=timestamp
        )
    
    def obtener(self, hash: str) -> Optional[Archivo]:
        for filename in os.listdir(self.directorio):
            ruta = os.path.join(self.directorio, filename)
            if os.path.isfile(ruta):
                with open(ruta, 'rb') as f:
                    contenido = f.read()
                    if hashlib.sha256(contenido).hexdigest() == hash:
                        return Archivo(
                            nombre=filename.split('_', 2)[2],
                            tamano=len(contenido),
                            hash=hash,
                            ruta=ruta,
                            timestamp=os.path.getmtime(ruta)
                        )
        return None
    
    def eliminar(self, hash: str) -> bool:
        archivo = self.obtener(hash)
        if archivo:
            os.remove(archivo.ruta)
            return True
        return False

# Uso
gestor = GestorArchivos()
archivo = gestor.guardar("documento.pdf", b"Contenido del PDF")
print(f"Archivo guardado: {archivo.hash}")

recuperado = gestor.obtener(archivo.hash)
print(f"Recuperado: {recuperado.nombre}")

"""
────────────────────────────────
EJERCICIO 372 - rate-limiter
────────────────────────────────
Descripción: Limitar tasa de requests.

Concepto: Token bucket, sliding window

Código:
"""
import time
from collections import defaultdict

class RateLimiter:
    def __init__(self, max_requests: int, ventana: int):
        """
        max_requests: máximo de requests permitidos
        ventana: ventana de tiempo en segundos
        """
        self.max_requests = max_requests
        self.ventana = ventana
        self.requests = defaultdict(list)
    
    def permitir(self, cliente_id: str) -> bool:
        ahora = time.time()
        
        # Limpiar requests antiguos
        self.requests[cliente_id] = [
            t for t in self.requests[cliente_id]
            if ahora - t < self.ventana
        ]
        
        # Verificar límite
        if len(self.requests[cliente_id]) >= self.max_requests:
            return False
        
        # Registrar request
        self.requests[cliente_id].append(ahora)
        return True
    
    def get_remaining(self, cliente_id: str) -> int:
        ahora = time.time()
        requests_recientes = [
            t for t in self.requests[cliente_id]
            if ahora - t < self.ventana
        ]
        return max(0, self.max_requests - len(requests_recientes))

# Uso
limiter = RateLimiter(max_requests=5, ventana=60)

for i in range(7):
    resultado = limiter.permitir("cliente_1")
    print(f"Request {i+1}: {'Permitido' if resultado else 'Bloqueado'}")

print(f"Requests restantes: {limiter.get_remaining('cliente_1')}")

"""
────────────────────────────────
EJERCICIO 373 - CACHE DISTRIBUIDO SIMPLE
────────────────────────────────
Descripción: Sistema de caché básico con expiración.

Concepto: TTL, eviction

Código:
"""
import time
import threading
from typing import Any, Optional
import hashlib

class CacheEntry:
    def __init__(self, valor: Any, ttl: float):
        self.valor = valor
        self.expira_en = time.time() + ttl
    
    def esta_expirado(self) -> bool:
        return time.time() > self.expira_en

class CacheDistribuido:
    def __init__(self, default_ttl: float = 300):
        self.cache: dict[str, CacheEntry] = {}
        self.default_ttl = default_ttl
        self.lock = threading.RLock()
    
    def set(self, clave: str, valor: Any, ttl: Optional[float] = None):
        ttl = ttl or self.default_ttl
        with self.lock:
            self.cache[clave] = CacheEntry(valor, ttl)
    
    def get(self, clave: str) -> Optional[Any]:
        with self.lock:
            if clave not in self.cache:
                return None
            
            entry = self.cache[clave]
            if entry.esta_expirado():
                del self.cache[clave]
                return None
            
            return entry.valor
    
    def delete(self, clave: str) -> bool:
        with self.lock:
            if clave in self.cache:
                del self.cache[clave]
                return True
            return False
    
    def clear(self):
        with self.lock:
            self.cache.clear()
    
    def keys(self) -> list[str]:
        with self.lock:
            return list(self.cache.keys())
    
    def cleanup(self):
        """Limpiar entradas expiradas"""
        with self.lock:
            expiradas = [
                k for k, v in self.cache.items()
                if v.esta_expirado()
            ]
            for k in expiradas:
                del self.cache[k]

# Uso
cache = CacheDistribuito(default_ttl=60)

cache.set("usuario:1", {"nombre": "Juan", "edad": 30})
print(cache.get("usuario: Con TTL1"))

# corto
cache.set("temp", "valor", ttl=1)
time.sleep(1.1)
print(cache.get("temp"))  # None (expirado)

"""
────────────────────────────────
EJERCICIO 374 - JOB QUEUE
────────────────────────────────
Descripción: Cola de trabajos asíncronos.

Concepto: Queue, workers, retry

Código:
"""
import time
import threading
import queue
from dataclasses import dataclass
from typing import Callable, Any, Optional
from enum import Enum
import uuid

class EstadoJob(Enum):
    PENDIENTE = "pendiente"
    PROCESANDO = "procesando"
    COMPLETADO = "completado"
    FALLIDO = "fallido"

@dataclass
class Job:
    id: str
    funcion: Callable
    args: tuple
    kwargs: dict
    estado: EstadoJob = EstadoJob.PENDIENTE
    resultado: Any = None
    error: Optional[str] = None
    intentos: int = 0

class JobQueue:
    def __init__(self, max_workers: int = 2, max_reintentos: int = 3):
        self.queue = queue.Queue()
        self.jobs: dict[str, Job] = {}
        self.max_workers = max_workers
        self.max_reintentos = max_reintentos
        self.ejecutando_workers = 0
        self.lock = threading.Lock()
        
        # Iniciar workers
        for _ in range(max_workers):
            t = threading.Thread(target=self._worker, daemon=True)
            t.start()
    
    def enqueue(self, funcion: Callable, *args, **kwargs) -> str:
        job_id = str(uuid.uuid4())[:8]
        job = Job(
            id=job_id,
            funcion=funcion,
            args=args,
            kwargs=kwargs
        )
        self.jobs[job_id] = job
        self.queue.put(job_id)
        return job_id
    
    def _worker(self):
        while True:
            try:
                job_id = self.queue.get(timeout=1)
            except queue.Empty:
                continue
            
            with self.lock:
                self.ejecutando_workers += 1
                job = self.jobs[job_id]
            
            job.estado = EstadoJob.PROCESANDO
            job.intentos += 1
            
            try:
                job.resultado = job.funcion(*job.args, **job.kwargs)
                job.estado = EstadoJob.COMPLETADO
            except Exception as e:
                job.error = str(e)
                if job.intentos < self.max_reintentos:
                    job.estado = EstadoJob.PENDIENTE
                    self.queue.put(job_id)
                else:
                    job.estado = EstadoJob.FALLIDO
            
            with self.lock:
                self.ejecutando_workers -= 1
            
            self.queue.task_done()
    
    def get_estado(self, job_id: str) -> Optional[Job]:
        return self.jobs.get(job_id)
    
    def esperar(self, job_id: str):
        job = self.jobs.get(job_id)
        if job:
            while job.estado in (EstadoJob.PENDIENTE, EstadoJob.PROCESANDO):
                time.sleep(0.1)
            return job

# Uso
def tarea_larga(n):
    time.sleep(2)
    return n * 2

job_queue = JobQueue(max_workers=2)

job_id = job_queue.enqueue(tarea_larga, 5)
print(f"Job {job_id} enqueued")

job = job_queue.esperar(job_id)
print(f"Job {job_id}: {job.estado.value}, Resultado: {job.resultado}")

"""
────────────────────────────────
EJERCICIO 375 - CQRS COMPLETO
────────────────────────────────
────────────────────────────────
Descripción: Implementación CQRS completa.

Concepto: Commands, Queries, Handlers

Código:
"""
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Generic, TypeVar
import uuid
import time

# Commands
class Command(ABC):
    pass

@dataclass
class CrearProductoCommand(Command):
    nombre: str
    precio: float

@dataclass
class ActualizarPrecioCommand(Command):
    producto_id: str
    nuevo_precio: float

@dataclass
class EliminarProductoCommand(Command):
    producto_id: str

# Queries
class Query(ABC):
    pass

@dataclass
class GetProductoQuery(Query):
    producto_id: str

@dataclass
class ListProductosQuery(Query):
    pass

# Eventos
class Evento:
    pass

@dataclass
class ProductoCreado(Evento):
    producto_id: str
    nombre: str
    precio: float
    timestamp: float = field(default_factory=time.time)

# Handlers
class CommandHandler:
    def __init__(self):
        self.productos = {}
        self.event_store = []
    
    def handle(self, command: Command):
        if isinstance(command, CrearProductoCommand):
            return self._crear_producto(command)
        elif isinstance(command, ActualizarPrecioCommand):
            return self._actualizar_precio(command)
        elif isinstance(command, EliminarProductoCommand):
            return self._eliminar_producto(command)
    
    def _crear_producto(self, cmd: CrearProductoCommand):
        producto_id = str(uuid.uuid4())[:8]
        evento = ProductoCreado(producto_id, cmd.nombre, cmd.precio)
        self.event_store.append(evento)
        
        self.productos[producto_id] = {
            'id': producto_id,
            'nombre': cmd.nombre,
            'precio': cmd.precio
        }
        return producto_id
    
    def _actualizar_precio(self, cmd: ActualizarPrecioCommand):
        if cmd.producto_id in self.productos:
            self.productos[cmd.producto_id]['precio'] = cmd.nuevo_precio
            return True
        return False
    
    def _eliminar_producto(self, cmd: EliminarProductoCommand):
        if cmd.producto_id in self.productos:
            del self.productos[cmd.producto_id]
            return True
        return False

class QueryHandler:
    def __init__(self, command_handler: CommandHandler):
        self.command_handler = command_handler
    
    def handle(self, query: Query):
        if isinstance(query, GetProductoQuery):
            return self._get_producto(query)
        elif isinstance(query, ListProductosQuery):
            return self._list_productos(query)
    
    def _get_producto(self, query: GetProductoQuery):
        return self.command_handler.productos.get(query.producto_id)
    
    def _list_productos(self, query: ListProductosQuery):
        return list(self.command_handler.productos.values())

# Uso
cmd_handler = CommandHandler()
qry_handler = QueryHandler(cmd_handler)

# Commands
id = cmd_handler.handle(CrearProductoCommand("Laptop", 1000))
cmd_handler.handle(ActualizarPrecioCommand(id, 899))

# Queries
producto = qry_handler.handle(GetProductoQuery(id))
print(producto)

todos = qry_handler.handle(ListProductosQuery())
print(todos)

"""
────────────────────────────────
EJERCICIO 376 - SERVICE REGISTRY
────────────────────────────────
Descripción: Registro de servicios para microservicios.

Concepto: Health check, discovery

Código:
"""
import time
import threading
from dataclasses import dataclass
from typing import Dict, Optional, List
from enum import Enum

class EstadoServicio(Enum):
    SALUDABLE = "saludable"
    NO_SALUDABLE = "no_saludable"
    DESCONOCIDO = "desconocido"

@dataclass
class Servicio:
    nombre: str
    host: str
    puerto: int
    estado: EstadoServicio = EstadoServicio.DESCONOCIDO
    ultima_vez_sano: float = 0
    metadatos: Dict = None
    
    def __post_init__(self):
        if self.metadatos is None:
            self.metadatos = {}

class ServiceRegistry:
    def __init__(self, health_check_interval: int = 30):
        self.servicios: Dict[str, Servicio] = {}
        self.health_check_interval = health_check_interval
        self.lock = threading.Lock()
        self.health_checks: Dict[str, callable] = {}
        
        # Iniciar health checks
        threading.Thread(target=self._health_check_loop, daemon=True).start()
    
    def registrar(self, servicio: Servicio):
        with self.lock:
            self.servicios[servicio.nombre] = servicio
            print(f"Servicio registrado: {servicio.nombre}")
    
    def desregistrar(self, nombre: str):
        with self.lock:
            if nombre in self.servicios:
                del self.servicios[nombre]
                print(f"Servicio desregistrado: {nombre}")
    
    def obtener(self, nombre: str) -> Optional[Servicio]:
        return self.servicios.get(nombre)
    
    def obtener_todos(self) -> List[Servicio]:
        return list(self.servicios.values())
    
    def registrar_health_check(self, nombre: str, check_func: callable):
        self.health_checks[nombre] = check_func
    
    def _health_check_loop(self):
        while True:
            with self.lock:
                for nombre, servicio in self.servicios.items():
                    if nombre in self.health_checks:
                        try:
                            sano = self.health_checks[nombre](servicio)
                            servicio.estado = EstadoServicio.SALUDABLE if sano else EstadoServicio.NO_SALUDABLE
                            if sano:
                                servicio.ultima_vez_sano = time.time()
                        except:
                            servicio.estado = EstadoServicio.NO_SALUDABLE
                    else:
                        servicio.estado = EstadoServicio.SALUDABLE
            
            time.sleep(self.health_check_interval)

# Uso
registry = ServiceRegistry()

def health_check_mysql(servicio):
    # Simular check
    return True

registry.registrar(Servicio("api-gateway", "localhost", 8080))
registry.registrar(Servicio("user-service", "localhost", 8081))
registry.registrar_health_check("user-service", health_check_mysql)

time.sleep(2)
print([s.nombre for s in registry.obtener_todos()])

"""
────────────────────────────────
EJERCICIO 377 - AUDIT LOG
────────────────────────────────
Descripción: Registro de auditoría.

Concepto: Tracking de acciones

Código:
"""
import json
import time
from dataclasses import dataclass, asdict
from typing import Any, Dict, Optional
from datetime import datetime
import threading

@dataclass
class AuditEntry:
    timestamp: float
    usuario: str
    accion: str
    recurso: str
    detalles: Dict[str, Any]
    ip: Optional[str] = None
    success: bool = True

class AuditLog:
    def __init__(self, archivo: str = "audit.log"):
        self.archivo = archivo
        self.lock = threading.Lock()
    
    def log(self, usuario: str, accion: str, recurso: str, 
            detalles: Dict[str, Any], ip: Optional[str] = None,
            success: bool = True):
        entry = AuditEntry(
            timestamp=time.time(),
            usuario=usuario,
            accion=accion,
            recurso=recurso,
            detalles=detalles,
            ip=ip,
            success=success
        )
        
        with self.lock:
            with open(self.archivo, 'a') as f:
                f.write(json.dumps(asdict(entry)) + '\n')
    
    def buscar(self, filtros: Dict[str, Any] = None, limite: int = 100) -> list:
        resultados = []
        
        with self.lock:
            try:
                with open(self.archivo, 'r') as f:
                    for line in f:
                        entry = json.loads(line)
                        
                        if filtros:
                            match = all(entry.get(k) == v for k, v in filtros.items())
                            if match:
                                resultados.append(entry)
                        else:
                            resultados.append(entry)
                        
                        if len(resultados) >= limite:
                            break
            except FileNotFoundError:
                pass
        
        return resultados

# Uso
audit = AuditLog("audit.log")

# Simular acciones
audit.log("juan@email.com", "LOGIN", "auth", {"metodo": "password"}, "192.168.1.1")
audit.log("juan@email.com", "CREATE", "documento", {"titulo": "Reporte"}, "192.168.1.1")
audit.log("admin@email.com", "DELETE", "usuario", {"usuario_id": "123"}, "192.168.1.1", False)

# Buscar
resultados = audit.buscar({"usuario": "juan@email.com"})
print(resultados)

"""
────────────────────────────────
EJERCICIO 378 - DISTRIBUTED LOCK
────────────────────────────────
Descripción: Lock distribuido básico.

Concepto: Mutex distribuido

Código:
"""
import time
import threading
import fcntl
import os
from contextlib import contextmanager
from typing import Optional

class DistributedLock:
    def __init__(self, nombre: str, directorio: str = "/tmp/locks"):
        self.directorio = directorio
        os.makedirs(directorio, exist_ok=True)
        self.lock_file = os.path.join(directorio, f"{nombre}.lock")
        self.file = None
    
    def acquire(self, timeout: float = 10) -> bool:
        inicio = time.time()
        
        while True:
            try:
                self.file = open(self.lock_file, 'w')
                fcntl.flock(self.file.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                self.file.write(str(os.getpid()))
                self.file.flush()
                return True
            except (IOError, OSError):
                if time.time() - inicio >= timeout:
                    return False
                time.sleep(0.1)
    
    def release(self):
        if self.file:
            try:
                fcntl.flock(self.file.fileno(), fcntl.LOCK_UN)
                self.file.close()
            except:
                pass
            self.file = None
    
    @contextmanager
    def lock(self, timeout: float = 10):
        if self.acquire(timeout):
            try:
                yield True
            finally:
                self.release()
        else:
            yield False

# Uso
lock = DistributedLock("mi-recurso")

# En un thread
with lock.lock() as acquired