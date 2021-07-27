// A S Nandanunni
// Reg No: 20219023
// CS - A

import java.io.*;

class Queue {
    private int first, last, size;
    private int[] arr;

    public Queue(int s) {
        size = s;
        arr = new int[size];
        first = last = 0;
    }

    public boolean isFull() {
        if (last == size)
            return true;
        return false;
    }

    public boolean isEmpty() {
        if (first == last)
            return true;
        return false;
    }

    public void enqueue(int item) {
        if (isFull()) {
            System.out.println("Queue Full !");
            return;
        }
        arr[last++] = item;
        System.out.println("Enqueued !");
    }

    public void dequeue() {
        if (isEmpty()) {
            System.out.println("Queue Empty !");
            return;
        }
        for (int i = 0; i < last - 1; i++)
            arr[i] = arr[i + 1];
        last--;
        System.out.println("Dequeued !");
    }

    public void display() {
        if (isEmpty()) {
            System.out.println("Queue Empty !");
            return;
        }
        System.out.print(arr[0]);
        for (int i = 1; i < last; i++)
            System.out.print(" <- " + arr[i]);
    }
}

class TestQueue {

    public static void main(String args[]) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        System.out.print("Enter the size of the queue: ");
        int size = Integer.parseInt(in.readLine());
        boolean online = true;
        int chosen = 1;
        Queue q = new Queue(size);
        while (online) {
            System.out.println("\n____________________________");
            System.out.println("\nSelect your Queue operation");
            System.out.print("1. Enqueue \t2. Dequeue \n3. Display \t4. Exit \n\n\t: ");
            chosen = Integer.parseInt(in.readLine());
            System.out.println("\n");
            switch (chosen) {
                case 1:
                    System.out.print("Enter the item to enqueue:");
                    int item = Integer.parseInt(in.readLine());
                    q.enqueue(item);
                    break;
                case 2:
                    q.dequeue();
                    break;
                case 3:
                    q.display();
                    break;
                case 4:
                    online = false;
                    break;
                default:
                    System.out.println("Invalid Choice! Try Again!");
            }
        }
    }
}