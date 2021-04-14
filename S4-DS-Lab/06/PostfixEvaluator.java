// A S Nandanunni
// Reg No: 20219023
// CS - A

import java.io.*;

class PostfixStack {
    private int max;
    private int[] arr;
    private int top;

    public PostfixStack(int s) {
        max = s;
        arr = new int[max];
        top = -1;
    }

    public void push(int item) {
        arr[++top] = item;
    }

    public int pop() {
        return arr[top--];
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


public class PostfixEvaluator {

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

    public static int calculate(int x, int y, char op) {
        int result = 0;
        Double pow_result;
        switch (op) {
            case '+':
                result = x + y;
                break;
            case '-':
                result = x > y ? x - y : y - x;
                break;
            case '*':
                result = x * y;
                break;
            case '/':
                result = x > y ? x / y : y / x;
                break;
            case '%':
                result = x % y;
                break;
            case '$':
                pow_result = Math.pow(Double.valueOf(x), Double.valueOf(y));
                result = pow_result.intValue();
                break;
        }
        return result;
    }

    public static void main(String[] args) throws IOException {
        String postfixString = new String("");
        System.out.print("\nEnter a postfix string : ");
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        postfixString = in.readLine();
        PostfixStack stack = new PostfixStack(postfixString.length());
        int firstOperand = 0, secondOperand = 0, calculatedValue;
        for (int i = 0; i < postfixString.length(); i++) {
            if (isOperand(postfixString.charAt(i))) {
                if (!stack.isFull()) {
                    stack.push(Integer.parseInt(String.valueOf(postfixString.charAt(i))));
                } // if
            } else if (isOperator(postfixString.charAt(i))) {
                if (!stack.isEmpty())
                    firstOperand = stack.pop();
                if (!stack.isEmpty())
                    secondOperand = stack.pop();
                calculatedValue = calculate(firstOperand, secondOperand, postfixString.charAt(i));
                if (!stack.isFull())
                    stack.push(calculatedValue);
            }
        }
        System.out.println("Postfix expression value : " + stack.pop());
    }
}
