---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.14 InvestmentAccount75", "66.1.24.14.5 OwnershipType <OwnrshTp>"]
file_pages: [4649]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.14.5 OwnershipType <OwnrshTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4649 to 4649.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4649

```text
66.1.24.14.5  OwnershipType <OwnrshTp>
Presence: [0..1]
Definition: Ownership status of the account, for example, joint owners.
OwnershipType <OwnrshTp> contains one of the following elements (see "OwnershipType2Choice"
on page 4640 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4640
Or}   Proprietary <Prtry> [1..1] ± 4642
66.1.24.14.6  TaxExemption <TaxXmptn>
Presence: [0..1]
Definition: Tax advantage specific to the account.
TaxExemption <TaxXmptn> contains one of the following elements (see
"TaxExemptionReason2Choice" on page 5250 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5251
Or}   Proprietary <Prtry> [1..1] ± 5254
66.1.24.14.7  StatementFrequency <StmtFrqcy>
Presence: [0..1]
Definition: Frequency at which a statement is issued.
StatementFrequency <StmtFrqcy> contains one of the following elements (see
"StatementFrequencyReason2Choice" on page 4534 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4535
Or}   Proprietary <Prtry> [1..1] ± 4535
66.1.24.14.8  ReferenceCurrency <RefCcy>
Presence: [0..1]
Definition: Currency chosen for reporting purposes by the account owner in agreement with the account
servicer.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4649 May 2026
```

