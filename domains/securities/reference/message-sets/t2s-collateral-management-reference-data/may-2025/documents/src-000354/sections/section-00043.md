---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["7 reda.044.001.01 EligibleCounterpartCSDStatusAdviceV01", "7.2 Structure"]
file_pages: [47]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.044.001.01"]
---

# 7.2 Structure

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 47 to 47.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 47

```text
7.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ElgblCntrptCSDStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  47
     MessageIdentification <MsgId> [1..1] Text 48
     CreationDateTime <CreDtTm> [0..1] DateTime 48
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 48
   StatusReason <StsRsn> [1..1]  C1 48
     Status <Sts> [1..1] CodeSet 49
     Reason <Rsn> [0..*]  49
       Reason <Rsn> [1..1]  49
{Or         Code <Cd> [1..1] CodeSet 50
Or}         Proprietary <Prtry> [1..1] Text 50
       AdditionalInformation <AddtlInf> [0..1] Text 50
   SupplementaryData <SplmtryData> [0..*] ± C2 50
7.3 Constraints
C1 StatusReasonRule
If Status equals 'Rejected' then Reason must be present.
C2 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
7.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
7.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
Approved by the Securities SEG on 17 April 2025. reda.044.001.01
EligibleCounterpartCSDStatusAdviceV01
Target2-Securities - Collateral Management Reference Data 47 May 2025
```

