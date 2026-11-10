---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.2 CodeSet", "35.2.2.101 RejectionReason71Code"]
file_pages: [2117]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.2.101 RejectionReason71Code

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 2117 to 2117.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2117

```text
CodeName Name Definition
SETR SettlementTransactionRejection Unrecognised or invalid settlement
transaction type.
SDUT LackOfStampDuty Required stamp duty information is
missing.
CADE TransactionCallDelay Unrecognised or invalid transaction call
delay.
FORF ForfeitAmount Unrecognised or invalid forfeit amount.
TERM ClosingDateTimeRejection Unrecognised or invalid closing date/
time.
VASU VariableRateSupportRejection Unrecognised or invalid variable rate
support (repurchase agreement).
REPA TerminationTransactionAmount Unrecognised or invalid termination
transaction amount.
REPO RepurchaseRate Unrecognised or invalid repurchase rate.
REPP PremiumAmount Unrecognised or invalid premium
amount.
RERT RepurchaseRateType Unrecognised or invalid repurchase rate
type.
RSPR SpreadRate Unrecognised or invalid spread rate.
ICAG ReceivingDeliveringParty1 Unrecognised or invalid participant of
delivering or receiving depository.
INPS PlaceOfSafekeeping Unrecognised, invalid or missing place of
safekeeping.
ICUS ReceivingDeliveringParty2 Unrecognised or invalid client of
delivering or receiving party 1.
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
35.2.2.101  RejectionReason71Code
Definition: Specifies the reason why the instruction/cancellation request has a rejected status.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Transaction/instruction received after the
account servicer's specified deadline.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2117 March 2026
```

