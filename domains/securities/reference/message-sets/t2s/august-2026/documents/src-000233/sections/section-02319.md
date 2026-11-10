---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.22 Postal Address", "82.1.22.6 PostalAddress3", "82.1.22.6.3 RegistrationAddressIndicator <RegnAdrInd>"]
file_pages: [3100]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.22.6.3 RegistrationAddressIndicator <RegnAdrInd>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 3100 to 3100.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3100

```text
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.22.6.3  RegistrationAddressIndicator <RegnAdrInd>
Presence: [1..1]
Definition: Indicates whether the address is the official address of the party.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 3323):
• Meaning When True: Yes
• Meaning When False: No
82.1.22.6.4  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress4" on
page 3097 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 3098
   Address <Adr> [1..1] ± 3098
82.1.22.7  CommunicationAddress3
Definition: Communication device number or electronic address used for communication.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 3100
   Phone <Phne> [0..1] Text 3100
   Mobile <Mob> [0..1] Text 3101
   FaxNumber <FaxNb> [0..1] Text 3101
   TelexAddress <TlxAdr> [0..1] Text 3101
   URLAddress <URLAdr> [0..1] Text 3101
82.1.22.7.1  Email <Email>
Presence: [0..1]
Definition: Address for electronic mail (e-mail).
Datatype: "Max256Text" on page 3327
82.1.22.7.2  Phone <Phne>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3100 August 2026
```

