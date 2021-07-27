// A S Nandanunni
// Reg No: 20219023
// CS - A

import java.io.*;

class Link {
    int data;
    Link next;

    public Link(int d) {
        data = d;
    }
}

class LinkedList {
    Link first = null;

    public boolean isEmpty() {
        return first == null;
    }

    public void insert(int data) {
        Link newLink = new Link(data);
        if (first == null)
            first = newLink;
        else if (newLink.data > first.data) {
            newLink.next = first;
            first = newLink;
        } else {
            Link currentLink = first;
            while (currentLink.next != null) {
                if (currentLink.next.data > newLink.data) {
                    currentLink = currentLink.next;
                } else {
                    break;
                }
            }
            newLink.next = currentLink.next;
            currentLink.next = newLink;
        }
    }

    public void remove() {
        if (!isEmpty()) {
            first = first.next;
        } else {
            System.out.print("Priority Queue is empty!");
        }
    }

    public void displayList() {
        Link currentLink = first;
        if (isEmpty()) {
            System.out.print("List is empty!");
        } else {
            System.out.print("Linkedlist: ");
            System.out.print(currentLink.data);
            while (currentLink.next != null) {
                currentLink = currentLink.next;
                System.out.print(" --> " + currentLink.data);
            }
        }
        System.out.println('\n');
    }

    public int peekMax() {
        return first.data;
    }

    public int peekMin() {
        Link currentLink = first;
        while (currentLink.next != null)
            currentLink = currentLink.next;
        return currentLink.data;
    }
}

class PriorityQueue {
    public static void main(String args[]) throws IOException {
        LinkedList list = new LinkedList();
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int element, chosen;
        boolean online = true;
        while (online) {
            System.out.println("\n____________________________");
            System.out.println("\nSelect your PriorityQueue operation");
            System.out.print("1. Insert \t2. Delete \n3. Peek Max \t\t4. Peek Min \n5. Exit \n\n\t: ");
            chosen = Integer.parseInt(in.readLine());
            System.out.println("\n");
            switch (chosen) {
                case 1:
                    System.out.println("Enter the element to be added: ");
                    element = Integer.parseInt(in.readLine());
                    list.insert(element);
                    list.displayList();
                    break;
                case 2:
                    System.out.println("Deleting element");
                    list.remove();
                    list.displayList();
                    break;
                case 3:
                    System.out.println("Peek Max: " + list.peekMax());
                    list.displayList();
                    break;
                case 4:
                    System.out.println("Peek Min: " + list.peekMin());
                    list.displayList();
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