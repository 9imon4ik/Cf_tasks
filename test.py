import main

# https://codeforces.com/blog/entry/63823
# CHT
l_cht = [(1083, 'E'), (319, 'C'), (631, 'E'), (1388, 'E'), (932, 'F'), (311, 'B'), (1303, 'G'), (1715, 'E'),
         (1175, 'G'), (455, 'E')]

# https://codeforces.com/blog/entry/43917
# LCA
l_lca = [(208, 'E'), (191, 'C'), (519, 'E'), (587, 'C'), (609, 'E'), (466, 'E')]

# https://codeforces.com/blog/entry/52492
# Centroids
l_centroids = [(321, 'C'), (766, 'E'), (716, 'E'), (161, 'D'), (379, 'F'), (342, 'E'), (293, 'E'), (914, 'E'),
               (1156, 'D'), ]

# https://codeforces.com/blog/entry/22616
l_segtree = [(339, 'D'), (356, 'A'), (459, 'D'), (61, 'E'), (380, 'C'), (474, 'F'), (292, 'E'), (501, 'D'), (220, 'E'),
             (338, 'E'), (540, 'E'), (609, 'F'), (594, 'D'), (455, 'E'), (446, 'C'), ]

# https://codeforces.com/blog/entry/22616
# Trees and euler tours
l_trees = [(383, 'C'), (343, 'D'), (173, 'E'), (276, 'E'), (516, 'D'), (375, 'D'), (1110, 'F')]

# Trees and hashing
l_tree_hash = [(1800, 'G'), (1671, 'E'), (1794, 'E'), (601, 'D')]

# Trees and combinatorics
l_tree_comb = [(1527, 'D'), (1551, 'F'), (1540, 'B'), (1486, 'F')]

tasks = set(
    l_cht.copy() + l_lca.copy() + l_centroids.copy() + l_segtree.copy() + l_trees.copy() + l_tree_hash.copy() + l_tree_comb.copy())
l_all = [l_cht.copy(), l_lca.copy(), l_centroids.copy(), l_segtree.copy(), l_trees.copy(), l_tree_hash.copy(),
         l_tree_comb.copy()]

for id, index in tasks:
    task = main.find_problem(id, index)
    if task == -1:
        continue
    l_cur = main.find_similar(main.tasks_parsed[task])
    cnt = 0
    for cur in l_cur:
        f = False
        for j in l_all:
            if (id, index) not in j:
                continue
            if (cur['contest_id'], cur['index']) in j:
                f = True
                break
        cnt += f
    print(cnt / 10)
