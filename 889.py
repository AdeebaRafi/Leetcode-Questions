class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        left_subtree_root = preorder[1]
        index_in_post = postorder.index(left_subtree_root)
        left_size = index_in_post + 1

        root.left = self.constructFromPrePost(preorder[1:left_size+1], postorder[0:left_size])
        root.right = self.constructFromPrePost(preorder[left_size+1:], postorder[left_size:-1])

        return root