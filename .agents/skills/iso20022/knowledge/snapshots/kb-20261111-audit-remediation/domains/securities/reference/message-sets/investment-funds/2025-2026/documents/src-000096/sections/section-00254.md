---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.22 TargetMarket <TrgtMkt>", "15.4.5.22.6 ClientObjectivesAndNeeds <ClntObjctvsAndNeeds>", "15.4.5.22.6.10 Other <Othr>"]
file_pages: [358]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.22.6.10 Other <Othr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 358 to 358.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 358

```text
15.4.5.22.6.10  Other <Othr>
Presence: [0..*]
Definition: Other investment need. 
Other <Othr> contains the following elements (see "OtherInvestmentNeed1" on page 4762 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ClientObjectivesAndNeedsType
<ClntObjctvsAndNeedsTp>
[0..1] Text 4762
   Target <Trgt> [0..1]  4762
{Or     Code <Cd> [1..1] CodeSet 4763
Or}     Proprietary <Prtry> [1..1] ± 4763
   AdditionalInformation <AddtlInf> [0..1] ± 4763
15.4.5.22.7  Other <Othr>
Presence: [0..*]
Definition: Other target market parameter.
Other <Othr> contains the following elements (see "OtherTargetMarket1" on page 4728 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TargetMarketType <TrgtMktTp> [1..1] Text 4728
   AdditionalInformation <AddtlInf> [0..1] ± 4728
15.4.5.23  DistributionStrategy <DstrbtnStrtgy>
Presence: [0..1]
Definition: Distribution strategy criteria.
DistributionStrategy <DstrbtnStrtgy> contains the following elements (see "DistributionStrategy1" on
page 4752 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExecutionOnly <ExctnOnly> [0..1] ± 4752
   ExecutionWithAppropriatenessTestOrNonAdvisedService
s <ExctnWthApprprtnssTstOrNonAdvsdSvcs>
[0..1] ± 4752
   InvestmentAdvice <InvstmtAdvc> [0..1] ± 4753
   PortfolioManagement <PrtflMgmt> [0..1] ± 4753
   Other <Othr> [0..1] ± 4753
15.4.5.24  CostsAndCharges <CostsAndChrgs>
Presence: [0..2]
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 358 May 2026
```

