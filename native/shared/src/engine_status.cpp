#include "akorede_vita/engine_status.h"

extern "C" int av_engine_is_ready(void) {
    // Deliberately false until a reviewed emulator-core integration exists.
    return 0;
}

extern "C" const char* av_engine_status_message(void) {
    return "Emulator core not connected";
}
