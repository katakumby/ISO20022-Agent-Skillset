---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.1 Account <Acct>", "3.4.4.2.1.14 StatementFrequencyAndFormat <StmtFrqcyAndFrmt>", "3.4.4.2.1.14.2 CommunicationMethod <ComMtd>", "3.4.4.2.1.14.2.2 Proprietary <Prtry>"]
file_pages: [85]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.1.14.2.2 Proprietary <Prtry>

Source: [src-000351](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 85 to 85.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 85

```text
3.4.4.2.1.14.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification of communication method using a bilaterally or
multilaterally agreed description.
Datatype: "Max35Text" on page 183
3.4.4.2.1.14.3  DeliveryAddress <DlvryAdr>
Presence: [1..1]
Definition: Specifies the delivery address for statements.
Datatype: "Max350Text" on page 183
3.4.4.2.1.14.4  Format <Frmt>
Presence: [1..1]
Definition: Specifies the format for statements.
Format <Frmt> contains one of the following CommunicationFormat1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 85
Or}   Proprietary <Prtry> [1..1] Text 85
3.4.4.2.1.14.4.1  Code <Cd>
Presence: [1..1]
Definition: Unique and unambiguous identification of communication format using a code list.
Datatype: "ExternalCommunicationFormat1Code" on page 176
3.4.4.2.1.14.4.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique and unambiguous identification of communication format using a proprietary
identification scheme.
Datatype: "Max35Text" on page 183
3.4.4.2.1.15  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Date when the account will be or was closed.
Datatype: "ISODate" on page 179
3.4.4.2.1.16  Restriction <Rstrctn>
Presence: [0..*]
Definition: Restriction on capability or operations allowed.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 85 August 2026
```

