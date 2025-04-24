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
        messageEl.className = `my-2 p-3 rounded-lg max-w-xl ${
            sender === "user" ? "bg-blue-200 self-end" : "bg-gray-300 dark:bg-gray-700 self-start"
        }`;
        messageEl.innerText = text;
        chatWindow.appendChild(messageEl);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function addTypingIndicator() {
        const typing = document.createElement("div");
        typing.id = "typingIndicator";
        typing.className = "my-2 p-3 bg-gray-300 dark:bg-gray-700 rounded-lg animate-pulse max-w-xs";
        typing.innerText = "Typing...";
        chatWindow.appendChild(typing);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

    function removeTypingIndicator() {
        const typing = document.getElementById("typingIndicator");
        if (typing) typing.remove();
    }
});
