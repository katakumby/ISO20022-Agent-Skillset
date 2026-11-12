---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.25 Settlement Chain", "35.1.25.1 SettlementParties125", "35.1.25.1.5 Party4 <Pty4>"]
file_pages: [1754]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.25.1.5 Party4 <Pty4>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1754 to 1754.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1754

```text
Party3 <Pty3> contains the following elements (see "PartyIdentificationAndAccount195" on page 1681
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1681
   LEI <LEI> [0..1] IdentifierSet 1681
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1682
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1682
   ProcessingIdentification <PrcgId> [0..1] Text 1682
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present, SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
35.1.25.1.5  Party4 <Pty4>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 3.
Impacted by: C18 "SafekeepingAccountOrBlockChainAddress1Rule", C20
"SafekeepingAccountOrBlockChainAddress2Rule"
Party4 <Pty4> contains the following elements (see "PartyIdentificationAndAccount195" on page 1681
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1681
   LEI <LEI> [0..1] IdentifierSet 1681
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1682
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1682
   ProcessingIdentification <PrcgId> [0..1] Text 1682
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1754 March 2026
```

