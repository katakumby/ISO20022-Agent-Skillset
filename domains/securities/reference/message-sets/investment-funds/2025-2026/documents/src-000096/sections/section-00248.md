---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.4 AbilityToBearLosses <AbltyToBearLosses>", "15.4.5.22.4.3 LimitedCapitalLossLevel <LtdCptlLossLvl>"]
file_pages: [352]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.4.3 LimitedCapitalLossLevel <LtdCptlLossLvl>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 352 to 352.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 352

```text
When used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
03020.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
15.4.5.22.4.3  LimitedCapitalLossLevel <LtdCptlLossLvl>
Presence: [0..1]
Definition: Specifies the percentage of loss that can be carried by the investor. This is only specified
when a clear partial capital guarantee is provided on the primary market. When used in reference to
MiFID, this is in the scope of the European MiFID Template (EMT) reference 03030.
Datatype: "PercentageRate" on page 5401
15.4.5.22.4.4  NoCapitalGuarantee <NoCptlGrnt>
Presence: [0..1]
Definition: Specifies the product is compatible with a client who does not need capital guarantee nor
protection. One hundred percent of the capital is at risk. When used in reference to MiFID, this is in the
scope of the European MiFID Template (EMT) reference 03040.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
15.4.5.22.4.5  LossBeyondCapital <LossByndCptl>
Presence: [0..1]
Definition: Specifies the product is compatible with a client who can bear loss beyond the capital. When
used in reference to MiFID, this is in the scope of the European MiFID Template (EMT) reference
03050.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
15.4.5.22.4.6  Other <Othr>
Presence: [0..*]
Definition: Specifies another type of loss bearing.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 352 May 2026
```

