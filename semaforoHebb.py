import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from sklearn.preprocessing import StandardScaler

def generarDatosdTrafico():
    X, Y, descripciones = [], [], []
    
    #  primer escenario: Tráfico pesado Norte-Sur (10 casos)
    for _ in range(10):
        norte = np.random.randint(12, 20)
        sur = np.random.randint(12, 20)
        este = np.random.randint(0, 5)
        oeste = np.random.randint(0, 5)
        X.append([norte, sur, este, oeste])
        Y.append(0)  # Verde N-S
        descripciones.append(f"Pesado N-S: N={norte}, S={sur}, E={este}, O={oeste}")
    
    #  segundo escenario: Tráfico pesado Este-Oeste (10 casos)
    for _ in range(10):
        norte = np.random.randint(0, 5)
        sur = np.random.randint(0, 5)
        este = np.random.randint(12, 20)
        oeste = np.random.randint(12, 20)
        X.append([norte, sur, este, oeste])
        Y.append(1)  # Verde E-O
        descripciones.append(f"Pesado E-O: N={norte}, S={sur}, E={este}, O={oeste}")
    
    # tercer escenario: Solo tráfico en Norte (7 casos)
    for _ in range(7):
        norte = np.random.randint(15, 20)
        sur = np.random.randint(0, 3)
        este = np.random.randint(0, 3)
        oeste = np.random.randint(0, 3)
        X.append([norte, sur, este, oeste])
        Y.append(2)  # Solo verde Norte
        descripciones.append(f"Solo Norte: N={norte}, S={sur}, E={este}, O={oeste}")
    
    # cuarto escenario: Solo tráfico en Sur (7 casos)
    for _ in range(7):
        norte = np.random.randint(0, 3)
        sur = np.random.randint(15, 20)
        este = np.random.randint(0, 3)
        oeste = np.random.randint(0, 3)
        X.append([norte, sur, este, oeste])
        Y.append(3)  # Solo verde Sur
        descripciones.append(f"Solo Sur: N={norte}, S={sur}, E={este}, O={oeste}")
    
    # quinto escenario: Solo tráfico en Este (8 casos)
    for _ in range(8):
        norte = np.random.randint(0, 3)
        sur = np.random.randint(0, 3)
        este = np.random.randint(15, 20)
        oeste = np.random.randint(0, 3)
        X.append([norte, sur, este, oeste])
        Y.append(4)  # Solo verde Este
        descripciones.append(f"Solo Este: N={norte}, S={sur}, E={este}, O={oeste}")
    
    # sexto escenario: Solo tráfico en Oeste (8 casos)
    for _ in range(8):
        norte = np.random.randint(0, 3)
        sur = np.random.randint(0, 3)
        este = np.random.randint(0, 3)
        oeste = np.random.randint(15, 20)
        X.append([norte, sur, este, oeste])
        Y.append(5)  # Solo verde Oeste
        descripciones.append(f"Solo Oeste: N={norte}, S={sur}, E={este}, O={oeste}")
    
    return np.array(X, dtype=float), np.array(Y), descripciones

# Generar datos
X, Y, descripciones = generarDatosdTrafico()

print("="*60)
print("SISTEMA DE SEMAFORO INTELIGENTE - RED HEBBIANA MULTICAPA")
print("="*60)
print(f"\nDatos generados: {len(X)} escenarios de trafico\n")

# Normalizar
scaler = StandardScaler()
X = scaler.fit_transform(X)

# arch de la red

n_features = 4  # Norte, Sur, Este, Oeste
n_hidden = 6
n_outputs = 6   # Verde N-S, Verde E-O, Verde N, Verde S, Verde E, Verde O

np.random.seed(42)
W1 = np.random.randn(n_hidden, n_features) * 0.1
W2 = np.random.randn(n_outputs, n_hidden) * 0.1

decisiones = ["Verde N-S", "Verde E-O", "Verde Solo N", "Verde Solo S", "Verde Solo E", "Verde Solo O"]
direcciones = ["Norte", "Sur", "Este", "Oeste"]

# animación red hebbiana

fig1, ax1 = plt.subplots(figsize=(12, 8))
plt.title("Red Hebbiana Multicapa – Control de Tráfico", fontsize=14)

# Posiciones de nodos
input_pos = [(1, i) for i in range(n_features)]
hidden_pos = [(2.5, i * 0.7) for i in range(n_hidden)]
output_pos = [(4, i) for i in range(n_outputs)]

