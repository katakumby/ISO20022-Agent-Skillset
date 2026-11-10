---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.20 Party Identification", "82.1.20.5 PartyIdentificationAndAccount197"]
file_pages: [3061]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.20.5 PartyIdentificationAndAccount197

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 3061 to 3061.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3061

```text
82.1.20.5  PartyIdentificationAndAccount197
Definition: Party and account details.
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
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
82.1.20.5.1  Identification <Id>
Presence: [0..1]
Definition: Identification of the party.
Identification <Id> contains one of the following elements (see "PartyIdentification120Choice" on
page 3079 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C2 3079
Or   ProprietaryIdentification <PrtryId> [1..1] ± 3079
Or}   NameAndAddress <NmAndAdr> [1..1] ± 3079
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 3061 August 2026
```

