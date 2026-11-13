---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.19 Miscellaneous", "82.1.19.33 BlockChainAddressWallet3"]
file_pages: [3016]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.19.33 BlockChainAddressWallet3

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3016 to 3016.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3016

```text
Constraints
• EventTypeRule
The use of a specific corporate action event type code is allowed only if this specific event triggers a
securities movement as per the Event Interpretation Grid published by the Securities Market Practice
Group (SMPG).
The corporate action event indicator code OTHR must only be used in case no other corporate
action event code is appropriate.
The corporate action event indicator code CHAN must only be used in case no other corporate
action event code is appropriate and only for an event which relates to a change.
The corporate action event indicator code REDM must only be used when the redemption is decided
by the issuer and not by the holders.
82.1.19.33  BlockChainAddressWallet3
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 3016
   Type <Tp> [0..1] ± 3016
   Name <Nm> [0..1] Text 3016
82.1.19.33.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: "Max140Text" on page 3326
82.1.19.33.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 2966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 2967
   Issuer <Issr> [1..1] Text 2967
   SchemeName <SchmeNm> [0..1] Text 2967
82.1.19.33.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3016 August 2026
```

