---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["55 reda.035.001.01 SecuritiesAccountActivityAdviceV01", "55.4 Message Building Blocks", "55.4.2 Pagination <Pgntn>"]
file_pages: [2238]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.035.001.01"]
---

# 55.4.2 Pagination <Pgntn>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2238 to 2238.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2238

```text
55.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 2980 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 2980
   LastPageIndicator <LastPgInd> [1..1] Indicator 2980
55.4.3 SecuritiesAccountActivity <SctiesAcctActvty>
Presence: [1..1]
Definition: Activity report of changes occurred for a specific securities account defined in the system.
SecuritiesAccountActivity <SctiesAcctActvty> contains the following
SecuritiesAccountStatement2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemDate <SysDt> [1..1] Date 2238
   Change <Chng> [0..*]  2238
     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 2239
     FieldName <FldNm> [1..1] Text 2239
     OldFieldValue <OdFldVal> [1..1] Text 2239
     NewFieldValue <NewFldVal> [1..1] Text 2239
     OperationTimeStamp <OprTmStmp> [1..1] DateTime 2239
55.4.3.1  SystemDate <SysDt>
Presence: [1..1]
Definition: Date for which the statement is valid.
Datatype: "ISODate" on page 3319
55.4.3.2  Change <Chng>
Presence: [0..*]
Definition: Provides information on the actual change occurred to a securities account.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.035.001.01
SecuritiesAccountActivityAdviceV01
Target2-Securities 2238 August 2026
```

