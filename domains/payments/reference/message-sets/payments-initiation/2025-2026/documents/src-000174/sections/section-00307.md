---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.3 InstructedAmount <InstdAmt>"]
file_pages: [445]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.3 InstructedAmount <InstdAmt>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 445 to 445.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 445

```text
PaymentTypeInformation <PmtTpInf> contains the following elements (see
"PaymentTypeInformation29" on page 569 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionPriority <InstrPrty> [0..1] CodeSet 569
   ServiceLevel <SvcLvl> [0..*]  570
{Or     Code <Cd> [1..1] CodeSet 570
Or}     Proprietary <Prtry> [1..1] Text 570
   LocalInstrument <LclInstrm> [0..1]  570
{Or     Code <Cd> [1..1] CodeSet 570
Or}     Proprietary <Prtry> [1..1] Text 571
   SequenceType <SeqTp> [0..1] CodeSet 571
   CategoryPurpose <CtgyPurp> [0..1]  571
{Or     Code <Cd> [1..1] CodeSet 571
Or}     Proprietary <Prtry> [1..1] Text 571
5.4.2.18.3  InstructedAmount <InstdAmt>
Presence: [1..1]
Definition: Amount of money to be moved between the debtor and creditor, before deduction of
charges, expressed in the currency as ordered by the initiating party.
Usage: This amount has to be transported unchanged through the transaction chain.
Impacted by: C2 "ActiveOrHistoricCurrency", C12 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 585
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
5.4.2.18.4  ChargeBearer <ChrgBr>
Presence: [0..1]
Definition: Specifies which party/parties will bear the charges associated with the processing of the
payment transaction.
Datatype: "ChargeBearerType1Code" on page 588
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 445 March 2026
```

