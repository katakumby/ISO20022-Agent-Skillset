---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.33 Postal Address", "66.1.33.6 PostalAddress21", "66.1.33.6.1 AddressType <AdrTp>", "66.1.33.6.1.1 Code <Cd>"]
file_pages: [5103]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.33.6.1.1 Code <Cd>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5103 to 5103.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5103

```text
66.1.33.6.1.1  Code <Cd>
Presence: [1..1]
Definition: Type of address expressed as a code.
Datatype: "AddressType2Code" on page 5276
CodeName Name Definition
ADDR Postal Address is the complete postal address.
PBOX POBox Address is a postal office (PO) box.
HOME Residential Address is the home address.
BIZZ Business Address is the business address.
MLTO MailTo Address is the address to which mail is
sent.
DLVY DeliveryTo Address is the address to which delivery
is to take place.
66.1.33.6.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of address expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.33.6.2  MailingIndicator <MlngInd>
Presence: [0..1]
Definition: Indicates whether mail should be sent to the address.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.33.6.3  RegistrationAddressIndicator <RegnAdrInd>
Presence: [0..1]
Definition: Indicates whether the address is the official address of the party.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5103 May 2026
```

