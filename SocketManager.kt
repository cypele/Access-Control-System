package com.example.accesscontrollsystem

import java.net.Socket

object SocketManager {
    private var socket: Socket? = null

    // Function to open socket asynchronously
    fun openSocket(ipAddress: String, port: Int, callback: (Socket?) -> Unit) {
        Thread {
            try {
                socket = Socket(ipAddress, port)
                callback(socket) // Pass the socket back to the caller
            } catch (e: Exception) {
                e.printStackTrace()
                callback(null) // Pass null to indicate failure
            }
        }.start()
    }

    fun closeSocket() {
        try {
            socket?.close()
        } catch (e: Exception) {
            e.printStackTrace()
        }
    }

    fun getSocket(): Socket? {
        return socket
    }
}