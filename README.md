# 🌟 Eleven Eleven

**Eleven Eleven** is a lightweight Python app that sends a Discord notification to your phone every day at **11:11 AM** and **11:11 PM**. It's designed to give you a gentle nudge — a daily reminder to **make a wish** ✨

---

## 📦 Features

- Sends a message to your Discord server via webhook
- Runs automatically using `cron` at 11:11 and 23:11
- Simple and easy to configure using environment variables

---

The application is configured to run on a schedule with the following entries in crontab:

```bash
11 11 * * * /usr/bin/python3 /full/path/to/eleven_eleven.py
11 23 * * * /usr/bin/python3 /full/path/to/eleven_eleven.py
```

Ensure that your discord webhook URL is stored in .env following the setup in .env.example


