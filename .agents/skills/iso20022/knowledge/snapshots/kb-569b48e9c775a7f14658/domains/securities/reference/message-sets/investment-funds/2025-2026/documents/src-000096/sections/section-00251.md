---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.6 ClientObjectivesAndNeeds <ClntObjctvsAndNeeds>", "15.4.5.22.6.1 ReturnProfilePreservation <RtrPrflPrsrvtn>"]
file_pages: [355]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.6.1 ReturnProfilePreservation <RtrPrflPrsrvtn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 355 to 355.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 355

```text
ClientObjectivesAndNeeds <ClntObjctvsAndNeeds> contains the following
InvestorRequirements4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReturnProfilePreservation <RtrPrflPrsrvtn> [0..1] CodeSet 355
   ReturnProfileGrowth <RtrPrflGrwth> [0..1] CodeSet 355
   ReturnProfileIncome <RtrPrflIncm> [0..1] CodeSet 356
   ReturnProfileHedging <RtrPrflHdgg> [0..1] CodeSet 356
   OptionOrLeveragedReturnProfile
<OptnOrLvrgdRtrPrfl>
[0..1] CodeSet 356
   ReturnProfilePensionSchemeGermany
<RtrPrflPnsnSchmeDE>
[0..1] CodeSet 356
   MinimumHoldingPeriod <MinHldgPrd> [0..1] ± 357
   SustainabilityPreferences <SstnbltyPrefs> [0..1] CodeSet 357
   OtherSpecificInvestmentNeed
<OthrSpcfcInvstmtNeed>
[0..1] ± 357
   Other <Othr> [0..*] ± 358
15.4.5.22.6.1  ReturnProfilePreservation <RtrPrflPrsrvtn>
Presence: [0..1]
Definition: Specifies whether the product is compatible with a client who is looking for the preservation
of capital. When used in reference to MiFID, this is in the scope of the European MiFID Template (EMT)
reference 05010.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
15.4.5.22.6.2  ReturnProfileGrowth <RtrPrflGrwth>
Presence: [0..1]
Definition: Specifies whether the product is compatible with a client looking for capitalisation growth.
When used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
05020.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 355 May 2026
```

