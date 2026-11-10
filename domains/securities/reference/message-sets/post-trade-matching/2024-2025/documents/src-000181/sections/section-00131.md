---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.1 Identification <Id>", "6.4.1.1 TransactionIdentification <TxId>"]
file_pages: [171]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.1.1 TransactionIdentification <TxId>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 171 to 171.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 171

```text
Definition: Information that unambiguously identifies an SecuritiesTradeConfirmationStatusAdvice
message as known by the account owner (or the instructing party acting on its behalf).
Identification <Id> contains the following TransactiontIdentification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 171
6.4.1.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: "Max35Text" on page 669
6.4.2 References <Refs>
Presence: [1..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
References <Refs> contains the following Linkages77 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNumber <MsgNb> [0..1] ± C35 171
   Reference <Ref> [1..1] ± C22 172
6.4.2.1  MessageNumber <MsgNb>
Presence: [0..1]
Definition: Message type number/message identifier of the message referenced in the linkage
sequence.
Impacted by: C35 "ShortLongNumberRule"
MessageNumber <MsgNb> contains one of the following elements (see "DocumentNumber17Choice"
on page 269 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ShortNumber <ShrtNb> [1..1] Text 269
Or   LongNumber <LngNb> [1..1] Text 269
Or}   ProprietaryNumber <PrtryNb> [1..1] ± 269
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 171 February 2025
```

