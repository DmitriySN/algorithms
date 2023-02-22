# https://contest.yandex.ru/contest/23758/problems/E/

# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:
    class DoubleConnectedNode:
        def __init__(self, value, next=None, prev=None):
            self.value = value
            self.next = next
            self.prev = prev

def solution(node):
    buf = node
    while node:
        # print(node.value)
        if node.next == None:
            buf = node
        node = node.next
    node = buf
    while node:
        prev = node.prev
        # print(node.value)
        node.prev = node.next
        node.next = prev
        node = prev
    return buf

def test():
    node3 = DoubleConnectedNode("node3")
    node2 = DoubleConnectedNode("node2")
    node1 = DoubleConnectedNode("node1")
    node0 = DoubleConnectedNode("node0")

    node0.next = node1

    node1.prev = node0
    node1.next = node2

    node2.prev = node1
    node2.next = node3

    node3.prev = node2
    new_head = solution(node0)
    assert new_head is node3
    assert node3.next is node2
    assert node2.next is node1
    assert node2.prev is node3
    assert node1.next is node0
    assert node1.prev is node2
    assert node0.prev is node1

if __name__ == '__main__':
    test()
