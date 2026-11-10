---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.3 Constraints"]
file_pages: [592, 593]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.3 Constraints

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 592 to 593.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 592

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or                 Proprietary <Prtry> [1..1]  609
                   Identification <Id> [1..1] Text 609
                   Issuer <Issr> [1..1] Text 609
                   SchemeName <SchmeNm> [0..1] Text 609
                   Balance <Bal> [1..1] Quantity 609
Or}                 QuantityAndAvailability <QtyAndAvlbty> [1..1]  610
                   Quantity <Qty> [1..1] ± 610
                   AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 610
             ValuationPrice <ValtnPric> [1..1]  610
               AmountPriceType <AmtPricTp> [1..1] ± 611
               PriceValue <PricVal> [1..1] ± 611
               FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 611
               PriceFixingDate <PricFxgDt> [1..1] Date 612
             CollateralValue <CollVal> [1..1] Amount C1, C6 612
Or}     OperationalError <OprlErr> [1..*]  612
       Error <Err> [1..1]  612
{Or         Code <Cd> [1..1] CodeSet 613
Or}         Proprietary <Prtry> [1..1] Text 613
       Description <Desc> [0..1] Text 613
   SupplementaryData <SplmtryData> [0..*] ± C15 613
25.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 592 August 2026
```

## File page 593

```text
C3 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C4 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C5 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C6 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C7 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C8 DescriptionUsageRule
Description must be used alone as the last resort.
C9 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C10 IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
C11 IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
C12 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C13 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C14 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C15 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 593 August 2026
```

