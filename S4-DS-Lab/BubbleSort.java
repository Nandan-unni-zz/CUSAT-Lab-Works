import java.io.*;

public class BubbleSort {

    public static int[] sort(int[] arr, int size) {
        int i = 0, ii = 0, temp;
        for (i = 0; i < size; i++)
            for (ii = i; ii < size; ii++)
                if (arr[ii] < arr[i]) {
                    temp = arr[i];
                    arr[i] = arr[ii];
                    arr[ii] = temp;
                }
        return arr;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
        int i = 0, size = 0;
        int[] arr;
        System.out.print("Enter the size of the array : ");
        size = Integer.parseInt(in.readLine());
        arr = new int[size];
        System.out.println("\nEnter the elements of the array : ");
        for (i = 0; i < size; i++)
            arr[i] = Integer.parseInt(in.readLine());

        System.out.print("\nThe input array is [");
        for (i = 0; i < size; i++)
            System.out.printf("%d, ", arr[i]);
        System.out.print("] \nThe sorted array is [");

        arr = sort(arr, size);

        for (i = 0; i < size; i++)
            System.out.printf("%d, ", arr[i]);
        System.out.println("]");
    }
}
