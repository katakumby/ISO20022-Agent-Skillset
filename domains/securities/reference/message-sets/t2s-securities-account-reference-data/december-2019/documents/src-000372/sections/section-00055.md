---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["8 reda.035.001.01 SecuritiesAccountActivityAdviceV01", "8.4 Message Building Blocks", "8.4.2 Pagination <Pgntn>"]
file_pages: [61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.035.001.01"]
---

# 8.4.2 Pagination <Pgntn>

Source: [src-000372](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 61 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 61

```text
8.4.2 Pagination <Pgntn>
Presence: [1..1]
Definition: Page number of the message (within a statement) and continuation indicator to indicate that
the statement is to continue or that the message is the last page of the statement.
Pagination <Pgntn> contains the following elements (see "Pagination1" on page 83 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 84
   LastPageIndicator <LastPgInd> [1..1] Indicator 84
8.4.3 SecuritiesAccountActivity <SctiesAcctActvty>
Presence: [1..1]
Definition: Activity report of changes occurred for a specific securities account defined in the system.
SecuritiesAccountActivity <SctiesAcctActvty> contains the following
SecuritiesAccountStatement2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SystemDate <SysDt> [1..1] Date 61
   Change <Chng> [0..*]  61
     SecuritiesAccountIdentification <SctiesAcctId> [1..1] ± 62
     FieldName <FldNm> [1..1] Text 62
     OldFieldValue <OdFldVal> [1..1] Text 62
     NewFieldValue <NewFldVal> [1..1] Text 62
     OperationTimeStamp <OprTmStmp> [1..1] DateTime 62
8.4.3.1  SystemDate <SysDt>
Presence: [1..1]
Definition: Date for which the statement is valid.
Datatype: "ISODate" on page 97
8.4.3.2  Change <Chng>
Presence: [0..*]
Definition: Provides information on the actual change occurred to a securities account.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.035.001.01
SecuritiesAccountActivityAdviceV01
Target2-Securities - Securities Account Reference Data 61 December 2019
```

