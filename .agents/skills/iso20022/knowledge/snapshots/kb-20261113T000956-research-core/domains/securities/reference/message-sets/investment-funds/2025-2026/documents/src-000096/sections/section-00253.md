---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.6 ClientObjectivesAndNeeds <ClntObjctvsAndNeeds>", "15.4.5.22.6.7 MinimumHoldingPeriod <MinHldgPrd>"]
file_pages: [357]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.6.7 MinimumHoldingPeriod <MinHldgPrd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 357 to 357.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 357

```text
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
15.4.5.22.6.7  MinimumHoldingPeriod <MinHldgPrd>
Presence: [0..1]
Definition: Minimum recommended holding period (RHP).
When used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
05080.
MinimumHoldingPeriod <MinHldgPrd> contains one of the following elements (see
"TimeHorizon2Choice" on page 4468 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NumberOfYears <NbOfYrs> [1..1] Quantity 4468
Or}   TimeFrame <TmFrame> [1..1]  4468
{Or     Code <Cd> [1..1] CodeSet 4469
Or}     Proprietary <Prtry> [1..1] ± 4469
15.4.5.22.6.8  SustainabilityPreferences <SstnbltyPrefs>
Presence: [0..1]
Definition: Specifies whether the product considers investors sustainability preferences. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 05105.
Datatype: "SustainabilityPreferences2Code" on page 5365
CodeName Name Definition
NEUT Neutral Neutral or has no impact.
YSCO InScope Yes, is applicable.
15.4.5.22.6.9  OtherSpecificInvestmentNeed <OthrSpcfcInvstmtNeed>
Presence: [0..1]
Definition: Specifies other specific investment needs. When used in reference to MiFID, this is in the
scope of the European MiFID Template (EMT) reference 05115.
OtherSpecificInvestmentNeed <OthrSpcfcInvstmtNeed> contains one of the following elements
(see "InvestmentNeed2Choice" on page 4743 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4743
Or}   Proprietary <Prtry> [1..1] ± 4743
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 357 May 2026
```

