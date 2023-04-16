# Global
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# Local
from modules import data, graph, dijkstra

# Read data base
data_base = data.read_data("data_base/lastfm_asia_edges.csv")

# Build graph
data_graph = graph.build(data_base)

# Dijkstra
distance = 0
route = []

# Functions


def plot_graph():
    # Cria um gráfico
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.plot([1, 2, 3, 4, 5], [10, 5, 20, 15, 25])

    # Cria um objeto FigureCanvasTkAgg para exibir o gráfico na janela
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack()


def search_dijkstra():
    node_a = button_node_a.get()
    node_b = button_node_b.get()
    distance_result, route_result = dijkstra.dijkstra(data_graph, node_a, node_b)
    distance, route = distance_result, route_result
    graph.show_route(data_graph, route)


# Create window
window = tk.Tk()
window.title("Dijkstra")
label = tk.Label(window, text="Busca do menor caminho entre dois vértices")
label.pack()

# Elements
label_button_a = tk.Label(window, text="Digite o primeiro vértice:")
button_node_a = tk.Entry(window)
label_button_b = tk.Label(window, text="Digite o segundo vértice:")
button_node_b = tk.Entry(window)
botao = tk.Button(window, text="Buscar", command=search_dijkstra)
label_button_a.pack()
button_node_a.pack()
label_button_b.pack()
button_node_b.pack()
botao.pack()


window.mainloop()


# def calculate():
#     num1 = float(entry1.get())
#     num2 = float(entry2.get())
#     result = num1 + num2
#     label_result.configure(text=f"Result: {result}")


# # criar janela
# window = tk.Tk()
# window.title("Calculadora")

# # criar inputs
# entry1 = tk.Entry(window)
# entry1.pack()

# entry2 = tk.Entry(window)
# entry2.pack()

# # criar botão de ação
# button = tk.Button(window, text="Calcular", command=calculate)
# button.pack()

# # criar label para exibir resultado
# label_result = tk.Label(window, text="Result: ")
# label_result.pack()

# # executar janela
# window.mainloop()
