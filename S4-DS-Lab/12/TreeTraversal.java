// A S Nandanunni
// Reg No: 20219023
// CS - A

import java.io.*;

class Node {
    int data;
    Node prev, next;

    Node(int d) {
        data = d;
        prev = next = null;
    }
}

public class TreeTraversal {
    Node root;

    TreeTraversal() {
        root = null;
    }

    void preOrder(Node node) {
        if (node == null)
            return;

        System.out.print(node.data + " ");
        preOrder(node.prev);
        preOrder(node.next);
    }

    void inOrder(Node node) {
        if (node == null)
            return;

        inOrder(node.prev);
        System.out.print(node.data + " ");
        inOrder(node.next);
    }

    void postOrder(Node node) {
        if (node == null)
            return;

        postOrder(node.prev);
        postOrder(node.next);
        System.out.print(node.data + " ");
    }

    void insertNode(int data) {
        Node newLink = new Node(data);
        if (root == null) {
            root = newLink;
            return;
        }
        Node currentLink = root;
        Node temp;
        while (currentLink != null) {
            temp = currentLink;
            if (data < currentLink.data) {
                currentLink = currentLink.prev;
                if (currentLink == null) {
                    temp.prev = newLink;
                }
            } else {
                currentLink = currentLink.next;
                if (currentLink == null) {
                    temp.next = newLink;
                }
            }
        }
    }

    public static void main(String args[]) throws IOException {
        TreeTraversal tree = new TreeTraversal();
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int data, chosen;
        boolean online = true;
        while (online) {
            System.out.println("\n____________________________");
            System.out.println("\nSelect your TreeTraversal operation");
            System.out.print("1. Insert \t2. In-Order \n3. Pre-Order \t4. Post-Order \n5. Exit \n\n\t: ");
            chosen = Integer.parseInt(in.readLine());
            System.out.println("\n");
            switch (chosen) {
                case 1:
                    System.out.print("Enter data to inserted: ");
                    data = Integer.parseInt(in.readLine());
                    tree.insertNode(data);
                    break;
                case 2:
                    System.out.print("In-Order traversal: ");
                    tree.inOrder(tree.root);
                    break;
                case 3:
                    System.out.print("Pre-Order traversal: ");
                    tree.preOrder(tree.root);
                    break;
                case 4:
                    System.out.print("Post-Order traversal: ");
                    tree.postOrder(tree.root);
                    break;
                case 5:
                    online = false;
                    break;
                default:
                    online = false;
                    break;
            }
        }
    }
}
