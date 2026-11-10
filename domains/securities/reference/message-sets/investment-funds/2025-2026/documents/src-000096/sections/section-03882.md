---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.5 ProformaStatusReason1Choice", "66.1.45.5.2 Reason <Rsn>"]
file_pages: [5172]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.5.2 Reason <Rsn>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5172 to 5172.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5172

```text
66.1.45.5.2  Reason <Rsn>
Presence: [1..*]
Definition: Reason for the proforma account status.
Reason <Rsn> contains the following ProformaStatusReason1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  5172
{Or     Code <Cd> [1..1] CodeSet 5172
Or}     Proprietary <Prtry> [1..1] ± 5172
   AdditionalInformation <AddtlInf> [0..1] Text 5173
66.1.45.5.2.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the proforma account status.
Code <Cd> contains one of the following ProformaStatusReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5172
Or}   Proprietary <Prtry> [1..1] ± 5172
66.1.45.5.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the enabled account status expressed as a code.
Datatype: "ProformaStatusReason1Code" on page 5345
CodeName Name Definition
MODI ModificationInProcess Modification to the account data is in
process.
RIGH Rights Account opening is waiting for rights
holder information.
66.1.45.5.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the enabled account status expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5172 May 2026
```

