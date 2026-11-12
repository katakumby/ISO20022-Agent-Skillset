---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["48 reda.028.001.01 CollateralDataStatusAdviceV01", "48.2 Structure"]
file_pages: [2194]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 48.2 Structure

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2194 to 2194.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2194

```text
48.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CollDataStsAdvc> [1..1]  C6, C7
   MessageHeader <MsgHdr> [0..1]  2195
     MessageIdentification <MsgId> [1..1] Text 2196
     CreationDateTime <CreDtTm> [0..1] DateTime 2196
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2196
   StatusReason <StsRsn> [0..1]  C8 2196
     Status <Sts> [1..1] CodeSet 2197
     Reason <Rsn> [0..*]  2197
       Reason <Rsn> [1..1]  2197
{Or         Code <Cd> [1..1] CodeSet 2198
Or}         Proprietary <Prtry> [1..1] Text 2198
       AdditionalInformation <AddtlInf> [0..1] Text 2198
   StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm> [0..1]  C9 2198
     Status <Sts> [1..1] CodeSet 2199
     Reason <Rsn> [0..*]  2199
       Reason <Rsn> [1..1]  2200
{Or         Code <Cd> [1..1] CodeSet 2200
Or}         Proprietary <Prtry> [1..1] ± 2200
       FinancialInstrument <FinInstrm> [0..1] ± C1, C2,
C3, C4,
C5
2200
       AdditionalInformation <AddtlInf> [0..1] Text 2201
     EligibilitySetProfile <ElgbltySetPrfl> [0..1] ± 2202
   SupplementaryData <SplmtryData> [0..*] ± C10 2202
48.3 Constraints
C1 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C2 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities 2194 August 2026
```

