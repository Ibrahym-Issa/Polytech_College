import tkinter as tk
from tkinter import ttk, messagebox
from graph import CityGraph
from dijkstra import dijkstra
from visualization import draw_graph_to_canvas

# Бастапқы 15 төбе мен 30 қабырғаны енгізу
def initialize_default_data(cg):
    edges = [
        ('A', 'B', 4, 4), ('A', 'C', 2, 2), ('B', 'C', 1, 1), ('B', 'D', 5, 5),
        ('C', 'E', 7, 7), ('C', 'F', 4, 4), ('D', 'E', 2, 2), ('D', 'G', 6, 6),
        ('E', 'F', 1, 1), ('E', 'H', 3, 3), ('F', 'H', 5, 5), ('F', 'I', 8, 8),
        ('G', 'H', 2, 2), ('G', 'J', 7, 7), ('H', 'I', 2, 2), ('H', 'K', 6, 6),
        ('I', 'L', 4, 4), ('I', 'M', 9, 9), ('J', 'K', 1, 1), ('J', 'N', 8, 8),
        ('K', 'L', 3, 3), ('K', 'N', 5, 5), ('L', 'M', 2, 2), ('L', 'O', 7, 7),
        ('M', 'O', 3, 3), ('N', 'O', 4, 4), ('B', 'F', 9, 9), ('E', 'K', 8, 8),
        ('C', 'H', 10, 10), ('G', 'N', 6, 6)
    ]
    for u, v, d, t in edges:
        cg.add_edge(u, v, d, t)

class SmartCityGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Ақылды қала: Маршруттау жүйесі")
        self.root.geometry("1000x650")
        
        # Графты инициализациялау
        self.cg = CityGraph()
        initialize_default_data(self.cg)
        self.nodes_list = sorted(list(self.cg.graph.keys()))
        
        # --- ИНТЕРФЕЙС ҚҰРЫЛЫМЫ ---
        # Сол жақ панель (Басқару элементтері)
        left_panel = ttk.Frame(root, padding="10", width=300)
        left_panel.pack(side="left", fill="y")
        
        # Оң жақ панель (Графты визуализациялау аймағы)
        self.canvas_frame = ttk.Frame(root, padding="5", relief="groove")
        self.canvas_frame.pack(side="right", fill="both", expand=True)
        
        # 1. Маршрут іздеу бөлімі
        ttk.Label(left_panel, text="МАРШРУТТЫ ЕСЕПТЕУ", font=("Arial", 11, "bold")).pack(pady=5)
        
        ttk.Label(left_panel, text="Бастапқы нүкте:").pack(anchor="w")
        self.combo_start = ttk.Combobox(left_panel, values=self.nodes_list, state="readonly")
        self.combo_start.pack(fill="x", pady=2)
        self.combo_start.current(0)
        
        ttk.Label(left_panel, text="Соңғы нүкте:").pack(anchor="w")
        self.combo_end = ttk.Combobox(left_panel, values=self.nodes_list, state="readonly")
        self.combo_end.pack(fill="x", pady=2)
        self.combo_end.current(14) # 'O' нүктесі
        
        ttk.Label(left_panel, text="Оңтайландыру критерийі:").pack(anchor="w")
        self.mode_var = tk.StringVar(value="distance")
        ttk.Radiobutton(left_panel, text="Арақашықтық (км)", variable=self.mode_var, value="distance").pack(anchor="w")
        ttk.Radiobutton(left_panel, text="Уақыт (минут)", variable=self.mode_var, value="time").pack(anchor="w")
        
        ttk.Button(left_panel, text="Ең тиімді жолды табу", command=self.calculate_route).pack(fill="x", pady=10)
        
        # Нәтижелерді шығару аймағы
        self.lbl_result = ttk.Label(left_panel, text="Маршрут: -\nЖалпы салмақ: -\nУақыт: -", justify="left", font=("Arial", 10))
        self.lbl_result.pack(fill="x", pady=5)
        
        ttk.Separator(left_panel, orient="horizontal").pack(fill="x", pady=10)
        
        # 2. Жолдарды басқару (Жабу / Ашу)
        ttk.Label(left_panel, text="ЖОЛДАРДЫ БАСҚАРУ (Апаттар)", font=("Arial", 11, "bold")).pack(pady=5)
        
        ttk.Label(left_panel, text="1-ші нүкте:").pack(anchor="w")
        self.combo_edge1 = ttk.Combobox(left_panel, values=self.nodes_list, state="readonly")
        self.combo_edge1.pack(fill="x", pady=2)
        
        ttk.Label(left_panel, text="2-ші нүкте:").pack(anchor="w")
        self.combo_edge2 = ttk.Combobox(left_panel, values=self.nodes_list, state="readonly")
        self.combo_edge2.pack(fill="x", pady=2)
        
        btn_close = ttk.Button(left_panel, text="Жолды уақытша жабу", command=lambda: self.toggle_edge(True))
        btn_close.pack(fill="x", pady=2)
        
        btn_open = ttk.Button(left_panel, text="Жолды қайта ашу", command=lambda: self.toggle_edge(False))
        btn_open.pack(fill="x", pady=2)
        
        # Бастапқы графты салу
        self.update_graph_view()

    def calculate_route(self):
        start = self.combo_start.get()
        end = self.combo_end.get()
        mode = self.mode_var.get()
        
        if start == end:
            messagebox.showwarning("Қате", "Бастапқы және соңғы нүктелер бірдей болмауы керек!")
            return
            
        path, total_weight, nodes_checked, exec_time = dijkstra(self.cg, start, end, mode)
        
        if not path:
            messagebox.showerror("Қате", "Бұл нүктелер арасында байланыс жоқ (жолдар жабылған болуы мүмкін)!")
            self.lbl_result.config(text="Маршрут: Табылмады\nЖалпы салмақ: шексіз")
            self.update_graph_view()
        else:
            path_str = " -> ".join(path)
            unit = "км" if mode == "distance" else "мин"
            self.lbl_result.config(text=f"Маршрут: {path_str}\nЖалпы салмақ: {total_weight} {unit}\nЕсептеу уақыты: {exec_time:.3f} мс")
            # Графты табылған жолмен бірге қайта салу
            draw_graph_to_canvas(self.cg, self.canvas_frame, path=path, mode=mode)

    def toggle_edge(self, is_closed):
        u = self.combo_edge1.get()
        v = self.combo_edge2.get()
        
        if not u or not v:
            messagebox.showwarning("Қате", "Екі нүктені де таңдаңыз!")
            return
        if u == v:
            messagebox.showwarning("Қате", "Нүктелер әртүрлі болуы керек!")
            return
            
        if v not in self.cg.graph.get(u, {}):
            messagebox.showerror("Қате", f"{u} және {v} арасында тікелей жол жоқ!")
            return
            
        self.cg.set_edge_status(u, v, is_closed=is_closed)
        status_text = "жабылды" if is_closed else "ашылды"
        messagebox.showinfo("Сәтті", f"{u}–{v} жолы сәтті {status_text}!")
        
        # Графты жаңарту
        self.update_graph_view()

    def update_graph_view(self):
        draw_graph_to_canvas(self.cg, self.canvas_frame, path=None, mode=self.mode_var.get())

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartCityGUI(root)
    root.mainloop()
