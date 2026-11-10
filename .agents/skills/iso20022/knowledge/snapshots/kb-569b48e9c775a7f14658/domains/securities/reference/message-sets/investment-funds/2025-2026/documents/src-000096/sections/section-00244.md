---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.2 InvestorType <InvstrTp>", "15.4.5.22.2.2 InvestorTypeProfessional <InvstrTpPrfssnl>"]
file_pages: [348]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.2.2 InvestorTypeProfessional <InvstrTpPrfssnl>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 348 to 348.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 348

```text
CodeName Name Definition
YSCO InScope Yes, is applicable.
NEUT Neutral Neutral or has no impact.
NSCO NotInScope No, is not applicable.
15.4.5.22.2.2  InvestorTypeProfessional <InvstrTpPrfssnl>
Presence: [0..1]
Definition: Specifies how the product is aimed at the professional investor. When used in reference to
MiFID, this is in the scope of the European MiFID Template (EMT) reference 01020.
InvestorTypeProfessional <InvstrTpPrfssnl> contains one of the following elements (see
"TargetMarket5Choice" on page 4810 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Type <Tp> [1..1] CodeSet 4810
Or}   Other <Othr> [1..1] CodeSet 4810
15.4.5.22.2.3  InvestorTypeEligibleCounterparty <InvstrTpElgblCtrPty>
Presence: [0..1]
Definition: Specifies whether the product is aimed at the eligible counterparty. When used in reference
to MiFID, this is in the scope of the European MiFID Template (EMT) reference 01030.
Datatype: "TargetMarket3Code" on page 5366
CodeName Name Definition
YSCO InScope Yes, is applicable.
NSCO NotInScope No, is not applicable.
15.4.5.22.2.4  Other <Othr>
Presence: [0..*]
Definition: Specifies another investor type.
Other <Othr> contains the following elements (see "OtherTargetMarketInvestor1" on page 4812 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InvestorType <InvstrTp> [0..1] Text 4812
   Target <Trgt> [0..1]  4812
{Or     Type <Tp> [1..1] CodeSet 4813
Or     Other <Othr> [1..1] CodeSet 4813
Or}     Proprietary <Prtry> [1..1] ± 4813
   AdditionalInformation <AddtlInf> [0..1] ± 4813
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 348 May 2026
```

