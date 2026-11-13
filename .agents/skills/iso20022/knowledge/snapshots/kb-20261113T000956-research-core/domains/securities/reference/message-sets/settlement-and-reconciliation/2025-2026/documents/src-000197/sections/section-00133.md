---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "7.4 Message Building Blocks"]
file_pages: [183]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.016.001.10"]
preceding_topic_continuations: [{"constraint_ids": ["C21", "C22"], "until_heading": "7.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 183, "topic": "7.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00132.md"}]
---

# 7.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 183 to 183.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 183, C21–C22 before **7.4 Message Building Blocks** continue [7.3 Constraints](section-00132.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 183

```text
On Condition
    /BlockChainAddressOrWallet is present
Following Must be True
    /SafekeepingAccount Must be absent
This constraint is defined at the MessageDefinition level.
C21 SafekeepingAccountOrBlockChainAddress3Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
Following Must be True
    /SafekeepingAccount Must be present
 Or    /BlockChainAddressOrWallet Must be present
This constraint is defined at the MessageDefinition level.
C22 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 1538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 1539
   LastPageIndicator <LastPgInd> [1..1] Indicator 1539
7.4.2 StatementGeneralDetails <StmtGnlDtls>
Presence: [1..1]
Definition: General information related to the report.
Impacted by: C18 "ReportNumberRule"
Approved by the Securities SEG on 27 January 2026 semt.016.001.10
IntraPositionMovementPostingReportV10
Settlement And Reconciliation - Maintenance 2025 - 2026 183 March 2026
```

