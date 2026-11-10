---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09", "31.2 Structure"]
file_pages: [779]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.008.001.09"]
---

# 31.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 779 to 779.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 779

```text
H. MarketPracticeVersion
Identifies the market practice to which the message conforms.
I. CopyDetails
Information provided when the message is a copy of a previous message.
31.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RvslOfTrfInConf> [1..1]  
   MessageIdentification <MsgId> [1..1] ± 780
   PoolReference <PoolRef> [0..1] ± 780
   PreviousReference <PrvsRef> [0..1] ± 780
   RelatedReference <RltdRef> [0..1] ± 780
   MasterReference <MstrRef> [0..1] Text 781
   Function <Fctn> [0..1] CodeSet 781
   ReversalReferences <RvslRefs> [1..*]  781
     TransferReference <TrfRef> [1..1] Text 782
     ClientReference <ClntRef> [0..1] ± 782
     TransferConfirmationReference <TrfConfRef> [0..1] Text 782
     CounterpartyReference <CtrPtyRef> [0..1] ± 782
     CancellationReference <CxlRef> [0..1] Text 782
     ReversalReason <RvslRsn> [0..1] Text 783
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 783
   CopyDetails <CpyDtls> [0..1] ± 783
31.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
Approved by the Securities SEG on 27 January 2026 sese.008.001.09
ReversalOfTransferInConfirmationV09
Investment Funds - Maintenance 2025 - 2026 779 May 2026
```

