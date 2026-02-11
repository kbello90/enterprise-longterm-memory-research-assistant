# enterprise-longterm-memory-research-assistant
Enterprise long-term memory financial research assistant (agentic RAG + persistent preferences/episodic memory) deployable to Azure.


🚀 **Overview**

The Enterprise Long-Term Memory Research Assistant is a financial-domain AI agent designed for enterprise use cases where:

User preferences must persist across sessions

Conversation context must be remembered

Responses must follow structured executive brief formats

The system must be deployable to Azure

This MVP demonstrates:

✅ Persistent preference memory
✅ Episodic conversation tracking
✅ Agent orchestration workflow
✅ Production-ready FastAPI backend
✅ Modular, Azure-deployable architecture

🎯 **Problem**

Enterprise financial research workflows require:

Reusable output formats (executive brief, tables, reports)

Consistent tone and language (e.g., bilingual EN/ES)

Context continuity across sessions

Auditability of previous interactions

Traditional chatbots do not persist preferences or long-term context.

💡 **Solution**

This project implements an agentic memory architecture with:

Preference Memory (long-term)

Episodic Memory (recent interactions)

Structured agent orchestration

Extensible RAG-ready backend

Azure-compatible deployment structure

🧠**Architecture**
High-Level Flow

User sends request to /chat

Agent loads persistent profile

Extracts preference updates

Updates memory

Generates structured response

Stores episode

Returns response + memory metadata

<img width="1197" height="728" alt="diagram" src="https://github.com/user-attachments/assets/73fbedf9-d0af-40f6-aca1-7003b7bfbf19" />