# Nodos
input_nodes = [plt.Circle(pos, 0.12, color='skyblue', ec='black', linewidth=2) for pos in input_pos]
hidden_nodes = [plt.Circle(pos, 0.10, color='lightgreen', ec='black', linewidth=2) for pos in hidden_pos]
output_nodes = [plt.Circle(pos, 0.14, color='salmon', ec='black', linewidth=2) for pos in output_pos]

for node in input_nodes + hidden_nodes + output_nodes:
    ax1.add_patch(node)

# Etiquetas
for i, dir_name in enumerate(direcciones):
    ax1.text(0.6, input_pos[i][1], dir_name, va='center', ha='right', fontsize=11, fontweight='bold')

for j, decision in enumerate(decisiones):
    ax1.text(4.4, output_pos[j][1], decision, va='center', fontsize=10, color='darkred', fontweight='bold')

# Conexiones
connections_1 = []
for i, inp in enumerate(input_pos):
    for j, hid in enumerate(hidden_pos):
        line, = ax1.plot([inp[0], hid[0]], [inp[1], hid[1]], 'gray', alpha=0.3, linewidth=0.5)
        connections_1.append(line)

connections_2 = []
for i, hid in enumerate(hidden_pos):
    for j, out in enumerate(output_pos):
        line, = ax1.plot([hid[0], out[0]], [hid[1], out[1]], 'gray', alpha=0.3, linewidth=0.5)
        connections_2.append(line)

ax1.set_xlim(0.3, 5.5)
ax1.set_ylim(-0.5, max(n_features, n_hidden * 0.7, n_outputs) + 0.5)
ax1.axis('off')

# visualizador semaforos

fig2, ax2 = plt.subplots(figsize=(10, 10))
plt.title("Vista de la Intersección", fontsize=14)

ax2.set_xlim(-2, 2)
ax2.set_ylim(-2, 2)
ax2.set_aspect('equal')
ax2.axis('off')

# Calles
ax2.plot([-2, 2], [0, 0], 'k-', linewidth=10, alpha=0.4)  # Horizontal
ax2.plot([0, 0], [-2, 2], 'k-', linewidth=10, alpha=0.4)  # Vertical

# Semáforos más grandes
semaforo_norte = plt.Circle((0, 1), 0.15, color='red', ec='black', linewidth=3)
semaforo_sur = plt.Circle((0, -1), 0.15, color='red', ec='black', linewidth=3)
semaforo_este = plt.Circle((1, 0), 0.15, color='red', ec='black', linewidth=3)
semaforo_oeste = plt.Circle((-1, 0), 0.15, color='red', ec='black', linewidth=3)

ax2.add_patch(semaforo_norte)
ax2.add_patch(semaforo_sur)
ax2.add_patch(semaforo_este)
ax2.add_patch(semaforo_oeste)

# Etiquetas
ax2.text(0, 1.5, 'NORTE ^', ha='center', fontsize=12, fontweight='bold')
ax2.text(0, -1.5, 'SUR v', ha='center', fontsize=12, fontweight='bold')
ax2.text(1.5, 0, 'ESTE >', va='center', fontsize=12, fontweight='bold')
ax2.text(-1.5, 0, '< OESTE', va='center', fontsize=12, fontweight='bold')

# Texto de información
texto_info = ax2.text(0, 1.8, '', ha='center', fontsize=10, 
                      bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))
texto_decision = ax2.text(0, -1.8, '', ha='center', fontsize=12, fontweight='bold',
                          bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.9))

### ---

def activation(x):
    return np.tanh(x)

# animación 

def update_red(frame):
    """Actualiza la red neuronal"""
    global W1, W2
    
    x = X[frame]
    y_target = np.zeros(n_outputs)
    y_target[Y[frame]] = 1
    
    # Aprendizaje Hebbiano
    h = activation(W1 @ x)
    y = activation(W2 @ h)
    
    W2 += np.outer(y_target, h) * 0.05
    W1 += np.outer(h, x) * 0.02
    
    ax1.set_title(f"Aprendizaje Hebbiano – Paso {frame+1}/{len(X)}", fontsize=14)
    
    # Actualizar conexiones capa 1
    idx = 0
    max_w1 = np.max(np.abs(W1)) if np.max(np.abs(W1)) > 0 else 1
    for i in range(n_features):
        for j in range(n_hidden):
            weight = W1[j, i]
            linewidth = 1 + abs(weight) * 3
            color = 'red' if weight > 0 else 'blue'
            alpha = min(0.9, abs(weight) / max_w1 + 0.1)
            connections_1[idx].set_linewidth(linewidth)
            connections_1[idx].set_color(color)
            connections_1[idx].set_alpha(alpha)
            idx += 1
    
    # Actualizar conexiones capa 2
    idx = 0
    max_w2 = np.max(np.abs(W2)) if np.max(np.abs(W2)) > 0 else 1
    for i in range(n_hidden):
        for j in range(n_outputs):
            weight = W2[j, i]
            linewidth = 1 + abs(weight) * 3
            color = 'orange' if weight > 0 else 'purple'
            alpha = min(0.9, abs(weight) / max_w2 + 0.1)
            connections_2[idx].set_linewidth(linewidth)
            connections_2[idx].set_color(color)
            connections_2[idx].set_alpha(alpha)
            idx += 1
    
    return connections_1 + connections_2

