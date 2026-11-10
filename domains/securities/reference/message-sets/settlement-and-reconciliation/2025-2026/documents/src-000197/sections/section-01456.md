---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.41 RejectionReason45Choice", "35.1.29.41.2 Proprietary <Prtry>"]
file_pages: [1944]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.41.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1944 to 1944.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1944

```text
CodeName Name Definition
DISC DisagreeWithCallAmount Party does not agree with the call
amount.
DISE DisagreeWithExposureAmount Party does not agree with the exposure
amount.
DORD RegistrationRequestDataAndOrderRejection Disagreement between the data on the
registration request and the order.
FEEE FeeCommissionRejection Unrecognised or invalid fee or
commission.
SETR SettlementTransactionRejection Unrecognised or invalid settlement
transaction type.
TERM ClosingDateTimeRejection Unrecognised or invalid closing date/
time.
VASU VariableRateSupportRejection Unrecognised or invalid variable rate
support (repurchase agreement).
INPS PlaceOfSafekeeping Unrecognised, invalid or missing place of
safekeeping.
SDUT LackOfStampDuty Required stamp duty information is
missing.
FORF ForfeitAmount Unrecognised or invalid forfeit amount.
ICUS ReceivingDeliveringParty2 Unrecognised or invalid client of
delivering or receiving party 1.
ICAG ReceivingDeliveringParty1 Unrecognised or invalid participant of
delivering or receiving depository.
DEPT ReceivingDeliveringDepository Unrecognised or invalid depository.
OTHR Other Other. See Narrative.
IEXE ReceivingDeliveringParty3 Unrecognised or invalid client of
delivering or receiving party 2.
INVE InvalidInvestorParty Unrecognised or invalid investor party.
May be used by an executing party to
reject an instruction for an investor (or
portfolio) for which it is not authorised to
act.
PLIS PlaceOfListing Unrecognised or invalid place of listing.
Used when the security identified is not
listed on the market supplied.
35.1.29.41.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1944 March 2026
```

