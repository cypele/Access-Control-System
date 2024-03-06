package com.example.accesscontrollsystem

import android.os.AsyncTask
import androidx.appcompat.app.AppCompatActivity
import android.os.Bundle
import android.widget.Button
import android.widget.TextView
import java.io.PrintWriter
import java.net.Socket

class MainDoorActivity : AppCompatActivity() {

    private lateinit var sendButton: Button
    private lateinit var tvAccessInfoContent: TextView
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main_door)
        sendButton = findViewById(R.id.sendButton)
        tvAccessInfoContent = findViewById(R.id.tvAccessInfoContent)

        val socket = SocketManager.getSocket()

        // Send data when the "Send" button is clicked
        sendButton.setOnClickListener {
            val message = "Data to send" // Change this to the data you want to send
            if (socket != null && !socket.isClosed) {
                SendDataTask(socket).execute(message)
            }
        }
    }

    inner class SendDataTask(private val socket: Socket) : AsyncTask<String, Void, Void>() {
        override fun doInBackground(vararg params: String?): Void? {
            val message = params[0]

            try {
                // Send data to the server
                val writer = PrintWriter(socket.getOutputStream(), true)
                writer.println(message)
            } catch (e: Exception) {
                e.printStackTrace()
            }
            return null
        }
    }
}
