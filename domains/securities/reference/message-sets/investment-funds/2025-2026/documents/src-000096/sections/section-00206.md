---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.3 Constraints"]
file_pages: [298, 299]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.3 Constraints

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 298 to 299.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 298

```text
15.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 AssessmentOfValueRule
If EMTDataReporting is present, then AssessmentOfValueRequiredUnderCOLLUK must be
present.
C4 CostsAndCharges1Guideline
One repetition of CostsAndCharges may be present for the specification of Ex Ante costs and
charges.
C5 CostsAndCharges2Guideline
One repetition of CostsAndCharges may be present for the specification of Ex Post costs and
charges
C6 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C7 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C8 DealingCutOffTimeFrameRule
If DealingCutOffTimeFrame is present, then DealingCutOffTimeFrame/
OtherTimeFrameDescription or DealingCutOffTimeFrame/ReferToOrderDesk or
DealingCutOffTimeFrame/TradeMinus must be present.
C9 DealingCutOffTimeFrameRule
If DealingCutOffTimeFrame is present, then DealingCutOffTimeFrame/
OtherTimeFrameDescription or DealingCutOffTimeFrame/ReferToOrderDesk or
DealingCutOffTimeFrame/TradeMinus must be present.
C10 DealingCutOffTimeFrameRule
If DealingCutOffTimeFrame is present, then DealingCutOffTimeFrame/
OtherTimeFrameDescription or DealingCutOffTimeFrame/ReferToOrderDesk or
DealingCutOffTimeFrame/TradeMinus must be present.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 298 May 2026
```

## File page 299

```text
C11 DealingCutOffTimeFrameRule
If DealingCutOffTimeFrame is present, then DealingCutOffTimeFrame/
OtherTimeFrameDescription or DealingCutOffTimeFrame/ReferToOrderDesk or
DealingCutOffTimeFrame/TradeMinus must be present.
C12 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C13 DescriptionUsageRule
Description must be used alone as the last resort.
C14 ExAnteOrExPost1Guideline
If ExAnteOrExPost contains ANTE then CostType must be an ex ante cost or charge.
C15 ExAnteOrExPost2Guideline
If ExAnteOrExPost contains POST then CostType must be an ex post cost or charge.
C16 ExAnteReferenceDateGuideline
The ex-ante reference date should not be confused with the reporting date as specified in the
European MiFID Template (EMT) reference 00050.
C17 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C18 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C19 IndividualCostAndCharge1Guideline
If ExAnteReferenceDate is present, then all repetitions of IndividualCostOrCharge must specify
Ex Ante costs
C20 InvestmentPlanRule
If PlanType/Code is not INVP the AdditionalSubscription and AdditionalSubscriptionFunction
must not be present.
C21 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C22 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C23 NonWorkingDayAdjustmentRule
If NonWorkingDayAdjustment is present then TradeMinus must also be present.
C24 NonWorkingDayAdjustmentRule
If NonWorkingDayAdjustment is present then TradePlus must also be present.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 299 May 2026
```

