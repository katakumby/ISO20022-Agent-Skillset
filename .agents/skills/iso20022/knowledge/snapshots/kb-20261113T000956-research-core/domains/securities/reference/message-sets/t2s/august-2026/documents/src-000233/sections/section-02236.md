---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.25 RegistrationReason5"]
file_pages: [3006]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.25 RegistrationReason5

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3006 to 3006.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3006

```text
Definition: Proprietary code to express the type of rate.
Proprietary <Prtry> contains the following elements (see "GenericIdentification13" on page 2968 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2969
   SchemeName <SchmeNm> [0..1] Text 2969
   Issuer <Issr> [1..1] Text 2969
82.1.19.25  RegistrationReason5
Definition: Reason of registration.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1]  3006
{Or     Code <Cd> [1..1] CodeSet 3006
Or}     Proprietary <Prtry> [1..1] ± 3007
   AdditionalInformation <AddtlInf> [0..1] Text 3007
82.1.19.25.1  Code <Cd>
Presence: [1..1]
Definition: Specifies the reason of the holding status.
Code <Cd> contains one of the following Registration10Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3006
Or}   Proprietary <Prtry> [1..1] ± 3007
82.1.19.25.1.1  Code <Cd>
Presence: [1..1]
Definition: Registration information expressed as an ISO 20022 code.
Datatype: "Registration2Code" on page 3283
CodeName Name Definition
PTYH PartyHold You or your party set the instruction in a
hold/frozen/preadvice mode.
CSDH CSDHold Central securities depository sets the
instruction in a hold/frozen/preadvice
mode.
CDEL ConditionalDelivery Instruction is in a hold/frozen/preadvice
mode as it fulfils predefined conditional
delivery rules in the market infrastructure
platform for conditional delivery.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3006 August 2026
```

