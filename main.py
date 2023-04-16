# Global
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
# Local
from modules import data, graph, dijkstra, setup

# Install dependencies
setup.install_dependencies()

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
    distance_result, route_result = dijkstra.dijkstra(
        data_graph, node_a, node_b)
    distance, route = distance_result, route_result
    graph.print_path_route(node_a, node_b, distance, route, window)
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
