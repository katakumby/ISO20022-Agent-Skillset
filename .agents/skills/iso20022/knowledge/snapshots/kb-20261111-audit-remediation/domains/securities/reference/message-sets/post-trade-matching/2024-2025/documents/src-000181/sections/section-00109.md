---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "4.4 Message Building Blocks"]
file_pages: [142]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.029.001.02"]
---

# 4.4 Message Building Blocks

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 142 to 142.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 142

```text
C7 LinkedIdentificationGuideline
InstructingPartyTransactionIdentification, ExecutingPartyTransactionIdentification,
MarketInfrastructureTransactionIdentification, ClientOrderLinkIdentification, PoolIdentification,
BlockIdentification, AllocationIdentification, IndexIdentification, CommonIdentification and
ComplianceIdentification must not appear more than once in the message.
C8 QualifiedForeignIntermediaryRule
If Qualified Foreign Intermediary is used, then the instruction must be a delivery.
C9 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C10 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 Identification <Id>
Presence: [1..1]
Definition: Information that unambiguously identifies an SecuritiesTradeConfirmationCancellation
message as known by the account owner (or the instructing party acting on its behalf).
Identification <Id> contains the following TransactiontIdentification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 142
4.4.1.1  TransactionIdentification <TxId>
Presence: [1..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: "Max35Text" on page 669
4.4.2 References <Refs>
Presence: [0..*]
Definition: Link to another transaction that must be processed after, before or at the same time.
References <Refs> contains the following elements (see "Linkages52" on page 294 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageNumber <MsgNb> [0..1] ± C9 294
   Reference <Ref> [1..1] ± C7 295
Approved by the Securities SEG on 13 February 2025 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Post Trade Matching - Maintenance 2024 - 2025 142 February 2025
```

