---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.9 Date Time", "82.1.9.3 SettlementDate17Choice"]
file_pages: [2912]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.9.3 SettlementDate17Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2912 to 2912.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2912

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.9.3  SettlementDate17Choice
Definition: Choice of format for the settlement date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 2912
Or}   DateCode <DtCd> [1..1] ± 2912
82.1.9.3.1  Date <Dt>
Presence: [1..1]
Definition: Date in ISO format.
Date <Dt> contains one of the following elements (see "DateAndDateTime2Choice" on page 2914 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
82.1.9.3.2  DateCode <DtCd>
Presence: [1..1]
Definition: Date and time at which the securities are to be delivered or received.
DateCode <DtCd> contains one of the following elements (see "SettlementDateCode7Choice" on
page 2913 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2913
Or}   Proprietary <Prtry> [1..1] ± 2913
82.1.9.4  DateAndDateTime1Choice
Definition: Choice between a date or a date and time format.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2912 August 2026
```

