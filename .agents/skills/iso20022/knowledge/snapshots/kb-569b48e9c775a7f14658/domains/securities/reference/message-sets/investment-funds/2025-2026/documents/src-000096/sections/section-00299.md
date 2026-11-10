---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["22 semt.006.001.02 StatementOfInvestmentFundTransactionsV02", "22.4 Message Building Blocks", "22.4.5 StatementGeneralDetails <StmtGnlDtls>", "22.4.5.5 UpdateType <UpdTp>"]
file_pages: [415]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.006.001.02"]
---

# 22.4.5.5 UpdateType <UpdTp>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 415 to 415.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 415

```text
CodeName Name Definition
OVNG Overnight Event takes place overnight.
ONDE OnDemand Event takes place on demand.
22.4.5.5  UpdateType <UpdTp>
Presence: [1..1]
Definition: Specifies if the statement is complete or only contains changes.
Datatype: "StatementUpdateTypeCode" on page 5365
CodeName Name Definition
COMP Complete Statement is complete.
DELT Delta Statement contains changes only.
22.4.5.6  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
22.4.5.7  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the statement.
Datatype: "Max5NumericText" on page 5404
22.4.6 InvestmentAccountDetails <InvstmtAcctDtls>
Presence: [1..1]
Definition: Information related to an investment account.
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
Approved by the Securities SEG on 27 January 2026 semt.006.001.02
StatementOfInvestmentFundTransactionsV02
Investment Funds - Maintenance 2025 - 2026 415 May 2026
```

