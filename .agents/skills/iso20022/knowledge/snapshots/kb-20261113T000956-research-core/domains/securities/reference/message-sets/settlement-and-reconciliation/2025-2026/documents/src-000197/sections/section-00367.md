---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["16 sese.022.001.08 SecuritiesStatusOrStatementQueryStatusAdviceV08", "17.4 Message Building Blocks", "17.4.17 OtherBusinessParties <OthrBizPties>", "17.4.17.2 QualifiedForeignIntermediary <QlfdFrgnIntrmy>"]
file_pages: [550]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.023.001.13"]
---

# 17.4.17.2 QualifiedForeignIntermediary <QlfdFrgnIntrmy>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 550 to 550.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 550

```text
Constraints
• IdentificationNationalityOfInvestorRule
Identification and/or Nationality must be present.
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
17.4.17.2  QualifiedForeignIntermediary <QlfdFrgnIntrmy>
Presence: [0..1]
Definition: Foreign financial institution which has been authorised by local authorities to act as account
management institution in the country.
Impacted by: C57 "SafekeepingAccountOrBlockChainAddress1Rule", C61
"SafekeepingAccountOrBlockChainAddress2Rule"
QualifiedForeignIntermediary <QlfdFrgnIntrmy> contains the following elements (see
"PartyIdentificationAndAccount198" on page 1684 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 1684
   LEI <LEI> [0..1] IdentifierSet 1685
   AlternateIdentification <AltrnId> [0..1] ± 1685
   SafekeepingAccount <SfkpgAcct> [0..1] Text 1685
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 1685
   ProcessingIdentification <PrcgId> [0..1] Text 1685
   AdditionalInformation <AddtlInf> [0..1] ± C5 1686
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Approved by the Securities SEG on 27 January 2026 sese.023.001.13
SecuritiesSettlementTransactionInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 550 March 2026
```

