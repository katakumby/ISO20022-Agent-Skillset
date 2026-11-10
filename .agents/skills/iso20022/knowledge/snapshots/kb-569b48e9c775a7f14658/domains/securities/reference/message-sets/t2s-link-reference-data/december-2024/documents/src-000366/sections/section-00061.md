---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
source_ids: ["src-000366"]
source_editions: ["december-2024"]
message_ids: []
heading_path: ["8 Message Items Types", "8.1 MessageComponents", "8.1.6 Miscellaneous"]
file_pages: [65]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 8.1.6 Miscellaneous

Source: [src-000366](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LinkReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_LinkReferenceData_v1.pdf`. Locator: one-based file pages 65 to 65.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 65

```text
Datatype: "Max35Text" on page 78
8.1.6 Miscellaneous
8.1.6.1  BlockChainAddressWallet3
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 65
   Type <Tp> [0..1] ± 65
   Name <Nm> [0..1] Text 65
8.1.6.1.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: "Max140Text" on page 77
8.1.6.1.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 63 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 63
   Issuer <Issr> [1..1] Text 63
   SchemeName <SchmeNm> [0..1] Text 63
8.1.6.1.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: "Max70Text" on page 79
8.1.6.2  MessageHeader1
Definition: Set of characteristics, such as the identification or the creation date and time, specific to the
message.
Approved by the Securities SEG on 21 November 2024. Message Items Types
Target2-Securities - Link Reference Data 65 December 2024
```

