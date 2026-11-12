---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks"]
file_pages: [28]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
preceding_topic_continuations: [{"constraint_ids": ["C39", "C40", "C41", "C42", "C43", "C44"], "until_heading": "2.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 28, "topic": "2.3 Constraints", "reference_path": "domains/securities/reference/message-sets/settlement-and-reconciliation/2025-2026/documents/src-000197/sections/section-00007.md"}]
---

# 2.4 Message Building Blocks

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 28 to 28.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 28, C39–C44 before **2.4 Message Building Blocks** continue [2.3 Constraints](section-00007.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 28

```text
 And    /StatementGeneralDetails/SubAccountIndicator is equal to value 'true'
Following Must be True
    /SubAccountDetails[*] Must be present
 And    /BalanceForAccount[*] Must be absent
This constraint is defined at the MessageDefinition level.
C39 SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
C40 SubBalanceAdditionalDetailsRule
Unless bilaterally agreed between the Sender and Receiver, if SubBalanceAdditionnalDetails is
used, them it must not contain information that can be provided in a structured field.
C41 SubSafekeepingReportingRule
Use of consolidated reports on a sub-safekeeping account must be bilaterally agreed between
sender and receiver.
C42 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C43 TotalEligibleCollateralValueRule
Total eligible collateral value is only to be used in (I)CSD-participant communication or if
bilaterally agreed between the sender and receiver.
C44 ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
2.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
2.4.1 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 1538 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 1539
   LastPageIndicator <LastPgInd> [1..1] Indicator 1539
2.4.2 StatementGeneralDetails <StmtGnlDtls>
Presence: [1..1]
Definition: Provides general information on the report.
Impacted by: C28 "ReportNumberRule"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 28 March 2026
```

