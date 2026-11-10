---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.10 CorporateActionDetails <CorpActnDtls>", "3.4.10.3 RateAndAmountDetails <RateAndAmtDtls>"]
file_pages: [110]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.10.3 RateAndAmountDetails <RateAndAmtDtls>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 110 to 110.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 110

```text
PeriodDetails <PrdDtls> contains the following elements (see "CorporateActionPeriod17" on page 836
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InterestPeriod <IntrstPrd> [0..1] ± 837
   CompulsoryPurchasePeriod <CmplsryPurchsPrd> [0..1] ± 838
   ClaimPeriod <ClmPrd> [0..1] ± 838
   DepositorySuspensionPeriodForBookEntryTransfer
<DpstrySspnsnPrdForBookNtryTrf>
[0..1] ± 838
   DepositorySuspensionPeriodForDepositAtAgent
<DpstrySspnsnPrdForDpstAtAgt>
[0..1] ± 838
   DepositorySuspensionPeriodForDeposit
<DpstrySspnsnPrdForDpst>
[0..1] ± 839
   DepositorySuspensionPeriodForPledge
<DpstrySspnsnPrdForPldg>
[0..1] ± 839
   DepositorySuspensionPeriodForSegregation
<DpstrySspnsnPrdForSgrtn>
[0..1] ± 839
   DepositorySuspensionPeriodForWithdrawalAtAgent
<DpstrySspnsnPrdForWdrwlAtAgt>
[0..1] ± 840
   DepositorySuspensionPeriodForWithdrawalInNomineeNa
me <DpstrySspnsnPrdForWdrwlInNmneeNm>
[0..1] ± 840
   DepositorySuspensionPeriodForWithdrawalInStreetName
<DpstrySspnsnPrdForWdrwlInStrtNm>
[0..1] ± 840
   BookClosurePeriod <BookClsrPrd> [0..1] ± 840
   CoDepositoriesSuspensionPeriod
<CoDpstriesSspnsnPrd>
[0..1] ± 841
   SplitPeriod <SpltPrd> [0..1] ± 841
   FiscalYearPeriod <FsclYrPrd> [0..1] ± 841
Constraints
• InterestPeriodRule
InterestPeriod must be used only if it is different from a normal accrued interest period.
3.4.10.3  RateAndAmountDetails <RateAndAmtDtls>
Presence: [0..1]
Definition: Provides information about rates and amounts related to a corporate action event.
Impacted by: C20 "DeclaredRateRule"
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 110 February 2026
```

