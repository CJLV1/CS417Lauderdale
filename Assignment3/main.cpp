#include <iostream>
#include <string>
#include "Tree.h"

using namespace std;

//The test driver was tabbed.
struct IndexCard
{
    int index;
    string contents;

    IndexCard(int i = 0, const string& c = "") : index(i), contents(c) {}
};

bool operator<(const IndexCard& a, const IndexCard& b)
{
    return a.index < b.index;
}

ostream& operator<<(ostream& out, const IndexCard& card)
{
    out << "[" << card.index << "]";
    return out;
}

int main()
{
    Tree<IndexCard> tree(IndexCard(50, "Mitochondria is the powerhouse of the cell"));
    tree.insert(IndexCard(30, "Buy milk, eggs, and coffee"));
    tree.insert(IndexCard(70, "The French Revolution began in 1789"));
    tree.insert(IndexCard(20, "Big-O of binary search is O(log n)"));
    tree.insert(IndexCard(40, "Call the dentist on Tuesday"));
    tree.insert(IndexCard(60, "Pi is roughly 3.14159"));
    tree.insert(IndexCard(80, "Haiku: five, seven, five"));

    cout << "Pre-order:  ";
    tree.preOrder();
    cout << "In-order:   ";
    tree.inOrder();
    cout << "Post-order: ";
    tree.postOrder();

    cout << "\nCard 40 says: " << tree.find(IndexCard(40))->contents << endl;

    Tree<IndexCard> copy(tree);
    copy.remove(IndexCard(50));
    cout << "\nCopy with card 50 removed: ";
    copy.inOrder();
    cout << "Original is unchanged:     ";
    tree.inOrder();

    return 0;
}
