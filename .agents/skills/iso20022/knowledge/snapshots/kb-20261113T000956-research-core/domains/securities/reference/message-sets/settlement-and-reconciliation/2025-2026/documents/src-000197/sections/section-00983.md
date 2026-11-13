---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.4 Balance", "35.1.4.7 SubBalanceType12Choice", "35.1.4.7.2 Proprietary <Prtry>"]
file_pages: [1419]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.4.7.2 Proprietary <Prtry>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1419 to 1419.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1419

```text
CodeName Name Definition
financial instruments for which legal
documentation has been received.
QUAS QuasiIssued In issuer agent / depository
communication, balance of issued
financial instruments for which legal
documentation has not yet been
received.
35.1.4.7.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Reason a security is not available or additional information about the financial instrument for
which the balance is given, for example, unregistered, registered in nominee name.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.4.8  BalanceAmounts3
Definition: Amounts linked to a securities balance, for example, holding value.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [0..1] ± 1419
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 1420
   BookValue <BookVal> [0..1] ± 1420
   EligibleCollateralValue <ElgblCollVal> [0..1] ± 1420
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1420
Constraints
• EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally agreed
between the sender and receiver.
35.1.4.8.1  HoldingValue <HldgVal>
Presence: [0..1]
Definition: Value of an individual financial instrument holding within a safekeeping account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1419 March 2026
```

