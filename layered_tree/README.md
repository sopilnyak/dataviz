## Layered Tree Draw algorithm implementation

### Input
CSV with two columns: node index in the binary tree and node value. Every record corresponds to a single node.

### Output
Image with the constructed layered tree.

### Steps
1. Assign y coordinates to each node. The y-coordinate is the number of layer in the tree.
2. Assign initial x coordinates to each node by performing an inorder traversal: the x coordinate of node is its rank in inorder traversal.
3. Assign actual x coordinates by performing the Layered Tree Draw algorithm (Algorithm 3.1 from *Battista, Eades, Tamassia, Tollis — Graph Drawing. Algorithms for the Visualization of Graphs*).
    Let *T* be a subtree of the binary tree.
    * Base case: if tree *T* consists of a single vertex, keep the x coordinate.
    * Let *r* be the root of *T*. Calculate max distance between two subtrees of *r* and move them so their distance becomes equal to 2. Place *r* half way between its children. If *r* has only one subtree (e.g. left one), place *r* at distance 1 to the right of its left child.
    * Recursively apply the algorithm to the left and right subtrees of *r*
4. Draw the result using the assigned coordinates.
