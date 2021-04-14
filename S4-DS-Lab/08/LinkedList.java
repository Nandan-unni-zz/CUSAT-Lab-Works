// A S Nandanunni
// Reg No: 20219023
// CS - A

import java.io.*;

class Link {
    public int data;
    public Link next;
    public Link (int d) {
        data = d;
    }

    public void displayLink() {
        System.out.print(data);
    }
}

class LinkedList {
    private Link first;

    public LinkedList() {
        first = null;
    }

    public boolean isEmpty() {
        return (first == null);
    }

    public void insertFirst(int element) {
        Link newLink = new Link(element);
        newLink.next = first;
        first = newLink;
    }

    public Link deleteFirst() {
        Link lastLink = first;
        if (!isEmpty()) {
            first = first.next;
            return lastLink;
        }
        return null;
    }

    public void insertLast(int element) {
        Link newLink = new Link(element);
        if (first == null) {
            first = newLink;
        } else { 
            Link current = null;
            current = first;
            while(current.next != null) {
                current = current.next;
            }
            current.next = newLink;
            newLink.next = null;
        }
    }

    public Link deleteLast() {
        Link lastLink = null;
        if (!isEmpty()) {
            lastLink = first;
            if (first.next != null)
                while (lastLink.next.next != null)
                        lastLink = lastLink.next;
            lastLink.next = null;
            return lastLink;
        }
        return null;
    }

    public void insert(int key, int d) {
        Link newLink = new Link(d);
        Link currentLink = first;
        Link previousLink = first;
        while (currentLink.data != key) {
            if (currentLink.next == null)
                break;
            else {
                previousLink = currentLink;
                currentLink = currentLink.next;
            }
        }
        newLink.next = previousLink.next;
        previousLink.next = newLink;
    }

    public Link delete(int key) {
        Link currentLink = first;
        Link previousLink = first;
        while (currentLink.data != key) {
            if (currentLink.next == null)
                return null;
            else {
                previousLink = currentLink;
                currentLink = currentLink.next;
            }
        }
        if (currentLink == first)
            first = first.next;
        else
            previousLink.next = currentLink.next;
        return currentLink;
    }

    public void displayList() {
        first.displayLink();
        Link currentLink = first.next;
        while(currentLink != null) {
            System.out.print(" -> ");
            currentLink.displayLink();
            currentLink = currentLink.next;
        }
    }

}

class TestLinkedList {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        boolean online = true;
        int chosen, key, element;
        LinkedList list = new LinkedList();
        Link link = new Link(0);
        while (online) {
            System.out.println("\n____________________________");
            System.out.println("\nSelect your LinkedList operation");
            System.out.print("1. Insert first \t2. Delete first \n3. Insert last \t\t4. Delete last \n5. Insert \t\t6. Delete \n7.Display \t\t8. Exit \n\n\t: ");
            chosen = Integer.parseInt(in.readLine());
            System.out.println("\n");
            switch (chosen) {
                case 1:
                    System.out.print("Enter the element to be inserted : ");
                    element = Integer.parseInt(in.readLine());
                    list.insertFirst(element);
                    System.out.printf("Element %d inserted at first position", element);
                    break;
                case 2:
                    link = list.deleteFirst();
                    if (link != null)
                        System.out.printf("Deleted %d from first position", link.data);
                    else
                        System.out.println("Empty List !");
                    break;
                case 3:
                    System.out.print("Enter the element to be inserted : ");
                    element = Integer.parseInt(in.readLine());
                    list.insertLast(element);
                    System.out.printf("Element %d inserted at last position", element);
                    break;
                case 4:
                    link = list.deleteLast();
                    if (link != null)
                        System.out.printf("Deleted %d from last position", link.data);
                    else
                        System.out.println("Empty List !");
                    break;
                case 5:
                    System.out.print("Enter the element to be inserted : ");
                    element = Integer.parseInt(in.readLine());
                    if (list.isEmpty()) {
                        list.insertFirst(element);
                        System.out.printf("Element %d inserted at first position", element);
                    } else {
                        System.out.print("Enter the previous element : ");
                        key = Integer.parseInt(in.readLine());
                        list.insert(key, element);
                        System.out.printf("Inserted %d to list after %d", element, key);
                    }
                    break;
                case 6:
                    System.out.print("Enter the element to be deleted : ");
                    key = Integer.parseInt(in.readLine());
                    link = list.delete(key);
                    if (link != null)
                        System.out.printf("Deleted %d", link.data);
                    else
                        System.out.printf("Element not found");
                    break;
                case 7:
                    System.out.print("The elements of the list are : ");
                    list.displayList();
                    break;
                case 8:
                    online = false;
                    break;
                default:
                    online = false;
                    break;
            }
        }
    }
}
