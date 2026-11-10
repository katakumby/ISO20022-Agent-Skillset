---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.33 Postal Address", "66.1.33.7 DeliveryParameters4"]
file_pages: [5106]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.33.7 DeliveryParameters4

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 5106 to 5106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5106

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
66.1.33.7  DeliveryParameters4
Definition: Parameters of a physical delivery.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RegisteredAddressIndicator <RegdAdrInd> [1..1] Indicator 5106
   NameAndAddress <NmAndAdr> [0..1] ± 5106
   ContactPerson <CtctPrsn> [0..1] ± 5106
Constraints
• NameAndAddress1Rule
If RegisteredAddressIndicator is "true" or "1" (Yes), then NameAndAddress is not allowed.
If RegisteredAddressIndicator is "false" or "0" (No), then NameAndAddress must be present.
66.1.33.7.1  RegisteredAddressIndicator <RegdAdrInd>
Presence: [1..1]
Definition: Indicates whether the address for the physical delivery is the registered address.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.33.7.2  NameAndAddress <NmAndAdr>
Presence: [0..1]
Definition: Name and address to/from which the physical delivery/receipt of the financial instrument
must take place.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress4" on
page 5100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 5100
   Address <Adr> [1..1] ± 5100
66.1.33.7.3  ContactPerson <CtctPrsn>
Presence: [0..1]
Definition: Contact person and contact information.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5106 May 2026
```

