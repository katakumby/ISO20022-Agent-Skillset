---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.9 Linkages52", "7.1.19.9.2 Reference <Ref>"]
file_pages: [295]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.9.2 Reference <Ref>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 295 to 295.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 295

```text
Constraints
• ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber must
contain the XML message identifier of the linked message.
7.1.19.9.2  Reference <Ref>
Presence: [1..1]
Definition: Reference to the linked transaction.
Impacted by: C7 "LinkedIdentificationGuideline"
Reference <Ref> contains one of the following elements (see "IdentificationReference8Choice" on
page 313 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   InstructingPartyTransactionIdentification <InstgPtyTxId> [1..1] Text 314
Or   ExecutingPartyTransactionIdentification <ExctgPtyTxId> [1..1] Text 314
Or   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[1..1] Text 314
Or   ClientOrderLinkIdentification <ClntOrdrLkId> [1..1] Text 315
Or   PoolIdentification <PoolId> [1..1] Text 315
Or   BlockIdentification <BlckId> [1..1] Text 315
Or   AllocationIdentification <AllcnId> [1..1] Text 315
Or   IndividualAllocationIdentification <IndvAllcnId> [1..1] Text 315
Or   SecondaryAllocationIdentification <ScndryAllcnId> [1..1] Text 315
Or   IndexIdentification <IndxId> [1..1] Text 315
Or   CommonIdentification <CmonId> [1..1] Text 316
Or   ComplianceIdentification <CmplcId> [1..1] Text 316
Or}   CollateralTransactionIdentification <CollTxId> [1..1] Text 316
Constraints
• LinkedIdentificationGuideline
InstructingPartyTransactionIdentification, ExecutingPartyTransactionIdentification,
MarketInfrastructureTransactionIdentification, ClientOrderLinkIdentification, PoolIdentification,
BlockIdentification, AllocationIdentification, IndexIdentification, CommonIdentification and
ComplianceIdentification must not appear more than once in the message.
7.1.19.10  StandingSettlementInstruction13
Definition: Details of the standing settlement instruction to be applied.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 295 February 2025
```

