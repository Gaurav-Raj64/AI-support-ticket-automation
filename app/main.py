from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from app.database import init_db, insert_ticket, ticket_exists, get_review_tickets
from app.llm import classify_ticket

app = FastAPI()

logging.basicConfig(level=logging.INFO)

init_db()

class Ticket(BaseModel):
    ticket_id: str
    message: str

@app.post("/webhook/ticket")
def receive_ticket(ticket: Ticket):

    logging.info(f"Received ticket: {ticket.ticket_id}")

    if ticket_exists(ticket.ticket_id):
        return {"status": "duplicate_ignored"}

    try:
        llm_output = classify_ticket(ticket.message)
    except Exception:
        raise HTTPException(status_code=500, detail="LLM processing failed")

    confidence = llm_output["confidence"]
    needs_review = 1 if confidence < 0.75 else 0

    insert_ticket((
        ticket.ticket_id,
        ticket.message,
        llm_output["category"],
        confidence,
        llm_output["draft_reply"],
        needs_review
    ))

    return {
        "status": "processed",
        "category": llm_output["category"],
        "confidence": confidence,
        "needs_review": bool(needs_review)
    }

@app.get("/tickets/review")
def review_queue():
    tickets = get_review_tickets()
    return {"review_tickets": tickets}
