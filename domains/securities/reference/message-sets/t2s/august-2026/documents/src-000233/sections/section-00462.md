---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["24 colr.001.001.02 CollateralValueQueryV02", "24.4 Message Building Blocks", "24.4.2 CollateralValueQueryDefinition <CollValQryDef>", "24.4.2.2 NewCriteria <NewCrit>", "24.4.2.2.2 SearchCriteria <SchCrit>", "24.4.2.2.2.1 CashAccountIdentification <CshAcctId>"]
file_pages: [584]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.001.001.02"]
---

# 24.4.2.2.2.1 CashAccountIdentification <CshAcctId>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 584 to 584.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 584

```text
SearchCriteria <SchCrit> contains the following CollateralValueSearchCriteria4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashAccountIdentification <CshAcctId> [0..1] ± 584
   Currency <Ccy> [0..*] CodeSet C1 584
   CashAccountOwner <CshAcctOwnr> [0..1] ± 585
   CashAccountServicer <CshAcctSvcr> [0..1] ± 585
   FinancialInstrumentIdentification <FinInstrmId> [0..*] ± C6, C7,
C9, C10,
C11
585
   SecuritiesAccountOwner <SctiesAcctOwnr> [0..1] ± 586
   SecuritiesAccountServicer <SctiesAcctSvcr> [0..1] ± 587
Constraints
• CashAccountIdentificationGuideline
If the account identification identifies a group of accounts with different types or in different
currencies, the currency and/or the account type can be used as additional search criteria.
24.4.2.2.2.1  CashAccountIdentification <CshAcctId>
Presence: [0..1]
Definition: Unique and unambiguous identification for the cash account between the account owner and
the account servicer.
CashAccountIdentification <CshAcctId> contains one of the following elements (see
"AccountIdentification4Choice" on page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
24.4.2.2.2.2  Currency <Ccy>
Presence: [0..*]
Definition: Medium of exchange of value.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 3212
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.001.001.02 CollateralValueQueryV02
Target2-Securities 584 August 2026
```

