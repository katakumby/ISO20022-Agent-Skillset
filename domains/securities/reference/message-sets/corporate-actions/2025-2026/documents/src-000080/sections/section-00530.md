---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["10 seev.038.001.09 CorporateActionNarrativeV09", "10.4 Message Building Blocks", "10.4.1 AccountDetails <AcctDtls>", "10.4.1.1 ForAllAccounts <ForAllAccts>"]
file_pages: [695]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.038.001.09"]
---

# 10.4.1.1 ForAllAccounts <ForAllAccts>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 695 to 695.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 695

```text
AccountDetails <AcctDtls> contains one of the following AccountIdentification72Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ForAllAccounts <ForAllAccts> [1..1] ± 695
Or}   AccountsListAndBalanceDetails
<AcctsListAndBalDtls>
[1..*]  C10,
C11,
C12,
C13
695
     SafekeepingAccount <SfkpgAcct> [0..1] Text 696
     BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 696
     AccountOwner <AcctOwnr> [0..1] ± 696
     SafekeepingPlace <SfkpgPlc> [0..1] ± 697
     ConfirmedBalance <ConfdBal> [1..1] ± 697
10.4.1.1  ForAllAccounts <ForAllAccts>
Presence: [1..1]
Definition: All safekeeping accounts that own underlying financial instrument.
ForAllAccounts <ForAllAccts> contains the following elements (see "AccountIdentification10" on
page 830 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationCode <IdCd> [1..1] CodeSet 830
10.4.1.2  AccountsListAndBalanceDetails <AcctsListAndBalDtls>
Presence: [1..*]
Definition: Selected safekeeping accounts list (and optionally balance information) to which the
corporate action event applies.
Impacted by: C10 "SafekeepingAccountOrBlockChainAddress1Rule", C11
"SafekeepingAccountOrBlockChainAddress2Rule", C12
"SafekeepingAccountOrBlockChainAddress3Rule", C13 "SafekeepingPlaceRule"
AccountsListAndBalanceDetails <AcctsListAndBalDtls> contains the following
AccountIdentification71 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [0..1] Text 696
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 696
   AccountOwner <AcctOwnr> [0..1] ± 696
   SafekeepingPlace <SfkpgPlc> [0..1] ± 697
   ConfirmedBalance <ConfdBal> [1..1] ± 697
Approved by the Securities SEG on 27 January 2026 seev.038.001.09 CorporateActionNarrativeV09
Corporate Actions - Maintenance 2025 - 2026 695 February 2026
```

