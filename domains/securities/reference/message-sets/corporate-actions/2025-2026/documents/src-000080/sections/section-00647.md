---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.4 Date Period", "16.1.4.1 CorporateActionPeriod17", "16.1.4.1.2 CompulsoryPurchasePeriod <CmplsryPurchsPrd>"]
file_pages: [838]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.4.1.2 CompulsoryPurchasePeriod <CmplsryPurchsPrd>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 838 to 838.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 838

```text
16.1.4.1.2  CompulsoryPurchasePeriod <CmplsryPurchsPrd>
Presence: [0..1]
Definition: Period during a take-over where any outstanding equity must be purchased by the take-over
company.
CompulsoryPurchasePeriod <CmplsryPurchsPrd> contains one of the following elements (see
"Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.3  ClaimPeriod <ClmPrd>
Presence: [0..1]
Definition: Period assigned by the court in a class action. It determines the client's eligible transactions
that will be included in the class action and used to determine the resulting entitlement.
ClaimPeriod <ClmPrd> contains one of the following elements (see "Period12Choice" on page 857
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.4  DepositorySuspensionPeriodForBookEntryTransfer
<DpstrySspnsnPrdForBookNtryTrf>
Presence: [0..1]
Definition: Period defining the last date for which book entry transfers will be accepted and the date on
which the suspension will be released and book entry transfer processing will resume.
DepositorySuspensionPeriodForBookEntryTransfer <DpstrySspnsnPrdForBookNtryTrf>
contains one of the following elements (see "Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.5  DepositorySuspensionPeriodForDepositAtAgent <DpstrySspnsnPrdForDpstAtAgt>
Presence: [0..1]
Definition: Period defining the last date for which deposits, into nominee name, at the agent will be
accepted and the date on which the suspension will be released and deposits at agent will resume.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 838 February 2026
```

