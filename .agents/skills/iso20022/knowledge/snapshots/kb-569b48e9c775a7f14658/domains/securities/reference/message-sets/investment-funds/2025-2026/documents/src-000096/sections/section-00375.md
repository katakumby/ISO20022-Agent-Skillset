---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "25.2 Structure"]
file_pages: [514]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.002.001.09"]
---

# 25.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 514 to 514.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 514

```text
Reference of the transfer to be cancelled.
G. MarketPracticeVersion
Identifies the market practice to which the message conforms.
H. CopyDetails
Information provided when the message is a copy of a previous message.
25.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TrfOutCxlReq> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 515
   PoolReference <PoolRef> [0..1] ± 515
   PreviousReference <PrvsRef> [0..1] ± 515
   RelatedReference <RltdRef> [0..1] ± 515
   MasterReference <MstrRef> [0..1] Text 516
   TransferReferences <TrfRefs> [1..*]  516
     TransferReference <TrfRef> [1..1] Text 516
     ClientReference <ClntRef> [0..1] ± 516
     CounterpartyReference <CtrPtyRef> [0..1] ± 517
     CancellationReference <CxlRef> [0..1] Text 517
     CancellationReason <CxlRsn> [0..1] Text 517
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 517
   CopyDetails <CpyDtls> [0..1] ± 518
25.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
25.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities SEG on 27 January 2026 sese.002.001.09
TransferOutCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 514 May 2026
```

