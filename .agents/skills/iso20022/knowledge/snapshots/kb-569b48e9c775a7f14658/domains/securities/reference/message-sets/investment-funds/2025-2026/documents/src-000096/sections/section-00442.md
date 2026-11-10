---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "27.2 Structure"]
file_pages: [603]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.004.001.09"]
---

# 27.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 603 to 603.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 603

```text
Information provided when the message is a copy of a previous message.
27.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RvslOfTrfOutConf> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 603
   PoolReference <PoolRef> [0..1] ± 604
   PreviousReference <PrvsRef> [0..1] ± 604
   RelatedReference <RltdRef> [0..1] ± 604
   MasterReference <MstrRef> [0..1] Text 605
   ReversalReferences <RvslRefs> [1..*]  605
     TransferReference <TrfRef> [1..1] Text 605
     ClientReference <ClntRef> [0..1] ± 605
     TransferConfirmationReference <TrfConfRef> [0..1] Text 606
     CounterpartyReference <CtrPtyRef> [0..1] ± 606
     CancellationReference <CxlRef> [0..1] Text 606
     ReversalReason <RvslRsn> [0..1] Text 606
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 606
   CopyDetails <CpyDtls> [0..1] ± 607
27.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
27.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
27.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 sese.004.001.09
ReversalOfTransferOutConfirmationV09
Investment Funds - Maintenance 2025 - 2026 603 May 2026
```

