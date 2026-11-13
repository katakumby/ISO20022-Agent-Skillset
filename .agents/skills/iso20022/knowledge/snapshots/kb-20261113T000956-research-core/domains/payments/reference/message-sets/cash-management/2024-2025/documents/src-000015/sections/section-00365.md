---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["15 camt.016.001.04 GetCurrencyExchangeRateV04", "15.4 Message Building Blocks", "15.4.2 CurrencyQueryDefinition <CcyQryDef>", "15.4.2.2 CurrencyCriteria <CcyCrit>", "15.4.2.2.2 NewCriteria <NewCrit>", "15.4.2.2.2.2 SearchCriteria <SchCrit>", "15.4.2.2.2.2.1 SourceCurrency <SrcCcy>"]
file_pages: [509, 510]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.016.001.04"]
---

# 15.4.2.2.2.2.1 SourceCurrency <SrcCcy>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 509 to 510.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 509

```text
SearchCriteria <SchCrit> contains the following CurrencyExchangeSearchCriteria1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SourceCurrency <SrcCcy> [1..1] CodeSet C1 509
   TargetCurrency <TrgtCcy> [1..1] CodeSet C1 509
15.4.2.2.2.2.1  SourceCurrency <SrcCcy>
Presence: [1..1]
Definition: Currency of the amount to be converted in a currency conversion.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
15.4.2.2.2.2.2  TargetCurrency <TrgtCcy>
Presence: [1..1]
Definition: Currency into which an amount is to be converted in a currency conversion.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 849
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
15.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that cannot be captured in the structured elements and/or any other
specific block.
Impacted by: C2 "SupplementaryDataRule"
Approved by the Payments SEG on 04 February 2025 camt.016.001.04 GetCurrencyExchangeRateV04
Cash Management - Maintenance 2024 - 2025 509 February 2025
```

## File page 510

```text
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 815 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 816
   Envelope <Envlp> [1..1] (External Schema) 816
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Payments SEG on 04 February 2025 camt.016.001.04 GetCurrencyExchangeRateV04
Cash Management - Maintenance 2024 - 2025 510 February 2025
```

