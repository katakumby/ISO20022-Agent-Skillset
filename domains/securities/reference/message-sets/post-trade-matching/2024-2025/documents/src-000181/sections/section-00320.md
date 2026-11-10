---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.59 IdentificationReference16Choice"]
file_pages: [384]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.59 IdentificationReference16Choice

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 384 to 384.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 384

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.59  IdentificationReference16Choice
Definition: Unique identifier of a document, message or transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InstructingPartyTransactionIdentification <InstgPtyTxId> [1..1] Text 384
Or   ExecutingPartyTransactionIdentification <ExctgPtyTxId> [1..1] Text 385
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 385
Or   ClientOrderLinkIdentification <ClntOrdrLkId> [1..1] Text 385
Or   PoolIdentification <PoolId> [1..1] Text 385
Or   BlockIdentification <BlckId> [1..1] Text 385
Or   AllocationIdentification <AllcnId> [1..1] Text 385
Or   IndividualAllocationIdentification <IndvAllcnId> [1..1] Text 385
Or   SecondaryAllocationIdentification <ScndryAllcnId> [1..1] Text 386
Or   IndexIdentification <IndxId> [1..1] Text 386
Or   CommonIdentification <CmonId> [1..1] Text 386
Or   ComplianceIdentification <CmplcId> [1..1] Text 386
Or   CancellationRequestIdentification <CxlReqId> [1..1] Text 386
Or   CollateralTransactionIdentification <CollTxId> [1..1] Text 386
Or}   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 386
Constraints
• LinkedIdentificationGuideline
InstructingPartyTransactionIdentification, ExecutingPartyTransactionIdentification,
MarketInfrastructureTransactionIdentification, ClientOrderLinkIdentification, PoolIdentification,
BlockIdentification, AllocationIdentification, IndexIdentification, CommonIdentification,
ComplianceIdentification and CancellationRequestIdentification must not appear more than once in
the message.
7.1.19.59.1  InstructingPartyTransactionIdentification <InstgPtyTxId>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 384 February 2025
```

