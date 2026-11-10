---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["70 semt.025.001.01 SecuritiesAccountPositionQueryV01", "70.4 Message Building Blocks", "70.4.2 SearchCriteria <SchCrit>", "70.4.2.8 OtherBusinessParties <OthrBizPties>"]
file_pages: [2407]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 70.4.2.8 OtherBusinessParties <OthrBizPties>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2407 to 2407.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2407

```text
70.4.2.8  OtherBusinessParties <OthrBizPties>
Presence: [0..1]
Definition: Other business parties relevant to the transaction.
OtherBusinessParties <OthrBizPties> contains the following OtherParties46 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C6, C10,
C11
2407
70.4.2.8.1  Investor <Invstr>
Presence: [0..*]
Definition: Party, either an individual or organisation, whose assets are being invested.
Impacted by: C6 "IdentificationNationalityOfInvestorRule", C10
"SafekeepingAccountOrBlockChainAddress1Rule", C11
"SafekeepingAccountOrBlockChainAddress2Rule"
Investor <Invstr> contains the following elements (see "PartyIdentificationAndAccount197" on
page 3061 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 3061
   LEI <LEI> [0..1] IdentifierSet 3062
   AlternateIdentification <AltrnId> [0..1] ± 3062
   Nationality <Ntlty> [0..1] CodeSet C3 3062
   SafekeepingAccount <SfkpgAcct> [0..1] Text 3062
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 3062
   ProcessingIdentification <PrcgId> [0..1] Text 3062
   AdditionalInformation <AddtlInf> [0..1] ± C1 3063
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities 2407 August 2026
```

