---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.4 Date Period", "16.1.4.1 CorporateActionPeriod17", "16.1.4.1.6 DepositorySuspensionPeriodForDeposit <DpstrySspnsnPrdForDpst>"]
file_pages: [839]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.4.1.6 DepositorySuspensionPeriodForDeposit <DpstrySspnsnPrdForDpst>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 839 to 839.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 839

```text
DepositorySuspensionPeriodForDepositAtAgent <DpstrySspnsnPrdForDpstAtAgt> contains one
of the following elements (see "Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.6  DepositorySuspensionPeriodForDeposit <DpstrySspnsnPrdForDpst>
Presence: [0..1]
Definition: Period defining the last date for which deposits will be accepted and the date on which the
suspension will be released and deposits will resume.
DepositorySuspensionPeriodForDeposit <DpstrySspnsnPrdForDpst> contains one of the following
elements (see "Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.7  DepositorySuspensionPeriodForPledge <DpstrySspnsnPrdForPldg>
Presence: [0..1]
Definition: Period defining the last date for which pledges will be accepted and the date on which the
suspension will be released and pledge processing will resume.
DepositorySuspensionPeriodForPledge <DpstrySspnsnPrdForPldg> contains one of the following
elements (see "Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.8  DepositorySuspensionPeriodForSegregation <DpstrySspnsnPrdForSgrtn>
Presence: [0..1]
Definition: Period defining the last date for which intra-position balances can be segregated and the
date on which the suspension will be released and the ability to segregate intra-position balances will
resume.
DepositorySuspensionPeriodForSegregation <DpstrySspnsnPrdForSgrtn> contains one of the
following elements (see "Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 839 February 2026
```

