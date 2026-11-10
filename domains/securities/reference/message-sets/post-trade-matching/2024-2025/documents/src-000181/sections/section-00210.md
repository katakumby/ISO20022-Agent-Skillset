---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.11 Date Time", "7.1.11.3 ClosingDate4Choice", "7.1.11.3.2 Code <Cd>"]
file_pages: [264]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.11.3.2 Code <Cd>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 264 to 264.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 264

```text
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 265 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 265
Or}   DateTime <DtTm> [1..1] DateTime 265
7.1.11.3.2  Code <Cd>
Presence: [1..1]
Definition: Closing date is defined using a code or data source scheme.
Code <Cd> contains one of the following Date3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 264
Or}   Proprietary <Prtry> [1..1] ± 264
7.1.11.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Date is defined using a code.
Datatype: "DateType2Code" on page 623
CodeName Name Definition
OPEN Open Open-dated, which indicates that the
date has not been established.
7.1.11.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Date is determined using a data source scheme and a code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.11.4  SettlementDate16Choice
Definition: Choice of format for the settlement date.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 264 February 2025
```

