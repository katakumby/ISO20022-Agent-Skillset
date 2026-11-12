---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["19 sese.025.001.13 SecuritiesSettlementTransactionConfirmationV13", "19.4 Message Building Blocks", "19.4.16 OtherBusinessParties <OthrBizPties>", "19.4.16.2 QualifiedForeignIntermediary <QlfdFrgnIntrmy>"]
file_pages: [648]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.025.001.13"]
---

# 19.4.16.2 QualifiedForeignIntermediary <QlfdFrgnIntrmy>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 648 to 648.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 648

```text
Investor <Invstr> contains the following elements (see "PartyIdentificationAndAccount197" on
page 1672 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 1673
   LEI <LEI> [0..1] IdentifierSet 1673
   AlternateIdentification <AltrnId> [0..1] ± 1673
   Nationality <Ntlty> [0..1] CodeSet C7 1674
   SafekeepingAccount <SfkpgAcct> [0..1] Text 1674
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 1674
   ProcessingIdentification <PrcgId> [0..1] Text 1674
   AdditionalInformation <AddtlInf> [0..1] ± C5 1674
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
19.4.16.2  QualifiedForeignIntermediary <QlfdFrgnIntrmy>
Presence: [0..1]
Definition: Foreign financial institution which has been authorised by local authorities to act as account
management institution in the country.
Impacted by: C45 "SafekeepingAccountOrBlockChainAddress1Rule", C49
"SafekeepingAccountOrBlockChainAddress2Rule"
Approved by the Securities SEG on 27 January 2026 sese.025.001.13
SecuritiesSettlementTransactionConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 648 March 2026
```

