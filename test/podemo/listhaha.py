class Node(object):
    def __init__(self, val=None):
        self.val = val
        self.next = None

class Node_handle():
    def __init__(self):
        self.cur_node = None
    #查找
    def find(self,node,num,a = 0):
        while node:
            if a == num:
                return node
            a += 1
            node = node.next
    #增加
    def add(self,data):
        node = Node()
        node.val = data
        node.next = self.cur_node
        self.cur_node = node
        return node
    #打印,并将链表值存入列表返回
    def printNode(self,node):
        lii = []
        while node:
            # print ('\nnode: ', node, ' value: ', node.val, ' next: ', node.next)
            s = node.val
            node = node.next
            lii.append(s)
        return lii
    # 删除
    def delete(self,node,num,b = 1):
        if num == 0:
            node = node.next
            return node
        while node and node.next:
            if num == b:
                node.next = node.next.next
            b += 1
            node = node.next
        return node
    # 翻转
    def reverse(self,nodelist):
        list = []
        while nodelist:
            list.append(nodelist.val)
            nodelist = nodelist.next
        result = Node()
        result_handle =Node_handle()
        for i in list:
            result = result_handle.add(i)
        return result
    def middleNode(self, head: Node) -> Node:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
if __name__ == "__main__":
    l1 = Node()
    ListNode_1 = Node_handle()
    l1_list = [1, 2, 3, 4, 5, 6, 7]
    l1_list.reverse()
    for i in l1_list:
        l1 = ListNode_1.add(i)
    # ListNode_1.printNode(l1)
    # l1 = ListNode_1.delete(l1,0)
    # ListNode_1.printNode(l1)
    # l1 = ListNode_1.reverse(l1)
    # ListNode_1.printNode(l1)
    # head = ListNode_1.find(l1, 0)
    # ListNode_1.printNode(l1)
    head = l1
    result = Node_handle().middleNode(head)
    result1 = ListNode_1.printNode(result)
    print(result1)
