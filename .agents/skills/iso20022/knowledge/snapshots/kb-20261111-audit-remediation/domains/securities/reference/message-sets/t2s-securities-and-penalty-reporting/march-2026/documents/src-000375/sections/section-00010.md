---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["2 semt.025.001.01 SecuritiesAccountPositionQueryV01", "2.4 Message Building Blocks", "2.4.2 SearchCriteria <SchCrit>", "2.4.2.8 OtherBusinessParties <OthrBizPties>"]
file_pages: [11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.025.001.01"]
---

# 2.4.2.8 OtherBusinessParties <OthrBizPties>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 11 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 11

```text
2.4.2.8  OtherBusinessParties <OthrBizPties>
Presence: [0..1]
Definition: Other business parties relevant to the transaction.
OtherBusinessParties <OthrBizPties> contains the following OtherParties46 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Investor <Invstr> [0..*] ± C6, C10,
C11
11
2.4.2.8.1  Investor <Invstr>
Presence: [0..*]
Definition: Party, either an individual or organisation, whose assets are being invested.
Impacted by: C6 "IdentificationNationalityOfInvestorRule", C10
"SafekeepingAccountOrBlockChainAddress1Rule", C11
"SafekeepingAccountOrBlockChainAddress2Rule"
Investor <Invstr> contains the following elements (see "PartyIdentificationAndAccount197" on
page 414 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 415
   LEI <LEI> [0..1] IdentifierSet 415
   AlternateIdentification <AltrnId> [0..1] ± 415
   Nationality <Ntlty> [0..1] CodeSet C3 416
   SafekeepingAccount <SfkpgAcct> [0..1] Text 416
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 416
   ProcessingIdentification <PrcgId> [0..1] Text 416
   AdditionalInformation <AddtlInf> [0..1] ± C1 416
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
Approved by the Securities SEG 19 February 2026. semt.025.001.01
SecuritiesAccountPositionQueryV01
Target2-Securities - Securities and Penalty Reporting 11 March 2026
```

