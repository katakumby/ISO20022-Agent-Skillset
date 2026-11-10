---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.1 ReferenceDate <RefDt>"]
file_pages: [347]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.1 ReferenceDate <RefDt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 347 to 347.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 347

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
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
   Other <Othr> [0..*] ± 358
15.4.5.22.1  ReferenceDate <RefDt>
Presence: [0..1]
Definition: Date to which the target market data refers. When used in reference to MiFID, this is in the
scope of the European MiFID Template (EMT) reference 01000.
Datatype: "ISODate" on page 5388
15.4.5.22.2  InvestorType <InvstrTp>
Presence: [0..1]
Definition: Investor for which the financial instrument is targeted.
InvestorType <InvstrTp> contains the following InvestorType2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InvestorTypeRetail <InvstrTpRtl> [0..1] CodeSet 347
   InvestorTypeProfessional <InvstrTpPrfssnl> [0..1] ± 348
   InvestorTypeEligibleCounterparty
<InvstrTpElgblCtrPty>
[0..1] CodeSet 348
   Other <Othr> [0..*] ± 348
15.4.5.22.2.1  InvestorTypeRetail <InvstrTpRtl>
Presence: [0..1]
Definition: Specifies whether the product is aimed at the retail investor. If neutral, the manufacturer
estimates that there is neither a negative nor a positive target market. When used in reference to MiFID,
this is in the scope of the European MiFID Template (EMT) reference 01010.
Datatype: "TargetMarket1Code" on page 5365
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 347 May 2026
```

