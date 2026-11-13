---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks"]
file_pages: [45]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
preceding_topic_continuations: [{"constraint_ids": ["C47", "C48", "C49", "C50", "C51"], "until_heading": "3.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 45, "topic": "3.3 Constraints", "reference_path": "domains/securities/reference/message-sets/post-trade-matching/2024-2025/documents/src-000181/sections/section-00027.md"}]
---

# 3.4 Message Building Blocks

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 45 to 45.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 45, C47–C51 before **3.4 Message Building Blocks** continue [3.3 Constraints](section-00027.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 45

```text
The use of SecuritiesTransactionTypes OWNI, OWNE, INSP and PORT and other booktransfer
related fields is governed by a market practice document.
• Block Trades:
The parent transaction must be identified using the BloclTrade field with code BLPA. The
children
transactions must be identified using the code BLCH.
For more details, see the relevant market practice document on www.smpg.info.
C47 ShortLongNumberRule
ShortNumber must contain the FIN message type number of the linked message. LongNumber
must contain the XML message identifier of the linked message.
C48 SignRule
When Sign is present, rate must not be zero.
C49 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C50 TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time
of the place of trade, eg, of the stock exchange, or of the selling broker for OTC.
C51 VendorPresenceRule
If the settlement standing instruction database is a vendor database, then the vendor must be
identified.
3.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
3.4.1 Identification <Id>
Presence: [1..1]
Definition: Information that unambiguously identifies an SecuritiesTradeConfirmation message as
known by the account owner (or the instructing party acting on its behalf).
Identification <Id> contains the following TransactiontIdentification4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TransactionIdentification <TxId> [1..1] Text 45
3.4.1.1  TransactionIdentification <TxId>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 45 February 2025
```

