---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 pacs.009.001.13 FinancialInstitutionCreditTransferV13", "7.4 Message Building Blocks", "7.4.2 CreditTransferTransactionInformation <CdtTrfTxInf>", "7.4.2.41 UnderlyingFinancialInstitutionCreditTransfer <UndrlygFICdtTrf>", "7.4.2.41.6 SettlementTimeIndication <SttlmTmIndctn>", "7.4.2.41.6.1 DebitDateTime <DbtDtTm>"]
file_pages: [990]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.009.001.13"]
---

# 7.4.2.41.6.1 DebitDateTime <DbtDtTm>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 990 to 990.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 990

```text
7.4.2.41.6.1  DebitDateTime <DbtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been debited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been debited at the central bank,
expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
7.4.2.41.6.2  CreditDateTime <CdtDtTm>
Presence: [0..1]
Definition: Date and time at which a payment has been credited at the transaction administrator. In the
case of TARGET, the date and time at which the payment has been credited at the receiving central
bank, expressed in Central European Time (CET).
Datatype: "ISODateTime" on page 1239
7.4.2.41.7  SettlementTimeRequest <SttlmTmReq>
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
7.4.2.41.8  ExpiryDateTime <XpryDtTm>
Presence: [0..1]
Definition: Date and time on which the payment should be expired if it has not settled.
Datatype: "ISODateTime" on page 1239
7.4.2.41.9  PaymentSignature <PmtSgntr>
Presence: [0..1]
Definition: Cryptographic key identifying terms agreed by agents within the payment chain pre-
settlement. This key can also be used post-settlement to confirm the payment has been credited as
intended.
PaymentSignature <PmtSgntr> contains one of the following CryptographicKey1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ILPV4 <ILPV4> [1..1] Text 991
Or}   Signature <Sgntr> [1..1] Text 991
Approved by the Payments SEG on 12 January 2026 pacs.009.001.13
FinancialInstitutionCreditTransferV13
Payments Clearing and Settlement - Maintenance 2025 -
2026
990 March 2026
```

