---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "37.2 Structure"]
file_pages: [1303]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.014.001.09"]
---

# 37.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1303 to 1303.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1303

```text
F. TransferReferences
Reference of the portfolio transfer instruction to be cancelled.
G. MarketPracticeVersion
Identifies the market practice to which the message conforms.
37.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <PrtflTrfCxlReq> [1..1]  
   MessageReference <MsgRef> [1..1] ± 1304
   PoolReference <PoolRef> [0..1] ± 1304
   PreviousReference <PrvsRef> [0..1] ± 1304
   RelatedReference <RltdRef> [0..1] ± 1304
   MasterReference <MstrRef> [0..1] Text 1305
   TransferReferences <TrfRefs> [1..1]  1305
     TransferReference <TrfRef> [1..1] Text 1305
     ClientReference <ClntRef> [0..1] ± 1305
     CounterpartyReference <CtrPtyRef> [0..1] ± 1306
     TransferConfirmationReference <TrfConfRef> [0..1] Text 1306
     CancellationReference <CxlRef> [0..1] Text 1306
     CancellationReason <CxlRsn> [0..1] Text 1306
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 1306
37.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
37.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
Approved by the Securities SEG on 27 January 2026 sese.014.001.09
PortfolioTransferCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 1303 May 2026
```

