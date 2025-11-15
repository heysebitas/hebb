# Sistema de Semaforo Inteligente - Red Hebbiana Multicapa

## Descripcion del Proyecto

Sistema de control de trafico inteligente que utiliza una **Red Neuronal Hebbiana Multicapa** para aprender y decidir que semaforo activar en una interseccion de 4 direcciones segun el flujo de trafico.

---

## Problema a Resolver

**Objetivo**: Aprender a dar prioridad en una interseccion segun la cantidad de carros esperando en cada direccion (Norte, Sur, Este, Oeste).

**Aplicacion real**: Optimizar el flujo vehicular reduciendo tiempos de espera.


### Parametros:
- **Entradas**: 4 (trafico en cada direccion: 0-20 carros)
- **Capa oculta**: 6 neuronas con activacion `tanh`
- **Salidas**: 6 decisiones posibles
- **Algoritmo**: Aprendizaje Hebbiano (`W += y * x`)

---

## Datos de Entrenamiento

Se generan **50 escenarios sinteticos** que simulan diferentes situaciones de trafico:

1. **Trafico pesado Norte-Sur** (10 ejemplos)
   - Norte: 12-20 carros, Sur: 12-20 carros
   - Este: 0-5 carros, Oeste: 0-5 carros
   - **Decision**: Verde Norte-Sur

2. **Trafico pesado Este-Oeste** (10 ejemplos)
   - Este: 12-20 carros, Oeste: 12-20 carros
   - Norte: 0-5 carros, Sur: 0-5 carros
   - **Decision**: Verde Este-Oeste

3. **Solo trafico en Norte** (7 ejemplos)
   - Norte: 15-20 carros
   - Otros: 0-3 carros
   - **Decision**: Verde Solo Norte

4. **Solo trafico en Sur** (7 ejemplos)
   - Sur: 15-20 carros
   - Otros: 0-3 carros
   - **Decision**: Verde Solo Sur

5. **Solo trafico en Este** (8 ejemplos)
   - Este: 15-20 carros
   - Otros: 0-3 carros
   - **Decision**: Verde Solo Este

6. **Solo trafico en Oeste** (8 ejemplos)
   - Oeste: 15-20 carros
   - Otros: 0-3 carros
   - **Decision**: Verde Solo Oeste

---

## Visualizacion

El programa muestra **2 graficas simultaneas**:

### 1. Red Neuronal Animada
- **Nodos azules**: Entradas (sensores de trafico)
- **Nodos verdes**: Capa oculta
- **Nodos rojos**: Salidas (decisiones)
- **Conexiones**: Cambian de grosor y color segun los pesos
  - Rojo/Naranja: Pesos positivos
  - Azul/Morado: Pesos negativos
  - Grosor: Magnitud del peso

### 2. Interseccion de Trafico
- Vista superior de la interseccion
- **Semaforos**: Cambian de rojo a verde segun la decision
- **Contadores**: Muestran numero de carros en cada direccion
- **Decision actual**: Texto indicando que semaforo esta activo

---

## Hora de probar

### Requisitos:
```bash
pip install numpy matplotlib scikit-learn
```

### Ejecutar:
```bash
python semaforoHebb.py
```

### Funcionamiento:
1. **Generacion de datos**: Crea 50 escenarios de trafico
2. **Animacion de entrenamiento**: Muestra como la red aprende paso a paso (2 ventanas)
3. **Evaluacion**: Calcula la precision en los datos de entrenamiento
4. **Prueba interactiva**: Permite ingresar trafico personalizado

---

## Resultados Esperados

- **Precision**: 95-100% en datos de entrenamiento
- **Aprendizaje**: Los pesos evolucionan para asociar patrones de trafico con decisiones optimas
- **Generalizacion**: La red aprende reglas como:
  - "Mucho trafico N-S + poco E-O -> Verde N-S"
  - "Solo trafico en una direccion -> Verde solo esa"

---

## Analisis del Aprendizaje

### Que aprendio la red?

La red aprende **asociaciones Hebbianas** entre:
- **Entrada**: Patrones de trafico (carros en cada direccion)
- **Salida**: Decision optima de semaforo

### Evolucion de los pesos:

1. **Inicialmente**: Pesos aleatorios pequeños (~0.1)
2. **Durante entrenamiento**: 
   - Aumentan las conexiones relevantes (como: mucho trafico Norte -> activar verde N o N-S)
   - Se mantienen bajas las conexiones irrelevantes
3. **Al final**: Pesos reflejan la "logica" del control de trafico

### Activaciones de salida:

Las activaciones son valores entre -1 y +1 que indican la "confianza" de cada decision:
- **Valores positivos**: La red sugiere esa opcion
- **Valores negativos**: La red descarta esa opcion
- **Valor maximo**: Decision final elegida

Ejemplo:
```
Verde N-S:     0.107  <- Positivo pero bajo
Verde E-O:    -0.393  <- Negativo (descartado)
Verde Solo N:  0.271  <- MAXIMO (ELEGIDO)
Verde Solo S: -0.050  <- Negativo
Verde Solo E: -0.071  <- Negativo
Verde Solo O: -0.120  <- Negativo
```

### Limitaciones:

- Aprendizaje supervisado simple: No optimiza globalmente
- Sensible al orden: El orden de presentacion afecta el resultado
- No olvida nada (re paila): Los pesos solo crecen (no decrece)
- Overfitting: Se ajusta exactamente a los datos de entrenamiento

### Posibles mejoras:

- Agregar más escenarios (hora pico, emergenciasm etc etc etc)
- Implementar normalización de pesos (evitar crecimiento infinito)
- Usar validación cruzada
- Agregar ruido en los datos para robustez
- Considerar tiempo de espera acumulado

---

## Conceptos Clave

### Regla de Hebb:
> "Lo que se dispara junto, se conecta junto"

**Matematicamente**:
```
W_nueva = W_antigua + eta * (salida_deseada * entrada)
```

Donde:
- `*` = Producto externo
- `eta` = Tasa de aprendizaje (0.02 para W1, 0.05 para W2)

### Red Multicapa:
- **Capa oculta**: Permite aprender representaciones no lineales
- **Funcion tanh**: Introduce no linealidad (valores entre -1 y 1)
- **Propagacion hacia adelante**: `h = tanh(W1 @ x)`, `y = W2 @ h`

---

## Para

Taller de Redes Hebbianas - Cibernética y Sistemas Inteligentes - Universidad Sergio Arboleda

## Licencia

Uso educativo libre