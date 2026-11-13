---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "45.2 Structure"]
file_pages: [2306]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.005.001.05"]
---

# 45.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2306 to 2306.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2306

```text
45.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RedOrdrCxlReq> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..1] ± 2307
   MasterReference <MstrRef> [0..1] Text 0
   OrderReferences <OrdrRefs> [1..*]  2307
     OrderReference <OrdrRef> [1..1] Text 2308
     ClientReference <ClntRef> [0..1] Text 2308
     NonceIdentification <NonceId> [0..1] Text 2308
     CancellationReference <CxlRef> [0..1] Text 2308
     CancellationReason <CxlRsn> [0..1] ± 2308
   CopyDetails <CpyDtls> [0..1] ± 0
45.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
45.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
45.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
Approved by the Securities SEG on 27 January 2026 setr.005.001.05
RedemptionOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 2306 May 2026
```

