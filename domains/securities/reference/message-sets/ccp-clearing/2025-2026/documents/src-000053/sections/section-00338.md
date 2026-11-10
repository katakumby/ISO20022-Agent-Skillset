---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.11 Margin Call Calculation", "12.1.11.2 MarginCalculation1", "12.1.11.2.1 TotalMarginAmount <TtlMrgnAmt>"]
file_pages: [431]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.11.2.1 TotalMarginAmount <TtlMrgnAmt>

Source: [src-000053](../../../../../../../../../raw-input/central_counterparty_clearing_ccp_clearing/ISO20022_MDRPart2_CentralCounterPartySecuritiesClearing_Maintenance_2025_2026_v1.pdf). Locator: one-based file pages 431 to 431.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 431

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalMarginAmount <TtlMrgnAmt> [1..1] ± 431
   CollateralOnDeposit <CollOnDpst> [0..*] ± 431
   MinimumRequirementDeposit <MinRqrmntDpst> [0..1] Amount   'C1,
  'C7
431
   MarginResult <MrgnRslt> [0..1]  432
{Or     ExcessAmount <XcssAmt> [1..1] Amount   'C1,
  'C7
432
Or}     DeficitAmount <DfcitAmt> [1..1] Amount   'C1,
  'C7
433
12.1.11.2.1  TotalMarginAmount <TtlMrgnAmt>
Presence: [1..1]
Definition: Total margin requirement (expressed in the reporting currency) that must be provided by the
clearing member to the central counterparty. This is the total requirement calculated to cover the initial
margin and the variation margin.
TotalMarginAmount <TtlMrgnAmt> contains the following elements (see AmountAndDirection20 on
page 378 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount   'C2,
  'C6
378
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 379
12.1.11.2.2  CollateralOnDeposit <CollOnDpst>
Presence: [0..*]
Definition: Provides details on the valuation of the collateral on deposit.
CollateralOnDeposit <CollOnDpst> contains the following elements (see Collateral6 on page 383 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PostHaircutValue <PstHrcutVal> [1..1] Amount   'C1,
  'C7
384
   MarketValue <MktVal> [1..1] Amount   'C1,
  'C7
384
   CollateralType <CollTp> [1..1] CodeSet 385
12.1.11.2.3  MinimumRequirementDeposit <MinRqrmntDpst>
Presence: [0..1]
Definition: Minimum requirement (expressed in the reporting currency) for a participant if their
requirement falls below a specific amount set by the central counterparty.
Impacted by:   'C1 ActiveCurrency  ',   'C7 CurrencyAmount  '
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 431
```

