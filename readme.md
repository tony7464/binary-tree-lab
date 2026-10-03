# Lab: Binary Trees – Depth and Ancestors

**Lab GitHub Repo**: [Binary Tree Lab](https://github.com/learn-co-curriculum/binary-tree-lab)

---

## How to Run

- **Requirements:** Python 3.8+, standard library only, no dependencies.
- From the repo root, run:

```bash
python binary_tree_tests.py
```

- **Success** looks like: `Ran 2 tests ... OK`.

## Solution Approach

- **`max_depth`:** recursive post-order (O(n) time, O(h) space).
- **`lowest_common_ancestor`:** walk down using BST ordering (O(h) time, O(1) space).

---

## Overview

In this lab, you'll implement two classic binary tree problems commonly seen in technical interviews and real-world applications:

1. **Maximum Depth of a Binary Tree**  
   Measure how deep a binary tree goes from root to leaf.

2. **Lowest Common Ancestor of a Binary Search Tree**  
   Given two nodes in a BST, find the node that is their lowest shared ancestor.

These problems will strengthen your understanding of:

- Tree traversal using recursion
- Node comparison and relationships
- Constructing and navigating binary trees

---

## Task 1: Define the Problem

### Problem 1: Maximum Depth

- Implement a function that returns the maximum depth of a binary tree.
- This involves finding the longest path from the root to any leaf.

### Problem 2: Lowest Common Ancestor (BST)

- Implement a function that returns the **lowest common ancestor** of two given nodes in a Binary Search Tree (BST).
- An ancestor of a node is any node on the path from the root to that node (including the node itself).

---

## Task 2: Determine the Design

You will be working with the following files:

### `binary_tree_lab.py`

You will implement:

- `max_depth(root: Optional[TreeNode]) -> int`
- `lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode`

The `TreeNode` class is already defined for you with `val`, `left`, and `right`.

### `binary_tree_tests.py`

This file contains unit tests to validate your implementations. You do not need to modify this file.

---

## 🛠 Task 3: Develop, Test, and Refine the Code

### Setup

1. **Fork and Clone**
   ```bash
   git clone https://github.com/tony7464/binary-tree-lab.git
   cd binary-tree-lab
   ```

## Open and Run

Open the project in your Python-friendly IDE (such as VSCode, PyCharm, or Replit).

---

## Implementation Details

The starter code includes function definitions for `max_depth` and `lowest_common_ancestor`, each containing a `pass` statement. These placeholders indicate where you should implement your logic.

### Steps to Implement

#### 1. Locate the Functions

- Open the `binary_tree_lab.py` file.
- Find the `max_depth` and `lowest_common_ancestor` functions.

#### 2. Understand the Objectives

**`max_depth(root: Optional[TreeNode]) -> int`**

- Goal: Determine the maximum depth (height) of a binary tree.
- Definition: Depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

**`lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode`**

- Goal: Find the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).
- Definition: The LCA is the deepest node that has both `p` and `q` as descendants (a node can be a descendant of itself).

#### 3. Implement the Logic

**`max_depth`**

- Use a recursive approach.
- At each node, compute the depth of the left and right subtrees.
- Return the greater of the two, plus one.

**`lowest_common_ancestor`**

- Leverage the properties of a BST:
  - If both `p` and `q` are less than the current node, recurse into the left subtree.
  - If both are greater, recurse into the right subtree.
  - Otherwise, the current node is the lowest common ancestor.

---

## Run Tests

To validate your code, run the test suite with:

```bash
python binary_tree_tests.py
```
Make sure all tests pass before submission.

4. **Push and Merge**:
   - Commit your work regularly.
   - Push to your feature branch.
   - Open a Pull Request (PR).
   - Merge to `main` after review.

---

## Task 4: Document and Maintain

### Best Practice Documentation Steps

- **Comment your logic**: Especially around recursive or loop-based behavior.
- **Explain your thinking** in your function definitions.
- **README**: Make sure your repo’s README includes how to run the project.
- **Clean Up**:
  - Remove debug prints.
  - Ensure your `.gitignore` ignores `.pyc`, `__pycache__`, etc.

---

## Submission
Once your lab is complete and all tests are passing:

- Push your code to GitHub.
- Submit the link to your repo through **Canvas using CodeGrade**.
