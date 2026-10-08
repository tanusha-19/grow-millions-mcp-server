# Single Prompt End-to-End Test

## Test Prompt
> Create a 30-day growth plan for my business, generate the first week's content, prepare social posts, create a Meta Ads campaign draft, check upcoming compliance requirements, and find useful automations from the marketplace.

## Workflow Execution Sequence
1. **MARK-AI / Strategist:** Fetches business profile and generates the 30-day strategy.
2. **Content Generator:** Uses strategy context to generate week 1 content drafts.
3. **Auto Post:** Queues post drafts (requires explicit user action to publish).
4. **Meta Ads:** Creates a campaign draft under `PENDING_APPROVAL` status.
5. **Compliance:** Retrieves upcoming tax/legal obligations.
6. **Marketplace:** Searches Concept Place for relevant automation tools.

## Status
SIMULATED ORCHESTRATION / E2E TEST READY