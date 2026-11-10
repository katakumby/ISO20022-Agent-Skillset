---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.2 CodeSet", "9.2.2.13 CreditDebitCode"]
file_pages: [324]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.2.13 CreditDebitCode

Source: [src-000381](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 324 to 324.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 324

```text
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
9.2.2.13  CreditDebitCode
Definition: Specifies if an operation is an increase or a decrease.
Type: CodeSet
CodeName Name Definition
CRDT Credit Operation is an increase.
DBIT Debit Operation is a decrease.
9.2.2.14  DateType3Code
Definition: Specifies a type of date.
Type: CodeSet
CodeName Name Definition
VARI Various Partial trades have occurred over a
period of two or more days.
9.2.2.15  DeniedReason4Code
Definition: Specifies the denied reason.
Type: CodeSet
CodeName Name Definition
ADEA AccountServicerDeadlineMissed Received after the account servicer's
deadline.
DCAN DeniedSinceAlreadyCancelled Cancellation request was denied since
the instruction has already been
cancelled.
DPRG DeniedSinceInProgress Cancellation request was denied
because the process of settlement is in
progress.
DREP DeniedSinceRepoEnded Cancellation request was denied
because the repo was cancelled.
DSET DeniedSinceAlreadySettled Cancellation request was denied
because the instruction was already
settled.
LATE MarketDeadlineMissed Received after market deadline.
OTHR Other Other. See Narrative.
CDRG ConditionalRegistrar Execution is denied due to the execution
of a process at the registrar.
CDCY ConditionalCurrency Execution is denied due to a process
linked to the currency of the transaction.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 324 September 2025
```

