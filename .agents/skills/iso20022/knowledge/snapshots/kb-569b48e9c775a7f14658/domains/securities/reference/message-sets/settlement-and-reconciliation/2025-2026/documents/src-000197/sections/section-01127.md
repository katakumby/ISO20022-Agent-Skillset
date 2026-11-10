---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.37 BlockChainAddressWallet3"]
file_pages: [1572]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.37 BlockChainAddressWallet3

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1572 to 1572.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1572

```text
• Meaning When True: Yes
• Meaning When False: No
35.1.16.37  BlockChainAddressWallet3
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
35.1.16.37.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: "Max140Text" on page 2191
35.1.16.37.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Type <Tp> contains the following elements (see "GenericIdentification30" on page 1502 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.37.3  Name <Nm>
Presence: [0..1]
Definition: Description of the account.
Datatype: "Max70Text" on page 2192
35.1.16.38  RepurchaseType23Choice
Definition: Choice of format for the repurchase transaction type information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1573
Or}   Proprietary <Prtry> [1..1] ± 1573
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1572 March 2026
```

