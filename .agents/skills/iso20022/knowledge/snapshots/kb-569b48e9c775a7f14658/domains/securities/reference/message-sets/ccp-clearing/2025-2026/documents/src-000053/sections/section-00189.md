---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["7 MX secl.006.001.02 DefaultFundContributionReportV02", "7.2 Structure"]
file_pages: [247, 248]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.006.001.02"]
---

# 7.2 Structure

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 247 to 248.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 247

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <DfltFndCntrbtnRpt> [1..1]  
   ReportParameters <RptParams> [1..1]  249
     ReportIdentification <RptId> [1..1] Text 250
     ReportDateAndTime <RptDtAndTm> [1..1] ± 250
     Frequency <Frqcy> [1..1] CodeSet 250
     ReportCurrency <RptCcy> [1..1] CodeSet C10 250
     CalculationDate <ClctnDt> [0..1] DateTime 251
   ClearingMember <ClrMmb> [1..1] ± 251
   ReportDetails <RptDtls> [1..*]  251
     DefaultFundCalculation <DfltFndClctn> [1..*] ± 251
     CollateralDescription <CollDesc> [1..*] ± 252
     NetExcessOrDeficit <NetXcssOrDfcit> [1..1] ± 252
   SupplementaryData <SplmtryData> [0..*] ± C9 253
7.3 Constraints
The tick symbol (') means that the rule is validated on the SWIFT Network, if the message is part of a
solution for which validation is enabled.
C1 ActiveCurrency  '
(Rule)
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00005
– Error Text: Invalid currency code
C2 ActiveOrHistoricCurrency  '
(Rule)
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged. (Algorithm)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.006.001.02
DefaultFundContributionReportV02
March 2026 247
```

## File page 248

```text
Error handling:
– Error severity: Fatal
– Error Code: D00006
– Error Text: Invalid currency code.
C3 AdditonalDetailsGuideline
(Guideline)
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C4 AnyBIC  '
(Rule)
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory,
and consists of eight (8) or eleven (11) contiguous characters. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00008
– Error Text: Invalid BIC.
C5 Country  '
(Rule)
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code). (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00004
– Error Text: Invalid Country Code.
C6 CurrencyAmount  '
(Rule)
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot. (Algorithm)
Error handling:
– Error severity: Fatal
– Error Code: D00007
– Error Text: Invalid currency code or too many decimal digits.
C7 CurrencyAmount  '
(Rule)
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.006.001.02
DefaultFundContributionReportV02
March 2026 248
```

