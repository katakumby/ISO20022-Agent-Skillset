---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.5 RiskTolerance <RskTlrnce>", "15.4.5.22.5.4 RiskToleranceForNonPRIIPSAndNonUCITSSpain <RskTlrnceForNonPRIIPSAndNonUCITSES>"]
file_pages: [354]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.5.4 RiskToleranceForNonPRIIPSAndNonUCITSSpain <RskTlrnceForNonPRIIPSAndNonUCITSES>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 354 to 354.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 354

```text
Definition: Specifies the risk tolerance for non-PRIIPs and non-UCITS instructions. When used in
reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference 04030.
Datatype: "RiskLevel1Code" on page 5358
CodeName Name Definition
HIGH High High.
LOWW Low Low.
MEDM Medium Medium.
15.4.5.22.5.4  RiskToleranceForNonPRIIPSAndNonUCITSSpain
<RskTlrnceForNonPRIIPSAndNonUCITSES>
Presence: [0..1]
Definition: Specifies the Summary Risk Indicator (SRI) for a Spanish product. When used in reference
to MiFID, this is in the scope of the European MiFID Template (EMT) reference 04040.
Datatype: "Max1Number" on page 5400
15.4.5.22.5.5  NotForInvestorsWithTheLowestRiskToleranceGermany
<NotForInvstrsWthTheLwstRskTlrnceDE>
Presence: [0..1]
Definition: Specifies the risk tolerance for a German product. When used in reference to MiFID, this is in
the scope of the European MiFID Template (EMT) reference 04050.
Datatype: "TargetMarket2Code" on page 5365
CodeName Name Definition
NEUT Neutral Neutral or has no impact.
YSCO InScope Yes, is applicable.
15.4.5.22.5.6  Other <Othr>
Presence: [0..*]
Definition: Specifies another type of risk tolerance.
Other <Othr> contains the following elements (see "OtherTargetMarketRiskTolerance1" on page 4810
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RiskToleranceType <RskTlrnceTp> [0..1] Text 4811
   Target <Trgt> [0..1]  4811
{Or     Code <Cd> [1..1] CodeSet 4811
Or}     Proprietary <Prtry> [1..1] ± 4811
   AdditionalInformation <AddtlInf> [0..1] ± 4812
15.4.5.22.6  ClientObjectivesAndNeeds <ClntObjctvsAndNeeds>
Presence: [0..1]
Definition: Investor's investment requirements.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 354 May 2026
```

