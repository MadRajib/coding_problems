last_seen = None
last_dict = dict()
def in_order(root):
    global last_seen
    global last_dict
    if not root : return True
    left = in_order(root.left)
    cur_seen = root.data
    if cur_seen in last_dict : return False
    last_dict[cur_seen] = cur_seen
    if last_seen and last_seen >= cur_seen : return False
    last_seen = cur_seen
    right = in_order(root.right)
    return left and right
    

def checkBST(root):
    return in_order(root)
