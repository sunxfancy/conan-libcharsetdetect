#include "charsetdetect.h"
#include "stdio.h"

int main(int argc, const char * argv[]) {
    csd_t csd = csd_open();
    if (csd == (csd_t)-1) {
        printf("csd_open failed\n");
        return 1;
    }
    return 0;
}
