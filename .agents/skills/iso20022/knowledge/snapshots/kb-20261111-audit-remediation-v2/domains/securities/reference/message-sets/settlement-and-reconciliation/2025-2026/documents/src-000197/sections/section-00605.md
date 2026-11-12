---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.9 SecuritiesFinancingDetails <SctiesFincgDtls>", "27.4.9.10 LegalFramework <LglFrmwk>"]
file_pages: [918]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.9.10 LegalFramework <LglFrmwk>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 918 to 918.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 918

```text
Definition: Specifies whether the collateral position should be subject to automatic revaluation by the
account servicer.
Revaluation <Rvaltn> contains one of the following elements (see "RevaluationIndicator3Choice" on
page 1545 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 1545
Or}   Proprietary <Prtry> [1..1] ± 1546
27.4.9.10  LegalFramework <LglFrmwk>
Presence: [0..1]
Definition: Legal framework of the transaction.
LegalFramework <LglFrmwk> contains one of the following elements (see "LegalFramework3Choice"
on page 1622 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1622
Or}   Proprietary <Prtry> [1..1] ± 1623
27.4.9.11  InterestComputationMethod <IntrstCmptnMtd>
Presence: [0..1]
Definition: Identifies the computation method of accrued interest of the related financial instrument.
InterestComputationMethod <IntrstCmptnMtd> contains one of the following elements (see
"InterestComputationMethodFormat4Choice" on page 1612 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1612
Or}   Proprietary <Prtry> [1..1] ± 1615
27.4.9.12  MaturityDateModification <MtrtyDtMod>
Presence: [0..1]
Definition: Indicates whether the maturity date of the securities financing transaction may be modified.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
27.4.9.13  InterestPayment <IntrstPmt>
Presence: [0..1]
Definition: Indicates whether the interest is to be paid to the collateral taker. If set to no, the interest is
paid to the collateral giver.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 918 March 2026
```

