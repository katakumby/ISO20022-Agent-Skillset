---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["3 acmt.026.001.02 AccountListReportV02", "3.4 Message Building Blocks", "3.4.4 ReportOrError <RptOrErr>", "3.4.4.2 AccountReport <AcctRpt>", "3.4.4.2.6 BalanceTransferAccount <BalTrfAcct>", "3.4.4.2.6.2 Currency <Ccy>"]
file_pages: [100]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.026.001.02"]
---

# 3.4.4.2.6.2 Currency <Ccy>

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 100 to 100.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 100

```text
3.4.4.2.6.2  Currency <Ccy>
Presence: [1..1]
Definition: Medium of exchange of value.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 173
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
3.4.4.2.7  TransferAccountServicerIdentification <TrfAcctSvcrId>
Presence: [0..1]
Definition: Identification of the transfer account servicer.
TransferAccountServicerIdentification <TrfAcctSvcrId> contains the following elements (see
"BranchAndFinancialInstitutionIdentification8" on page 140 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  140
     BICFI <BICFI> [0..1] IdentifierSet C4 140
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 141
     LEI <LEI> [0..1] IdentifierSet 141
     Name <Nm> [0..1] Text 141
     PostalAddress <PstlAdr> [0..1] ± 141
     Other <Othr> [0..1] ± 142
   BranchIdentification <BrnchId> [0..1]  143
     Identification <Id> [0..1] Text 143
     LEI <LEI> [0..1] IdentifierSet 143
     Name <Nm> [0..1] Text 143
     PostalAddress <PstlAdr> [0..1] ± 143
3.4.4.2.8  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
acmt.026.001.02 AccountListReportV02
Target2-Securities - Cash Account Query and Report 100 August 2026
```

