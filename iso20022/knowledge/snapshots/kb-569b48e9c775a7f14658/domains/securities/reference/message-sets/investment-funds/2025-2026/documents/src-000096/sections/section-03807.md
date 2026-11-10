---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.32 Person Identification", "66.1.32.8 ContactIdentification2", "66.1.32.8.3 Name <Nm>"]
file_pages: [5096]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.32.8.3 Name <Nm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5096 to 5096.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5096

```text
66.1.32.8.3  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max35Text" on page 5403
66.1.32.8.4  PhoneNumber <PhneNb>
Presence: [0..1]
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: "PhoneNumber" on page 5405
66.1.32.8.5  MobileNumber <MobNb>
Presence: [0..1]
Definition: Collection of information that identifies a mobile phone number, as defined by telecom
services.
Datatype: "PhoneNumber" on page 5405
66.1.32.8.6  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: "PhoneNumber" on page 5405
66.1.32.8.7  EmailAddress <EmailAdr>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: "Max256Text" on page 5403
66.1.33 Postal Address
66.1.33.1  DeliveryParameters3
Definition: Parameters of a physical delivery.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Address <Adr> [1..1] ± 5096
   IssuedCertificateNumber <IssdCertNb> [0..1] Text 5097
66.1.33.1.1  Address <Adr>
Presence: [1..1]
Definition: Address for physical delivery.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5096 May 2026
```

