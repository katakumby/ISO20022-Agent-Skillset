---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["9 seev.037.001.17 CorporateActionMovementReversalAdviceV17", "9.4 Message Building Blocks", "9.4.7 AccountDetails <AcctDtls>", "9.4.7.1 SafekeepingAccount <SfkpgAcct>"]
file_pages: [678]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.037.001.17"]
---

# 9.4.7.1 SafekeepingAccount <SfkpgAcct>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 678 to 678.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 678

```text
Impacted by: C19 "SafekeepingAccountOrBlockChainAddress1Rule", C20
"SafekeepingAccountOrBlockChainAddress2Rule", C21
"SafekeepingAccountOrBlockChainAddress3Rule"
AccountDetails <AcctDtls> contains the following AccountAndBalance50 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingAccount <SfkpgAcct> [0..1] Text 678
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] Text 678
   ConfirmedBalance <ConfdBal> [1..1] ± 678
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
9.4.7.1  SafekeepingAccount <SfkpgAcct>
Presence: [0..1]
Definition: Account where financial instruments are maintained.
Datatype: "Max35Text" on page 1251
9.4.7.2  BlockChainAddressOrWallet <BlckChainAdrOrWllt>
Presence: [0..1]
Definition: Blockchain address or wallet where digital assets are maintained. This is the equivalent of
safekeeping account for digital assets.
Datatype: "Max140Text" on page 1249
9.4.7.3  ConfirmedBalance <ConfdBal>
Presence: [1..1]
Definition: Balance to which the payment applies (less or equal to the total eligible balance).
Approved by the Securities SEG on 27 January 2026 seev.037.001.17
CorporateActionMovementReversalAdviceV17
Corporate Actions - Maintenance 2025 - 2026 678 February 2026
```

