# 最小堆，合并k个有序数组

import sys

class HeapNode:
    def __init__(self,x,y=0,z=0):
        self.value=x
        self.i=y
        self.j=z


def Min_Heap(heap):#构造一个堆，将堆中所有数据重新排序
    HeapSize = len(heap)#将堆的长度单独拿出来方便
    for i in range((HeapSize -2)//2,-1,-1):#从后往前出数
        Min_Heapify(heap,i)


def Min_Heapify(heap,root):
    heapsize=len(heap)
    MIN=root
    left=2*root+1
    right=left+1
    if left<heapsize and heap[MIN].value>heap[left].value:
        MIN=left
    if right <heapsize and heap[MIN].value>heap[right].value:
        MIN=right
    if MIN!=root:
        heap[MIN], heap[root] = heap[root], heap[MIN]
        Min_Heapify(heap, MIN)

def MergeKArray(nums,n):
    # 合并k个有序数组，每个数组长度都为k
    knums=[]
    output=[]
    for i in range(len(nums)):
        subnums=nums[i]
        knums.append(HeapNode(subnums[0],i,1))
    #k个元素初始化最小堆 　　Min_Heap(knums)

    for i in range(len(nums)*n):
        # 取堆顶，存结果
        root=knums[0]
        output.append(root.value)
        #替换堆顶
        if root.j<n:
            root.value=nums[root.i][root.j]
            root.j+=1
        else:
            root.value=sys.maxsize
        knums[0]=root
        Min_Heapify(knums,0)
    return output


knums=[[1,2,3],[1,3,6],[4,5,8]]
print(MergeKArray(knums,3))
