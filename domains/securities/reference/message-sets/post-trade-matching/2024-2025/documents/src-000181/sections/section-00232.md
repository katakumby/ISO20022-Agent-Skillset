---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.1 Linkages76", "7.1.19.1.2 Reference <Ref>"]
file_pages: [286]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.1.2 Reference <Ref>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 286 to 286.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 286

```text
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
7.1.19.1.2  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Impacted by: C7 "LinkedIdentificationGuideline"
Reference <Ref> contains one of the following elements (see "IdentificationReference15Choice" on
page 386 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InstructingPartyTransactionIdentification <InstgPtyTxId> [1..1] Text 387
Or   ExecutingPartyTransactionIdentification <ExctgPtyTxId> [1..1] Text 387
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 387
Or   ClientOrderLinkIdentification <ClntOrdrLkId> [1..1] Text 388
Or   PoolIdentification <PoolId> [1..1] Text 388
Or   BlockIdentification <BlckId> [1..1] Text 388
Or   AllocationIdentification <AllcnId> [1..1] Text 388
Or   IndividualAllocationIdentification <IndvAllcnId> [1..1] Text 388
Or   SecondaryAllocationIdentification <ScndryAllcnId> [1..1] Text 388
Or   IndexIdentification <IndxId> [1..1] Text 388
Or   CommonIdentification <CmonId> [1..1] Text 389
Or   ComplianceIdentification <CmplcId> [1..1] Text 389
Or   CollateralTransactionIdentification <CollTxId> [1..1] Text 389
Or}   UniqueTransactionIdentifier <UnqTxIdr> [1..1] IdentifierSet 389
Constraints
• LinkedIdentificationGuideline
InstructingPartyTransactionIdentification, ExecutingPartyTransactionIdentification,
MarketInfrastructureTransactionIdentification, ClientOrderLinkIdentification, PoolIdentification,
BlockIdentification, AllocationIdentification, IndexIdentification, CommonIdentification and
ComplianceIdentification must not appear more than once in the message.
7.1.19.2  SettlementSystemMethod4Choice
Definition: Choice of format for the settlement system/method.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 286 February 2025
```

