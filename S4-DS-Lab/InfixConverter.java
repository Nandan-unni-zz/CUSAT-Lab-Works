// A S Nandanunni
// Reg No: 20219023
// CS - A

import java.io.*;

class InfixStack {
    private int max;
    private char[] arr;
    private int top;

    public InfixStack(int s) {
        max = s;
        arr = new char[max];
        top = -1;
    }

    public void push(char item) {
        arr[++top] = item;
    }

    public char pop() {
        return arr[top--];
    }

    public char peek() {
        return arr[top];
    }

    public boolean isFull() {
        return top == max - 1;
    }

    public boolean isEmpty() {
        return top == -1;
    }
}

class InfixConverter {

    public static String reverseString(String str) {
        StringBuffer sBuffer = new StringBuffer(str);
        sBuffer.reverse();
        str = sBuffer.toString();
        return str;
    }

    public static int precedence(char ch) {
        switch (ch) {
            case '+':
            case '-':
                return 1;
            case '*':
            case '/':
            case '%':
                return 2;
            case '$':
                return 3;
        }
        return -1;
    }

    public static boolean isOperand(char ch) {
        return Character.isLetterOrDigit(ch);
    }

    public static boolean isOperator(char ch) {
        return precedence(ch) > 0;
    }

    public static String infixToPostfixConverter(String infixString) {
        String postfixString = new String("");
        InfixStack stack = new InfixStack(infixString.length());
        char nextChar, poppedItem;
        while (!infixString.isEmpty()) {
            nextChar = infixString.charAt(0);
            infixString = infixString.substring(1);
            if (Character.compare('(', nextChar) == 0)
                stack.push(nextChar);
            if (isOperand(nextChar))
                postfixString += nextChar;
            if (Character.compare(')', nextChar) == 0) {
                while (!stack.isEmpty()) {
                    poppedItem = stack.pop();
                    if (Character.compare('(', poppedItem) == 0)
                        break;
                    else
                        postfixString += poppedItem;
                } // while
            } // if
            if (isOperator(nextChar)) {
                if (stack.isEmpty())
                    stack.push(nextChar);
                else if (precedence(nextChar) > precedence(stack.peek()))
                    stack.push(nextChar);
                else {
                    postfixString += stack.pop();
                    stack.push(nextChar);
                } // else
            } // if
        } // while
        while (!stack.isEmpty()) {
            postfixString += stack.pop();
        } // while
        return postfixString;
    }

    public static String infixToPrefixConverter(String infixString) {
        String prefixString = new String("");
        infixString = reverseString(infixString);
        char[] infixArray = infixString.toCharArray();
        for (int i = 0; i < infixArray.length; i++) {
            if (infixArray[i] == '(') {
                infixArray[i] = ')';
            } else if (infixArray[i] == ')') {
                infixArray[i] = '(';
            }
        }
        infixString = new String(infixArray);
        prefixString = infixToPostfixConverter(infixString);
        prefixString = reverseString(prefixString);
        return prefixString;
    }

    public static void main(String[] args) throws IOException {
        String infixString = new String("");
        String postfixString = new String("");
        String prefixString = new String("");
        System.out.print("\nEnter a infix string : ");
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        infixString = in.readLine();
        System.out.println("Infix : " + infixString);
        postfixString = infixToPostfixConverter(infixString);
        System.out.println("Postfix : " + postfixString);
        prefixString = infixToPrefixConverter(infixString);
        System.out.println("Prefix : " + prefixString);
    } // main
}
