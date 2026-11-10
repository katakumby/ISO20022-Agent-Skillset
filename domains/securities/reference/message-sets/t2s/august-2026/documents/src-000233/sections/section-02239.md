---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.26 MessageHeader2", "82.1.19.26.3 RequestType <ReqTp>", "82.1.19.26.3.3 Proprietary <Prtry>"]
file_pages: [3009]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.26.3.3 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3009 to 3009.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3009

```text
CodeName Name Definition
RT14 SuspiciousTransactionEnquiry Type is an enquiry on a suspicious
transaction.
RT15 PendingInwardCreditsEnquiry Type is an enquiry on pending inward
credits.
82.1.19.26.3.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Request type is in proprietary format.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2966
   SchemeName <SchmeNm> [0..1] Text 2966
   Issuer <Issr> [0..1] Text 2966
82.1.19.27  OptionStyle8Choice
Definition: Choice of format for the option style.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3009
Or}   Proprietary <Prtry> [1..1] ± 3009
82.1.19.27.1  Code <Cd>
Presence: [1..1]
Definition: Option style expressed as an ISO 20022 code.
Datatype: "OptionStyle2Code" on page 3266
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
EURO European Option that can be exercised on expiry
date only.
82.1.19.27.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Option style expressed as a proprietary code.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3009 August 2026
```