def update_interseccion(frame):
    """Actualiza la intersección"""
    x_original = scaler.inverse_transform([X[frame]])[0]
    norte = int(round(x_original[0]))
    sur = int(round(x_original[1]))
    este = int(round(x_original[2]))
    oeste = int(round(x_original[3]))
    
    texto_info.set_text(f"Carros: N={norte} | S={sur} | E={este} | O={oeste}")
    
    decision = Y[frame]
    
    # Resetear semáforos
    semaforo_norte.set_color('red')
    semaforo_sur.set_color('red')
    semaforo_este.set_color('red')
    semaforo_oeste.set_color('red')
    
    # Activar según decisión
    if decision == 0:
        semaforo_norte.set_color('lime')
        semaforo_sur.set_color('lime')
        texto_decision.set_text('[OK] VERDE NORTE-SUR')
    elif decision == 1:
        semaforo_este.set_color('lime')
        semaforo_oeste.set_color('lime')
        texto_decision.set_text('[OK] VERDE ESTE-OESTE')
    elif decision == 2:
        semaforo_norte.set_color('lime')
        texto_decision.set_text('[OK] VERDE SOLO NORTE')
    elif decision == 3:
        semaforo_sur.set_color('lime')
        texto_decision.set_text('[OK] VERDE SOLO SUR')
    elif decision == 4:
        semaforo_este.set_color('lime')
        texto_decision.set_text('[OK] VERDE SOLO ESTE')
    elif decision == 5:
        semaforo_oeste.set_color('lime')
        texto_decision.set_text('[OK] VERDE SOLO OESTE')
    
    ax2.set_title(f"Intersección – Paso {frame+1}/{len(X)}", fontsize=14)
    
    return [semaforo_norte, semaforo_sur, semaforo_este, semaforo_oeste, texto_info, texto_decision]

# Crear animaciones
print("\nejecutando...")

ani1 = animation.FuncAnimation(fig1, update_red, frames=len(X), interval=1000, blit=False, repeat=False)
ani2 = animation.FuncAnimation(fig2, update_interseccion, frames=len(X), interval=1000, blit=False, repeat=False)

plt.show()

print("\n*** Animacion completada.")
plt.close('all')

def predict_traffic(carros_norte, carros_sur, carros_este, carros_oeste):
    x_input = np.array([[carros_norte, carros_sur, carros_este, carros_oeste]], dtype=float)
    x_normalized = scaler.transform(x_input)[0]
    h = activation(W1 @ x_normalized)
    activations = W2 @ h
    decision_idx = np.argmax(activations)
    return decisiones[decision_idx], activations

print("="*60)
print("EVALUACION DEL MODELO")
print("="*60)

correctas = 0
for i in range(len(X)):
    x_original = scaler.inverse_transform([X[i]])[0]
    pred, _ = predict_traffic(x_original[0], x_original[1], x_original[2], x_original[3])
    esperado = decisiones[Y[i]]
    correctas += (pred == esperado)

precision = (correctas / len(X)) * 100
print(f"\nPrecision: {precision:.1f}% ({correctas}/{len(X)})")

## prueba con datos nuestros

print("\n" + "="*60)
print("PRUEBA INTERACTIVA")
print("="*60)

try:
    norte = int(input("Carros en NORTE (0-20): "))
    sur = int(input("Carros en SUR (0-20): "))
    este = int(input("Carros en ESTE (0-20): "))
    oeste = int(input("Carros en OESTE (0-20): "))
    
    decision, activations = predict_traffic(norte, sur, este, oeste)
    
    print(f"\nDECISION: {decision}")
    print("\nActivaciones:")
    for i, dec in enumerate(decisiones):
        bar = "#" * int(activations[i] * 10) if activations[i] > 0 else ""
        print(f"  {dec}: {activations[i]:6.3f} {bar}")
    
except ValueError:
    print("Paila, solo numeros enteros")

print("\n" + "="*60)
print("Programa finalizado")
print("="*60)