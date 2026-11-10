---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["6 reda.028.001.01 CollateralDataStatusAdviceV01", "6.2 Structure"]
file_pages: [37]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 6.2 Structure

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 37 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 37

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <CollDataStsAdvc> [1..1]  C6, C7
   MessageHeader <MsgHdr> [0..1]  38
     MessageIdentification <MsgId> [1..1] Text 39
     CreationDateTime <CreDtTm> [0..1] DateTime 39
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 39
   StatusReason <StsRsn> [0..1]  C8 39
     Status <Sts> [1..1] CodeSet 40
     Reason <Rsn> [0..*]  40
       Reason <Rsn> [1..1]  40
{Or         Code <Cd> [1..1] CodeSet 41
Or}         Proprietary <Prtry> [1..1] Text 41
       AdditionalInformation <AddtlInf> [0..1] Text 41
   StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm> [0..1]  C9 41
     Status <Sts> [1..1] CodeSet 42
     Reason <Rsn> [0..*]  42
       Reason <Rsn> [1..1]  43
{Or         Code <Cd> [1..1] CodeSet 43
Or}         Proprietary <Prtry> [1..1] ± 43
       FinancialInstrument <FinInstrm> [0..1] ± C1, C2,
C3, C4,
C5
43
       AdditionalInformation <AddtlInf> [0..1] Text 44
     EligibilitySetProfile <ElgbltySetPrfl> [0..1] ± 45
   SupplementaryData <SplmtryData> [0..*] ± C10 45
6.3 Constraints
C1 DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification
must be present.
C2 DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG on 17 April 2025. reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 37 May 2025
```

