---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.4 AbilityToBearLosses <AbltyToBearLosses>"]
file_pages: [351]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.4 AbilityToBearLosses <AbltyToBearLosses>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 351 to 351.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 351

```text
Other <Othr> contains the following elements (see "OtherTargetMarketInvestorKnowledge1" on
page 4814 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InvestorKnowledgeType <InvstrKnwldgTp> [0..1] Text 4814
   Target <Trgt> [0..1]  4814
{Or     Code <Cd> [1..1] CodeSet 4814
Or}     Proprietary <Prtry> [1..1] ± 4815
   AdditionalInformation <AddtlInf> [0..1] ± 4815
15.4.5.22.4  AbilityToBearLosses <AbltyToBearLosses>
Presence: [0..1]
Definition: Investor's ability to bear losses.
AbilityToBearLosses <AbltyToBearLosses> contains the following LossBearing2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoCapitalLoss <NoCptlLoss> [0..1] CodeSet 351
   LimitedCapitalLoss <LtdCptlLoss> [0..1] CodeSet 351
   LimitedCapitalLossLevel <LtdCptlLossLvl> [0..1] Rate 352
   NoCapitalGuarantee <NoCptlGrnt> [0..1] CodeSet 352
   LossBeyondCapital <LossByndCptl> [0..1] CodeSet 352
   Other <Othr> [0..*] ± 352
15.4.5.22.4.1  NoCapitalLoss <NoCptlLoss>
Presence: [0..1]
Definition: Specifies whether the product is compatible with a client who cannot bear loss of capital.
Minor losses especially due to costs are possible. For a negative target (no), the product should not be
sold to investors that cannot bear losses. When used in reference to MiFID, this is in the scope of the
European MiFID Template (EMT) reference 03010.
Datatype: "TargetMarket1Code" on page 5365
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
15.4.5.22.4.2  LimitedCapitalLoss <LtdCptlLoss>
Presence: [0..1]
Definition: Specifies whether the product is compatible with a client who is seeking to preserve capital
or who can bear losses limited to a level specified by a structured security or structure fund product.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 351 May 2026
```

