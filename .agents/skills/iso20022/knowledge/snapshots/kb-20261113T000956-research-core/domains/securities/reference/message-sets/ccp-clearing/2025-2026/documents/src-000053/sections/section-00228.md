---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["10 MX secl.009.001.03 BuyInConfirmationV03", "10.4 Message Building Blocks"]
file_pages: [299]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.009.001.03"]
preceding_topic_continuations: [{"constraint_ids": ["C12", "C13"], "until_heading": "10.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 299, "topic": "10.3 Constraints", "reference_path": "domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00227.md"}]
---

# 10.4 Message Building Blocks

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 299 to 299.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 299, C12–C13 before **10.4 Message Building Blocks** continue [10.3 Constraints](section-00227.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 299

```text
C12 OtherIdentificationPresenceRule  '
(Rule)
If OtherIdentification is not present then either ISIN or Description must be
present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
C13 SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
10.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
10.4.1 TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: Max35Text on page 493
10.4.2 ClearingMember <ClrMmb>
Presence: [1..1]
Definition: Provides the identification of the clearing member (individual clearing member or general
clearing member).
ClearingMember <ClrMmb> contains one of the following elements (see PartyIdentification35Choice
on page 452 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C4 452
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 452
10.4.3 BuyInDetails <BuyInDtls>
Presence: [1..1]
Definition: Provides the buy-in details.
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.009.001.03 BuyInConfirmationV03
March 2026 299
```

