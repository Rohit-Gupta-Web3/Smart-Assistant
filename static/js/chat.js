document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("messageInput");
    const chatWindow = document.getElementById("chatWindow");
    const themeToggle = document.getElementById("themeToggle");

    form.addEventListener("submit", async (e) => {
        e.preventDefault();
        const userMessage = input.value.trim();
        if (!userMessage) return;

        addMessage("user", userMessage);
        input.value = "";

        addTypingIndicator();

        try {
            const response = await axios.post("/api/chat/", { message: userMessage });
            removeTypingIndicator();
            addMessage("bot", response.data.response);
        } catch (error) {
            removeTypingIndicator();
            addMessage("bot", "⚠️ Error contacting assistant.");
        }
    });

    themeToggle.addEventListener("click", () => {
        document.documentElement.classList.toggle("dark");
    });

    function addMessage(sender, text) {
        const messageEl = document.createElement("div");
        messageEl.className = `my-2 p-3 rounded-3 ${sender === "user" ? "bg-primary text-white ms-auto" : "bg-light text-dark"}`;
        messageEl.innerText = text;
        chatWindow.appendChild(messageEl);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function addTypingIndicator() {
        const typing = document.createElement("div");
        typing.id = "typingIndicator";
        typing.className = "my-2 p-3 bg-light text-dark rounded-3 animate-pulse";
        typing.innerText = "Typing...";
        chatWindow.appendChild(typing);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function removeTypingIndicator() {
        const typing = document.getElementById("typingIndicator");
        if (typing) typing.remove();
    }
});
