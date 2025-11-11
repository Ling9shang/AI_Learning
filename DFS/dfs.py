# ============================================
# 1. 图的邻接表表示
# ============================================
class Graph:
    """图类：使用邻接表表示图"""
    
    def __init__(self):
        """初始化图"""
        self.graph = {}  # 使用字典存储邻接表
    
    def add_edge(self, u, v):
        """
        添加边
        :param u: 起始节点
        :param v: 目标节点
        """
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
    
    def dfs_recursive(self, start, visited=None):
        """
        递归实现的DFS
        :param start: 起始节点
        :param visited: 已访问节点集合
        :return: 访问顺序列表
        """
        if visited is None:
            visited = set()
        
        # 标记当前节点为已访问
        visited.add(start)
        print(f"访问节点: {start}")
        
        # 递归访问所有未访问的邻居节点
        if start in self.graph:
            for neighbor in self.graph[start]:
                if neighbor not in visited:
                    self.dfs_recursive(neighbor, visited)
        
        return visited
    
    def dfs_iterative(self, start):
        """
        使用栈实现的迭代DFS
        :param start: 起始节点
        :return: 访问顺序列表
        """
        visited = set()
        stack = [start]  # 使用列表模拟栈
        result = []
        
        while stack:
            # 从栈中弹出节点
            node = stack.pop()
            
            if node not in visited:
                # 标记为已访问
                visited.add(node)
                result.append(node)
                print(f"访问节点: {node}")
                
                # 将所有未访问的邻居节点压入栈
                if node in self.graph:
                    # 倒序添加，以保持与递归版本相同的遍历顺序
                    for neighbor in reversed(self.graph[node]):
                        if neighbor not in visited:
                            stack.append(neighbor)
        
        return result
    
    def dfs_path(self, start, goal, path=None, visited=None):
        """
        查找从start到goal的路径（使用DFS）
        :param start: 起始节点
        :param goal: 目标节点
        :param path: 当前路径
        :param visited: 已访问节点集合
        :return: 找到的路径，如果不存在则返回None
        """
        if path is None:
            path = []
        if visited is None:
            visited = set()
        
        # 将当前节点添加到路径
        path = path + [start]
        visited.add(start)
        
        # 如果到达目标节点，返回路径
        if start == goal:
            return path
        
        # 如果当前节点不在图中，返回None
        if start not in self.graph:
            return None
        
        # 递归搜索邻居节点
        for neighbor in self.graph[start]:
            if neighbor not in visited:
                new_path = self.dfs_path(neighbor, goal, path, visited)
                if new_path:
                    return new_path
        
        return None
    
    def dfs_all_paths(self, start, goal, path=None):
        """
        查找从start到goal的所有路径（使用DFS）
        :param start: 起始节点
        :param goal: 目标节点
        :param path: 当前路径
        :return: 所有路径的列表
        """
        if path is None:
            path = []
        
        # 将当前节点添加到路径
        path = path + [start]
        
        # 如果到达目标节点，返回当前路径
        if start == goal:
            return [path]
        
        # 如果当前节点不在图中，返回空列表
        if start not in self.graph:
            return []
        
        # 收集所有可能的路径
        all_paths = []
        for neighbor in self.graph[start]:
            # 避免环路
            if neighbor not in path:
                new_paths = self.dfs_all_paths(neighbor, goal, path)
                all_paths.extend(new_paths)
        
        return all_paths


# ============================================
# 2. 树的DFS遍历（前序、中序、后序）
# ============================================

class TreeNode:
    """二叉树节点"""
    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def preorder_traversal(root, result=None):
    """
    前序遍历（根-左-右）
    :param root: 根节点
    :param result: 结果列表
    :return: 遍历结果
    """
    if result is None:
        result = []
    
    if root:
        result.append(root.value)  # 访问根节点
        preorder_traversal(root.left, result)  # 遍历左子树
        preorder_traversal(root.right, result)  # 遍历右子树
    
    return result


def inorder_traversal(root, result=None):
    """
    中序遍历（左-根-右）
    :param root: 根节点
    :param result: 结果列表
    :return: 遍历结果
    """
    if result is None:
        result = []
    
    if root:
        inorder_traversal(root.left, result)  # 遍历左子树
        result.append(root.value)  # 访问根节点
        inorder_traversal(root.right, result)  # 遍历右子树
    
    return result


