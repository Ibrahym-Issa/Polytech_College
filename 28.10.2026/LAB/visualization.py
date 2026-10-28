import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Төбелердің орналасуы әр жаңарған сайын өзгермеуі үшін тұрақты позиция сақтаймыз
_saved_pos = None

def draw_graph_to_canvas(city_graph, canvas_frame, path=None, mode="distance"):
    """Графты tkinter терезесінің ішіндегі арнайы фреймге салады"""
    global _saved_pos
    
    # Алдыңғы салынған суреттерді тазалау
    for widget in canvas_frame.winfo_children():
        widget.destroy()
        
    G = nx.Graph()
    
    # Граф құрылымын NetworkX-ке көшіру
    for u in city_graph.graph:
        for v, data in city_graph.graph[u].items():
            if not data.get("closed", False):
                G.add_edge(u, v, weight=data[mode])
                
    fig, ax = plt.subplots(figsize=(7, 5))
    
    # Позицияны бір рет қана есептеп, сақтап қоямыз
    if _saved_pos is None or set(_saved_pos.keys()) != set(G.nodes()):
        _saved_pos = nx.spring_layout(G, seed=42)
        
    # Төбелер мен атауларын салу
    nx.draw_networkx_nodes(G, _saved_pos, node_color='lightblue', node_size=500, ax=ax)
    nx.draw_networkx_labels(G, _saved_pos, font_size=10, font_weight='bold', ax=ax)
    
    # Әдеттегі қабырғалардың салмақтары
    edge_labels = {}
    for u, v, data in G.edges(data=True):
        edge_labels[(u, v)] = f"{data['weight']}"
        
    nx.draw_networkx_edges(G, _saved_pos, width=1, edge_color='gray', style='dashed', ax=ax)
    
    # Егер ең қысқа жол табылса, оны қызыл қалың сызықпен ерекшелейміз
    if path and len(path) > 1:
        path_edges = list(zip(path[:-1], path[1:]))
        nx.draw_networkx_edges(G, _saved_pos, edgelist=path_edges, width=3, edge_color='red', ax=ax)
        
    nx.draw_networkx_edge_labels(G, _saved_pos, edge_labels=edge_labels, font_color='darkgreen', font_size=8, ax=ax)
    
    ax.axis('off')
    fig.tight_layout()
    
    # Matplotlib суретін Tkinter Canvas-қа айналдыру
    canvas = FigureCanvasTkAgg(fig, master=canvas_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both", expand=True)
    plt.close(fig) # Жадты үнемдеу үшін жабамыз
