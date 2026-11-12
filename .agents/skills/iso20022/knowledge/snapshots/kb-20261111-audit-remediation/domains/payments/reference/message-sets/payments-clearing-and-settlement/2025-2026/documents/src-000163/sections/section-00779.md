---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["8 pacs.010.001.06 FinancialInstitutionDirectDebitV06", "8.4 Message Building Blocks", "8.4.2 CreditInstruction <CdtInstr>", "8.4.2.21 DirectDebitTransactionInformation <DrctDbtTxInf>", "8.4.2.21.5 SettlementPriority <SttlmPrty>"]
file_pages: [1042]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.010.001.06"]
---

# 8.4.2.21.5 SettlementPriority <SttlmPrty>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1042 to 1042.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1042

```text
8.4.2.21.5  SettlementPriority <SttlmPrty>
Presence: [0..1]
Definition: Indicator of the urgency or order of importance that the instructing party would like the
instructed party to apply to the processing of the settlement instruction.
Datatype: "Priority3Code" on page 1236
CodeName Name Definition
URGT Urgent Priority level is urgent (highest priority
possible).
HIGH High Priority level is high.
NORM Normal Priority level is normal.
8.4.2.21.6  SettlementTimeIndication <SttlmTmIndctn>
Presence: [0..1]
Definition: Provides information on the occurred settlement time(s) of the payment transaction.
SettlementTimeIndication <SttlmTmIndctn> contains the following SettlementDateTimeIndication1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitDateTime <DbtDtTm> [0..1] DateTime 1042
   CreditDateTime <CdtDtTm> [0..1] DateTime 1042
8.4.2.21.6.1  DebitDateTime <DbtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been debited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been debited at the central bank,
expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
8.4.2.21.6.2  CreditDateTime <CdtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been credited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been credited at the receiving central
bank, expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
8.4.2.21.7  SettlementTimeRequest <SttlmTmReq>
Presence: [0..1]
Definition: Provides information on the requested settlement time(s) of the payment instruction.
Approved by the Payments SEG on 12 January 2026 pacs.010.001.06 FinancialInstitutionDirectDebitV06
Payments Clearing and Settlement - Maintenance 2025 -
2026
1042 March 2026
```

