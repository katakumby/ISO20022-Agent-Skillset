---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.53 SecuritiesTransactionType44Choice", "82.1.19.53.2 Proprietary <Prtry>"]
file_pages: [3039]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.53.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3039 to 3039.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3039

```text
CodeName Name Definition
REDI Withdrawal Relates to the withdrawal of specified
amounts from specified subaccounts.
REBL Rebalancing Relates to a rebalanced transaction.
82.1.19.53.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.54  SafekeepingPlaceFormat29Choice
Definition: Choice between formats for the place of safekeeping.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Identification <Id> [1..1]  3039
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 3040
     Identification <Id> [0..1] Text 3040
Or   Country <Ctry> [1..1] CodeSet C3 3040
Or   TypeAndIdentification <TpAndId> [1..1]  3040
     SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 3040
     Identification <Id> [1..1] IdentifierSet C2 3041
Or}   Proprietary <Prtry> [1..1] ± 3041
82.1.19.54.1  Identification <Id>
Presence: [1..1]
Definition: Place of safekeeping expressed as a code and a narrative description.
Identification <Id> contains the following SafekeepingPlaceTypeAndText8 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceType <SfkpgPlcTp> [1..1] CodeSet 3040
   Identification <Id> [0..1] Text 3040
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3039 August 2026
```

