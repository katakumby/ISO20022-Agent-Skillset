---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.3 Constraints"]
file_pages: [18, 19]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.3 Constraints

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 18 to 19.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 18

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Or                 Proprietary <Prtry> [1..1]  35
                   Identification <Id> [1..1] Text 35
                   Issuer <Issr> [1..1] Text 35
                   SchemeName <SchmeNm> [0..1] Text 35
                   Balance <Bal> [1..1] Quantity 35
Or}                 QuantityAndAvailability <QtyAndAvlbty> [1..1]  36
                   Quantity <Qty> [1..1] ± 36
                   AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 36
             ValuationPrice <ValtnPric> [1..1]  36
               AmountPriceType <AmtPricTp> [1..1] ± 37
               PriceValue <PricVal> [1..1] ± 37
               FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 37
               PriceFixingDate <PricFxgDt> [1..1] Date 38
             CollateralValue <CollVal> [1..1] Amount C1, C6 38
Or}     OperationalError <OprlErr> [1..*]  38
       Error <Err> [1..1]  38
{Or         Code <Cd> [1..1] CodeSet 39
Or}         Proprietary <Prtry> [1..1] Text 39
       Description <Desc> [0..1] Text 39
   SupplementaryData <SplmtryData> [0..*] ± C15 39
3.3 Constraints
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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
18 March 2024
```

## File page 19

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
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
19 March 2024
```

