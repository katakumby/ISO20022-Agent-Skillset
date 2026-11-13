---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["61 setr.051.001.03 RedemptionOrderConfirmationCancellationInstructionV03", "61.2 Structure"]
file_pages: [4266]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.051.001.03"]
---

# 61.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4266 to 4266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4266

```text
Information provided when the message is a copy of a previous message.
61.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RedOrdrConfCxlInstr> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 4267
   PreviousReference <PrvsRef> [0..*] ± 0
   RelatedReference <RltdRef> [0..1] ± 0
   AmendmentIndicator <AmdmntInd> [1..1] Indicator 4268
   MasterReference <MstrRef> [0..1] Text 0
   OrderReferences <OrdrRefs> [1..*]  4268
     OrderReference <OrdrRef> [1..1] Text 4268
     ClientReference <ClntRef> [0..1] Text 4269
     DealReference <DealRef> [0..1] Text 4269
     NonceIdentification <NonceId> [0..1] Text 4269
     CancellationReference <CxlRef> [0..1] Text 4269
     CancellationReason <CxlRsn> [0..1] ± 4269
   CopyDetails <CpyDtls> [0..1] ± 4269
61.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
61.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
61.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.051.001.03
RedemptionOrderConfirmationCancellationInstructio
nV03
Investment Funds - Maintenance 2025 - 2026 4266 May 2026
```

