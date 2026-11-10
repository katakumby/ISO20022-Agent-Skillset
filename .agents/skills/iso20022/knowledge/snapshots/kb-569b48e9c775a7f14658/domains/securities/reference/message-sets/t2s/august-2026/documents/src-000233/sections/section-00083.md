---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02", "8.4 Message Building Blocks", "8.4.6 CashAccountOwner <CshAcctOwnr>"]
file_pages: [123]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.067.001.02"]
---

# 8.4.6 CashAccountOwner <CshAcctOwnr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 123 to 123.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 123

```text
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
8.4.6 CashAccountOwner <CshAcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the cash account.
CashAccountOwner <CshAcctOwnr> contains the following elements (see
"SystemPartyIdentification8" on page 3078 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 3078
   ResponsiblePartyIdentification <RspnsblPtyId> [0..1] ± 3078
8.4.7 CashAccountServicer <CshAcctSvcr>
Presence: [0..1]
Definition: Party that manages the cash account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.067.001.02
IntraBalanceMovementStatusAdviceV02
Target2-Securities 123 August 2026
```

