# Constructor
def tree(label,branches=[]):
	# print('return:',[label] ,'    branches:', list(branches))
	return [label]  + list(branches)
# Selectors
def label(tree):
	# print(tree)
	return tree[0]
def branches(tree):
    return tree[1:]

# Q1: 
def is_leaf(tree,branches,lst): 
# *return t is a leaf or not. * （判断t是否为leaf）
	# print(tree)
	# 空树
	if tree == []:
		return lst
	# 叶子结点
	elif len(tree) == 1:
		lst.append(tree[0])
		return lst
	# 遍历所有节点
	for x in tree[1:]:
		# print('x',x)
		bran = branches(x)
		# print('bran',bran)
		# if (isinstance(bran,list)) == False:
		# 每个节点的子节点都用序列表示，如果是空序列则为叶子
		if bran ==[]:
			# print('1',x)
			lst.append(x)
		elif (isinstance(bran,list)):
			# print('2',x)
			lst = is_leaf(x,branches,lst)
	return lst
# Q2: 
def square_tree(tree):
    #   *return a tree with the square of every element in t.*
    # （t中的每一个数都为原来的平方）
# print(type(tree[0]))
    for x in tree:
        if isinstance(x,int):
            n = tree.index(x)
            tree[n] = x ** 2
        elif isinstance(x,list):
            square_tree(x)

# Q3: 
def height(tree,depth):
#           *return the height of a tree.* （计算t的高度）
# 整棵树的高度即整棵树的深度
	index = depth
	# 空树，高度为1且只有一个节点或0节点。
	if tree == [] and index == 0:
		return -1
	elif len(tree) == 1 and index == 0:
		return index
	# 记录上一层深度+1则为本层深度
	index = index + 1
	# 初始化本层为大深度
	max_depth = index
	for x in tree:
		# 遍历每一个子节点，如果是list则表示为下一层节点，继续往下查深度。
		if isinstance(x,list):
			# 下一层节点，传入本层深度，返回本分支查到的最大深度
			n = height(x,index)
			# 对比分支最大深度和已知最大深度，选大的作为最大深度。
			max_depth = max(n,max_depth)
	# 返回本层深度（叶子）或本层以下分支中最大深度。
	return max_depth


# Q4: 
def tree_max(tree,max_num):
#           *return the max of a tree.* （找出t的最大值）
    n = max_num
    for x in tree:
        if isinstance(x,int):
            max_num = max (max_num,x)
        elif isinstance(x,list):
        	# 遍历分枝中的最大值
            n = tree_max(x,max_num)
    max_num = max (max_num,n)
    return max_num


if __name__ == '__main__':

	# 测试数据
	t1 = tree('subjects',[tree('sciences', 
		[tree('biology'), tree('chemistry')]),
		tree('philosophy'),
		tree('languages',
			[tree('Chinese'), tree('English')])])

	t2 = tree('English')

	number_tree = [10, [2, [5], [6]], [3], [4,[1],[8]]]

	nt = tree(10, [
		 tree(2, [tree(5), tree(6)]), 
	 	tree(3), 
	 	tree(4, [tree(1,[tree(9),tree(7)]), tree(11)])])

	null_tree = []

	node = tree(6)

	print('问题1:找出叶子结点')
	lst=[]
	a = is_leaf(t1,branches,lst=[])
	print('a:',a)
	b = is_leaf(t2,branches,lst=[])
	print("b:",b)

	print('问题2:平方数字')
	square_tree(number_tree)
	print(number_tree)
	square_tree(nt)
	print(nt)

	print('问题3:找出树的高度')
	deep_num = height(nt,0)
	print(deep_num)
	null_tree_num = height(null_tree,0)
	print(null_tree_num)
	node_num = height(node,0)
	print(node_num)

	print('问题4:找出树中最大值')
	deep = tree_max(nt,0)
	print(deep)

