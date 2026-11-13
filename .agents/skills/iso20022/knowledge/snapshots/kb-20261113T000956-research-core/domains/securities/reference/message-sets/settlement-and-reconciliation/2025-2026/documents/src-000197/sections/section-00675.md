---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.6 QuantityAndAccountDetails <QtyAndAcctDtls>", "29.4.6.1 SettledQuantity <SttldQty>"]
file_pages: [1019]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.6.1 SettledQuantity <SttldQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1019 to 1019.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1019

```text
QuantityAndAccountDetails <QtyAndAcctDtls> contains the following QuantityAndAccount120
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettledQuantity <SttldQty> [1..1] ± 1019
   PreviouslySettledQuantity <PrevslySttldQty> [0..1] ± C20 1020
   RemainingToBeSettledQuantity <RmngToBeSttldQty> [0..1] ± C20 1020
   PreviouslySettledAmount <PrevslySttldAmt> [0..1] ± 1021
   RemainingToBeSettledAmount <RmngToBeSttldAmt> [0..1] ± 1021
   AccountOwner <AcctOwnr> [0..1] ± 1021
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1021
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1022
   CashAccount <CshAcct> [0..1] ± 1022
   SafekeepingPlace <SfkpgPlc> [0..1] ± C48 1022
Constraints
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
• SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
29.4.6.1  SettledQuantity <SttldQty>
Presence: [1..1]
Definition: Quantity of financial instrument effectively settled.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1019 March 2026
```

