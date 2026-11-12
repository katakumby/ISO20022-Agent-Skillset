---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "54.2 Structure"]
file_pages: [3798]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.014.001.05"]
---

# 54.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3798 to 3798.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3798

```text
54.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SwtchOrdrCxlReq> [1..1]  C3
   MessageIdentification <MsgId> [1..1] ± 0
   PoolReference <PoolRef> [0..1] ± 0
   PreviousReference <PrvsRef> [0..1] ± 3799
   MasterReference <MstrRef> [0..1] Text 0
   OrderReferences <OrdrRefs> [1..*]  3799
     OrderReference <OrdrRef> [1..1] Text 3800
     ClientReference <ClntRef> [0..1] Text 3800
     NonceIdentification <NonceId> [0..1] Text 3800
     CancellationReference <CxlRef> [0..1] Text 3800
     CancellationReason <CxlRsn> [0..1] ± 3800
   CopyDetails <CpyDtls> [0..1] ± 3801
54.3 Constraints
C1 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 SwitchRule
The cancellation of a switch order must be a full cancellation. Partial cancellations are not
allowed, for example, the cancellation of a given leg.
This constraint is defined at the MessageDefinition level.
54.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
54.4.1 MessageIdentification <MsgId>
Presence: [1..1]
Definition: Reference that uniquely identifies the message from a business application standpoint.
Approved by the Securities SEG on 27 January 2026 setr.014.001.05
SwitchOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 3798 May 2026
```

