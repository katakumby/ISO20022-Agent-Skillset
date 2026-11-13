---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 pacs.003.001.12 FIToFICustomerDirectDebitV12", "3.4 Message Building Blocks", "3.4.2 DirectDebitTransactionInformation <DrctDbtTxInf>", "3.4.2.35 RemittanceInformation <RmtInf>", "3.4.2.35.2 Structured <Strd>", "3.4.2.35.2.8 SecuritiesData <SctiesData>", "3.4.2.35.2.8.1 UniqueTransactionIdentifier <UnqTxIdr>"]
file_pages: [244, 245]
content_origin: "source-text-extraction"
mentioned_message_ids: ["pacs.003.001.12"]
---

# 3.4.2.35.2.8.1 UniqueTransactionIdentifier <UnqTxIdr>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 244 to 245.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 244

```text
SecuritiesData <SctiesData> contains the following SecuritiesAttributes1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 244
   Amount <Amt> [0..1] Amount C1, C10 244
3.4.2.35.2.8.1  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [1..1]
Definition: Unique transaction identifier will be created at the time a transaction is first executed, shared
with all registered entities and counterparties involved in the transaction, and used to track that
particular transaction during its lifetime. This identifier can also be known as the Unique Swap Identifier
(USI).
Datatype: "UTIIdentifier" on page 1241
3.4.2.35.2.8.2  Amount <Amt>
Presence: [0..1]
Definition: Amount of money for the trade.
Impacted by: C1 "ActiveCurrency", C10 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 1222
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
3.4.2.35.2.9  AdditionalRemittanceInformation <AddtlRmtInf>
Presence: [0..3]
Definition: Additional information, in free text form, to complement the structured remittance information.
Datatype: "Max140Text" on page 1244
3.4.2.36  SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C32 "SupplementaryDataRule"
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
244 March 2026
```

## File page 245

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1190 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1191
   Envelope <Envlp> [1..1] (External Schema) 1191
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
3.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C32 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 1190 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 1191
   Envelope <Envlp> [1..1] (External Schema) 1191
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 12 January 2026 pacs.003.001.12 FIToFICustomerDirectDebitV12
Payments Clearing and Settlement - Maintenance 2025 -
2026
245 March 2026
```

