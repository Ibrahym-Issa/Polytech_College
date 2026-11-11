import json
import os

class CityGraph:
    def __init__(self):
        # Adjacency list құрылымы: { u: { v: {"distance": d, "time": t, "closed": False}, ... }, ... }
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = {}

    def remove_node(self, node):
        if node in self.graph:
            # Осы төбеге байланған барлық қабырғаларды жою
            for neighbor in list(self.graph[node].keys()):
                if node in self.graph[neighbor]:
                    del self.graph[neighbor][node]
            del self.graph[node]

    def add_edge(self, u, v, distance, time):
        if distance < 0 or time < 0:
            raise ValueError("Салмақ (қашықтық немесе уақыт) теріс мән болмауы керек!")
        
        self.add_node(u)
        self.add_node(v)
        
        # Бағытталмаған граф болғандықтан, екі жаққа да қосамыз
        self.graph[u][v] = {"distance": distance, "time": time, "closed": False}
        self.graph[v][u] = {"distance": distance, "time": time, "closed": False}

    def remove_edge(self, u, v):
        if u in self.graph and v in self.graph[u]:
            del self.graph[u][v]
        if v in self.graph and u in self.graph[v]:
            del self.graph[v][u]

    def set_edge_status(self, u, v, is_closed=True):
        """Жолды уақытша жабу немесе қайта ашу функциясы"""
        if u in self.graph and v in self.graph[u]:
            self.graph[u][v]["closed"] = is_closed
        if v in self.graph and u in self.graph[v]:
            self.graph[v][u]["closed"] = is_closed

    def save_to_json(self, filepath):
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(self.graph, f, ensure_ascii=False, indent=4)

    def load_from_json(self, filepath):
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                self.graph = json.load(f)
