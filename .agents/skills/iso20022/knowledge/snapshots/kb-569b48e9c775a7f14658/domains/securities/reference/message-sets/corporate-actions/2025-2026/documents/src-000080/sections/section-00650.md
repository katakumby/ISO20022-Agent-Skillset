---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.4 Date Period", "16.1.4.1 CorporateActionPeriod17", "16.1.4.1.13 CoDepositoriesSuspensionPeriod <CoDpstriesSspnsnPrd>"]
file_pages: [841]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.4.1.13 CoDepositoriesSuspensionPeriod <CoDpstriesSspnsnPrd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 841 to 841.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 841

```text
Definition: Period defining the last date on which shareholder registration will be accepted by the issuer
and the date on which shareholder registration will resume.
BookClosurePeriod <BookClsrPrd> contains one of the following elements (see "Period12Choice" on
page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.13  CoDepositoriesSuspensionPeriod <CoDpstriesSspnsnPrd>
Presence: [0..1]
Definition: Period during which the settlement activities at the co-depositories are suspended in order to
stabilise the holdings at the CSD.
CoDepositoriesSuspensionPeriod <CoDpstriesSspnsnPrd> contains one of the following elements
(see "Period12Choice" on page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.14  SplitPeriod <SpltPrd>
Presence: [0..1]
Definition: Period during which a physical certificate can be split.
SplitPeriod <SpltPrd> contains one of the following elements (see "Period12Choice" on page 857 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
16.1.4.1.15  FiscalYearPeriod <FsclYrPrd>
Presence: [0..1]
Definition: Period defining the fiscal or tax year the dividend pertains to in order to correctly deduct
taxes for residents.
FiscalYearPeriod <FsclYrPrd> contains one of the following elements (see "Period12Choice" on
page 857 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Period <Prd> [1..1] ± 857
Or}   PeriodCode <PrdCd> [1..1] CodeSet 857
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 841 February 2026
```

