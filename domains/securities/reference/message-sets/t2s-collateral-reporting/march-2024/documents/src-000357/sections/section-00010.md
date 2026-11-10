---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["2 colr.001.001.02 CollateralValueQueryV02", "2.4 Message Building Blocks", "2.4.2 CollateralValueQueryDefinition <CollValQryDef>", "2.4.2.2 NewCriteria <NewCrit>", "2.4.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.1 CashAccountIdentification <CshAcctId>"]
file_pages: [10]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 2.4.2.2.2.1 CashAccountIdentification <CshAcctId>

Source: [src-000357](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 10 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
SearchCriteria <SchCrit> contains the following CollateralValueSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountIdentification <CshAcctId> [0..1] ± 10
   Currency <Ccy> [0..*] CodeSet C1 10
   CashAccountOwner <CshAcctOwnr> [0..1] ± 11
   CashAccountServicer <CshAcctSvcr> [0..1] ± 11
   FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C9, C10,
C11
11
   SecuritiesAccountOwner <SctiesAcctOwnr> [0..1] ± 12
   SecuritiesAccountServicer <SctiesAcctSvcr> [0..1] ± 13
Constraints
• CashAccountIdentificationGuideline
If the account identification identifies a group of accounts with different types or in different
currencies, the currency and/or the account type can be used as additional search criteria.
2.4.2.2.2.1  CashAccountIdentification <CshAcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the cash account between the account owner and
the account servicer.
CashAccountIdentification <CshAcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 45 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C9 45
Or}   Other <Othr> [1..1] ± 45
2.4.2.2.2.2  Currency <Ccy>
Presence: [0..*]
Definition: Medium of exchange of value.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 74
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.001.001.02 CollateralValueQueryV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
10 March 2024
```

