# Autonomous GPT Bridge Registry

## Purpose
Define every bridge category the Intelligence Cube should know how to route, validate, and document before AUTO_BUILDER-V1 implementation.

## Bridge Classes

| # | Bridge | Purpose | Default Mode | Validation Receipt |
|---|---|---|---|---|
| 1 | GitHub Connector | Branches, commits, PRs, code/doc evidence | Branch-only | receipts/github/ |
| 2 | Vercel Connector | Project, deployment, logs, cron and agent run evidence | Read/preview | receipts/vercel/ |
| 3 | Google Drive Connector | Canon docs, workbook storage, release folders | Read/draft | receipts/drive/ |
| 4 | Google Sheets Connector | Ops sheets, workbook tables, queue ledgers | Read/draft | receipts/sheets/ |
| 5 | Google Docs Connector | SOPs, runbooks, client docs | Draft | receipts/docs/ |
| 6 | Gmail Connector | Inbox research and draft messages | Draft only | receipts/gmail/ |
| 7 | Google Calendar Connector | Scheduling and operating cadence | Draft/read | receipts/calendar/ |
| 8 | Supabase Connector | Schema, queues, storage, telemetry | Dry-run first | receipts/supabase/ |
| 9 | Stripe Connector | Product/payment source truth | Read/draft only | receipts/stripe/ |
| 10 | Shopify Connector | Store, product, content source truth | Read/draft only | receipts/shopify/ |
| 11 | Slack or Google Chat Bridge | Operator alerts and swarm communication | Draft/read | receipts/comms/ |
| 12 | Twilio Bridge | SMS/voice workflow planning | Draft/read | receipts/twilio/ |
| 13 | Notion Connector | Knowledge docs and tasks | Draft/read | receipts/notion/ |
| 14 | HubSpot Connector | CRM and pipeline state | Read/draft | receipts/hubspot/ |
| 15 | Figma Connector | UI source truth and mockup handoff | Read/draft | receipts/figma/ |
| 16 | Playwright Browser Bridge | Screenshots, route validation, UI smoke | Sandbox | receipts/browser/ |
| 17 | Vercel AI Gateway Bridge | Model routing, budgets, fallback policy | Read/draft | receipts/ai-gateway/ |
| 18 | Codex Branch Agent Bridge | Code planning and branch implementation | Branch-only | receipts/codex/ |
| 19 | Base44 Orchestrator Bridge | System packaging and agent handoff | Draft/branch | receipts/base44/ |
| 20 | Metricool or Social Analytics Bridge | Content performance and posting plans | Read/draft | receipts/social/ |
| 21 | HeyGen Bridge | Video/avatar workflow planning | Draft/read | receipts/video/ |
| 22 | Klaviyo Bridge | Email/SMS campaign intelligence | Read/draft | receipts/klaviyo/ |
| 23 | Semrush Bridge | SEO and competitor intelligence | Read | receipts/seo/ |
| 24 | OpenAI Platform Bridge | API key and model setup evidence | Read/draft | receipts/openai-platform/ |
| 25 | Browser Worker Bridge | Long-running public research tasks | Sandbox | receipts/browser-worker/ |

## Universal Bridge Rule
Each bridge must declare: input, allowed action, blocked action, evidence output, rollback or reversal note, receipt path, and next approval gate.
