---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10", "24.4 Message Building Blocks", "24.4.7 AccountDetails <AcctDtls>", "24.4.8.2 TransfereeRegisteredAccount <TrfeeRegdAcct>", "24.4.8.2.6 BlockChainAddressOrWallet <BlckChainAdrOrWllt>"]
file_pages: [499]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24.4.8.2.6 BlockChainAddressOrWallet <BlckChainAdrOrWllt>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 499 to 499.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 499

```text
Definition: Sub-accounts that are grouped in a master or omnibus account.
SubAccountDetails <SubAcctDtls> contains the following elements (see "SubAccount5" on page 4329
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4329
   Name <Nm> [0..1] Text 4329
   Characteristic <Chrtc> [0..1] Text 4329
24.4.8.2.6  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Digital account where digital assets or digital tokens can be stored and where an entry is
made.
BlockChainAddressOrWallet <BlckChainAdrOrWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 4846 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4846
   Type <Tp> [0..1] ± 4846
   Name <Nm> [0..1] Text 4846
24.4.8.3  IntermediaryInformation <IntrmyInf>
Presence: [0..*]
Definition: Identification of a related party or intermediary.
IntermediaryInformation <IntrmyInf> contains the following elements (see "Intermediary43" on
page 5040 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 5040
   Account <Acct> [0..1]  5041
     Identification <Id> [0..1] Text 5041
     AccountServicer <AcctSvcr> [1..1] ± 5041
   Role <Role> [0..1] ± 5041
   ContactPerson <CtctPrsn> [0..1] ± 5041
24.4.8.4  SecuritiesForm <SctiesForm>
Presence: [0..1]
Definition: Form, that is, ownership, of the security, that is, registered or bearer.
Datatype: "FormOfSecurity1Code" on page 5304
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 499 May 2026
```

