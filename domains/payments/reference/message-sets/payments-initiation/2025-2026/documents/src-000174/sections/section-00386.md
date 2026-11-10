---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.6 Direct Debit", "6.1.6.1 CreditTransferMandateData1", "6.1.6.1.8 Frequency <Frqcy>"]
file_pages: [537]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.6.1.8 Frequency <Frqcy>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 537 to 537.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 537

```text
6.1.6.1.8  Frequency <Frqcy>
Presence: [0..1]
Definition: Regularity with which credit transfer instructions are to be created and processed.
Frequency <Frqcy> contains one of the following elements (see "Frequency36Choice" on page 544
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Type <Tp> [1..1] CodeSet 545
Or   Period <Prd> [1..1]  545
     Type <Tp> [1..1] CodeSet 546
     CountPerPeriod <CntPerPrd> [1..1] Quantity 546
Or}   PointInTime <PtInTm> [1..1]  546
     Type <Tp> [1..1] CodeSet 546
     PointInTime <PtInTm> [1..1] Text 547
6.1.6.1.9  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the setup of the credit transfer mandate.
Usage:
The reason will allow the user to distinguish between different mandates for the same creditor.
Reason <Rsn> contains one of the following MandateSetupReason1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 537
Or}   Proprietary <Prtry> [1..1] Text 537
6.1.6.1.9.1  Code <Cd>
Presence: [1..1]
Definition: Reason for the mandate setup, as published in an external reason code list.
Datatype: "ExternalMandateSetupReason1Code" on page 595
6.1.6.1.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason for the mandate setup, in a proprietary form.
Datatype: "Max70Text" on page 610
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 537 March 2026
```

