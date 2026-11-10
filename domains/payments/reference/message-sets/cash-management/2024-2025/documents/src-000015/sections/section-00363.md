---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["15 camt.016.001.04 GetCurrencyExchangeRateV04", "15.4 Message Building Blocks", "15.4.2 CurrencyQueryDefinition <CcyQryDef>"]
file_pages: [507]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.016.001.04"]
---

# 15.4.2 CurrencyQueryDefinition <CcyQryDef>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 507 to 507.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 507

```text
MessageHeader <MsgHdr> contains the following elements (see "MessageHeader1" on page 811 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MessageIdentification <MsgId> [1..1] Text 812
   CreationDateTime <CreDtTm> [0..1] DateTime 812
15.4.2 CurrencyQueryDefinition <CcyQryDef>
Presence: [0..1]
Definition: Definition of the currency exchange query.
CurrencyQueryDefinition <CcyQryDef> contains the following CurrencyQueryDefinition3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryType <QryTp> [0..1] CodeSet 507
   CurrencyCriteria <CcyCrit> [0..1]  508
{Or     QueryName <QryNm> [1..1] Text 508
Or}     NewCriteria <NewCrit> [1..1]  508
       NewQueryName <NewQryNm> [0..1] Text 508
       SearchCriteria <SchCrit> [1..*]  508
         SourceCurrency <SrcCcy> [1..1] CodeSet C1 509
         TargetCurrency <TrgtCcy> [1..1] CodeSet C1 509
15.4.2.1  QueryType <QryTp>
Presence: [0..1]
Definition: Specifies the type of matching items to be returned in the response to the query.
Datatype: "QueryType2Code" on page 872
CodeName Name Definition
ALLL All Specifies that the query requests that all
matching items be returned.
CHNG Changed Specifies that the query requests that
only new matching items since the last
similar query be returned.
MODF Modified Specifies that the query requests that
only items that have changed since the
last query be returned.
DELD Deleted Specifies that the query requests that
items that have been deleted since the
last query be returned.
Approved by the Payments SEG on 04 February 2025 camt.016.001.04 GetCurrencyExchangeRateV04
Cash Management - Maintenance 2024 - 2025 507 February 2025
```

