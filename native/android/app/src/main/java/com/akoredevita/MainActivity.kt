package com.akoredevita

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.Arrangement
import androidx.compose.foundation.layout.Column
import androidx.compose.foundation.layout.Spacer
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.height
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.Surface
import androidx.compose.material3.Text
import androidx.compose.material3.darkColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        System.loadLibrary("akorede_vita_android")
        setContent {
            MaterialTheme(colorScheme = darkColorScheme()) {
                VitaHomeScreen(
                    engineReady = nativeEngineReady(),
                    engineStatus = nativeEngineStatus()
                )
            }
        }
    }

    private external fun nativeEngineReady(): Boolean
    private external fun nativeEngineStatus(): String
}

@Composable
private fun VitaHomeScreen(engineReady: Boolean, engineStatus: String) {
    Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
        Column(
            modifier = Modifier.fillMaxSize().padding(28.dp),
            verticalArrangement = Arrangement.Center,
            horizontalAlignment = Alignment.Start
        ) {
            Text("AKOREDE VITA", fontSize = 30.sp, color = MaterialTheme.colorScheme.primary)
            Spacer(Modifier.height(12.dp))
            Text("Android application foundation")
            Spacer(Modifier.height(28.dp))
            Text(if (engineReady) "Emulator engine ready" else engineStatus)
            Spacer(Modifier.height(8.dp))
            Text("This development build is an application shell, not a playable emulator.")
        }
    }
}
