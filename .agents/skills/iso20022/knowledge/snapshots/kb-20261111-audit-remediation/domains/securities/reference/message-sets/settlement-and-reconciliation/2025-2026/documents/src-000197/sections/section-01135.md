---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.43 RepurchaseType22Choice", "35.1.16.43.1 Code <Cd>"]
file_pages: [1580]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.43.1 Code <Cd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1580 to 1580.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1580

```text
35.1.16.43.1  Code <Cd>
Presence: [1..1]
Definition: Type of securities financing transaction process expressed as an ISO 20022 code.
Datatype: "RepurchaseType9Code" on page 2135
CodeName Name Definition
PAIR Pairoff Relates to a transaction that is paired off
and netted against one or more previous
transactions. A paired off transaction is a
buyback to offset and effectively
liquidate a prior sale of securities or a
sellback to offset and effectively liquidate
a prior buy of securities.
PADJ PrincipalExposureAdjustment Relates to a principal adjustment.
RATE RepoRate Is part of a pair-off.
CALL RepurchaseCall Relates to the early closing/maturity date
for a term repo or a termination date of
an open repo with the underlying
collateral.
ROLP RepoContractRollover Relates to a repo rollover of a contract
extending the closing or maturity date
without the underlying collateral
impacted.
CADJ Swap Relates to a swap/substitution.
TOPU TopUp Relates to a repo rollover of a position
extending the closing or maturity date.
WTHD Withdrawal Relates to a repo rollover of a position
extending the closing or maturity date.
35.1.16.43.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of securities financing transaction process expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 1502 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 1502
   Issuer <Issr> [1..1] Text 1502
   SchemeName <SchmeNm> [0..1] Text 1502
35.1.16.44  UnilateralSplit3Choice
Definition: Specifies the matching processing change requested.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1580 March 2026
```

