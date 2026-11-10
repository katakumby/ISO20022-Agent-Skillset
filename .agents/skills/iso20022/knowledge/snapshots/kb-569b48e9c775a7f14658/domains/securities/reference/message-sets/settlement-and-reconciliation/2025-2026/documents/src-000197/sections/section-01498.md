---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.29 Status", "35.1.29.75 RepairReason11Choice", "35.1.29.75.2 Proprietary <Prtry>"]
file_pages: [1991]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.29.75.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1991 to 1991.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1991

```text
CodeName Name Definition
REPA TerminationTransactionAmount Unrecognised or invalid termination
transaction amount.
CADE TransactionCallDelay Unrecognised or invalid transaction call
delay.
RERT RepurchaseRateType Unrecognised or invalid repurchase rate
type.
RSPR SpreadRate Unrecognised or invalid spread rate.
VASU VariableRateSupport Unrecognised or invalid variable rate
support (repurchase agreement).
REPO RepurchaseRate Unrecognised or invalid repurchase rate.
REPP PremiumAmount Unrecognised or invalid premium
amount.
TERM ClosingDateTime Unrecognised or invalid closing date/
time.
FORF ForfeitAmount Unrecognised or invalid forfeit amount.
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline. Processed on best effort basis.
BUSE TypeOfOrderRepair Unrecognised or invalid type of order.
COMC CommercializationContractRepair Unrecognized or invalid
commercialization contract.
FEEE FeeCommissionRepair Unrecognised or invalid fee or
commission.
INNA NarrativeInformationRepair Unrecognised or invalid service level
agreement pre-agreed narrative
information.
NRGM NoMatch Cancellation request is in repair since
more than one instruction match to the
cancellation criteria.
NRGN NotFound Cancellation request is in repair since
the instruction could not be found.
ULNK Unknown Message was not recognised. Unknown
linked reference.
35.1.29.75.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1991 March 2026
```

