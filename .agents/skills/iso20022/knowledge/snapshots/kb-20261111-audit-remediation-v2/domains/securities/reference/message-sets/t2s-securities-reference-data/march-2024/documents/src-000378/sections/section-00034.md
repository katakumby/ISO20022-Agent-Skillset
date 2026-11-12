---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["5 reda.009.001.01 SecurityActivityAdviceV01", "5.4 Message Building Blocks", "5.4.3 SecurityActivity <SctyActvty>", "5.4.3.1 SystemDate <SysDt>"]
file_pages: [74]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.009.001.01"]
---

# 5.4.3.1 SystemDate <SysDt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 74 to 74.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 74

```text
5.4.3.1  SystemDate <SysDt>
Presence: [1..1]
Definition: Date for which the statement is valid.
Datatype: "ISODate" on page 529
5.4.3.2  Change <Chng>
Presence: [0..*]
Definition: Provides information on the actual change occurred to a financial instrument.
Change <Chng> contains the following SecuritiesReferenceDataChange3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C1, C2,
C3, C4,
C5
74
   FieldName <FldNm> [1..1] Text 75
   OldFieldValue <OdFldVal> [1..1] Text 75
   NewFieldValue <NewFldVal> [1..1] Text 75
   OperationTimeStamp <OprTmStmp> [1..1] DateTime 75
5.4.3.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identifies the financial instrument for which the changes are listed in the advice.
Impacted by: C1 "DescriptionPresenceRule", C2 "DescriptionUsageRule", C3 "ISINGuideline", C4
"ISINPresenceRule", C5 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification39" on page 474 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 475
   OtherIdentification <OthrId> [0..*]  475
     Identification <Id> [1..1] Text 475
     Suffix <Sfx> [0..1] Text 475
     Type <Tp> [1..1] ± 475
   Description <Desc> [0..1] Text 476
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities - Securities Reference Data 74 March 2024
```

