---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>"]
file_pages: [345, 346]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22 TargetMarket <TrgtMkt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 345 to 346.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 345

```text
15.4.5.22  TargetMarket <TrgtMkt>
Presence: [0..1]
Definition: Target market criteria.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 345 May 2026
```

## File page 346

```text
TargetMarket <TrgtMkt> contains the following TargetMarket4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReferenceDate <RefDt> [0..1] Date 347
   InvestorType <InvstrTp> [0..1]  347
     InvestorTypeRetail <InvstrTpRtl> [0..1] CodeSet 347
     InvestorTypeProfessional <InvstrTpPrfssnl> [0..1] ± 348
     InvestorTypeEligibleCounterparty
<InvstrTpElgblCtrPty>
[0..1] CodeSet 348
     Other <Othr> [0..*] ± 348
   KnowledgeAndOrExperience <KnwldgAndOrExprnc> [0..1]  349
     BasicInvestor <BsicInvstr> [0..1] CodeSet 349
     InformedInvestor <InfrmdInvstr> [0..1] CodeSet 349
     AdvancedInvestor <AdvncdInvstr> [0..1] CodeSet 350
     ExpertInvestorGermany <ExprtInvstrDE> [0..1] CodeSet 350
     Other <Othr> [0..*] ± 350
   AbilityToBearLosses <AbltyToBearLosses> [0..1]  351
     NoCapitalLoss <NoCptlLoss> [0..1] CodeSet 351
     LimitedCapitalLoss <LtdCptlLoss> [0..1] CodeSet 351
     LimitedCapitalLossLevel <LtdCptlLossLvl> [0..1] Rate 352
     NoCapitalGuarantee <NoCptlGrnt> [0..1] CodeSet 352
     LossBeyondCapital <LossByndCptl> [0..1] CodeSet 352
     Other <Othr> [0..*] ± 352
   RiskTolerance <RskTlrnce> [0..1]  353
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
     NotForInvestorsWithTheLowestRiskToleranceGerm
any <NotForInvstrsWthTheLwstRskTlrnceDE>
[0..1] CodeSet 354
     Other <Othr> [0..*] ± 354
   ClientObjectivesAndNeeds <ClntObjctvsAndNeeds> [0..1]  354
     ReturnProfilePreservation <RtrPrflPrsrvtn> [0..1] CodeSet 355
     ReturnProfileGrowth <RtrPrflGrwth> [0..1] CodeSet 355
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 346 May 2026
```

