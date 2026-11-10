---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["7 MX secl.006.001.02 DefaultFundContributionReportV02", "7.4 Message Building Blocks", "7.4.3 ReportDetails <RptDtls>", "7.4.3.2 CollateralDescription <CollDesc>"]
file_pages: [252]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.006.001.02"]
---

# 7.4.3.2 CollateralDescription <CollDesc>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 252 to 252.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 252

```text
DefaultFundCalculation <DfltFndClctn> contains the following elements (see DefaultFund1 on
page 401 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DefaultFundAccount <DfltFndAcct> [1..1] ± 401
   TotalDefaultFundAmount <TtlDfltFndAmt> [1..1] Amount   'C1,
  'C7
402
   Contribution <Cntrbtn> [0..*]  402
     Account <Acct> [0..1] ± 403
     RequiredAmount <ReqrdAmt> [1..1] Amount   'C1,
  'C7
403
     IncreaseCoverageAmount <IncrCvrgAmt> [0..1] Amount   'C1,
  'C7
404
     NonClearingMember <NonClrMmb> [0..1] ± 404
   IncreaseCoverageAmount <IncrCvrgAmt> [0..1] Amount   'C1,
  'C7
405
7.4.3.2  CollateralDescription <CollDesc>
Presence: [1..*]
Definition: Provides details about the collateral held.
CollateralDescription <CollDesc> contains the following elements (see Collateral3 on page 381 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostHaircutValue <PstHrcutVal> [1..1] Amount   'C1,
  'C7
382
   MarketValue <MktVal> [1..1] Amount   'C1,
  'C7
382
   CollateralType <CollTp> [1..1] CodeSet 383
7.4.3.3  NetExcessOrDeficit <NetXcssOrDfcit>
Presence: [1..1]
Definition: Excess amount that the central counterparty will restitute to the clearing member or deficit to
be provided by the member for the guarantee fund.
NetExcessOrDeficit <NetXcssOrDfcit> contains the following elements (see AmountAndDirection21
on page 377 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
377
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 378
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.006.001.02
DefaultFundContributionReportV02
March 2026 252
```

