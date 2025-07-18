
let protocol = window.location.protocol === "https:" ? "wss:" : "ws:"
let url = window.location.host;

const wsurl = `${protocol}//${url}/ws/`

let socket = new WebSocket(wsurl)

if (socket.onopen){
    console.log("Connected to websocket!")
} else {
    console.error("Could not connect to websocket!")
}

socket.send({"text":"Hello world"})