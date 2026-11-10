---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["38 reda.018.001.01 SecuritiesAccountCreationRequestV01", "38.4 Message Building Blocks", "38.4.2 SecuritiesAccount <SctiesAcct>", "38.4.2.4 OpeningDate <OpngDt>"]
file_pages: [2103]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.018.001.01"]
---

# 38.4.2.4 OpeningDate <OpngDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2103 to 2103.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2103

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
38.4.2.4  OpeningDate <OpngDt>
Presence: [1..1]
Definition: Legal opening date of the securities account.
Datatype: "ISODate" on page 3319
38.4.2.5  ClosingDate <ClsgDt>
Presence: [0..1]
Definition: Legal closing date of the securities account.
Datatype: "ISODate" on page 3319
38.4.2.6  HoldIndicator <HldInd>
Presence: [1..1]
Definition: Indicates whether the securities account is on hold or not.
Usage:
- Meaning when true: account is in hold status.
- Meaning when false: account is in release status.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
38.4.2.7  NegativePosition <NegPos>
Presence: [1..1]
Definition: Indicates whether the securities account can hold a negative position in a security or not.
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
38.4.2.8  MarketSpecificAttribute <MktSpcfcAttr>
Presence: [0..*]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.018.001.01
SecuritiesAccountCreationRequestV01
Target2-Securities 2103 August 2026
```

