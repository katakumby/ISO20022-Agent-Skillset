---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.3 AccountsDetails <AcctsDtls>", "11.4.3.2 AccountsList <AcctsList>"]
file_pages: [711]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.3.2 AccountsList <AcctsList>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 711 to 711.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 711

```text
11.4.3.2  AccountsList <AcctsList>
Presence: [1..*]
Definition: Selected safekeeping accounts list to which the corporate action event applies.
Impacted by: C10 "SafekeepingAccountOrBlockChainAddress1Rule", C11
"SafekeepingAccountOrBlockChainAddress2Rule", C12
"SafekeepingAccountOrBlockChainAddress3Rule", C13 "SafekeepingPlaceRule"
AccountsList <AcctsList> contains the following AccountIdentification69 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [0..1] Text 711
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 712
   AccountOwner <AcctOwnr> [0..1] ± 712
   SafekeepingPlace <SfkpgPlc> [0..1] ± 712
Constraints
• SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
• SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
• SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
On Condition
    /SafekeepingAccount is present
Following Must be True
    /BlockChainAddressOrWallet Must be absent
• SafekeepingPlaceRule
The SafekeepingPlace is only to be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the local
CSD.
11.4.3.2.1  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account where financial instruments are maintained.
Datatype: "Max35Text" on page 1251
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 711 February 2026
```

