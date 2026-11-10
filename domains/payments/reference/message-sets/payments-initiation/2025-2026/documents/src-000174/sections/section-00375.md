---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["4 pain.007.001.13 CustomerPaymentReversalV13", "5.4 Message Building Blocks", "5.4.2.18 DirectDebitTransactionInformation <DrctDbtTxInf>", "5.4.2.18.17 RemittanceInformation <RmtInf>", "5.4.2.18.17.2 Structured <Strd>", "5.4.2.18.17.2.8 SecuritiesData <SctiesData>", "5.4.2.18.17.2.8.1 UniqueTransactionIdentifier <UnqTxIdr>"]
file_pages: [525, 526]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pain.008.001.12"]
---

# 5.4.2.18.17.2.8.1 UniqueTransactionIdentifier <UnqTxIdr>

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 525 to 526.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 525

```text
SecuritiesData <SctiesData> contains the following SecuritiesAttributes1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 525
   Amount <Amt> [0..1] Amount C1, C13 525
5.4.2.18.17.2.8.1  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [1..1]
Definition: Unique transaction identifier will be created at the time a transaction is first executed, shared
with all registered entities and counterparties involved in the transaction, and used to track that
particular transaction during its lifetime. This identifier can also be known as the Unique Swap Identifier
(USI).
Datatype: "UTIIdentifier" on page 605
5.4.2.18.17.2.8.2  Amount <Amt>
Presence: [0..1]
Definition: Amount of money for the trade.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 585
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
5.4.2.18.17.2.9  AdditionalRemittanceInformation <AddtlRmtInf>
Presence: [0..3]
Definition: Additional information, in free text form, to complement the structured remittance information.
Datatype: "Max140Text" on page 608
5.4.2.18.18  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C21 "SupplementaryDataRule"
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 525 March 2026
```

## File page 526

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 553
   Envelope <Envlp> [1..1] (External Schema) 554
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
5.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C21 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 553 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 553
   Envelope <Envlp> [1..1] (External Schema) 554
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 12 January 2026 pain.008.001.12 CustomerDirectDebitInitiationV12
Payments Initiation - Maintenance 2025 - 2026 526 March 2026
```

