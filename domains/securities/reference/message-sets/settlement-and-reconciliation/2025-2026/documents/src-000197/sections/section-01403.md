---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.4 RejectionStatus38Choice", "35.1.29.4.2 Reason <Rsn>", "35.1.29.4.2.1 Code <Cd>", "35.1.29.4.2.1.2 Proprietary <Prtry>"]
file_pages: [1876]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.4.2.1.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1876 to 1876.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1876

```text
CodeName Name Definition
TXST TaxStatusRejection Unrecognised or invalid tax status of the
securities instructed.
SETS SettlementSystemMethodRejection Unrecognised or invalid settlement
system/method instructed.
IIND CommonReferenceRejection Unrecognised, invalid or missing
common reference.
CAEV CorporateActionRejection Corporate action pending on the
financial instrument instructed.
CASY ImpossibleCashSettlementSystem Impossible standing arrangements
override instruction for the cash
settlement system.
DDAT SettlementDateRejection Unrecognised or invalid settlement date.
SETR SettlementTransactionRejection Unrecognised or invalid settlement
transaction type.
SDUT LackOfStampDuty Required stamp duty information is
missing.
INPS PlaceOfSafekeeping Unrecognised, invalid or missing place of
safekeeping.
OTHR Other Other. See Narrative.
ICUS ReceivingDeliveringParty2 Unrecognised or invalid client of
delivering or receiving party 1.
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
35.1.29.4.2.1.2  Proprietary <Prtry>
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1876 March 2026
```

