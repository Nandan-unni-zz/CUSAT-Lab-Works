// A S Nandanunni
// Reg No: 20219023
// CS - A

import java.io.*;

class Link {
    public Link prev;
    public int rollno;
    public int rank;
    public String name;
    public Link next;

    public Link(int rollnoParam, String nameParam, int rankParam) {
        rollno = rollnoParam;
        name = nameParam;
        rank = rankParam;
        prev = null;
        next = null;
    }

    public void displayLink() {
        System.out.printf("Roll No: %d\n", rollno);
        System.out.printf("Name: %s\n", name);
        System.out.printf("Rank: %d\n\n", rank);
    }
}

class DoublyLinkedList {
    private Link first;

    public DoublyLinkedList() {
        first = null;
    }

    public boolean isEmpty() {
        return (first == null);
    }

    public void insertFirst(int rollno, String name, int rank) {
        Link newLink = new Link(rollno, name, rank);
        if (isEmpty()) {
            first = newLink;
        } else {
            newLink.next = first;
            first.prev = newLink;
            newLink.prev = null;
            first = newLink;
        }
    }

    public void insertLast(int rollno, String name, int rank) {
        Link newLink = new Link(rollno, name, rank);
        if (first == null) {
            first = newLink;
        } else {
            Link currentLink = null;
            currentLink = first;
            while (currentLink.next != null) {
                currentLink = currentLink.next;
            }
            currentLink.next = newLink;
            newLink.prev = currentLink;
            newLink.next = null;
        }
    }

    public Link deleteFirst() {
        Link deletedLink = first;
        if (!isEmpty()) {
            if (first.next == null) {
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
        if (!isEmpty()) {
            if (first.next == null) {
                first = null;
            } else {
                Link currentLink = first;
                while (currentLink.next != null) {
                    currentLink = currentLink.next;
                }
                currentLink.prev.next = null;
            }
        }
        return null;
    }

    public void swapStudent(Link student1, Link student2) {
        int tempRollno, tempRank;
        String tempName;
        tempRollno = student1.rollno;
        student1.rollno = student2.rollno;
        student2.rollno = tempRollno;

        tempName = student1.name;
        student1.name = student2.name;
        student2.name = tempName;

        tempRank = student1.rank;
        student1.rank = student2.rank;
        student2.rank = tempRank;
    }

    public void sortByRollno() {
        if (!isEmpty()) {
            Link currentLink = null, index = null;
            for(currentLink = first; currentLink.next != null; currentLink = currentLink.next) {
                for(index = currentLink.next; index != null; index = index.next) {
                    if(currentLink.rollno > index.rollno) {
                        swapStudent(currentLink, index);
                    }
                }
            }
        }
    }

    public void sortByRank() {
        if (!isEmpty()) {
            Link currentLink = null, index = null;
            for(currentLink = first; currentLink.next != null; currentLink = currentLink.next) {
                for(index = currentLink.next; index != null; index = index.next) {
                    if(currentLink.rank > index.rank) {
                        swapStudent(currentLink, index);
                    }
                }
            }
        }
    }

    public void displayList() {
        if (!isEmpty()) {
            first.displayLink();
            Link currentLink = first.next;
            while (currentLink != null) {
                currentLink.displayLink();
                currentLink = currentLink.next;
            }
        } else
            System.out.print("Empty List");
    }

}

class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        boolean online = true;
        int chosen, rollno, rank;
        String name = new String("");
        DoublyLinkedList list = new DoublyLinkedList();
        Link link = new Link(0, "", 0);
        while (online) {
            System.out.println("\n____________________________");
            System.out.println("\nSelect your LinkedList operation");
            System.out.print("1. Insert first \t2. Insert last \n3. Delete first \t4. Delete last");
            System.out.print("\n5. Sort By Rollno \t6. Sort By Rank \n7. Display List \t8. Exit \n\n\t: ");
            chosen = Integer.parseInt(in.readLine());
            System.out.println("\n");
            switch (chosen) {
            case 1:
                System.out.print("Enter the roll no : ");
                rollno = Integer.parseInt(in.readLine());
                System.out.print("Enter the name : ");
                name = in.readLine();
                System.out.print("Enter the rank : ");
                rank = Integer.parseInt(in.readLine());
                list.insertFirst(rollno, name, rank);
                System.out.printf("Student %s inserted at first position", name);
                break;
            case 2:
                System.out.print("Enter the roll no : ");
                rollno = Integer.parseInt(in.readLine());
                System.out.print("Enter the name : ");
                name = in.readLine();
                System.out.print("Enter the rank : ");
                rank = Integer.parseInt(in.readLine());
                list.insertLast(rollno, name, rank);
                System.out.printf("Student %s inserted at last position", name);
                break;
            case 3:
                link = list.deleteFirst();
                if (link != null)
                    System.out.printf("Deleted %s from first position", link.name);
                else
                    System.out.println("Empty List !");
                break;
            case 4:
                link = list.deleteLast();
                if (link != null)
                    System.out.printf("Deleted %s from last position", link.name);
                else
                    System.out.println("Empty List !");
                break;
            case 5:
                list.sortByRollno();
                System.out.println("List sorted by roll no!");
                break;
            case 6:
                list.sortByRank();
                System.out.println("List sorted by rank !");
                break;
            case 7:
                System.out.print("The elements of the list are : \n");
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
