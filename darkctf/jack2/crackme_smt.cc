#include<stdio.h>
#include<string.h>

#define EXIT_SUCCESS 0
#define EXIT_FAILURE 1

int SHR(int v, int n) {
    return (v >> n) & (1 << (32 -n ));
}

int SHL(int v, int n) {
    return (v << n) & (1 >> (32 -n ));
}

void parse_string(int i, int k, char flag[], unsigned int h[]) {
    h[i] = flag[k] + (flag[k+1] << 8) + (flag[k+2] << 16) + (flag[k+3] << 24);
}

void check_flag(unsigned int h[]) {
    if (h[0] == 0xcb9f59b7 && h[1] == 0x5b90f617 && h[2] == 0x20e59633 && h[3] == 0x102fd1da) {
        puts("Good Work!");
    } else {
        puts("Try Harder");
    }
}

int main() {
    char buf[17];
    int i,k = 0;
    unsigned int uVar1;
    int iVar2;
    unsigned int hash[4];
    puts("Enter your key: ");
    fgets(buf, 17, stdin);
    fflush(stdout);

    buf[16] = '\0';
    if (strlen(buf) != 16) {
        puts("Try Harder");
        return EXIT_FAILURE;
    }

    for (i = 0 ; i < 4; i++) {
        parse_string(i, k, buf, hash);
        for(int j = 0 ; j < 2; j++) {
            uVar1 = hash[i];
            iVar2 = SHR(hash[i],3);
            hash[i] = uVar1 ^ hash[i] * 0x20 + iVar2;
            uVar1 = hash[i];
            iVar2 = SHL(hash[i],5);
            hash[i] = uVar1 ^ hash[i] * 0x80 + iVar2;
            hash[i] = hash[i] + (hash[i] >> 1 & 0xff);
        }
        k = k+4;
    }
    //printf("\n0x%x, 0x%x, 0x%x, 0x%x", hash[0], hash[1], hash[2], hash[3]);
    check_flag(hash);
}

void __attribute__((destructor))
    bye() {
        puts("bye");
    }
