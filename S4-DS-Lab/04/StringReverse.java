// A S Nandanunni
// Reg No: 20219023
// CS - A

import java.io.*;

class CharStack {
    private int max;
    private char[] arr;
    private int top;

    public CharStack(int s) {
        max = s;
        arr = new char[max];
        top = -1;
    }

    public void push(char item) {
        top++;
        arr[top] = item;
        // or --> arr[++top] = item
    }

    public char pop() {
        char item = arr[top];
        top--;
        return item;
        // or --> return arr[top--]
    }

    public char peek() {
        if (top != -1)
            return arr[top];
        else
            return '0';
    }

    public boolean isFull() {
        return top == max - 1;
    }

    public boolean isEmpty() {
        return top == -1;
    }
}

public class StringReverse {
    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        String orginalString = new String("");
        String revrsedString = new String("");
        System.out.print("\nEnter a string : ");
        orginalString = in.readLine();
        int stringLength = orginalString.length();
        CharStack string = new CharStack(stringLength);
        for (int i = 0; i < stringLength; i++) {
            char poppedItem = orginalString.charAt(i);
            string.push(poppedItem);
        }
        while (!string.isEmpty()) {
            char poppedItem = string.pop();
            revrsedString += poppedItem;
        }
        System.out.print("\nReversed string : " + revrsedString + "\n");
    }
}
