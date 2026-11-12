---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.29 TaxCapacityParty4Choice", "82.1.19.29.1 Code <Cd>"]
file_pages: [3011]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.29.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3011 to 3011.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3011

```text
82.1.19.29.1  Code <Cd>
Presence: [1..1]
Definition: Party tax capacity expressed as an ISO 20022 code.
Datatype: "TaxLiability1Code" on page 3306
CodeName Name Definition
PRIN TaxPrincipal Settlement party is acting as a principal
for tax liability.
AGEN TaxAgent Settlement party is acting as an agent for
tax liability.
82.1.19.29.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Party tax capacity expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.30  SupplementaryData1
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 3011
   Envelope <Envlp> [1..1] (External Schema) 3012
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
82.1.19.30.1  PlaceAndName <PlcAndNm>
Presence: [0..1]
Definition: Unambiguous reference to the location where the supplementary data must be inserted in
the message instance.
In the case of XML, this is expressed by a valid XPath.
Datatype: "Max350Text" on page 3328
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3011 August 2026
```