def postorder_traversal(root, result=None):
    """
    后序遍历（左-右-根）
    :param root: 根节点
    :param result: 结果列表
    :return: 遍历结果
    """
    if result is None:
        result = []
    
    if root:
        postorder_traversal(root.left, result)  # 遍历左子树
        postorder_traversal(root.right, result)  # 遍历右子树
        result.append(root.value)  # 访问根节点
    
    return result


# ============================================
# 3. 迷宫问题（DFS应用）
# ============================================

def solve_maze(maze, start, end):
    """
    使用DFS解决迷宫问题
    :param maze: 二维列表，0表示可通行，1表示墙
    :param start: 起始位置 (row, col)
    :param end: 终点位置 (row, col)
    :return: 路径列表，如果无解返回None
    """
    rows, cols = len(maze), len(maze[0])
    visited = set()
    
    def dfs(row, col, path):
        # 边界检查
        if row < 0 or row >= rows or col < 0 or col >= cols:
            return None
        
        # 检查是否是墙或已访问
        if maze[row][col] == 1 or (row, col) in visited:
            return None
        
        # 添加到路径和已访问集合
        path.append((row, col))
        visited.add((row, col))
        
        # 检查是否到达终点
        if (row, col) == end:
            return path
        
        # 四个方向：上、下、左、右
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            result = dfs(row + dr, col + dc, path.copy())
            if result:
                return result
        
        return None
    
    return dfs(start[0], start[1], [])


# ============================================
# 4. 示例和测试
# ============================================

def main():
    print("=" * 60)
    print("深度优先搜索 (DFS) 示例")
    print("=" * 60)
    
    # ----------------
    # 示例1: 图的DFS遍历
    # ----------------
    print("\n【示例1：图的DFS遍历】")
    print("-" * 60)
    
    # 创建图
    #     A
    #    / \
    #   B   C
    #  / \   \
    # D   E   F
    
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('B', 'E')
    g.add_edge('C', 'F')
    
    print("\n1.1 递归实现的DFS:")
    g.dfs_recursive('A')
    
    print("\n1.2 迭代实现的DFS:")
    g.dfs_iterative('A')
    
    # ----------------
    # 示例2: 路径查找
    # ----------------
    print("\n\n【示例2：路径查找】")
    print("-" * 60)
    
    g2 = Graph()
    g2.add_edge('A', 'B')
    g2.add_edge('A', 'C')
    g2.add_edge('B', 'D')
    g2.add_edge('C', 'D')
    g2.add_edge('C', 'E')
    g2.add_edge('D', 'E')
    
    print("\n2.1 查找单一路径 (A -> E):")
    path = g2.dfs_path('A', 'E')
    print(f"找到路径: {' -> '.join(path)}")
    
    print("\n2.2 查找所有路径 (A -> E):")
    all_paths = g2.dfs_all_paths('A', 'E')
    for i, path in enumerate(all_paths, 1):
        print(f"路径 {i}: {' -> '.join(path)}")
    
    # ----------------
    # 示例3: 二叉树遍历
    # ----------------
    print("\n\n【示例3：二叉树的DFS遍历】")
    print("-" * 60)
    
    # 创建二叉树
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    print("\n3.1 前序遍历 (根-左-右):")
    print(f"结果: {preorder_traversal(root)}")
    
    print("\n3.2 中序遍历 (左-根-右):")
    print(f"结果: {inorder_traversal(root)}")
    
    print("\n3.3 后序遍历 (左-右-根):")
    print(f"结果: {postorder_traversal(root)}")
    
    # ----------------
    # 示例4: 迷宫求解
    # ----------------
    print("\n\n【示例4：迷宫求解】")
    print("-" * 60)
    
    # 创建迷宫 (0=可通行, 1=墙)
    maze = [
        [0, 1, 0, 0, 0],
        [0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0]
    ]
    
    print("\n迷宫地图 (0=路径, 1=墙, S=起点, E=终点):")
    start = (0, 0)
    end = (4, 4)
    
    for i, row in enumerate(maze):
        row_display = []
        for j, cell in enumerate(row):
            if (i, j) == start:
                row_display.append('S')
            elif (i, j) == end:
                row_display.append('E')
            else:
                row_display.append('□' if cell == 0 else '■')
        print(' '.join(row_display))
    
    solution = solve_maze(maze, start, end)
    if solution:
        print(f"\n找到解决方案！路径长度: {len(solution)}")
        print(f"路径: {solution}")
    else:
        print("\n没有找到解决方案！")
    
    print("\n" + "=" * 60)
    print("示例演示完成！")
    print("=" * 60)


if __name__ == "__main__":
    main()
