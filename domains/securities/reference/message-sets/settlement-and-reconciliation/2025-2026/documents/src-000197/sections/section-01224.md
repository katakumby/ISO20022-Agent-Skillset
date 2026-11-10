---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.18 Party Identification", "35.1.18.12 PartyIdentificationAndAccount195"]
file_pages: [1681]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.18.12 PartyIdentificationAndAccount195

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1681 to 1681.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1681

```text
Constraints
• AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails, RegistrationDetails
and PartyContactDetails must not contain information that can be provided in a structured field.
35.1.18.12  PartyIdentificationAndAccount195
Definition: Party and account details.
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
35.1.18.12.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 1689 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C5 1689
Or   ProprietaryIdentification <PrtryId> [1..1] ± 1689
Or}   NameAndAddress <NmAndAdr> [1..1] ± 1690
35.1.18.12.2  LEI <LEI>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1681 March 2026
```

