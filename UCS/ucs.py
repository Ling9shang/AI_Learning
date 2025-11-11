# ============================================
# 1. 图的邻接表表示（带权重）
# ============================================
import heapq

class Graph:
    """图类：使用邻接表表示带权图"""
    
    def __init__(self):
        """初始化图"""
        self.graph = {}  # 使用字典存储邻接表，每个邻居是 (node, weight)
    
    def add_edge(self, u, v, weight=1):
        """
        添加带权边
        :param u: 起始节点
        :param v: 目标节点
        :param weight: 边的权重
        """
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append((v, weight))
    
    def ucs(self, start, goal):
        """
        统一代价搜索 (UCS)
        :param start: 起始节点
        :param goal: 目标节点
        :return: (路径, 总代价)，如果无路径则返回 (None, inf)
        """
        # 优先队列：(代价, 节点, 路径)
        pq = [(0, start, [start])]
        visited = set()
        
        while pq:
            cost, node, path = heapq.heappop(pq)
            
            if node in visited:
                continue
            
            visited.add(node)
            
            # 如果到达目标节点，返回路径和代价
            if node == goal:
                return path, cost
            
            # 扩展邻居节点
            if node in self.graph:
                for neighbor, weight in self.graph[node]:
                    if neighbor not in visited:
                        new_cost = cost + weight
                        new_path = path + [neighbor]
                        heapq.heappush(pq, (new_cost, neighbor, new_path))
        
        return None, float('inf')


# ============================================
# 2. 示例和测试
# ============================================

def main():
    print("=" * 60)
    print("统一代价搜索 (UCS) 示例")
    print("=" * 60)
    
    # ----------------
    # 示例1: 图的UCS路径查找
    # ----------------
    print("\n【示例1：图的UCS路径查找】")
    print("-" * 60)
    
    # 创建带权图
    #     A --2-- B --1-- D
    #     |      |      |
    #     4      3      5
    #     |      |      |
    #     C --2-- E --1-- F
    
    g = Graph()
    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 4)
    g.add_edge('B', 'D', 1)
    g.add_edge('B', 'E', 3)
    g.add_edge('C', 'E', 2)
    g.add_edge('D', 'F', 5)
    g.add_edge('E', 'F', 1)
    
    print("\n查找从 A 到 F 的最小代价路径:")
    path, cost = g.ucs('A', 'F')
    if path:
        print(f"找到路径: {' -> '.join(path)}")
        print(f"总代价: {cost}")
    else:
        print("没有找到路径")
    
    print("\n" + "=" * 60)
    print("示例演示完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
