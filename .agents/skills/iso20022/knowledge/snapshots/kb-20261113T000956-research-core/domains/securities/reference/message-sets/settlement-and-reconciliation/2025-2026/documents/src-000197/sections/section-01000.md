---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.8 Date Time", "35.1.8.2 TerminationDate6Choice", "35.1.8.2.1 Date <Dt>"]
file_pages: [1437]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.8.2.1 Date <Dt>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1437 to 1437.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1437

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1437
Or}   Code <Cd> [1..1]  1437
{Or     Code <Cd> [1..1] CodeSet 1437
Or}     Proprietary <Prtry> [1..1] ± 1437
35.1.8.2.1  Date <Dt>
Presence: [1..1]
Definition: Date in ISO format.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 1441 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.8.2.2  Code <Cd>
Presence: [1..1]
Definition: Closing date/time or maturity date/time of the transaction expressed as an ISO 20022 code.
Code <Cd> contains one of the following DateCode18Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1437
Or}   Proprietary <Prtry> [1..1] ± 1437
35.1.8.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Date expressed as an ISO 20022 code.
Datatype: "DateType5Code" on page 2058
CodeName Name Definition
OPEN Open Open-dated, which indicates that the
date has not been established.
35.1.8.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Date expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1437 March 2026
```

