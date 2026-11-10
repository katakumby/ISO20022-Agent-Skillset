---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.4 Type <Tp>"]
file_pages: [4621]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.4 Type <Tp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4621 to 4621.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4621

```text
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 5403
66.1.24.9.4  Type <Tp>
Presence: [0..1]
Definition: Type of account.
Type <Tp> contains one of the following elements (see "AccountType2Choice" on page 4327 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4327
Or}   Proprietary <Prtry> [1..1] ± 4327
66.1.24.9.5  OwnershipType <OwnrshTp>
Presence: [1..1]
Definition: Ownership status of the account, for example, joint owners.
OwnershipType <OwnrshTp> contains one of the following elements (see "OwnershipType2Choice"
on page 4640 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4640
Or}   Proprietary <Prtry> [1..1] ± 4642
66.1.24.9.6  TaxExemption <TaxXmptn>
Presence: [0..1]
Definition: Tax advantage specific to the account.
TaxExemption <TaxXmptn> contains one of the following elements (see
"TaxExemptionReason2Choice" on page 5250 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5251
Or}   Proprietary <Prtry> [1..1] ± 5254
66.1.24.9.7  StatementFrequency <StmtFrqcy>
Presence: [0..1]
Definition: Frequency at which a statement is issued.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4621 May 2026
```

