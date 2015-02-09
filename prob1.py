def BST(root):
	"""
	creates new instance of a binary search tree
	@param root - the root element of the BST
	"""
	return [root, [], []]

def insertNewNode(btree, newNode):
	"""
	recursive function that populates the tree
	uses list of lists
	@param btree - the already populated tree
	@param newNode - the node to be added
	"""
	r = btree[0]
	if newNode < r: #left branch
		t = btree.pop(1)
		if len(t) < 1:
			btree.insert(1, [newNode, [], []])
		else:
			btree.insert(1, insertNewNode(t, newNode))
	else:	#right branch
		t = btree.pop(2)
		if len(t) < 1:
			btree.insert(2, [newNode, [], []])
		else:
			btree.insert(2, insertNewNode(t, newNode))
	return btree

def getBST(btree):
	return btree

def searchForNode(btree, node, parent = None):
	"""
	recursive function that search for a node in BT
	@param btree - the binary tree
	@param node - searching node
	@param parent - node's parent
	@returns node and node's parent if found or None, None
	"""
	r = btree[0]
	if node < r: #search on the left
		t = btree[1]
		if len(t) < 1:
			return None, None
		else:
			return searchForNode(t, node, r)
	elif node > r: #search on the right
		t = btree[2]
		if len(t) < 1:
			return None, None
		else:
			return searchForNode(t, node, r)
	else: # found it
		return node, parent

def findAllNodesBetween(btree, sval, gval, nodes = []):
	"""
	finds all nodes between an interval
	uses the preorder traversal
	@param btree - searching tree
	@params sval and gval - the interval values
	@returns a list containing the nodes that have value in interval
	"""
	current_node = btree[0]
	if current_node >= sval and current_node <= gval:
		nodes.append(current_node)
	left = btree[1]
	if len(left) > 1:
		findAllNodesBetween(left, sval, gval, nodes)
	right = btree[2]
	if len(right) > 1:
		findAllNodesBetween(right, sval, gval, nodes)
	return nodes


r = BST(50)
insertNewNode(r, 17)
insertNewNode(r, 72)
insertNewNode(r, 12)
insertNewNode(r, 54)
insertNewNode(r, 23)
insertNewNode(r, 9)
insertNewNode(r, 14)
insertNewNode(r, 19)
insertNewNode(r, 76)
insertNewNode(r, 67)
l = getBST(r)
print(l)

node, parent = searchForNode(r, 23)
print("Node:")
print(node)
print("Parent:")
print(parent)

nodes = findAllNodesBetween(r, 9, 20)
print(nodes)
