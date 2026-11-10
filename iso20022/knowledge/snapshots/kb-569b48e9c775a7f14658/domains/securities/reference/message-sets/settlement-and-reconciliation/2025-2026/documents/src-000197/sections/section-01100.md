---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.9 SettlementTypeAndAdditionalParameters14", "35.1.16.9.3 CommonIdentification <CmonId>"]
file_pages: [1541]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.9.3 CommonIdentification <CmonId>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1541 to 1541.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1541

```text
CodeName Name Definition
APMT AgainstPaymentSettlement Settlement of the financial instrument
and cash takes place in a delivery
versus payment (DVP) environment, that
is, through an International Central
Securities Depository (ICSD) or Central
Securities Depository (CSD).
35.1.16.9.3  CommonIdentification <CmonId>
Presence: [0..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 2192
35.1.16.9.4  CorporateActionEventIdentification <CorpActnEvtId>
Presence: [0..1]
Definition: Identification assigned by the account servicer to unambiguously identify a corporate action
event.
Datatype: "Max35Text" on page 2192
35.1.16.9.5  ReconciliationIndicator <RcncltnInd>
Presence: [0..1]
Definition: Indicates whether the settlement transaction was already sent on the market and that it is
only sent by an account owner to an account servicer for reconciliation purposes.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
35.1.16.10  PriorityNumeric4Choice
Definition: Choice of format for the priority.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 1541
Or}   Proprietary <Prtry> [1..1] ± 1541
35.1.16.10.1  Numeric <Nmrc>
Presence: [1..1]
Definition: Specifies the execution priority of the instruction with a number between 0001 and 9999.
Datatype: "Exact4NumericText" on page 2190
35.1.16.10.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the execution priority of the instruction with a proprietary scheme.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1541 March 2026
```

