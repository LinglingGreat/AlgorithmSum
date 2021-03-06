# -*- coding: utf-8 -*-
# @Time    : 2018/9/9 18:57
# @Author  : Liling
"""
完全多部图
给定一张包含N个点、M条边的无向图，每条边连接两个不同的点，且任意两点间最多只有一条边。对于这样的简单无向图，如果能将所有点划分成若干个集合，使得任意两个同一集合内的点之间没有边相连，任意两个不同集合内的点之间有边相连，则称该图为完全多部图。现在你需要判断给定的图是否为完全多部图。

输入
第一行输入一个整数T表示数据组数，1≤T≤10。

每组数据格式为：

第一行包含两个整数N和M，1≤N≤1000，0≤M≤N(N-1)/2；

接下来M行，每行包含两个整数X和Y，表示第X个点和第Y个点之间有一条边，1≤X，Y≤N。

输出
每组输出占一行，如果给定的图为完全多部图，输出Yes，否则输出No。


样例输入
2
5 7
1 3
1 5
2 3
2 5
3 4
4 5
3 5
4 3
1 2
2 3
3 4
样例输出
Yes
No
"""

t = int(input())
for i in range(t):
    n, m = [int(i) for i in input().split()]
    edgelist = [[0]*(n+1) for i in range(n+1)]
    for j in range(m):
        x, y = [int(i) for i in input().split()]
        edgelist[x][y] = edgelist[y][x] = 1
    group = [[x] for x in range(1, n+1)]
    indx = 0
    indy = indx + 1
    while indy < len(group):
        x = group[indx][0]
        y = group[indy][0]
        if indx != indy and edgelist[x][y] != 0:
            group[indx] += group[indy]
            group.pop(indy)
        else:
            indy += 1



