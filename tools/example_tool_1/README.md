# Log File Analyzer: A TrashmanHacker Tool

## "Don’t Panic" — Your Guide to Understanding Logs

Welcome to the **Log File Analyzer**, your trusty sidekick in navigating the galaxy of log files. Whether you're unraveling mysteries hidden in server logs or hunting down pesky error codes, this tool simplifies the chaos and turns raw data into actionable insights.

---

## 🛠️ Features

- **IP Analysis:** Identify unique IP addresses and their frequency of appearance.
- **HTTP Method Breakdown:** See which methods (e.g., GET, POST) are used most often.
- **Error Detection:** Quickly spot 4xx and 5xx error codes for debugging.
- **Summarized Insights:** Provides an easy-to-read summary of the log data.

---

## 🚀 How to Use

1. **Get the Tool:** Clone this repository and ensure you have Python installed on your system.
2. **Run the Script:**
   ```bash
   python log_file_analyzer.py
   ```
3. **Input the Log File Path:** When prompted, enter the full path to your log file.
4. **Review the Summary:** Sit back and let the tool do its magic.

---

## 📂 Example Input
A typical log file entry might look like this:
```
192.168.1.1 - - [10/Jan/2025:10:00:00] "GET /index.html HTTP/1.1" 200 512
192.168.1.2 - - [10/Jan/2025:10:01:00] "POST /login HTTP/1.1" 403 1024
```

---

## 📊 Example Output
After analyzing the file, you’ll see a summary like this:
```
=== Log Analysis Summary ===
Total Lines in Log: 2

Unique IP Addresses:
192.168.1.1: 1
192.168.1.2: 1

HTTP Methods:
GET: 1
POST: 1

Error Codes:
403: 1
```

---

## 🌌 Why Use This Tool?
In the vast expanse of log files, this tool is your digital towel, helping you make sense of server events, debug faster, and understand user behavior. It’s designed to make your life easier, one log at a time.

---

## 📜 License
This tool is part of the TrashmanHacker arsenal. Use it wisely and share the knowledge. Licensed under MIT.

---

## "Remember: Logs are like stars in the sky. They may seem overwhelming, but with the right guide, you can map the universe."
