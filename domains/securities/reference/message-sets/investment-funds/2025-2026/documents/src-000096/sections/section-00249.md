---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.5 RiskTolerance <RskTlrnce>"]
file_pages: [353]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.5 RiskTolerance <RskTlrnce>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 353 to 353.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 353

```text
Other <Othr> contains the following elements (see "OtherTargetMarketLossBearing1" on page 4807 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AbilityToBearLossesType <AbltyToBearLossesTp> [0..1] Text 4807
   Target <Trgt> [0..1]  4807
{Or     Code <Cd> [1..1] CodeSet 4808
Or}     Proprietary <Prtry> [1..1] ± 4808
   AdditionalInformation <AddtlInf> [0..1] ± 4808
15.4.5.22.5  RiskTolerance <RskTlrnce>
Presence: [0..1]
Definition: Investor's tolerance to risk.
RiskTolerance <RskTlrnce> contains the following RiskTolerance1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RiskTolerancePRIIPSMethodology
<RskTlrncePRIIPSMthdlgy>
[0..1] Quantity 353
   RiskToleranceUCITSMethodology
<RskTlrnceUCITSMthdlgy>
[0..1] Quantity 353
   RiskToleranceInternal <RskTlrnceIntl> [0..1] CodeSet 353
   RiskToleranceForNonPRIIPSAndNonUCITSSpain
<RskTlrnceForNonPRIIPSAndNonUCITSES>
[0..1] Quantity 354
   NotForInvestorsWithTheLowestRiskToleranceGerma
ny <NotForInvstrsWthTheLwstRskTlrnceDE>
[0..1] CodeSet 354
   Other <Othr> [0..*] ± 354
15.4.5.22.5.1  RiskTolerancePRIIPSMethodology <RskTlrncePRIIPSMthdlgy>
Presence: [0..1]
Definition: Specifies the Summary Risk Indicator (SRI). When used in reference to MiFID, this is in the
scope of the European MiFID Template (EMT) reference 04010.
Datatype: "Max1Number" on page 5400
15.4.5.22.5.2  RiskToleranceUCITSMethodology <RskTlrnceUCITSMthdlgy>
Presence: [0..1]
Definition: Specifies the Synthetic Risk and Reward Indicator (SRRI). When used in reference to MiFID,
this is in the scope of the European MiFID Template (EMT) reference 04020.
Datatype: "Max1Number" on page 5400
15.4.5.22.5.3  RiskToleranceInternal <RskTlrnceIntl>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 353 May 2026
```

