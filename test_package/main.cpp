#include "charsetdetect.h"
#include "stdio.h"

#define BUFFER_SIZE 4096

int main(int argc, const char * argv[]) {
    csd_t csd = csd_open();
    if (csd == (csd_t)-1) {
        printf("csd_open failed\n");
        return 1;
    }

    int size;
    char buf[BUFFER_SIZE] = {0};

    while ((size = fread(buf, 1, sizeof(buf), stdin)) != 0) {
        int result = csd_consider(csd, buf, size);
        if (result < 0) {
            printf("csd_consider failed\n");
            return 3;
        } else if (result > 0) {
            // Already have enough data
            break;
        }
    }

    const char *result = csd_close(csd);
    if (result == NULL) {
        printf("Unknown character set\n");
        return 2;
    } else {
        printf("%s\n", result);
        return 0;
    }
}
