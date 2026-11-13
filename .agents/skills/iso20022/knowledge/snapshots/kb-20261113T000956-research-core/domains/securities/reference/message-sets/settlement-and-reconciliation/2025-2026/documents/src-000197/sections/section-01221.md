---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.10 Pledgee3", "35.1.18.10.2 LEI <LEI>"]
file_pages: [1678]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.10.2 LEI <LEI>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1678 to 1678.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1678

```text
35.1.18.10.2  LEI <LEI>
Presence: [0..1]
Definition: Legal entity identification as an alternate identification for a party.
Datatype: "LEIIdentifier" on page 2187
35.1.18.11  PartyIdentificationAndAccount199
Definition: Party and account details.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1678
   LEI <LEI> [0..1] IdentifierSet 1679
   AlternateIdentification <AltrnId> [0..1] ± 1679
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1679
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1679
   ProcessingDate <PrcgDt> [0..1] ± 1680
   ProcessingIdentification <PrcgId> [0..1] Text 1680
   AdditionalInformation <AddtlInf> [0..1] ± C5 1680
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
35.1.18.11.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1678 March 2026
```

