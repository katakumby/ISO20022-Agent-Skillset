---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.11 Financial Instrument", "35.1.11.5 FinancialInstrument72"]
file_pages: [1473]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.11.5 FinancialInstrument72

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1473 to 1473.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1473

```text
35.1.11.5  FinancialInstrument72
Definition: Identifying features of a financial instrument that is a sub-set of an investment fund.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SupplementaryIdentification <SplmtryId> [0..1] Text 1473
   SecuritiesForm <SctiesForm> [0..1] CodeSet 1473
   ClassType <ClssTp> [0..1] Text 1473
   DistributionPolicy <DstrbtnPlcy> [0..1] CodeSet 1473
   ClassificationType <ClssfctnTp> [0..1] ± 1474
35.1.11.5.1  SupplementaryIdentification <SplmtryId>
Presence: [0..1]
Definition: Additional information about a financial instrument to help identify the instrument.
Datatype: "Max35Text" on page 2192
35.1.11.5.2  SecuritiesForm <SctiesForm>
Presence: [0..1]
Definition: Specifies the form, that is, ownership, of the security.
Datatype: "FormOfSecurity1Code" on page 2079
CodeName Name Definition
BEAR Bearer The financial instrument does not specify
any registration of ownership, and is
payable to whomever possesses the
certificate.
REGD Registered Shareholder name of the financial
instrument appears in the corporation/
funds books.
35.1.11.5.3  ClassType <ClssTp>
Presence: [0..1]
Definition: Features of units offered by a fund. for example, a unit may have a specific load structure, for
example, front end or back end, an income policy, for example, pay out or accumulate, or a trailer
policy, for example, with or without. Fund classes are typically denoted by a single character, for
example, 'Class A', 'Class 2'.
Datatype: "Max35Text" on page 2192
35.1.11.5.4  DistributionPolicy <DstrbtnPlcy>
Presence: [0..1]
Definition: Income policy relating to a class type, that is, if income is paid out or retained in the fund.
Datatype: "DistributionPolicy1Code" on page 2061
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1473 March 2026
```

