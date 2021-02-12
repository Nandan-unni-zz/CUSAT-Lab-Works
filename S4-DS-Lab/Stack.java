import java.io.*;

class Stack {
    private int max;
    private int[] arr;
    private int top;

    public Stack(int s) {
        max = s;
        arr = new int[max];
        top = -1;
    }

    public void push(int item) {
        top++;
        arr[top] = item;
        // or --> arr[++top] = item
    }

    public int pop() {
        int item = arr[top];
        top--;
        return item;
        // or --> return arr[top--]
    }

    public int peek() {
        return arr[top];
    }

    public boolean isFull() {
        return top == max - 1;
    }

    public boolean isEmpty() {
        return top == -1;
    }
}

class TestStack {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        boolean online = true;
        int chosen, item = 0, size = 0;
        System.out.print("\nEnter the size of the stack : ");
        size = Integer.parseInt(in.readLine());
        Stack stack = new Stack(size);
        while (online) {
            System.out.println("\n____________________________");
            System.out.println("\nSelect your stack operation");
            System.out.print("1. Push \t2. Pop \n3. Peek \t4. Exit \n\n\t:");
            chosen = Integer.parseInt(in.readLine());
            System.out.println("\n");
            switch (chosen) {
                case 1:
                    if (!stack.isFull()) {
                        System.out.print("Enter the element to be pushed : ");
                        item = Integer.parseInt(in.readLine());
                        stack.push(item);
                        System.out.printf("Pushed %d to stack", item);
                    } else {
                        System.out.println("Stack Overflow !");
                    }
                    break;
                case 2:
                    if (!stack.isEmpty()) {
                        item = stack.pop();
                        System.out.printf("Popped %d from stack", item);
                    } else {
                        System.out.println("Stack Underflow !");
                    }
                    break;
                case 3:
                    if (!stack.isEmpty()) {
                        item = stack.peek();
                        System.out.printf("%d is at the top of stack", item);
                    } else {
                        System.out.println("Stack Underflow !");
                    }
                    break;
                case 4:
                    online = false;
                    break;
                default:
                    online = false;
                    break;
            }
        }
    }
}