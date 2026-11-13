---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.8 Date Time", "35.1.8.1 TradeDate8Choice", "35.1.8.1.2 DateCode <DtCd>"]
file_pages: [1436]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.8.1.2 DateCode <DtCd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1436 to 1436.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1436

```text
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 1441 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 1441
Or}   DateTime <DtTm> [1..1] DateTime 1441
35.1.8.1.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date expressed as a code.
DateCode <DtCd> contains one of the following TradeDateCode3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1436
Or}   Proprietary <Prtry> [1..1] ± 1436
35.1.8.1.2.1  Code <Cd>
Presence: [1..1]
Definition: Trade date expressed as an ISO 20022 code.
Datatype: "DateType3Code" on page 2058
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
35.1.8.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade date expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.8.2  TerminationDate6Choice
Definition: Choice of format for the termination date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1436 March 2026
```

