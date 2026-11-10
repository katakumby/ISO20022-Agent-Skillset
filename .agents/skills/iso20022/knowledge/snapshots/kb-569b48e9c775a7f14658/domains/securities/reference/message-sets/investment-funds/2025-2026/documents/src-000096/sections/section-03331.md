---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.3 InvestmentAccount74", "66.1.24.3.27 TransactionChannelType <TxChanlTp>"]
file_pages: [4570]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.3.27 TransactionChannelType <TxChanlTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4570 to 4570.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4570

```text
Definition: Date the investor or account owner signs the open account form.
AccountSignatureDateTime <AcctSgntrDtTm> contains one of the following elements (see
"DateAndDateTime1Choice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4467
Or}   DateTime <DtTm> [1..1] DateTime 4467
66.1.24.3.27  TransactionChannelType <TxChanlTp>
Presence: [0..1]
Definition: Means by which the investor or account owner submits the open account form.
TransactionChannelType <TxChanlTp> contains one of the following elements (see
"TransactionChannelType1Choice" on page 4824 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4824
Or}   Proprietary <Prtry> [1..1] ± 4824
66.1.24.3.28  InvestmentAccountCategory <InvstmtAcctCtgy>
Presence: [0..1]
Definition: Specifies the category of the account.
InvestmentAccountCategory <InvstmtAcctCtgy> contains one of the following elements (see
"InvestmentAccountCategory1Choice" on page 4595 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4595
Or}   Proprietary <Prtry> [1..1] ± 4595
66.1.24.3.29  Pledging <Pldgg>
Presence: [0..1]
Definition: Specifies whether the holdings in the account are eligible for pledging.
Datatype: "Eligible1Code" on page 5295
CodeName Name Definition
ELIG Eligible Item is eligible.
NELI NotEligible Item is not eligible.
66.1.24.3.30  Collateral <Coll>
Presence: [0..1]
Definition: Specifies whether the holdings in the account are used as collateral.
Datatype: "Collateral1Code" on page 5285
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4570 May 2026
```

