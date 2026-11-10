---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.41 RestrictionIdentification1"]
file_pages: [3024]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.41 RestrictionIdentification1

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3024 to 3024.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3024

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.41  RestrictionIdentification1
Definition: Restriction References applied on the transaction for which the securities settlement
condition modification is requested.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet 3024
   Identification <Id> [1..1] Text 3024
82.1.19.41.1  Code <Cd>
Presence: [1..1]
Definition: Restriction identification removal or addition applied on the transaction expressed as a code.
Datatype: "RestrictionReference1Code" on page 3288
CodeName Name Definition
ADDC AddCashRestrictionReference Addition of a cash restriction reference
representing a cash sub-balance to be
utilised within the settlement instruction
for the debiting or crediting of cash.
ADDS AddSecuritiesRestrictionReference Addition of a securities restriction
reference representing a securities sub-
position to be utilised within the
settlement instruction for the delivery or
receipt of securities.
REMC RemoveCashRestrictionReference Removal of a cash restriction reference,
already present within the settlement
instruction, representing a cash sub-
balance to be utilised within the
settlement instruction for the debiting or
crediting of cash.
REMS RemoveSecuritiesRestrictionReference Removal of a securities restriction
reference, already present within the
settlement instruction, representing a
securities sub-position to be utilised
within the settlement instruction for the
delivery or receipt of securities.
82.1.19.41.2  Identification <Id>
Presence: [1..1]
Definition: Restriction identification applied on the transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3024 August 2026
```

