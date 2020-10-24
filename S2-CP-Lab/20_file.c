// A S Nandanunni
// Reg No: 20219023
// CS - A

#include <stdio.h>
#include <string.h>

int main()
{
    int ch_count = 0, ln_count = 0;
    char ch, filename[40];
    FILE* file;
    printf("Enter the filename : ");
    scanf("%s", filename);
    file = fopen(filename, "r");
    if (file == NULL)
    {
        printf("File not found\n");
        return 0;
    }
    for (ch = getc(file); ch != EOF; ch = getc(file))
    {
        ch_count++;
        if (ch == '\n')
            ln_count++;
    }
    printf("The file %s have %d characters and %d lines.", filename, ch_count, ln_count + 1);
    fclose(file);
    return 0;
}

/*
OUTPUT


*/