#include <jni.h>
#include "akorede_vita/engine_status.h"

extern "C" JNIEXPORT jboolean JNICALL
Java_com_akoredevita_MainActivity_nativeEngineReady(JNIEnv*, jobject) {
    return av_engine_is_ready() ? JNI_TRUE : JNI_FALSE;
}

extern "C" JNIEXPORT jstring JNICALL
Java_com_akoredevita_MainActivity_nativeEngineStatus(JNIEnv* env, jobject) {
    return env->NewStringUTF(av_engine_status_message());
}
