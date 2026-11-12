---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.41 CRSStatus4", "66.1.30.41.1 Type <Tp>"]
file_pages: [5035]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.41.1 Type <Tp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5035 to 5035.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5035

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  5035
{Or     Code <Cd> [1..1] CodeSet 5035
Or}     Proprietary <Prtry> [1..1] ± 5036
   Source <Src> [0..1]  5036
{Or     Code <Cd> [1..1] CodeSet 5037
Or}     Proprietary <Prtry> [1..1] ± 5037
   ExceptionalReportingCountry <XcptnlRptgCtry> [0..1] CodeSet C12 5037
66.1.30.41.1  Type <Tp>
Presence: [1..1]
Definition: Common Reporting Standard (CRS) status.
Type <Tp> contains one of the following CRSStatus3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5035
Or}   Proprietary <Prtry> [1..1] ± 5036
66.1.30.41.1.1  Code <Cd>
Presence: [1..1]
Definition: Common Reporting Standard (CRS) status expressed as a code.
Datatype: "CRSStatus1Code" on page 5292
CodeName Name Definition
C101 CRS101 Account holder type is a passive non-
financial entity with one or more
controlling persons that are foreign
persons.
C102 CRS102 Account holder type is a foreign person.
C103 CRS103 Account holder type is a passive foreign
non-financial entity without controlling
persons that are foreign persons.
C104 CRS104 Account holder type is a financial
institution such as a depositary, a
custodial institution or a specified
insurance company.
C105 CRS105 Account holder type is a financial
institution such as an investment entity
of a non-participating jurisdiction and
managed by another financial institution
without one or more controlling persons
that are foreign persons.
C106 CRS106 Account holder type is a financial
institution such as an investment entity
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5035 May 2026
```

