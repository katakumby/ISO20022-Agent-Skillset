---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 camt.003.001.08 GetAccountV08", "2.4 Message Building Blocks", "2.4.2 AccountQueryDefinition <AcctQryDef>", "2.4.2.2 AccountCriteria <AcctCrit>", "2.4.2.2.2 NewCriteria <NewCrit>", "2.4.2.2.2.2 SearchCriteria <SchCrit>", "2.4.2.2.2.2.4 Balance <Bal>", "2.4.2.2.2.2.4.5 ProcessingDate <PrcgDt>", "2.4.2.2.2.2.4.5.2 Date <Dt>", "2.4.2.2.2.2.4.5.2.3 FromToDate <FrToDt>"]
file_pages: [39]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.003.001.08"]
---

# 2.4.2.2.2.2.4.5.2.3 FromToDate <FrToDt>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 39 to 39.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 39

```text
Datatype: "ISODate" on page 883
2.4.2.2.2.2.4.5.2.3  FromToDate <FrToDt>
Presence: [1..1]
Definition: Particular time span specified between a start date and an end date.
FromToDate <FrToDt> contains the following elements (see "DatePeriod2" on page 800 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 800
   ToDate <ToDt> [1..1] Date 800
2.4.2.2.2.2.4.5.2.4  EqualDate <EQDt>
Presence: [1..1]
Definition: Specified date to match.
Datatype: "ISODate" on page 883
2.4.2.2.2.2.4.5.2.5  NotEqualDate <NEQDt>
Presence: [1..1]
Definition: Specified date to be excluded from the search.
Datatype: "ISODate" on page 883
2.4.2.2.2.2.5  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Owner of the account which is being queried.
Approved by the Payments SEG on 04 February 2025 camt.003.001.08 GetAccountV08
Cash Management - Maintenance 2024 - 2025 39 February 2025
```

