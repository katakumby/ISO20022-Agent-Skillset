---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 pacs.008.001.14 FIToFICustomerCreditTransferV14", "6.4 Message Building Blocks", "6.4.2.6 SettlementTimeIndication <SttlmTmIndctn>", "6.4.2.6.1 DebitDateTime <DbtDtTm>"]
file_pages: [742]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.008.001.14"]
---

# 6.4.2.6.1 DebitDateTime <DbtDtTm>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 742 to 742.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 742

```text
6.4.2.6.1  DebitDateTime <DbtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been debited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been debited at the central bank,
expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
6.4.2.6.2  CreditDateTime <CdtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been credited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been credited at the receiving central
bank, expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
6.4.2.7  SettlementTimeRequest <SttlmTmReq>
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
6.4.2.8  AdditionalDateTime <AddtlDtTm>
Presence: [0..1]
Definition: Series of additional date and time data that can be applied to the payment.
Impacted by: C3 "AdditionalDateTimePresenceRule"
AdditionalDateTime <AddtlDtTm> contains the following AdditionalDateTime1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AcceptanceDateTime <AccptncDtTm> [0..1] DateTime 743
   PoolingAdjustmentDate <PoolgAdjstmntDt> [0..1] Date 743
   ExpiryDateTime <XpryDtTm> [0..1] DateTime 743
Approved by the Payments SEG on 12 January 2026 pacs.008.001.14 FIToFICustomerCreditTransferV14
Payments Clearing and Settlement - Maintenance 2025 -
2026
742 March 2026
```

