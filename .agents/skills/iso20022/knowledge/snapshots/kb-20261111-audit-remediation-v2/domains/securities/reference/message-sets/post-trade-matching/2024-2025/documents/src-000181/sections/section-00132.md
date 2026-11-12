---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["6 setr.044.001.04 SecuritiesTradeConfirmationStatusAdviceV04", "6.4 Message Building Blocks", "6.4.2 References <Refs>", "6.4.2.2 Reference <Ref>"]
file_pages: [172]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.044.001.04"]
---

# 6.4.2.2 Reference <Ref>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 172 to 172.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 172

```text
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
6.4.2.2  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Impacted by: C22 "LinkedIdentificationGuideline"
Reference <Ref> contains one of the following elements (see "IdentificationReference16Choice" on
page 384 for details)
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
Approved by the Securities SEG on 13 February 2025 setr.044.001.04
SecuritiesTradeConfirmationStatusAdviceV04
Post Trade Matching - Maintenance 2024 - 2025 172 February 2025
```

