---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["29 sese.006.001.09 TransferInCancellationRequestV09", "29.2 Structure"]
file_pages: [690]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.006.001.09"]
---

# 29.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 690 to 690.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 690

```text
Function of the transfer-in, that is, whether the message is used as a request to cancel a previously
sent instruction or as a cancellation of a previously sent advice and request for information. The
absence of Function indicates the message is a request to cancel a previously sent instruction.
G. TransferReferences
Reference of the transfer to be cancelled.
H. MarketPracticeVersion
Identifies the market practice to which the message conforms.
I. CopyDetails
Information provided when the message is a copy of a previous message.
29.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <TrfInCxlReq> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 691
   PoolReference <PoolRef> [0..1] ± 691
   PreviousReference <PrvsRef> [0..1] ± 691
   RelatedReference <RltdRef> [0..1] ± 692
   MasterReference <MstrRef> [0..1] Text 692
   Function <Fctn> [0..1] CodeSet 692
   TransferReferences <TrfRefs> [1..*]  693
     TransferReference <TrfRef> [1..1] Text 693
     ClientReference <ClntRef> [0..1] ± 693
     CounterpartyReference <CtrPtyRef> [0..1] ± 693
     CancellationReference <CxlRef> [0..1] Text 694
     CancellationReason <CxlRsn> [0..1] Text 694
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 694
   CopyDetails <CpyDtls> [0..1] ± 694
Approved by the Securities SEG on 27 January 2026 sese.006.001.09
TransferInCancellationRequestV09
Investment Funds - Maintenance 2025 - 2026 690 May 2026
```

