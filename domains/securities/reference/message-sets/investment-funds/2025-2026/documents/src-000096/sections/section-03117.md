---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.3 Address", "66.1.3.1 CommunicationAddress6", "66.1.3.1.1 AddressType <AdrTp>"]
file_pages: [4341]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.3.1.1 AddressType <AdrTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4341 to 4341.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4341

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AddressType <AdrTp> [0..1]  4341
{Or     Code <Cd> [1..1] CodeSet 4341
Or}     Proprietary <Prtry> [1..1] ± 4341
   Email <Email> [0..1] Text 4342
   Phone <Phne> [0..1] Text 4342
   Mobile <Mob> [0..1] Text 4342
   FaxNumber <FaxNb> [0..1] Text 4342
   TelexAddress <TlxAdr> [0..1] Text 4342
   URLAddress <URLAdr> [0..1] Text 4342
66.1.3.1.1  AddressType <AdrTp>
Presence: [0..1]
Definition: Type of communication address.
AddressType <AdrTp> contains one of the following AddressType1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4341
Or}   Proprietary <Prtry> [1..1] ± 4341
66.1.3.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Type expressed as a code.
Datatype: "AddressType1Code" on page 5276
CodeName Name Definition
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
66.1.3.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type expressed as a proprietary code.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4341 May 2026
```

