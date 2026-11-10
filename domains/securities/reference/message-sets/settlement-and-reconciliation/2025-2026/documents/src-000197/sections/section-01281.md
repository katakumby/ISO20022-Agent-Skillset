---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.14 QuantityBreakdown63", "35.1.21.14.5 LotPrice <LotPric>"]
file_pages: [1738]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.14.5 LotPrice <LotPric>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1738 to 1738.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1738

```text
35.1.21.14.5  LotPrice <LotPric>
Presence: [0..1]
Definition: Price at which the lot was purchased.
LotPrice <LotPric> contains the following elements (see "Price7" on page 1715 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1] ± 1716
   Value <Val> [1..1] ± 1716
35.1.21.14.6  TypeOfPrice <TpOfPric>
Presence: [0..1]
Definition: Specifies the type of price and information about the price.
TypeOfPrice <TpOfPric> contains one of the following elements (see "TypeOfPrice29Choice" on
page 1711 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1711
Or}   Proprietary <Prtry> [1..1] ± 1711
35.1.21.15  QuantityAndAccount116
Definition: Details on a quantity, account and other related information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SettlementQuantity <SttlmQty> [1..1] ± C12 1739
   DenominationChoice <DnmtnChc> [0..1] Text 1739
   AccountOwner <AcctOwnr> [0..1] ± 1740
   SafekeepingAccount <SfkpgAcct> [0..1] ± 1740
   BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1740
   CashAccount <CshAcct> [0..1] ± 1740
   QuantityBreakdown <QtyBrkdwn> [0..*] ± 1741
   SafekeepingPlace <SfkpgPlc> [0..1] ± C33 1741
Constraints
• DenominationRule
Unless bilaterally agreed between the account owner and servicer, if DenominationChoice is used, it
must not contain information that can be provided in a structured field.
• SafekeepingAccountOrBlockChainAddress1Rule
If SafekeepingAccount is present, BlockChainAddressOrWallet must be absent.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1738 March 2026
```

