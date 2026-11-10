---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.5 SecurityIdentification19", "82.1.13.5.1 ISIN <ISIN>"]
file_pages: [2952]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.5.1 ISIN <ISIN>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2952 to 2952.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2952

```text
    /ISIN Must be present
 Or    /Description Must be present
82.1.13.5.1  ISIN <ISIN>
Presence: [0..1]
Definition: International Securities Identification Number (ISIN). A numbering system designed by the
United Nation's International Organisation for Standardisation (ISO). The ISIN is composed of a 2-
character prefix representing the country of issue, followed by the national security number (if one
exists), and a check digit. Each country has a national numbering agency that assigns ISIN numbers for
securities in that country.
Datatype: "ISINOct2015Identifier" on page 3322
82.1.13.5.2  OtherIdentification <OthrId>
Presence: [0..*]
Definition: Identification of a security by proprietary or domestic identification scheme.
OtherIdentification <OthrId> contains the following OtherIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2952
   Suffix <Sfx> [0..1] Text 2952
   Type <Tp> [1..1] ± 2952
82.1.13.5.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security.
Datatype: "Max35Text" on page 3328
82.1.13.5.2.2  Suffix <Sfx>
Presence: [0..1]
Definition: Identifies the suffix of the security identification.
Datatype: "Max16Text" on page 3326
82.1.13.5.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 2965 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2965
Or}   Proprietary <Prtry> [1..1] Text 2965
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2952 August 2026
```

