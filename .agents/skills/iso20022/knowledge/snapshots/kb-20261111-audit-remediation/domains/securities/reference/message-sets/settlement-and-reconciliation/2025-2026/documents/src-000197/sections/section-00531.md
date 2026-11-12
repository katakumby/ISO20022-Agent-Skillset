---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10", "24.4 Message Building Blocks", "24.4.5 AdditionalInformation <AddtlInf>", "24.4.5.12 ReceivingParty1 <RcvgPty1>"]
file_pages: [800]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.030.001.10"]
---

# 24.4.5.12 ReceivingParty1 <RcvgPty1>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 800 to 800.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 800

```text
DeliveringParty1 <DlvrgPty1> contains the following elements (see
"PartyIdentificationAndAccount195" on page 1681 for details)
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
24.4.5.12  ReceivingParty1 <RcvgPty1>
Presence: [0..1]
Definition: Party that, in a settlement chain, interacts with the depository.
Impacted by: C16 "SafekeepingAccountOrBlockChainAddress1Rule", C19
"SafekeepingAccountOrBlockChainAddress2Rule"
ReceivingParty1 <RcvgPty1> contains the following elements (see
"PartyIdentificationAndAccount195" on page 1681 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1681
   LEI <LEI> [0..1] IdentifierSet 1681
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1682
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1682
   ProcessingIdentification <PrcgId> [0..1] Text 1682
Approved by the Securities SEG on 27 January 2026 sese.030.001.10
SecuritiesSettlementConditionsModificationRequest
V10
Settlement And Reconciliation - Maintenance 2025 - 2026 800 March 2026
```

