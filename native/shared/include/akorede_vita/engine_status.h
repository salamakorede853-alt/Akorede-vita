#pragma once

#ifdef __cplusplus
extern "C" {
#endif

// Reports whether a real emulator engine has been connected to this app.
int av_engine_is_ready(void);

// Returns a static status message owned by the shared library.
const char* av_engine_status_message(void);

#ifdef __cplusplus
}
#endif
