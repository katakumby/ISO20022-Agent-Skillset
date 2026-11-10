---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["81 semt.044.001.01 SecuritiesTransactionPenaltiesReportV01", "81.4 Message Building Blocks", "81.4.2 ReportGeneralDetails <RptGnlDtls>", "81.4.2.5 PenaltyListType <PnltyListTp>"]
file_pages: [2770]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.044.001.01"]
---

# 81.4.2.5 PenaltyListType <PnltyListTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2770 to 2770.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2770

```text
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 2958
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2958
Or}   Proprietary <Prtry> [1..1] ± 2959
81.4.2.5  PenaltyListType <PnltyListTp>
Presence: [0..1]
Definition: Specifies whether the penalty list reported contains new computed penalties or updated/
removed penalties.
PenaltyListType <PnltyListTp> contains one of the following PenaltyListType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2770
Or}   Proprietary <Prtry> [1..1] ± 2770
81.4.2.5.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the penalty list reported, in a coded format.
Datatype: "PenaltyListType1Code" on page 3268
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
81.4.2.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the penalty list reported, in a proprietary format.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.044.001.01
SecuritiesTransactionPenaltiesReportV01
Target2-Securities 2770 August 2026
```

