package com.example.accesscontrollsystem

import android.content.Intent
import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import java.net.Socket

class MainActivity : AppCompatActivity() {

    private val ipAddress = "192.168.0.83" // Predefined IP address
    private val port = 8080 // Predefined port
    private lateinit var mainDoorButton: Button
    private lateinit var tvWebSocketStatus: TextView

    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        mainDoorButton = findViewById(R.id.mainDoorButton)
        tvWebSocketStatus = findViewById(R.id.tvWebSocketStatus)

        // Directly connect to the server when the "Main Door" button is clicked
        mainDoorButton.setOnClickListener {
            SocketManager.openSocket(ipAddress, port) { socket ->
                if (socket != null) {
                    // Connection successful
                    runOnUiThread {
                        tvWebSocketStatus.text = "Connection successful"
                        // Open MainDoorActivity
                        val intent = Intent(this@MainActivity, MainDoorActivity::class.java)
                        startActivity(intent)
                    }
                } else {
                    // Connection failed
                    runOnUiThread {
                        tvWebSocketStatus.text = "Connection failed"
                    }
                }
            }
        }
    }
}