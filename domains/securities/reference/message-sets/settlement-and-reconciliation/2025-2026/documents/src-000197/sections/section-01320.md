---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.25 Settlement Chain", "35.1.25.5 SettlementParties128", "35.1.25.5.6 Party5 <Pty5>"]
file_pages: [1780]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.25.5.6 Party5 <Pty5>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1780 to 1780.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1780

```text
Party4 <Pty4> contains the following elements (see "PartyIdentificationAndAccount196" on page 1667
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1668
   LEI <LEI> [0..1] IdentifierSet 1668
   AlternateIdentification <AltrnId> [0..1] ± 1668
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1669
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1669
   ProcessingDate <PrcgDt> [0..1] ± 1669
   ProcessingIdentification <PrcgId> [0..1] Text 1669
   AdditionalInformation <AddtlInf> [0..1] ± C5 1669
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
35.1.25.5.6  Party5 <Pty5>
Presence: [0..1]
Definition: Party that, in a settlement chain interacts with the party 4.
Impacted by: C29 "SafekeepingAccountOrBlockChainAddress1Rule", C31
"SafekeepingAccountOrBlockChainAddress2Rule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1780 March 2026
```

