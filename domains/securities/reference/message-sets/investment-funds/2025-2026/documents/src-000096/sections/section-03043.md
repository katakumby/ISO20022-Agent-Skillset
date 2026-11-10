---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["56 setr.016.001.05 OrderInstructionStatusReportV05", "59.2 Structure"]
file_pages: [4254]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.047.001.03"]
---

# 59.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4254 to 4254.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4254

```text
Information provided when the message is a copy of a previous message.
59.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SbcptOrdrConfCxlInstr> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 4255
   PreviousReference <PrvsRef> [0..*] ± 0
   RelatedReference <RltdRef> [0..1] ± 0
   AmendmentIndicator <AmdmntInd> [1..1] Indicator 0
   MasterReference <MstrRef> [0..1] Text 0
   OrderReferences <OrdrRefs> [1..*]  4256
     OrderReference <OrdrRef> [1..1] Text 4256
     ClientReference <ClntRef> [0..1] Text 4257
     DealReference <DealRef> [0..1] Text 4257
     NonceIdentification <NonceId> [0..1] Text 4257
     CancellationReference <CxlRef> [0..1] Text 4257
     CancellationReason <CxlRsn> [0..1] ± 4257
   CopyDetails <CpyDtls> [0..1] ± 4257
59.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
59.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
59.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 setr.047.001.03
SubscriptionOrderConfirmationCancellationInstructi
onV03
Investment Funds - Maintenance 2025 - 2026 4254 May 2026
```

