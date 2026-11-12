---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["6 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "6.4 Message Building Blocks", "6.4.2 ReportGeneralDetails <RptGnlDtls>", "6.4.2.5 PenaltyListType <PnltyListTp>"]
file_pages: [188]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 6.4.2.5 PenaltyListType <PnltyListTp>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 188 to 188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 188

```text
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 345 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 345
Or}   Proprietary <Prtry> [1..1] ± 345
6.4.2.5  PenaltyListType <PnltyListTp>
Presence: [0..1]
Definition: Specifies whether the penalty list reported contains new computed penalties or updated/
removed penalties.
PenaltyListType <PnltyListTp> contains one of the following PenaltyListType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 188
Or}   Proprietary <Prtry> [1..1] ± 188
6.4.2.5.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the penalty list reported, in a coded format.
Datatype: "PenaltyListType1Code" on page 517
CodeName Name Definition
CURR Current To report the new penalties and the
modified penalties in one single
message /report.
FWAM ForwardAmend To report a penalty list that has been
amended (that is the penalty list contains
only updated and/or removed penalties
that have already been previously
reported in a FWIS Penalty List).
FWIS ForwardInitialSubmission To report a daily penalty list created for
the first time (that is the penalty list
contains only newly computed penalties)
6.4.2.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the penalty list reported, in a proprietary format.
Approved by the Securities SEG 19 February 2026. semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities - Securities and Penalty Reporting 188 March 2026
```

