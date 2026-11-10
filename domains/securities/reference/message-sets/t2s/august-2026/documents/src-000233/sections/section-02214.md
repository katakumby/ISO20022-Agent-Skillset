---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.2 SettlementSystemMethod4Choice"]
file_pages: [2977]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.2 SettlementSystemMethod4Choice

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2977 to 2977.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2977

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.2  SettlementSystemMethod4Choice
Definition: Choice of format for the settlement system/method.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2977
Or}   Proprietary <Prtry> [1..1] ± 2977
82.1.19.2.1  Code <Cd>
Presence: [1..1]
Definition: Settlement system expressed as an ISO 20022 code.
Datatype: "SettlementSystemMethod1Code" on page 3301
CodeName Name Definition
NSET Default Settle through the default settlement
system/method. If there is a standing
instruction in place for settlement
through the alternate settlement system/
method, then this standing instruction is
to be ignored.
YSET Alternative Settle through the alternate settlement
system/method. If there is a standing
instruction in place for settlement
through the default settlement system/
method, then this standing instruction is
to be ignored.
82.1.19.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Settlement system expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2977 August 2026
```

