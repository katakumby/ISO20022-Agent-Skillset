---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["30 reda.009.001.01 SecurityActivityAdviceV01", "30.2 Structure"]
file_pages: [1759]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.009.001.01"]
---

# 30.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1759 to 1759.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1759

```text
30.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctyActvtyAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1] ± 1760
   Pagination <Pgntn> [1..1] ± 1760
   SecurityActivity <SctyActvty> [1..1]  1760
     SystemDate <SysDt> [1..1] Date 1761
     Change <Chng> [0..*]  1761
       FinancialInstrumentIdentification <FinInstrmId> [1..1] ± C1, C2,
C3, C4,
C5
1761
       FieldName <FldNm> [1..1] Text 1762
       OldFieldValue <OdFldVal> [1..1] Text 1762
       NewFieldValue <NewFldVal> [1..1] Text 1762
       OperationTimeStamp <OprTmStmp> [1..1] DateTime 1762
   SupplementaryData <SplmtryData> [0..*] ± C6 1763
30.3 Constraints
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.009.001.01 SecurityActivityAdviceV01
Target2-Securities 1759 August 2026
```

