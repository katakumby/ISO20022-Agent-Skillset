---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.33 RejectionStatus39Choice", "35.1.29.33.2 Reason <Rsn>", "35.1.29.33.2.1 Code <Cd>", "35.1.29.33.2.1.2 Proprietary <Prtry>"]
file_pages: [1933]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.33.2.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1933 to 1933.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1933

```text
CodeName Name Definition
ICAG ReceivingDeliveringParty1 Unrecognised or invalid participant of
delivering or receiving depository.
DEPT ReceivingDeliveringDepository Unrecognised or invalid depository.
IEXE ReceivingDeliveringParty3 Unrecognised or invalid client of
delivering or receiving party 2.
INVB InvalidBalance Instruction aims at using an invalid
balance.
INVL InvalidLink Invalid or unrecognized link.
INVN InvalidLotNumber Invalid or unrecognized lot number.
VALR InvalidRule Account servicer validation rule rejection.
INVE InvalidInvestorParty Unrecognised or invalid investor party.
May be used by an executing party to
reject an instruction for an investor (or
portfolio) for which it is not authorised to
act.
PLIS PlaceOfListing Unrecognised or invalid place of listing.
Used when the security identified is not
listed on the market supplied.
35.1.29.33.2.1.2  Proprietary <Prtry>
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
35.1.29.33.2.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional reason information that cannot be provided in a structured field.
Datatype: "Max210Text" on page 2191
35.1.29.34  RejectionAndRepairReason38Choice
Definition: Choice of format for the rejection or repair reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1934
Or}   Proprietary <Prtry> [1..1] ± 1934
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1933 March 2026
```

