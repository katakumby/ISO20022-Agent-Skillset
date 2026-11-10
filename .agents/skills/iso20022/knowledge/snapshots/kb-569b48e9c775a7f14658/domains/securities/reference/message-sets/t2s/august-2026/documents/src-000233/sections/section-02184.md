---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.13 Financial Instrument", "82.1.13.3 SecurityIdentification39", "82.1.13.3.2 OtherIdentification <OthrId>"]
file_pages: [2947]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.13.3.2 OtherIdentification <OthrId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2947 to 2947.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2947

```text
Datatype: "ISIN2021Identifier" on page 3321
82.1.13.3.2  OtherIdentification <OthrId>
Presence: [0..*]
Definition: Identification of a security by proprietary or domestic identification scheme.
OtherIdentification <OthrId> contains the following OtherIdentification1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2947
   Suffix <Sfx> [0..1] Text 2947
   Type <Tp> [1..1] ± 2947
82.1.13.3.2.1  Identification <Id>
Presence: [1..1]
Definition: Identification of a security.
Datatype: "Max35Text" on page 3328
82.1.13.3.2.2  Suffix <Sfx>
Presence: [0..1]
Definition: Identifies the suffix of the security identification.
Datatype: "Max16Text" on page 3326
82.1.13.3.2.3  Type <Tp>
Presence: [1..1]
Definition: Type of the identification.
Type <Tp> contains one of the following elements (see "IdentificationSource3Choice" on page 2965 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2965
Or}   Proprietary <Prtry> [1..1] Text 2965
82.1.13.3.3  Description <Desc>
Presence: [0..1]
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 3326
82.1.13.4  FinancialInstrument21
Definition: Security that is a sub-set of an investment fund, and is governed by the same investment
fund policy, for example, dividend option or valuation currency.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2947 August 2026
```

