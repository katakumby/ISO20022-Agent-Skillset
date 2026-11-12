---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.4 Date Period", "16.1.4.1 CorporateActionPeriod17", "16.1.4.1.9 DepositorySuspensionPeriodForWithdrawalAtAgent <DpstrySspnsnPrdForWdrwlAtAgt>"]
file_pages: [840]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.4.1.9 DepositorySuspensionPeriodForWithdrawalAtAgent <DpstrySspnsnPrdForWdrwlAtAgt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 840 to 840.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 840

```text
16.1.4.1.9  DepositorySuspensionPeriodForWithdrawalAtAgent
<DpstrySspnsnPrdForWdrwlAtAgt>
Presence: [0..1]
Definition: Period defining the last date for which withdrawals, from nominee name at the agent will be
accepted and the date on which the suspension will be released and withdrawals at agent processing
will resume.
DepositorySuspensionPeriodForWithdrawalAtAgent <DpstrySspnsnPrdForWdrwlAtAgt>
contains one of the following elements (see "Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.10  DepositorySuspensionPeriodForWithdrawalInNomineeName
<DpstrySspnsnPrdForWdrwlInNmneeNm>
Presence: [0..1]
Definition: Period defining the last date for which physical withdrawals in the nominee's name will be
accepted and the date on which the suspension will be released and physical withdrawals in the
nominee's name will resume.
DepositorySuspensionPeriodForWithdrawalInNomineeName
<DpstrySspnsnPrdForWdrwlInNmneeNm> contains one of the following elements (see
"Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.11  DepositorySuspensionPeriodForWithdrawalInStreetName
<DpstrySspnsnPrdForWdrwlInStrtNm>
Presence: [0..1]
Definition: Period defining the last date on which withdrawal requests in street name's will be accepted
on the event security and the date on which the suspension will be released and withdrawal in street
name's processing on the event security will resume.
DepositorySuspensionPeriodForWithdrawalInStreetName
<DpstrySspnsnPrdForWdrwlInStrtNm> contains one of the following elements (see
"Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.12  BookClosurePeriod <BookClsrPrd>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 840 February 2026
```

