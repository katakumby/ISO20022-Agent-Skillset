---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.14 SettlementTimeIndication <SttlmTmIndctn>"]
file_pages: [313]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.14 SettlementTimeIndication <SttlmTmIndctn>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 313 to 313.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 313

```text
4.4.3.14  SettlementTimeIndication <SttlmTmIndctn>
Presence: [0..1]
Definition: Provides information on the occurred settlement time of the payment transaction.
SettlementTimeIndication <SttlmTmIndctn> contains the following SettlementDateTimeIndication1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebitDateTime <DbtDtTm> [0..1] DateTime 313
   CreditDateTime <CdtDtTm> [0..1] DateTime 313
4.4.3.14.1  DebitDateTime <DbtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been debited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been debited at the central bank,
expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
4.4.3.14.2  CreditDateTime <CdtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been credited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been credited at the receiving central
bank, expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
4.4.3.15  SettlementTimeRequest <SttlmTmReq>
Presence: [0..1]
Definition: Provides information on the requested settlement time of the payment instruction.
SettlementTimeRequest <SttlmTmReq> contains the following elements (see
"SettlementTimeRequest2" on page 1202 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CLSTime <CLSTm> [0..1] Time 1202
   TillTime <TillTm> [0..1] Time 1203
   FromTime <FrTm> [0..1] Time 1203
   RejectTime <RjctTm> [0..1] Time 1203
4.4.3.16  ReturnedInstructedAmount <RtrdInstdAmt>
Presence: [0..1]
Definition: Amount of money to be moved between the debtor and the creditor, before deduction of
charges, in the returned transaction.
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
313 March 2026
```

