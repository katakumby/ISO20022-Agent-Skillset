---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.23 Identification Information", "66.1.23.17 IdentificationSource1Choice", "66.1.23.17.2 Proprietary <Prtry>"]
file_pages: [4551]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.23.17.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4551 to 4551.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4551

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.23.17.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Entity that issues the proprietary identification.
Datatype: "Max35Text" on page 5403
66.1.23.18  References64Choice
Definition: Choice of references used to reference a previous transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   RelatedReference <RltdRef> [1..2] ± 4551
Or}   OtherReference <OthrRef> [1..2] ± 4551
66.1.23.18.1  RelatedReference <RltdRef>
Presence: [1..2]
Definition: Reference to a linked message that was previously received.
RelatedReference <RltdRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
66.1.23.18.2  OtherReference <OthrRef>
Presence: [1..2]
Definition: Reference to a linked proprietary message or reference of a system that was previously
received.
OtherReference <OthrRef> contains the following elements (see "AdditionalReference10" on
page 4545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reference <Ref> [1..1] Text 4545
   ReferenceIssuer <RefIssr> [0..1] ± 4546
   MessageName <MsgNm> [0..1] Text 4546
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4551 May 2026
```

