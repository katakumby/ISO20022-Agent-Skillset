---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 pain.001.001.13 CustomerCreditTransferInitiationV13", "2.4 Message Building Blocks", "2.4.2 PaymentInformation <PmtInf>", "2.4.2.19 CreditTransferTransactionInformation <CdtTrfTxInf>", "2.4.2.19.3 Amount <Amt>"]
file_pages: [52]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.001.001.13"]
---

# 2.4.2.19.3 Amount <Amt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 52 to 52.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 52

```text
PaymentTypeInformation <PmtTpInf> contains the following elements (see
"PaymentTypeInformation26" on page 567 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 567
   ServiceLevel <SvcLvl> [0..*]  567
{Or     Code <Cd> [1..1] CodeSet 568
Or}     Proprietary <Prtry> [1..1] Text 568
   LocalInstrument <LclInstrm> [0..1]  568
{Or     Code <Cd> [1..1] CodeSet 568
Or}     Proprietary <Prtry> [1..1] Text 568
   CategoryPurpose <CtgyPurp> [0..1]  568
{Or     Code <Cd> [1..1] CodeSet 569
Or}     Proprietary <Prtry> [1..1] Text 569
2.4.2.19.3  Amount <Amt>
Presence: [1..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Amount <Amt> contains one of the following elements (see "AmountType4Choice" on page 532 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InstructedAmount <InstdAmt> [1..1] Amount C2, C19 532
Or}   EquivalentAmount <EqvtAmt> [1..1]  533
     Amount <Amt> [1..1] Amount C2, C19 533
     CurrencyOfTransfer <CcyOfTrf> [1..1] CodeSet C2 533
2.4.2.19.4  ExchangeRateInformation <XchgRateInf>
Presence: [0..1]
Definition: Provides details on the currency exchange rate and contract.
Approved by the Payments SEG on 12 January 2026 pain.001.001.13
CustomerCreditTransferInitiationV13
Payments Initiation - Maintenance 2025 - 2026 52 March 2026
```

