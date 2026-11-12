---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 semt.015.001.10 IntraPositionMovementConfirmationV10", "6.4 Message Building Blocks", "6.4.3 AccountOwner <AcctOwnr>"]
file_pages: [168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.015.001.10"]
---

# 6.4.3 AccountOwner <AcctOwnr>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 168 to 168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 168

```text
Definition: Unambiguous identification of a securities settlement transaction as known by the account
owner (or instructing party acting on its behalf).
Datatype: "Max35Text" on page 2192
6.4.3 AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 1664 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1664
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1665
6.4.4 SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account to or from which a securities entry is made.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 1340 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1341
   Type <Tp> [0..1] ± 1341
   Name <Nm> [0..1] Text 1341
6.4.5 BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 1572 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1572
   Type <Tp> [0..1] ± 1572
   Name <Nm> [0..1] Text 1572
6.4.6 SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 semt.015.001.10
IntraPositionMovementConfirmationV10
Settlement And Reconciliation - Maintenance 2025 - 2026 168 March 2026
```

