node = []
node_list = []
class Dijkstra():
    def __init__(self, node_map):
        self.node_map = node_map
        self.node_length = len(node_map)
        self.used_node_list = []
        self.collected_node_dict = {}
    
    def __call__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self._init_dijkstra()
        return self._format_path()
    def _init_dijkstra(self):
        self.used_node_list.append(self.from_node)
        self.collected_node_dict[self.from_node] = [0, -1]
        for index1, node1 in enumerate(self.node_map[self.from_node]):
            if node1:
                self.collected_node_dict[index1] = [node1, self.from_node]
                self._foreach_dijkstra()
    def _foreach_dijkstra(self):
        if len(self.used_node_list) == self.node_length - 1:
            return
        for key, val in self.collected_node_dict.items():  
            if key not in self.used_node_list and key != to_node:
                self.used_node_list.append(key)
            else:
                continue
        for index1, node1 in enumerate(self.node_map[key]):  
            if node1 and index1 in self.collected_node_dict and self.collected_node_dict[index1][0] > node1 + val[0]:
                self.collected_node_dict[index1][0] = node1 + val[0]
                self.collected_node_dict[index1][1] = key
            elif node1 and index1 not in self.collected_node_dict:
                self.collected_node_dict[index1] = [node1 + val[0], key]
                self._foreach_dijkstra()
    def _format_path(self):
        node_list = []
        sort_list = []
        temp_node = self.to_node
        node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        while self.collected_node_dict[temp_node][1] != -1:
            temp_node = self.collected_node_dict[temp_node][1]
            node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
            node_list.reverse()
        for i in node_list:
            sort_list.append((i[1], node[i[0]]))
        sort_list.reverse()
        return sort_list
def set_node_map(node_map, node, node_list):
    for x, y, val in node_list:
        node_map[node.index(x)][node.index(y)] = node_map[node.index(y)][node.index(x)] =  val
if __name__ == "__main__":
    map = open('map.txt', 'r', encoding='utf-8')
    lines = map.readlines()
    node_list = []
    node = []
    node_set = set()
    for i in lines:
        text = i.split()
        node_list.append((text[0],text[1], float(text[2])))
        node_set.add(text[0])
        node_set.add(text[1])
    map.close()
    node = list(node_set)
    node_map = [[0 for val in range(len(node))] for val in range(len(node))]
    set_node_map(node_map, node, node_list)    
    from_node = node.index('A')
    to_node = node.index('G')
    dijkstrapath = Dijkstra(node_map)
    path = dijkstrapath(from_node, to_node)
    path.sort()
    print(path)
    res = ''
    road = 0
    for i in path:
        res = res + '->' + i[1]
        road += i[0]
    print(res, road)
