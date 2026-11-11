import heapq
import time

def dijkstra(city_graph, start, end, mode="distance"):
    """
    mode: "distance" немесе "time" (Күрделендірілген тапсырма талабы)
    """
    if start not in city_graph.graph or end not in city_graph.graph:
        return None, float('inf'), 0, 0.0

    start_time_perf = time.perf_counter()
    
    # Инициализация
    distances = {node: float('inf') for node in city_graph.graph}
    previous = {node: None for node in city_graph.graph}
    distances[start] = 0
    
    # Басымдық кезегі (heapq): (ағымдағы_салмақ, төбе)
    queue = [(0, start)]
    visited_count = 0
    
    while queue:
        current_weight, u = heapq.heappop(queue)
        visited_count += 1
        
        if u == end:
            break
            
        if current_weight > distances[u]:
            continue
            
        for v, edge_data in city_graph.graph[u].items():
            # Егер жол уақытша жабылған болса, оны аттап өтеміз
            if edge_data.get("closed", False):
                continue
                
            weight = edge_data[mode]
            relaxation = current_weight + weight
            
            if relaxation < distances[v]:
                distances[v] = relaxation
                previous[v] = u
                heapq.heappush(queue, (relaxation, v))
                
    # Маршрутты қалпына келтіру
    path = []
    curr = end
    if distances[end] != float('inf'):
        while curr is not None:
            path.append(curr)
            curr = previous[curr]
        path.reverse()
        
    execution_time = (time.perf_counter() - start_time_perf) * 1000 # миллисекундпен
    
    return path, distances[end], visited_count, execution_time
