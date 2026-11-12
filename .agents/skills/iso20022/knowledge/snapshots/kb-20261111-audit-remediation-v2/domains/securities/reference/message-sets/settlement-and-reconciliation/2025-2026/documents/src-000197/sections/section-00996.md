---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.20 ClosingBalance5", "35.1.4.20.2 ClosingBalance <ClsgBal>"]
file_pages: [1433]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.20.2 ClosingBalance <ClsgBal>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1433 to 1433.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1433

```text
Datatype: "ShortLong1Code" on page 2171
CodeName Name Definition
SHOR Short Position is short, that is, the balance is
negative.
LONG Long Position is long, that is, the balance is
positive.
35.1.4.20.2  ClosingBalance <ClsgBal>
Presence: [1..1]
Definition: Closing balance for the statement period (final closing balance) or of this page (intermediary
closing balance).
ClosingBalance <ClsgBal> contains one of the following elements (see "ClosingBalance6Choice" on
page 1414 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Final <Fnl> [1..1] ± 1414
Or}   Intermediary <Intrmy> [1..1] ± 1414
35.1.5 Cash
35.1.5.1  CashSettlementSystem6Choice
Definition: Choice of format for the cash settlement system.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1433
Or}   Proprietary <Prtry> [1..1] ± 1433
35.1.5.1.1  Code <Cd>
Presence: [1..1]
Definition: Cash settlement system expressed as an ISO 20022 code.
Datatype: "CashSettlementSystem3Code" on page 2049
CodeName Name Definition
DCSS DigitalCashSettlementSystem Digital cash settlement system used for
the payment.
GROS GrossSettlementSystem Settle money through gross settlement
system.
NETS NetSettlementSystem Settle money through net settlement
system.
35.1.5.1.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1433 March 2026
```

