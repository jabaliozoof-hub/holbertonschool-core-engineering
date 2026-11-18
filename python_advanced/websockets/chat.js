const socket = new WebSocket("ws://localhost:8000/ws");

const statusEl = document.getElementById("status");
const messagesEl = document.getElementById("messages");
const formEl = document.getElementById("form");
const inputEl = document.getElementById("input");

function addMessage(text, kind) {
    const div = document.createElement("div");
    div.className = "message " + kind;
    div.textContent = text;
    messagesEl.appendChild(div);
    messagesEl.scrollTop = messagesEl.scrollHeight;
}

socket.onopen = () => {
    statusEl.textContent = "Connected";
};

socket.onmessage = (event) => {
    addMessage(event.data, "received");
};

socket.onclose = () => {
    statusEl.textContent = "Disconnected";
};

socket.onerror = () => {
    statusEl.textContent = "Connection error";
};

formEl.addEventListener("submit", (event) => {
    event.preventDefault();
    const text = inputEl.value.trim();
    if (text === "" || socket.readyState !== WebSocket.OPEN) {
        return;
    }
    socket.send(text);
    addMessage(text, "sent");
    inputEl.value = "";
});
