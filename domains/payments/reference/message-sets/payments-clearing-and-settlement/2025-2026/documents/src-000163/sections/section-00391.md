---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pacs.004.001.15 PaymentReturnV15", "4.4 Message Building Blocks", "4.4.1 GroupHeader <GrpHdr>", "4.4.3.27 OriginalTransactionReference <OrgnlTxRef>", "4.4.3.27.24 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "4.4.3.27.24.6 SettlementTimeIndication <SttlmTmIndctn>", "4.4.3.27.24.6.2 CreditDateTime <CdtDtTm>"]
file_pages: [537]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.004.001.15"]
---

# 4.4.3.27.24.6.2 CreditDateTime <CdtDtTm>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 537 to 537.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 537

```text
Definition: Date and time at which a payment has been debited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been debited at the central bank,
expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
4.4.3.27.24.6.2  CreditDateTime <CdtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been credited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been credited at the receiving central
bank, expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
4.4.3.27.24.7  SettlementTimeRequest <SttlmTmReq>
Presence: [0..1]
Definition: Provides information on the requested settlement time(s) of the payment instruction.
SettlementTimeRequest <SttlmTmReq> contains the following elements (see
"SettlementTimeRequest2" on page 1202 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CLSTime <CLSTm> [0..1] Time 1202
   TillTime <TillTm> [0..1] Time 1203
   FromTime <FrTm> [0..1] Time 1203
   RejectTime <RjctTm> [0..1] Time 1203
4.4.3.27.24.8  ExpiryDateTime <XpryDtTm>
Presence: [0..1]
Definition: Date and time on which the payment should be expired if it has not settled.
Datatype: "ISODateTime" on page 1239
4.4.3.27.24.9  PaymentSignature <PmtSgntr>
Presence: [0..1]
Definition: Cryptographic key identifying terms agreed by agents within the payment chain pre-
settlement. This key can also be used post-settlement to confirm the payment has been credited as
intended.
PaymentSignature <PmtSgntr> contains one of the following CryptographicKey1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ILPV4 <ILPV4> [1..1] Text 537
Or}   Signature <Sgntr> [1..1] Text 538
4.4.3.27.24.9.1  ILPV4 <ILPV4>
Presence: [1..1]
Approved by the Payments SEG on 12 January 2026 pacs.004.001.15 PaymentReturnV15
Payments Clearing and Settlement - Maintenance 2025 -
2026
537 March 2026
```

