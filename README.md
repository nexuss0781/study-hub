# Telegram Bot Boilerplate

A minimal, working Telegram bot boilerplate for **Vercel** (serverless, webhook).

Fork it, deploy, and start building your bot — no setup headaches.

## What's Inside

- `/webhook` — handles incoming Telegram updates (example: `/start` → "Hello World")
- `/dashboard` — live status page to verify the bot is healthy
- `/api/test-webhook` — JSON endpoint for uptime monitoring

Built with FastAPI + python-telegram-bot. Deploys on Vercel free tier. ~90 lines.

## Why

Old `python-telegram-bot` versions break on Vercel's Python runtime. This repo solves that — latest PTB, no vendored dependency conflicts, async-native, serverless-friendly.

Fork it, swap the command logic, add your features. That's it.

## Quick Start

1. Fork, push to GitHub, import into Vercel
2. Set `TOKEN` env var (from [@BotFather](https://t.me/botfather))
3. Deploy, then register webhook:

```bash
curl -X POST "https://api.telegram.org/bot<TOKEN>/setWebhook?url=https://<VERCEL_URL>/webhook"
```

Done. Your bot is live.

## Local Dev

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt uvicorn
export TOKEN=<token>
uvicorn api.index:app --reload --port 8000
```
