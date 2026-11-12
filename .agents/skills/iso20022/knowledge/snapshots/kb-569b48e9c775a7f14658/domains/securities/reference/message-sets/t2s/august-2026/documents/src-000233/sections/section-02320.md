---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.22 Postal Address", "82.1.22.7 CommunicationAddress3", "82.1.22.7.3 Mobile <Mob>"]
file_pages: [3101]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.22.7.3 Mobile <Mob>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3101 to 3101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3101

```text
Definition: Collection of information that identifies a phone number, as defined by telecom services.
Datatype: "PhoneNumber" on page 3330
82.1.22.7.3  Mobile <Mob>
Presence: [0..1]
Definition: Collection of information that identifies a mobile phone number, as defined by telecom
services.
Datatype: "PhoneNumber" on page 3330
82.1.22.7.4  FaxNumber <FaxNb>
Presence: [0..1]
Definition: Collection of information that identifies a FAX number, as defined by telecom services.
Datatype: "PhoneNumber" on page 3330
82.1.22.7.5  TelexAddress <TlxAdr>
Presence: [0..1]
Definition: Address for a telex machine.
Datatype: "Max35Text" on page 3328
82.1.22.7.6  URLAddress <URLAdr>
Presence: [0..1]
Definition: Address for the Universal Resource Locator (URL), for example an address used over the
www (HTTP) service.
Datatype: "Max256Text" on page 3327
82.1.23 Price
82.1.23.1  Price7
Definition: Type and information about a price.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 3101
   Value <Val> [1..1] ± 3102
82.1.23.1.1  Type <Tp>
Presence: [1..1]
Definition: Specification of the price type.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3101 August 2026
```

