class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def display_tree(node):
    def get_lines(node):
        if not node:
            return []
        
        label = str(node.data)
        left = get_lines(node.left)
        right = get_lines(node.right)

        if not left and not right:
            return [label]
        
        if not left:
            edge = [label + "──┐"]
            edge.extend(["  " + line for line in right])
            return edge
            

        if not right:
            edge = ["┌──" + label]
            edge.extend([line + "  " for line in left])
            return edge

        left_width = len(left[0])
        right_width = len(right[0])

        edge = [" " * left_width + label + " " * right_width]
        edge.append("┌" + "─" * (left_width - 1) + "┴" + "─" * (right_width - 1) + "┐")
        
        for i in range(max(len(left), len(right))):
            left_line = left[i] if i < len(left) else " " * left_width
            right_line = right[i] if i < len(right) else " " * right_width
            edge.append(left_line + " " + right_line)
            
        return edge

    for line in get_lines(node):
        print(line)

abc = Node("A")
abc.left = Node("B")
abc.right = Node("C")
abc.left.left = Node("D")
abc.left.right = Node("E")
abc.right.left = Node("F")
abc.right.right = Node("G")
abc.left.left.left = Node("H")
abc.left.left.right = Node("I")
abc.right.left.left = Node("J")
abc.right.left.right = Node("K")
abc.right.right.left = Node("L")
abc.right.right.right = Node("M")

exam = Node("Exam")
exam.left = Node("Continuous assessment")
exam.right = Node("Re-exam")
exam.left.left = Node("Promote")
exam.left.right = Node("Retake")
exam.right.left = Node("Continuous assessment")
exam.right.right = Node("Re-exam")
exam.right.left.left = Node("Promote")
exam.right.left.right = Node("Retake")

display_tree(abc)
display_tree(exam)
