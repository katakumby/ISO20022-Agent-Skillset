---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.8 SafekeepingAccount <SfkpgAcct>"]
file_pages: [41]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.8 SafekeepingAccount <SfkpgAcct>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 41 to 41.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 41

```text
Priority <Prty> contains one of the following elements (see "PriorityNumeric4Choice" on page 364 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Numeric <Nmrc> [1..1] Text 364
Or}   Proprietary <Prtry> [1..1] ± 365
3.4.1.2.8  SafekeepingAccount <SfkpgAcct>
Presence: [0..*]
Definition: Account where financial instruments are maintained.
SafekeepingAccount <SfkpgAcct> contains the following elements (see "SecuritiesAccount19" on
page 246 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 246
   Type <Tp> [0..1] ± 246
   Name <Nm> [0..1] Text 246
3.4.1.2.9  CashAccount <CshAcct>
Presence: [0..*]
Definition: Account in which cash is maintained.
CashAccount <CshAcct> contains one of the following
AccountIdentificationSearchCriteria2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] ± 41
Or   ContainText <CTTxt> [1..1] Text 42
Or}   NotContainText <NCTTxt> [1..1] Text 42
3.4.1.2.9.1  Equal <EQ>
Presence: [1..1]
Definition: Search for one or more accounts based on exact identification of the account(s).
Equal <EQ> contains one of the following elements (see "AccountIdentification4Choice" on page 249
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C8 250
Or}   Other <Othr> [1..1] ± 250
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 41 March 2026
```

