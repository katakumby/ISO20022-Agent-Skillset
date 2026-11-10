---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.45 Status", "66.1.45.17 ClosedStatusReason1Choice", "66.1.45.17.2 Reason <Rsn>", "66.1.45.17.2.1 Code <Cd>", "66.1.45.17.2.1.1 Code <Cd>"]
file_pages: [5189]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.45.17.2.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5189 to 5189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5189

```text
Code <Cd> contains one of the following ClosedStatusReason2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5189
Or}   Proprietary <Prtry> [1..1] ± 5189
66.1.45.17.2.1.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the closed account status expressed as a code.
Datatype: "ClosedStatusReason1Code" on page 5284
CodeName Name Definition
ASIN AccountServicerInstruction Account is closed, following an
instruction from the account servicer to
close the account.
CLIN ClientInstruction Account is closed, following an
instruction from the client, or an
authorised party, to close the account.
66.1.45.17.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the closed account status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.45.17.2.2  AdditionalInformation <AddtlInf>
Presence: [0..1]
Definition: Additional information about the reason for the closed account status.
Datatype: "Max350Text" on page 5403
66.1.45.18  CancellationReason31Choice
Definition: Choice of format for the cancellation reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5190
Or}   Proprietary <Prtry> [1..1] ± 5191
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5189 May 2026
```

