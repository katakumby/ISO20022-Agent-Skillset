---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.21 Quantity", "35.1.21.15 QuantityAndAccount116", "35.1.21.15.1 SettlementQuantity <SttlmQty>"]
file_pages: [1739]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.21.15.1 SettlementQuantity <SttlmQty>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1739 to 1739.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1739

```text
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
• SafekeepingPlaceRule
The SafekeepingPlace functionality in the settlement instructions is only to be used for global
custodians that allow their clients to specify where the securities are to be held, for example, in an
ICSD account versus an account at the local CSD.
35.1.21.15.1  SettlementQuantity <SttlmQty>
Presence: [1..1]
Definition: Total quantity of securities to be settled.
Impacted by: C12 "DigitalTokenUnitUsageRule"
SettlementQuantity <SttlmQty> contains one of the following elements (see
"FinancialInstrumentQuantity33Choice" on page 1726 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1726
Or   FaceAmount <FaceAmt> [1..1] Amount 1726
Or   AmortisedValue <AmtsdVal> [1..1] Amount 1726
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1727
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
35.1.21.15.2  DenominationChoice <DnmtnChc>
Presence: [0..1]
Definition: Denomination of the security to be received or delivered.
Datatype: "Max210Text" on page 2191
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1739 March 2026
```

