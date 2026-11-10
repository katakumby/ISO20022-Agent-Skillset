---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.9 InvestmentAccount73", "66.1.24.9.22 AccountUsageType <AcctUsgTp>"]
file_pages: [4628]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.9.22 AccountUsageType <AcctUsgTp>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4628 to 4628.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4628

```text
66.1.24.9.22  AccountUsageType <AcctUsgTp>
Presence: [0..1]
Definition: Type of usage of the account.
AccountUsageType <AcctUsgTp> contains one of the following elements (see
"AccountUsageType2Choice" on page 4555 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4555
Or}   Proprietary <Prtry> [1..1] ± 4555
66.1.24.9.23  ForeignStatusCertification <FrgnStsCertfctn>
Presence: [0..1]
Definition: Specifies if documentary evidence has been provided for the foreign resident.
Datatype: "Provided1Code" on page 5345
CodeName Name Definition
NPRO NotProvided Not provided.
PROV Provided Provided.
66.1.24.9.24  AccountSignatureDateTime <AcctSgntrDtTm>
Presence: [0..1]
Definition: Date the investor or account owner signs the open account form.
AccountSignatureDateTime <AcctSgntrDtTm> contains one of the following elements (see
"DateAndDateTime1Choice" on page 4466 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 4467
Or}   DateTime <DtTm> [1..1] DateTime 4467
66.1.24.9.25  TransactionChannelType <TxChanlTp>
Presence: [0..1]
Definition: Means by which the investor or account owner submits the open account form.
TransactionChannelType <TxChanlTp> contains one of the following elements (see
"TransactionChannelType1Choice" on page 4824 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4824
Or}   Proprietary <Prtry> [1..1] ± 4824
66.1.24.9.26  InvestmentAccountCategory <InvstmtAcctCtgy>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4628 May 2026
```

