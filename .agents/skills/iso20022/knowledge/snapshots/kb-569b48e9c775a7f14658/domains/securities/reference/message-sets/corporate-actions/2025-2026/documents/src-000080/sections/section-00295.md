---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.11 AccountDetails <AcctDtls>", "7.4.11.2 AccountsListAndBalanceDetails <AcctsListAndBalDtls>", "7.4.11.2.1 SafekeepingAccount <SfkpgAcct>"]
file_pages: [406]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.11.2.1 SafekeepingAccount <SfkpgAcct>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 406 to 406.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 406

```text
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
7.4.11.2.1  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account where financial instruments are maintained.
Datatype: "Max35Text" on page 1251
7.4.11.2.2  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Datatype: "Max140Text" on page 1249
7.4.11.2.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains one of the following elements (see
"PartyIdentification127Choice" on page 1037 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C1 1038
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 1038
7.4.11.2.4  SafekeepingPlace <SfkpgPlc>
Presence: [0..1]
Definition: Location where the financial instruments are/will be safekept.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 406 February 2026
```

