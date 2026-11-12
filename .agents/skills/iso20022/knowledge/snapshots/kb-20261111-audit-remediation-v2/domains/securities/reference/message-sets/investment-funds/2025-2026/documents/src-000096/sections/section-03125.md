---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.5 Balance", "66.1.5.2 StatementOfInvestmentFundTransactions2", "66.1.5.2.1 StatementGeneralDetails <StmtGnlDtls>", "66.1.5.2.1.7 ReportNumber <RptNb>"]
file_pages: [4350]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.5.2.1.7 ReportNumber <RptNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4350 to 4350.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4350

```text
Definition: Indicates whether there is activity reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
66.1.5.2.1.7  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the statement.
Datatype: "Max5NumericText" on page 5404
66.1.5.2.2  InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [0..1]
Definition: Information related to an investment account of the statement that is being cancelled.
InvestmentAccountDetails <InvstmtAcctDtls> contains the following elements (see
"InvestmentAccount25" on page 4662 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4662
   Name <Nm> [0..1] Text 4662
   Designation <Dsgnt> [0..1] Text 4662
   IntermediaryInformation <IntrmyInf> [0..10] ± 4663
   AccountServicer <AcctSvcr> [0..1] ± 4663
66.1.5.2.3  TransactionOnAccount <TxOnAcct>
Presence: [0..*]
Definition: Creation/cancellation of investment units on the books of the fund or its designated agent, as
a result of executing an investment fund order.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4350 May 2026
```

