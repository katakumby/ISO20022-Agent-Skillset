---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.9 Date Time"]
file_pages: [2910]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.9 Date Time

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2910 to 2910.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2910

```text
FromDateToDate <FrDtToDt> contains the following elements (see "Period2" on page 2915 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 2915
   ToDate <ToDt> [1..1] Date 2915
82.1.9 Date Time
82.1.9.1  TradeDate8Choice
Definition: Choice of format for the trade date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 2910
Or}   DateCode <DtCd> [1..1]  2910
{Or     Code <Cd> [1..1] CodeSet 2910
Or}     Proprietary <Prtry> [1..1] ± 2911
82.1.9.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as an ISO date.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 2914 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
82.1.9.1.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date expressed as a code.
DateCode <DtCd> contains one of the following TradeDateCode3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2910
Or}   Proprietary <Prtry> [1..1] ± 2911
82.1.9.1.2.1  Code <Cd>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2910 August 2026
```

