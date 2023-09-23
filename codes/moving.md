# Searching spaces definition
## linear
## two dimensional
## divide and conquer : recursive
### binary tree
- left vs right
  - [max depth of binary tree](binary_tree/max_depth_bt.py)
- left / right -> logic operations: or/and
  - [same tree](binary_tree/same_tree.py)
- pre_order: operate the current node, then operate its children with the recursive call (call same function with children as args)
  - [invert binary tree](binary_tree/invert_bt.py)
  - [construct binary tree from preorder and inorder traversal](binary_tree/construct_bt_from_preorder_and_inorder.py)
  - [path sum](binary_tree/path_sum.py)
  - [sum root to leaf numbers](binary_tree/sum_root_to_leaf_numbers.py)
  - [count complete tree nodes](binary_tree/count_complete_tree_nodes.py) : 2^n - 1
  - [convert sorted array to binary search tree](divide_conquer/convert_sorted_array_to_bst.py)
  - [construct quad tree](divide_conquer/construct_quad_tree.py)
- post-order: operate the children nodes, then operate on the root node : backwards
  - [flatten binary tree to linked list](binary_tree/flatten-bt_to_linked_list.py)
  - [lowest common ancestor of a binary tree](binary_tree/lowest_common_ancestor_bt.py)
- inorder:
  - [min absolute difference in BST](binary_tree/min_absolute_difference_bt.py)
- path may or may not include the current node
  - [binary tree max path sum](binary_tree/bt_max_path_sum.cpp)
### question's natural data structure
### question
# Direction
## Stack
- current state needs to know or operate on most recent states
  - [valid parentheses](stack/valid_parentheses.py)
  - [simplify path](stack/simplify_path.py)
  - [evaluate reverse polish notation](stack/evaluate_reverse_polish_notation.py)
- operate on BST : check the st[-1]'s right, and then loop the right's lefts into st
  - [binary search tree iterator](binary_tree/bst_iterator.py)
## Two pointers
### same direction
#### sliding window
- O(n) as iterating each item once/twice 
- move right until not able to move; then move left -> if/else internally
  - [summary ranges](intervals/summary_ranges.py)
- intervals
  - [merge intervals](intervals/merge_intervals.py) : right -> merge; left -> update results
  - [min number of arrows to burst balloons](intervals/min_number_arrow_bust_balloons.py)
#### linked list
- slow and fast pointer
- two pointers on two lists or two parts on the same list
  - [linked list cycle](linked_list/linked_list_cycle.py)
  - [remove nth node from end of list](linked_list/remove_nth_node_from_end_of_list.py) : the diff of slow and fast is n
  - [remove duplicates from sorted list II](linked_list/remove_duplicates_from_sorted_list_II.py)
  - [partition list](linked_list/partition_list.py)
  - [sort list](divide_conquer/sort_list.py)
#### two pointers from two lists
- merge two sorted lists
### face-to-face
#### quick sort
#### binary search
- anchor needed for making decision
    - [search insert position](binary_search/search_insert_positon.py)
    - [find peak element](binary_search/find_peak_element.py)
    - [search in rotated sorted array](binary_search/search_rotated_sorted_array.py)
    - [find first and last position of element in sorted array](binary_search/find_first_last_positon_in_sorted_array.py)
    - [find min in rotated sorted array](binary_search/find_min_in_rotated_arry.py)
    - [median of two sorted arrays](binary_search/median_two_sorted_array.py)
## DFS
### two dimensional 
- row_down -> col_right
- backtracking 
  - update the results, normally within a for loop to try others
  - visited array
- [combinations](backtracking/combinations.py)
- [permutations](backtracking/permutations.py)
- [generate parentheses](backtracking/generate_parentheses.py)
- [word search](backtracking/word_search.py)
### neighbor based
- check neighbors 
- [number of island](graph/number_of_islands.py)
- [surrounded regions](graph/surrounded_regions.py)
- [evaluate division](graph/evaluate_division.py)
### how to quit
- reach the asked length
- reach to the boarder
- the node has been visited
### return value
## BFS
### use cases
- explicit directions : level
  - tree
    - [binary tree level order traversal](binary_tree/bt_level_order_traversal.py)
    - [binary tree right side view](binary_tree/bt_right_side_view.py)
    - [average of levels in binary tree](binary_tree/average_levels_in_bt.py)
    - [binary tree zigzag level order traversal](binary_tree/bt_zigzag_level_order_traversal.py)
  - graph
    - [clone graph](graph/clone_graph.py)
    - [course schedule](graph/course_schedule.py)
  - dependences
- min steps to reach the destination
  - [min genetic mutation](graph/min_genetic_mutation.py)
### basice operations on queue
- init queue and add the first items
- visited to avoid duplicates
- logic for updating states when pop up: q.popleft()
- logic for checking and adding new items into queue: q.append() 
### neighbor based
- check same level
  - [populating next right pointers in each node II](binary_tree/populating_next_right_pointers_in_each_node_II.py)
- check neighbors
- update visited states within checking loop 
  - [course schedule](graph/course_schedule.py)
  - [minimum genetic mutation](graph/min_genetic_mutation.py)
### how to quit
- queue is empty
- reach the destination with min steps
  - [snakes and ladders](graph/snakes_ladders.py)
# Steps
