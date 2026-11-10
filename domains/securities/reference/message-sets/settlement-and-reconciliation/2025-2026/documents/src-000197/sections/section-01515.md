---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.86 RepairStatus12Choice", "35.1.29.86.2 Reason <Rsn>", "35.1.29.86.2.1 Code <Cd>", "35.1.29.86.2.1.2 Proprietary <Prtry>"]
file_pages: [2013]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.86.2.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2013 to 2013.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2013

```text
CodeName Name Definition
INPS PlaceOfSafekeeping Unrecognised, invalid or missing Place
of Safekeeping.
SDUT StampDuty Required stamp duty information is
missing.
OTHR Other Other. See Narrative.
IEXE ReceivingDeliveringParty3 Client of delivering or receiving party 2
mismatch.
ICAG ReceivingDeliveringParty1 Participant of delivering or receiving
depository mismatch.
DEPT ReceivingDeliveringDepository Depository mismatch.
ICUS ReceivingDeliveringParty2 Client of delivering or receiving party 1
mismatch.
35.1.29.86.2.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.29.86.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.87  PendingProcessingReason22Choice
Definition: Choice of format for the pending processing reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2013
Or}   Proprietary <Prtry> [1..1] ± 2014
35.1.29.87.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason why the instruction has a pending processing status.
Datatype: "PendingProcessingReason8Code" on page 2094
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2013 March 2026
```

