---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.9 Identification Information", "10.1.9.1 References80Choice", "10.1.9.1.9 TradeIdentification <TradId>"]
file_pages: [1183]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.9.1.9 TradeIdentification <TradId>

Source: [src-000163](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart2_PaymentsClearingandSettlement_2025_2026_v1.pdf). Locator: one-based file pages 1183 to 1183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1183

```text
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 1246
10.1.9.1.9  TradeIdentification <TradId>
Presence: [1..1]
Definition: Reference assigned to the trade by the investor or the trading party. This reference will be
used throughout the trade life cycle to access/update the trade details.
Datatype: "Max35Text" on page 1246
10.1.9.1.10  UniqueTransactionIdentifier <UnqTxIdr>
Presence: [1..1]
Definition: Unique Transaction Identifier (UTI) as agreed with the other counterparty.
Datatype: "UTIIdentifier" on page 1241
10.1.9.1.11  OtherTransactionIdentification <OthrTxId>
Presence: [1..1]
Definition: Identification of a transaction that cannot be identified using a standard reference element
present in the message.
Datatype: "Max35Text" on page 1246
10.1.9.2  PaymentIdentification13
Definition: Provides further means of referencing a payment transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   InstructionIdentification <InstrId> [0..1] Text 1183
   EndToEndIdentification <EndToEndId> [1..1] Text 1184
   TransactionIdentification <TxId> [0..1] Text 1184
   UETR <UETR> [0..1] IdentifierSet 1184
   ClearingSystemReference <ClrSysRef> [0..1] Text 1184
Constraints
• TransactionIdentificationPresenceRule
TransactionIdentification or UETR must be present. Both may be present
Following Must be True
    /TransactionIdentification Must be present
 Or    /UETR Must be present
10.1.9.2.1  InstructionIdentification <InstrId>
Presence: [0..1]
Definition: Unique identification, as assigned by an instructing party for an instructed party, to
unambiguously identify the instruction.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1183 March 2026
```

