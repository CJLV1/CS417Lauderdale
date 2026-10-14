#ifndef TREE_H
#define TREE_H

#include <iostream>
template <typename type>

class Tree
{
private:
    struct Node
    {
        type data;
        Node* left;
        Node* right;

        Node(const type& value) : data(value), left(nullptr), right(nullptr) {}
    };

    Node* root;

    Node* copyNodes(const Node* node) const
    {
        if (node == nullptr)
            return nullptr;

        Node* newNode = new Node(node->data);
        newNode->left = copyNodes(node->left);
        newNode->right = copyNodes(node->right);
        return newNode;
    }

    void destroy(Node* node)
    {
        if (node == nullptr)
            return;

        destroy(node->left);
        destroy(node->right);
        delete node;
    }

    bool insert(Node*& node, const type& value)
    {
        if (node == nullptr)
        {
            node = new Node(value);
            return true;
        }
        if (value < node->data)
            return insert(node->left, value);
        if (node->data < value)
            return insert(node->right, value);
        return false; // duplicate
    }

    bool remove(Node*& node, const type& value)
    {
        if (node == nullptr)
            return false;

        if (value < node->data)
            return remove(node->left, value);
        if (node->data < value)
            return remove(node->right, value);

        
        if (node->left != nullptr && node->right != nullptr)
        {
            
            Node* successor = node->right;
            while (successor->left != nullptr)
                successor = successor->left;
            node->data = successor->data;
            return remove(node->right, successor->data);
        }

       
        Node* old = node;
        node = (node->left != nullptr) ? node->left : node->right;
        delete old;
        return true;
    }

    void preOrder(const Node* node, std::ostream& out) const
    {
        if (node == nullptr)
            return;
        out << node->data << " ";
        preOrder(node->left, out);
        preOrder(node->right, out);
    }

    void inOrder(const Node* node, std::ostream& out) const
    {
        if (node == nullptr)
            return;
        inOrder(node->left, out);
        out << node->data << " ";
        inOrder(node->right, out);
    }

    void postOrder(const Node* node, std::ostream& out) const
    {
        if (node == nullptr)
            return;
        postOrder(node->left, out);
        postOrder(node->right, out);
        out << node->data << " ";
    }

public:
    

    // Empty tree
    Tree() : root(nullptr) {}

    // Tree with a single node
    Tree(const type& value) : root(new Node(value)) {}

    // Copy constructor: deep copy of another tree
    Tree(const Tree<type>& other) : root(copyNodes(other.root)) {}

    ~Tree()
    {
        destroy(root);
    }

    
    Tree<type>& operator=(const Tree<type>& other) = delete;

   

    
    const type* find(const type& value) const
    {
        Node* current = root;
        while (current != nullptr)
        {
            if (value < current->data)
                current = current->left;
            else if (current->data < value)
                current = current->right;
            else
                return &current->data;
        }
        return nullptr;
    }

    bool insert(const type& value)
    {
        return insert(root, value);
    }

    bool remove(const type& value)
    {
        return remove(root, value);
    }

    void preOrder(std::ostream& out = std::cout) const
    {
        preOrder(root, out);
        out << std::endl;
    }

    void inOrder(std::ostream& out = std::cout) const
    {
        inOrder(root, out);
        out << std::endl;
    }

    void postOrder(std::ostream& out = std::cout) const
    {
        postOrder(root, out);
        out << std::endl;
    }
};

#endif
