---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.9 Date Time", "82.1.9.1 TradeDate8Choice", "82.1.9.1.2 DateCode <DtCd>", "82.1.9.1.2.2 Proprietary <Prtry>"]
file_pages: [2911]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.9.1.2.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2911 to 2911.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2911

```text
Definition: Trade date expressed as an ISO 20022 code.
Datatype: "DateType3Code" on page 3235
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
82.1.9.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Trade date expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.9.2  SettlementDateCode8Choice
Definition: Choice of format for the settlement date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2911
Or}   Proprietary <Prtry> [1..1] ± 2911
82.1.9.2.1  Code <Cd>
Presence: [1..1]
Definition: Settlement date expressed as an ISO 20022 code.
Datatype: "DateType4Code" on page 3235
CodeName Name Definition
OPEN Open Open-dated, which indicates that the
date has not been established.
UKWN Unknown Date is unknown by the sender or has
not been established.
82.1.9.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement date expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2911 August 2026
```

