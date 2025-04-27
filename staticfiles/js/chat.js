document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("chatForm");
    const input = document.getElementById("messageInput");
    const chatWindow = document.getElementById("chatWindow");
    const themeToggle = document.getElementById("themeToggle");
    const historyPanel = document.getElementById("historyPanel");
    const historyContent = document.getElementById("historyContent");
    const toggleHistory = document.getElementById("toggleHistory");
    const chatHistory = document.getElementById("chatHistory");
    const clearHistoryBtn = document.getElementById("clearHistory");

    toggleHistory?.addEventListener("click", () => {
        chatHistory?.classList.toggle("d-none");
    });

    themeToggle?.addEventListener("click", () => {
        const htmlEl = document.documentElement;
        const isDark = htmlEl.classList.toggle("dark");
        localStorage.setItem("theme", isDark ? "dark" : "light");
        document.body.classList.toggle("bg-dark", isDark);
        document.body.classList.toggle("text-light", isDark);
        document.body.classList.toggle("bg-light", !isDark);
        document.body.classList.toggle("text-dark", !isDark);
    });

    if (localStorage.getItem("theme") === "dark") {
        document.documentElement.classList.add("dark");
        document.body.classList.add("bg-dark", "text-light");
        document.body.classList.remove("bg-light", "text-dark");
    }

    clearHistoryBtn?.addEventListener("click", () => {
        localStorage.removeItem("chatHistory");
        historyContent.innerHTML = "";
    });

    function saveHistoryToLocalStorage() {
        localStorage.setItem("chatHistory", historyContent.innerHTML);
    }

    function loadHistoryFromLocalStorage() {
        const saved = localStorage.getItem("chatHistory");
        if (saved) historyContent.innerHTML = saved;
    }

    function formatTime(date) {
        return date.toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });
    }

    function addMessageToHistory(content, sender) {
        const time = formatTime(new Date());
        const messageElem = document.createElement("div");
        messageElem.classList.add("history-message", "mb-2");
        messageElem.innerHTML = `
            <div class="d-flex align-items-center">
                <div class="avatar me-2">
                    <img src="/static/img/${sender}.png" alt="${sender}" width="30" height="30" class="rounded-circle">
                </div>
                <div>
                    <div class="message bg-light p-2 rounded">${marked.parse(content)}</div>
                    <div class="text-muted small mt-1">${time}</div>
                </div>
            </div>`;
        historyContent.appendChild(messageElem);
        historyPanel.scrollTop = historyPanel.scrollHeight;
        saveHistoryToLocalStorage();
    }

    function appendMessage(content, sender = 'user') {
        const time = formatTime(new Date());
        const messageElem = document.createElement("div");
        messageElem.className = `chat-message ${sender === 'user' ? 'chat-user' : 'chat-bot'} mb-3`;
        messageElem.innerHTML = `
            <div class="d-flex align-items-start">
                <div class="avatar me-2">
                    <img src="/static/img/${sender}.png" alt="${sender}" width="40" height="40" class="rounded-circle">
                </div>
                <div>
                    <div class="message bg-light p-3 rounded shadow-sm">${marked.parse(content)}</div>
                    <div class="text-muted small mt-1">${time}</div>
                </div>
            </div>`;
        chatWindow.appendChild(messageElem);
        chatWindow.scrollTop = chatWindow.scrollHeight;
        addMessageToHistory(content, sender);
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
        document.getElementById("typingIndicator")?.remove();
    }

    function addMessage(sender, text) {
        const messageEl = document.createElement("div");
        messageEl.className = `my-2 p-3 rounded-3 ${sender === "user" ? "bg-primary text-white ms-auto" : "bg-light text-dark"}`;
        messageEl.innerText = text;
        chatWindow.appendChild(messageEl);
        chatWindow.scrollTop = chatWindow.scrollHeight;
    }

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

    loadHistoryFromLocalStorage();
});
