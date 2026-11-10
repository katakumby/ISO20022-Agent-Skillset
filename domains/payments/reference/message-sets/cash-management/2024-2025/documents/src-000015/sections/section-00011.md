---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.2.1 AccountIdentification <AcctId>"]
file_pages: [29]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.2.1 AccountIdentification <AcctId>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 29 to 29.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 29

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         NotEqualDateTime <NEQDtTm> [1..1] DateTime 38
Or}       Date <Dt> [1..1]  38
{Or         FromDate <FrDt> [1..1] Date 38
Or         ToDate <ToDt> [1..1] Date 38
Or         FromToDate <FrToDt> [1..1] ± 39
Or         EqualDate <EQDt> [1..1] Date 39
Or}         NotEqualDate <NEQDt> [1..1] Date 39
   AccountOwner <AcctOwnr> [0..1] ± 39
   AccountServicer <AcctSvcr> [0..1] ± 40
Constraints
• CashAccountIdentificationGuideline
If the account identification identifies a group of accounts with different types or in different
currencies, the currency and/or the account type can be used as additional search criteria.
2.4.2.2.2.2.1  AccountIdentification <AcctId>
Presence: [0..*]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
AccountIdentification <AcctId> contains one of the following
AccountIdentificationSearchCriteria2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Equal <EQ> [1..1] ± 29
Or   ContainText <CTTxt> [1..1] Text 30
Or}   NotContainText <NCTTxt> [1..1] Text 30
2.4.2.2.2.2.1.1  Equal <EQ>
Presence: [1..1]
Definition: Search for one or more accounts based on exact identification of the account(s).
Equal <EQ> contains one of the following elements (see "AccountIdentification4Choice" on page 787
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 787
Or}   Other <Othr> [1..1] ± 788
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 29 February 2025
```

