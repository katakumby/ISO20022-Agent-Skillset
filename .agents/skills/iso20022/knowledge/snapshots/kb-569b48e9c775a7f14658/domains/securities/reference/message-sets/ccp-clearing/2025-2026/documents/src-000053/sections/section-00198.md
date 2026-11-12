---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["8 MX secl.007.001.03 BuyInNotificationV03", "8.4 Message Building Blocks"]
file_pages: [259]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.007.001.03"]
---

# 8.4 Message Building Blocks

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 259 to 259.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 259

```text
C13 OtherIdentificationPresenceRule  '
(Rule)
If OtherIdentification is not present then either ISIN or Description must be
present. (CrossElementComplexRule)
Error handling:
– Error severity: Fatal
– Error Code: X00193
– Error Text: At least one identification must be present.
C14 SupplementaryDataRule
(Rule)
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C15 TransactionIdentificationPresenceRule  '
(Rule)
If NotificationDetails/WarningIndicator is "false" or "0" (No), then TransactionIdentification must
be present. (CrossElementComplexRule)
On Condition
    /NotificationDetails/WarningIndicator is equal to value 'false'
Following Must be True
    /TransactionIdentification Must be present
Error handling:
– Error severity: Fatal
– Error Code: X00361
– Error Text: TransactionIdentification must be present.
This constraint is defined at the MessageDefinition level.
8.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
8.4.1 TransactionIdentification <TxId>
Presence: [0..1]
Definition: Unambiguous identification of the transaction as known by the instructing party.
Datatype: Max35Text on page 493
8.4.2 ClearingMember <ClrMmb>
Presence: [1..1]
Definition: Provides the identification of the clearing member (individual clearing member or general
clearing member).
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.007.001.03 BuyInNotificationV03
March 2026 259
```

