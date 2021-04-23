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

    public void deleteMiddle() {
        Link currentLink = first;
        int length = 0, i = 0;
        while (currentLink.next != null) {
            length++;
            currentLink = currentLink.next;
        }
        currentLink = first;
        while (i != ((length + 1) / 2) - 1) {
            i++;
            currentLink = currentLink.next;
        }
        currentLink.next = currentLink.next.next;
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

class DeleteMiddleLast {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        boolean online = true;
        int number;
        String choice;
        LinkedList list = new LinkedList();
        while (online) {
            System.out.println("\n____________________________");
            System.out.print("\nEnter the number to be inserted : ");
            number = Integer.parseInt(in.readLine());
            list.insertLast(number);
            System.out.print("\nDo you want to continue (y/n) ? : ");
            choice = in.readLine();
            if (choice.equals("y")) online = true;
            else online = false;
        }
        System.out.print("\nThe linked list is : ");
        list.displayList();
        System.out.println("\n\nDeleting node in the middle...");
        list.deleteMiddle();
        list.displayList();
        System.out.println("\n\nDeleting node in the last...");
        list.deleteLast();
        list.displayList();
    }
}
