---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.62 OptionType8Choice", "82.1.19.62.1 Code <Cd>"]
file_pages: [3048]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.62.1 Code <Cd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3048 to 3048.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3048

```text
82.1.19.62.1  Code <Cd>
Presence: [0..*]
Definition: Option type expressed as an ISO 20022 code.
Datatype: "OptionType1Code" on page 3267
CodeName Name Definition
CALL Call Right to buy a quantity of an asset for an
agreed price at exercise date.
PUTO Put Right to sell a quantity of an asset for an
agreed price at exercise date.
82.1.19.62.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.63  SettlingCapacity7Choice
Definition: Choice of format for the settlement capacity information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3048
Or}   Proprietary <Prtry> [1..1] ± 3049
82.1.19.63.1  Code <Cd>
Presence: [1..1]
Definition: Settlement capacity expressed as an ISO 20022 code.
Datatype: "SettlingCapacity2Code" on page 3303
CodeName Name Definition
SAGE SettlingAgent Settlement party is trading and settling
transactions in financial instruments on
behalf of its client(s).
CUST SettlingCustodian Settlement party is a custodian. It
receives/delivers the securities and
carries out custodial duties.
SPRI SettlingPrincipal Settlement party is settling its own
trades.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3048 August 2026
```

