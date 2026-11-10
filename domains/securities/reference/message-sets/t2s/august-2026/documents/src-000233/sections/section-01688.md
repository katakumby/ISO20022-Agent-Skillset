---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["61 reda.044.001.01 EligibleCounterpartCSDStatusAdviceV01", "61.2 Structure"]
file_pages: [2336]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.044.001.01"]
---

# 61.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2336 to 2336.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2336

```text
61.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <ElgblCntrptCSDStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  2336
     MessageIdentification <MsgId> [1..1] Text 2337
     CreationDateTime <CreDtTm> [0..1] DateTime 2337
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2337
   StatusReason <StsRsn> [1..1]  C1 2337
     Status <Sts> [1..1] CodeSet 2338
     Reason <Rsn> [0..*]  2338
       Reason <Rsn> [1..1]  2338
{Or         Code <Cd> [1..1] CodeSet 2339
Or}         Proprietary <Prtry> [1..1] Text 2339
       AdditionalInformation <AddtlInf> [0..1] Text 2339
   SupplementaryData <SplmtryData> [0..*] ± C2 2339
61.3 Constraints
C1 StatusReasonRule
If Status equals 'Rejected' then Reason must be present.
C2 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
61.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
61.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.044.001.01
EligibleCounterpartCSDStatusAdviceV01
Target2-Securities 2336 August 2026
```

