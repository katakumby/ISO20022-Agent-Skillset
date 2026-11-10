---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.65 LinkageType3Choice", "82.1.19.65.2 Proprietary <Prtry>"]
file_pages: [3057]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.65.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3057 to 3057.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3057

```text
82.1.19.65.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Linkage type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.66  Statement89
Definition: Defines the criteria used to report on the securities account positions.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DateOrPeriod <DtOrPrd> [0..1] ± 3057
   HistoricData <HstrcData> [1..1] Indicator 3057
   StatementType <StmtTp> [0..1] ± 3057
82.1.19.66.1  DateOrPeriod <DtOrPrd>
Presence: [0..1]
Definition: Date or period of the statement.
DateOrPeriod <DtOrPrd> contains one of the following elements (see "DateAndPeriod3Choice" on
page 2915 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementDate <StmtDt> [1..1] ± 2915
Or}   StatementPeriod <StmtPrd> [1..1] ± 2916
82.1.19.66.2  HistoricData <HstrcData>
Presence: [1..1]
Definition: Specifies whether the data is either historical (true) or current (false).
Datatype: One of the following values must be used (see "TrueFalseIndicator" on page 3323):
• Meaning When True: True
• Meaning When False: False
82.1.19.66.3  StatementType <StmtTp>
Presence: [0..1]
Definition: Type of balance on which the statement is prepared.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3057 August 2026
```

