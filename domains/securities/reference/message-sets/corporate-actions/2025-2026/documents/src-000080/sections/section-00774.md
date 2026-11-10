---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.46 Statement72", "16.1.15.46.3 StatementIdentification <StmtId>"]
file_pages: [967]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.46.3 StatementIdentification <StmtId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 967 to 967.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 967

```text
16.1.15.46.3  StatementIdentification <StmtId>
Presence: [1..1]
Definition: Reference of the statement.
Datatype: "Max35Text" on page 1251
16.1.15.46.4  InstructionAggregationPeriod <InstrAggtnPrd>
Presence: [0..1]
Definition: Indicates the period of instruction details within the statement.
InstructionAggregationPeriod <InstrAggtnPrd> contains the following elements (see "DatePeriod2"
on page 842 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 842
   ToDate <ToDt> [1..1] Date 842
16.1.15.46.5  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the statement.
Datatype: "Max5NumericText" on page 1251
16.1.15.46.6  StatementDateTime <StmtDtTm>
Presence: [1..1]
Definition: Date of the statement.
StatementDateTime <StmtDtTm> contains one of the following elements (see
"DateAndDateTime2Choice" on page 848 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 848
Or}   DateTime <DtTm> [1..1] DateTime 849
16.1.15.46.7  Frequency <Frqcy>
Presence: [1..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see "Frequency25Choice" on page 874 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 874
Or}   Proprietary <Prtry> [1..1] ± 875
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 967 February 2026
```

