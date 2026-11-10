---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.16 QuantityAndAccount118", "35.1.21.16.5 QuantityBreakdown <QtyBrkdwn>"]
file_pages: [1744]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.16.5 QuantityBreakdown <QtyBrkdwn>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1744 to 1744.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1744

```text
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
35.1.21.16.5  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of a quantity into lots such as tax lots, instrument series.
QuantityBreakdown <QtyBrkdwn> contains the following elements (see "QuantityBreakdown62" on
page 1733 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   LotNumber <LotNb> [0..1] ± 1733
   LotQuantity <LotQty> [0..1] ± C12 1734
   LotDateTime <LotDtTm> [0..1] ± 1734
   LotPrice <LotPric> [0..1] ± 1734
   TypeOfPrice <TpOfPric> [0..1] ± 1735
35.1.21.17  QuantityAndAccount119
Definition: Details on a quantity, account and other related information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [1..1] ± C12 1745
   AccountOwner <AcctOwnr> [0..1] ± 1745
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1745
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1746
   CashAccount <CshAcct> [0..1] ± 1746
   SafekeepingPlace <SfkpgPlc> [0..1] ± C33 1746
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1744 March 2026
```

