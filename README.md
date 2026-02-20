# AI Support Ticket Triage Automation

AI-powered webhook-triggered automation system that classifies support tickets, generates draft responses, and routes low-confidence outputs for human review.

Built to simulate production-ready AI workflows for operational and support teams.

---

## 🚀 Problem Statement

Support teams manually triage incoming tickets, classify categories, and draft responses — leading to delays and operational inefficiencies.

This project automates:
- Ticket classification
- Draft response generation
- Confidence-based routing
- Human review safeguards

---

## 🏗 System Architecture

Webhook → FastAPI → SQLite  
         → OpenAI API  
         → Classification + Draft  
         → Confidence Threshold  
         → Review Queue (if needed)

Key reliability safeguards:
- Idempotent processing (duplicate ticket prevention)
- Retry handling for LLM failures
- Structured JSON outputs
- Logging for monitoring

---

## ⚙️ Features

- Webhook-based ticket ingestion
- LLM-powered ticket classification (Billing, Technical, Shipping, Other)
- Automated draft response generation
- Confidence-based routing logic
- Human-in-the-loop review endpoint
- SQLite persistence layer
- Retry logic for transient API failures
- Idempotent request handling
- Structured REST API responses

---

## 🛠 Tech Stack

- Python
- FastAPI
- OpenAI API
- SQLite
- REST APIs
- JSON Handling
- Structured Prompting

---

## 📬 API Endpoints

### 1️⃣ Receive Ticket

POST `/webhook/ticket`

Request Body:

```json
{
  "ticket_id": "123",
  "message": "I was charged twice for my order"
}
-Response
{
  "status": "processed",
  "category": "Billing",
  "confidence": 0.87,
  "needs_review": false
}
