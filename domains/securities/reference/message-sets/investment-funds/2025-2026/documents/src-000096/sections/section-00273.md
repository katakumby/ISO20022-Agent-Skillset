---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["18 semt.002.001.02 CustodyStatementOfHoldingsV02", "18.4 Message Building Blocks", "18.4.5 StatementGeneralDetails <StmtGnlDtls>", "18.4.5.6 ActivityIndicator <ActvtyInd>"]
file_pages: [382]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.02"]
---

# 18.4.5.6 ActivityIndicator <ActvtyInd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 382 to 382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 382

```text
18.4.5.6  ActivityIndicator <ActvtyInd>
Presence: [1..1]
Definition: Indicates whether there is activity or information update reported in the statement.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 5400):
• Meaning When True: Yes
• Meaning When False: No
18.4.5.7  StatementBasis <StmtBsis>
Presence: [1..1]
Definition: Type of balance on which the statement is prepared.
StatementBasis <StmtBsis> contains one of the following elements (see
"StatementBasisCodeAndDSSCodeChoice" on page 5162 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementBasisAsCode <StmtBsisAsCd> [1..1] CodeSet 5163
Or}   StatementBasisAsDSS <StmtBsisAsDSS> [1..1] ± 5163
18.4.5.8  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the statement.
Datatype: "Max5NumericText" on page 5404
18.4.6 AccountDetails <AcctDtls>
Presence: [1..1]
Definition: The safekeeping or investment account.
AccountDetails <AcctDtls> contains the following elements (see "SafekeepingAccount2" on page 4643
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4643
   FungibleIndicator <FngbInd> [1..1] Indicator 4643
   Name <Nm> [0..1] Text 4644
   Designation <Dsgnt> [0..1] Text 4644
   IntermediaryInformation <IntrmyInf> [0..10] ± 4644
   AccountOwner <AcctOwnr> [0..1] ± 4644
   AccountServicer <AcctSvcr> [0..1] ± 4645
Approved by the Securities SEG on 27 January 2026 semt.002.001.02 CustodyStatementOfHoldingsV02
Investment Funds - Maintenance 2025 - 2026 382 May 2026
```

