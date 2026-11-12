---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["14 seev.042.001.14 CorporateActionInstructionStatementReportV14", "14.4 Message Building Blocks"]
file_pages: [763]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.042.001.14"]
preceding_topic_continuations: [{"constraint_ids": ["C16", "C17", "C18", "C19", "C20", "C21", "C22", "C23"], "until_heading": "14.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 763, "topic": "14.3 Constraints", "reference_path": "domains/securities/reference/message-sets/corporate-actions/2025-2026/documents/src-000080/sections/section-00586.md"}]
---

# 14.4 Message Building Blocks

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 763 to 763.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 763, C16–C23 before **14.4 Message Building Blocks** continue [14.3 Constraints](section-00586.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 763

```text
C16 MultipleAccountAndStatementDetailsRule
If StatementGeneralDetails/ReportingType is MASE (Multiple Accounts) then
AccountAndStatementDetails may be repeated and AccountAndStatementDetails/
CorporateActionEventAndBalance must not be repeated in any occurrences of
AccountAndStatementDetails.
If StatementGeneralDetails/ReportingType is SAME (Multiple Events) then
AccountAndStatementDetails must not be repeated, and AccountAndStatementDetails/
CorporateActionEventAndBalance may be repeated.
This constraint is defined at the MessageDefinition level.
C17 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C18 PaginationRule
If pagination is present, then StatementGeneralDetails/StatementIdentification must be present.
On Condition
    /Pagination is present
Following Must be True
    /StatementGeneralDetails/StatementIdentification Must be present
This constraint is defined at the MessageDefinition level.
C19 SafekeepingAccountOrBlockChainAddress1Rule
Either SafekeepingAccount or BlockChainAddressOrWallet must be present but not both.
C20 SafekeepingAccountOrBlockChainAddress2Rule
If BlockChainAddressOrWallet is present then SafekeepingAccount must be absent.
C21 SafekeepingAccountOrBlockChainAddress3Rule
If SafekeepingAccount is present, then BlockChainAddressOrWallet must be absent.
C22 SafekeepingPlaceRule
SafekeepingPlace is only to be used by global custodians that allow their clients to specify
where the securities are to be held, for example, in an ICSD account versus an account at the
local CSD.
C23 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
14.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
14.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Approved by the Securities SEG on 27 January 2026 seev.042.001.14
CorporateActionInstructionStatementReportV14
Corporate Actions - Maintenance 2025 - 2026 763 February 2026
```

