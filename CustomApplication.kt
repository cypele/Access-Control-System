package com.example.accesscontrollsystem


import android.app.Application
import java.net.Socket

class CustomApplication : Application() {

    private var socket: Socket? = null

    fun setSocket(socket: Socket) {
        this.socket = socket
    }

    fun getSocket(): Socket? {
        return socket
    }
}
