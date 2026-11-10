---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.35 BlockTrade4Choice"]
file_pages: [3018]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.35 BlockTrade4Choice

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3018 to 3018.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3018

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.35  BlockTrade4Choice
Definition: Choice of format for the block trade information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3018
Or}   Proprietary <Prtry> [1..1] ± 3018
82.1.19.35.1  Code <Cd>
Presence: [1..1]
Definition: Block parent or child information expressed as an ISO 20022 code.
Datatype: "BlockTrade1Code" on page 3216
CodeName Name Definition
BLPA Parent Transaction is a block trade parent.
BLCH Child Transaction is a block trade child.
82.1.19.35.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Block parent or child information expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.36  SettlementOrCorporateActionEvent26Choice
Definition: Choice between transaction type, corporate action event and settlement transaction.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3018 August 2026
```

