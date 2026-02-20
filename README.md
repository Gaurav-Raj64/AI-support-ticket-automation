# AI Support Ticket Triage Automation

An AI-powered webhook-triggered automation system that classifies support tickets, generates draft responses, and routes low-confidence outputs for human review.

## Features

- Webhook-based ticket ingestion
- LLM-powered classification
- Confidence-based routing
- Human-in-the-loop review workflow
- Idempotent processing
- Retry handling
- Structured JSON responses
- Logging for monitoring

## Setup

1. Clone repository
2. Create `.env` from `.env.example`
3. Install dependencies:

pip install -r requirements.txt

4. Run server:

uvicorn app.main:app --reload

## Example Request

POST /webhook/ticket

{
  "ticket_id": "123",
  "message": "I was charged twice for my order"
}

Built to simulate production-ready AI workflow automation for operational teams.
