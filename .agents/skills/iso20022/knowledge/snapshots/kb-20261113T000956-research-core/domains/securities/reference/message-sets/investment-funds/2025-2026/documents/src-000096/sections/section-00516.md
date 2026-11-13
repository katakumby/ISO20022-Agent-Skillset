---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks"]
file_pages: [706]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
preceding_topic_continuations: [{"constraint_ids": ["C31", "C32", "C33", "C34", "C35"], "until_heading": "30.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 706, "topic": "30.3 Constraints", "reference_path": "domains/securities/reference/message-sets/investment-funds/2025-2026/documents/src-000096/sections/section-00515.md"}]
---

# 30.4 Message Building Blocks

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 706 to 706.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 706, C31–C35 before **30.4 Message Building Blocks** continue [30.3 Constraints](section-00515.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 706

```text
C31 PhysicalTransferDetails2Rule
If PhysicalTransfer is DEMT (Dematerialised), then PhysicalTransferDetails is not allowed.
C32 RequestedSettlementDateRule
Either TransferDetails/RequestedSettlementDate may be present in one or more occurrences
of TransferDetails or SettlementDetails/RequestedSettlementDate may be present, but not
both.
This constraint is defined at the MessageDefinition level.
C33 SettlementChainGuideline
SMPG recommends that at least three settlement parties be instructed in equity or fixed income
receive
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
C34 TotalUnitsNumberRule
TotalUnitsNumber must be the sum of all occurrences of UnitsDetails/UnitsNumber when
UnitsDetails is present.
C35 TransactionOverheadElementRule
One of the elements (TotalOverheadApplied, TotalFees, TotalTaxes,
CommercialAgreementReference, IndividualFee, IndividualTax) must be present.
30.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
30.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
MessageIdentification <MsgId> contains the following elements (see "MessageIdentification1" on
page 4548 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4548
   CreationDateTime <CreDtTm> [1..1] DateTime 4549
30.4.2 PoolReference <PoolRef>
Presence: [0..1]
Definition: Collective reference identifying a set of messages.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 706 May 2026
```

