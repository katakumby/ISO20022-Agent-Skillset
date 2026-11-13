---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.26 IdentificationReference8Choice", "7.1.19.26.11 CommonIdentification <CmonId>"]
file_pages: [316]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.26.11 CommonIdentification <CmonId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 316 to 316.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 316

```text
7.1.19.26.11  CommonIdentification <CmonId>
Presence: [1..1]
Definition: Unique reference agreed upon by the two trade counterparties to identify the trade.
Datatype: "Max35Text" on page 669
7.1.19.26.12  ComplianceIdentification <CmplcId>
Presence: [1..1]
Definition: Identification used to represent this transaction for compliance purposes.
Datatype: "Max35Text" on page 669
7.1.19.26.13  CollateralTransactionIdentification <CollTxId>
Presence: [1..1]
Definition: Unambiguous identification of a collateral transaction as assigned by the instructing party.
Datatype: "Max35Text" on page 669
7.1.19.27  AmountOrPercentageRange1
Definition: Provides constrains on a range of business values.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Operation <Opr> [0..1] CodeSet 316
   Term <Term> [0..10]  316
     Operator <Oprtr> [1..1] CodeSet 317
     Value <Val> [1..1]  317
{Or       RateValue <RateVal> [1..1] Rate 317
Or}       AbsoluteValue <AbsVal> [1..1] Quantity 317
7.1.19.27.1  Operation <Opr>
Presence: [0..1]
Definition: Indication of the relationship between two variables.
Datatype: "Operation1Code" on page 636
CodeName Name Definition
TILL Till Indicates a range delimited by two
variables.
ORRR Or Indicates either of two variables is valid,
but not both.
ANDD And Indicates that only when both variables
are given, the operation is valid.
7.1.19.27.2  Term <Term>
Presence: [0..10]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 316 February 2025
```

