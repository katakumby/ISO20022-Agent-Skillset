---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.60 FormOfSecurity6Choice", "82.1.19.60.2 Proprietary <Prtry>"]
file_pages: [3046]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.60.2 Proprietary <Prtry>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3046 to 3046.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3046

```text
Datatype: "FormOfSecurity1Code" on page 3254
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
82.1.19.60.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Form of the security expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 2966 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.61  MessageHeader9
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 3046
   CreationDateTime <CreDtTm> [0..1] DateTime 3046
   RequestType <ReqTp> [0..1]  3047
{Or     PaymentControl <PmtCtrl> [1..1] CodeSet 3047
Or     Enquiry <Enqry> [1..1] CodeSet 3047
Or}     Proprietary <Prtry> [1..1] ± 3047
82.1.19.61.1  MessageIdentification <MsgId>
Presence: [1..1]
Definition: Point to point reference, as assigned by the sender, to unambiguously identify the message.
Usage: The sender has to make sure that MessageIdentification is unique for a pre-agreed period.
Datatype: "Max35Text" on page 3328
82.1.19.61.2  CreationDateTime <CreDtTm>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3046 August 2026
```

