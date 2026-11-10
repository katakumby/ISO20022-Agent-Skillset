---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["30 reda.009.001.01 SecurityActivityAdviceV01", "30.4 Message Building Blocks", "30.4.3 SecurityActivity <SctyActvty>", "30.4.3.1 SystemDate <SysDt>"]
file_pages: [1761]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.009.001.01"]
---

# 30.4.3.1 SystemDate <SysDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1761 to 1761.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1761

```text
30.4.3.1  SystemDate <SysDt>
Presence: [1..1]
Definition: Date for which the statement is valid.
Datatype: "ISODate" on page 3319
30.4.3.2  Change <Chng>
Presence: [0..*]
Definition: Provides information on the actual change occurred to a financial instrument.
Change <Chng> contains the following SecuritiesReferenceDataChange3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C1, C2,
C3, C4,
C5
1761
   FieldName <FldNm> [1..1] Text 1762
   OldFieldValue <OdFldVal> [1..1] Text 1762
   NewFieldValue <NewFldVal> [1..1] Text 1762
   OperationTimeStamp <OprTmStmp> [1..1] DateTime 1762
30.4.3.2.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identifies the financial instrument for which the changes are listed in the advice.
Impacted by: C1 "DescriptionPresenceRule", C2 "DescriptionUsageRule", C3 "ISINGuideline", C4
"ISINPresenceRule", C5 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification39" on page 2945 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2946
   OtherIdentification <OthrId> [0..*]  2947
     Identification <Id> [1..1] Text 2947
     Suffix <Sfx> [0..1] Text 2947
     Type <Tp> [1..1] ± 2947
   Description <Desc> [0..1] Text 2947
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities 1761 August 2026
```

