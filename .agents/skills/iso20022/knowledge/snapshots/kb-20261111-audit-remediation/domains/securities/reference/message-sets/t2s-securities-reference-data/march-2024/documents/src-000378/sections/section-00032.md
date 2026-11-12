---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["5 reda.009.001.01 SecurityActivityAdviceV01", "5.2 Structure"]
file_pages: [72]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.009.001.01"]
---

# 5.2 Structure

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 72 to 72.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 72

```text
5.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyActvtyAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 73
   Pagination <Pgntn> [1..1] ± 73
   SecurityActivity <SctyActvty> [1..1]  73
     SystemDate <SysDt> [1..1] Date 74
     Change <Chng> [0..*]  74
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C1, C2,
C3, C4,
C5
74
       FieldName <FldNm> [1..1] Text 75
       OldFieldValue <OdFldVal> [1..1] Text 75
       NewFieldValue <NewFldVal> [1..1] Text 75
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 75
   SupplementaryData <SplmtryData> [0..*] ± C6 76
5.3 Constraints
C1 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C2 DescriptionUsageRule
Description must be used alone as the last resort.
C3 ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C4 ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification
must be present.
C5 OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
C6 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities - Securities Reference Data 72 March 2024
```

