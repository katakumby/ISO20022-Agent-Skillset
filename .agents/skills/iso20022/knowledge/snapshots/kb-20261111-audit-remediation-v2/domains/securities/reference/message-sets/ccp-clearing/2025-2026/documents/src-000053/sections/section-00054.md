---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["3 MX secl.002.001.05 TradeLegNotificationCancellationV05", "3.4 Message Building Blocks"]
file_pages: [74]
content_origin: "source-text-extraction"
mentioned_message_ids: ["secl.002.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C20"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 74, "topic": "3.3 Constraints", "reference_path": "domains/securities/reference/message-sets/ccp-clearing/2025-2026/documents/src-000053/sections/section-00053.md"}]
---

# 3.4 Message Building Blocks

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 74 to 74.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 74, C20 before **3.4 Message Building Blocks** continue [3.3 Constraints](section-00053.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 74

```text
Error handling:
– Error severity: Fatal
– Error Code: X00658
– Error Text: TradeIdentification Or TradeExecutionIdentification Or UniqueTradeIdentifier
Must be present.
C20 ValidationByTable
(Rule)
Must be a valid currency code which is registered with the ISO 4217 Maintenance Agency, and
consist of three contiguous letters. (Algorithm)
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 ClearingMember <ClrMmb>
Presence: [1..1]
Definition: Provides the identification of the account owner, that is the clearing member (individual
clearing member or general clearing member).
ClearingMember <ClrMmb> contains one of the following elements (see PartyIdentification253Choice
on page 453 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BIC <BIC> [1..1] IdentifierSet   'C3 453
Or}   ProprietaryIdentification <PrtryId> [1..1] ± 453
3.4.2 ClearingAccount <ClrAcct>
Presence: [1..1]
Definition: Identifies the clearing member account at the Central counterparty through which the trade
must be cleared.
ClearingAccount <ClrAcct> contains the following elements (see SecuritiesAccount18 on page 373
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 373
   Type <Tp> [1..1] CodeSet 373
   Name <Nm> [0..1] Text 373
3.4.3 DeliveryAccount <DlvryAcct>
Presence: [0..1]
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
MX secl.002.001.05
TradeLegNotificationCancellationV05
March 2026 74
```

