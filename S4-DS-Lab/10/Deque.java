// A S Nandanunni
// Reg No: 20219023
// CS - A

import java.io.*;

class Link {
    public Link prev;
    public int data;
    public Link next;
    public Link (int d) {
        data = d;
    }

    public void displayLink() {
        System.out.print(data);
    }
}

class Deque {
    private Link first;
    private Link last;

    public Deque() {
        first = null;
        last = null;
    }

    public boolean isEmpty() {
        return (first == null);
    }

    public void insertFirst(int element) {
        Link newLink = new Link(element);
        if (isEmpty()) {
            last = newLink;
            first = newLink;
        } else {
            first.prev = newLink;
            newLink.next = first;
            first = newLink;
        }
    }

    public void insertLast(int element) {
        Link newLink = new Link(element);
        if (isEmpty()) {
            first = newLink;
            last = newLink;
        } else {
            last.next = newLink;
            newLink.prev = last;
            last = newLink;
        }
    }

    public Link deleteFirst() {
        Link deletedLink = first;
        if (!isEmpty()) {
            if (first.next == null) {
                last = null;
                first = null;
            } else {
                first.next.prev = null;
                first = first.next;
            }
            return deletedLink;
        }
        return null;
    }

    public Link deleteLast() {
        Link deletedLink = last;
        if (!isEmpty()) {
            if (first.next == null) {
                last = null;
                first = null;
            } else {
                last.prev.next = null;
                last = last.prev;
            }
        }
        return deletedLink;
    }

    public Link getFirst() {
        return first;
    }

    public Link getLast() {
        return last;
    }

    public void displayQueue() {
        if (!isEmpty()) {
            first.displayLink();
            Link currentLink = first.next;
            while(currentLink != null) {
                System.out.print(" <-> ");
                currentLink.displayLink();
                currentLink = currentLink.next;
            }
        } else
            System.out.print("Empty Queue");
    }

}


class DequeLinkedList {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        boolean online = true;
        int chosen, element;
        Deque queue = new Deque();
        Link link = new Link(0);
        while (online) {
            System.out.println("\n____________________________");
            System.out.println("\nSelect your LinkedList operation");
            System.out.print("1. Insert first \t2. Insert last \n3. Delete first \t4. Delete last");
            System.out.print("\n5. Get first \t\t6. Get last \n7. Display Deque \t8. Exit \n\n\t: ");
            chosen = Integer.parseInt(in.readLine());
            System.out.println("\n");
            switch (chosen) {
                case 1:
                    System.out.print("Enter the element to be inserted : ");
                    element = Integer.parseInt(in.readLine());
                    queue.insertFirst(element);
                    System.out.printf("Element %d inserted at first position", element);
                    break;
                case 2:
                    System.out.print("Enter the element to be inserted : ");
                    element = Integer.parseInt(in.readLine());
                    queue.insertLast(element);
                    System.out.printf("Element %d inserted at last position", element);
                    break;
                case 3:
                    link = queue.deleteFirst();
                    if (link != null)
                        System.out.printf("Deleted %d from first position", link.data);
                    else
                        System.out.println("Empty List !");
                    break;
                case 4:
                    link = queue.deleteLast();
                    if (link != null)
                        System.out.printf("Deleted %d from last position", link.data);
                    else
                        System.out.println("Empty List !");
                    break;
                case 5:
                    link = queue.getFirst();
                    if (link != null) {
                        System.out.print("The first element is ");
                        link.displayLink();
                    }
                    else
                        System.out.println("Empty List !");
                    break;
                case 6:
                    link = queue.getLast();
                    if (link != null) {
                        System.out.print("The last element is ");
                        link.displayLink();
                    }
                    else
                        System.out.println("Empty List !");
                    break;
                case 7:
                    System.out.print("The elements of the queue are : ");
                    queue.displayQueue();
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
