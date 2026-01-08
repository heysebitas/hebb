# 🚦 Sistema de Semáforo Inteligente - Red Hebbiana Multicapa

## Descripción del Proyecto

Sistema de control de tráfico inteligente que utiliza una **Red Neuronal Hebbiana Multicapa** para aprender y decidir qué semáforo activar en una intersección de 4 direcciones según el flujo de tráfico.

---

## Problema a Resolver

**Objetivo**: Aprender a dar prioridad en una intersección según la cantidad de carros esperando en cada dirección (Norte, Sur, Este, Oeste).

**Aplicación real**: Optimizar el flujo vehicular reduciendo tiempos de espera.


### Parámetros:
- **Entradas**: 4 (tráfico en cada dirección: 0-20 carros)
- **Capa oculta**: 6 neuronas con activación `tanh`
- **Salidas**: 6 decisiones posibles
- **Algoritmo**: Aprendizaje Hebbiano (`W += y * x`)

---

## Datos de Entrenamiento

Se generan **50 escenarios sintéticos** que simulan diferentes situaciones de tráfico:

1. **Tráfico pesado Norte-Sur** (10 ejemplos)
   - Norte: 12-20 carros, Sur: 12-20 carros
   - Este: 0-5 carros, Oeste: 0-5 carros
   - **Decisión**: Verde Norte-Sur

2. **Tráfico pesado Este-Oeste** (10 ejemplos)
   - Este: 12-20 carros, Oeste: 12-20 carros
   - Norte: 0-5 carros, Sur: 0-5 carros
   - **Decisión**: Verde Este-Oeste

3. **Solo tráfico en Norte** (7 ejemplos)
   - Norte: 15-20 carros
   - Otros: 0-3 carros
   - **Decisión**: Verde Solo Norte

4. **Solo tráfico en Sur** (7 ejemplos)
   - Sur: 15-20 carros
   - Otros: 0-3 carros
   - **Decisión**: Verde Solo Sur

5. **Solo tráfico en Este** (8 ejemplos)
   - Este: 15-20 carros
   - Otros: 0-3 carros
   - **Decisión**: Verde Solo Este

6. **Solo tráfico en Oeste** (8 ejemplos)
   - Oeste: 15-20 carros
   - Otros: 0-3 carros
   - **Decisión**: Verde Solo Oeste

---

## Visualización

El programa muestra **2 gráficas simultáneas**:

### 1. Red Neuronal Animada
- **Nodos azules**: Entradas (sensores de tráfico)
- **Nodos verdes**: Capa oculta
- **Nodos rojos**: Salidas (decisiones)
- **Conexiones**: Cambian de grosor y color según los pesos
  - Rojo/Naranja: Pesos positivos
  - Azul/Morado: Pesos negativos
  - Grosor: Magnitud del peso

### 2. Intersección de Tráfico
- Vista superior de la intersección
- **Semáforos**: Cambian de rojo a verde según la decisión
- **Contadores**: Muestran número de carros en cada dirección
- **Decisión actual**: Texto indicando qué semáforo está activo

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
1. **Generación de datos**: Crea 50 escenarios de tráfico
2. **Animación de entrenamiento**: Muestra cómo la red aprende paso a paso (2 ventanas)
3. **Evaluación**: Calcula la precisión en los datos de entrenamiento
4. **Prueba interactiva**: Permite ingresar tráfico personalizado

---

## Resultados Esperados

- **Precisión**: 95-100% en datos de entrenamiento
- **Aprendizaje**: Los pesos evolucionan para asociar patrones de tráfico con decisiones óptimas
- **Generalización**: La red aprende reglas como:
  - "Mucho tráfico N-S + poco E-O -> Verde N-S"
  - "Solo tráfico en una dirección -> Verde solo esa"

---

## Análisis del Aprendizaje

### ¿Qué aprendió la red?

La red aprende **asociaciones Hebbianas** entre:
- **Entrada**: Patrones de tráfico (carros en cada dirección)
- **Salida**: Decisión óptima de semáforo

### Evolución de los pesos:

1. **Inicialmente**: Pesos aleatorios pequeños (~0.1)
2. **Durante entrenamiento**: 
   - Aumentan las conexiones relevantes (como: mucho tráfico Norte -> activar verde N o N-S)
   - Se mantienen bajas las conexiones irrelevantes
3. **Al final**: Pesos reflejan la "lógica" del control de tráfico

### Activaciones de salida:

Las activaciones son valores entre -1 y +1 que indican la "confianza" de cada decisión:
- **Valores positivos**: La red sugiere esa opción
- **Valores negativos**: La red descarta esa opción
- **Valor máximo**: Decisión final elegida

Ejemplo:
```
Verde N-S:     0.107  <- Positivo pero bajo
Verde E-O:    -0.393  <- Negativo (descartado)
Verde Solo N:  0.271  <- MÁXIMO (ELEGIDO)
Verde Solo S: -0.050  <- Negativo
Verde Solo E: -0.071  <- Negativo
Verde Solo O: -0.120  <- Negativo
```

### Limitaciones:

- Aprendizaje supervisado simple: No optimiza globalmente
- Sensible al órden: El órden de presentación afecta el resultado
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

**Matemáticamente**:
```
W_nueva = W_antigua + eta * (salida_deseada * entrada)
```

Donde:
- `*` = Producto externo
- `eta` = Tasa de aprendizaje (0.02 para W1, 0.05 para W2)

### Red Multicapa:
- **Capa oculta**: Permite aprender representaciones no lineales
- **Función tanh**: Introduce no linealidad (valores entre -1 y 1)
- **Propagación hacia adelante**: `h = tanh(W1 @ x)`, `y = W2 @ h`

---

## Para

Taller de Redes Hebbianas - Cibernética y Sistemas Inteligentes - Universidad Sergio Arboleda

## Licencia

Uso educativo libre