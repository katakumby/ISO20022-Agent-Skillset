---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["31 sese.037.001.09 PortfolioTransferNotificationV09", "31.4 Message Building Blocks"]
file_pages: [1102]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.037.001.09"]
preceding_topic_continuations: [{"constraint_ids": ["C36", "C37", "C38"], "until_heading": "31.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 1102, "topic": "31.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00738.md"}]
---

# 31.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1102 to 1102.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 1102, C36–C38 before **31.4 Message Building Blocks** continue [31.3 Constraints](section-00738.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 1102

```text
free or against payment settlement instructions; the depository, the participant of the depository
(Party1) and the client of Party1 (Party2).
The data format for the identification of Party1 depends on the market. If no country specific
requirement is available, BIC is recommended.
For more details, see the relevant market practice document on www.smpg.info.
C36 SettlementDetailsRule
If SettlementDetails elements are used, then their conditions of use must be pre-agreed
between account owner and account servicer.
C37 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C38 TradeDateRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time
of the place of trade, for example, of the stock exchange, or of the selling broker for OTC.
31.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
31.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 1538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 1539
   LastPageIndicator <LastPgInd> [1..1] Indicator 1539
31.4.2 StatementGeneralDetails <StmtGnlDtls>
Presence: [1..1]
Definition: Provides general information on the notification.
Approved by the Securities SEG on 27 January 2026 sese.037.001.09 PortfolioTransferNotificationV09
Settlement And Reconciliation - Maintenance 2025 - 2026 1102 March 2026
```

