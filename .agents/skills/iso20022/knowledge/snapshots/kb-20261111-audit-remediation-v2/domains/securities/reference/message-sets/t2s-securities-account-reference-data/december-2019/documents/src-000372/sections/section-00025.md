---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["4 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "4.2 Structure"]
file_pages: [27]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.020.001.01"]
---

# 4.2 Structure

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 27 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 27

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  27
     MessageIdentification <MsgId> [1..1] Text 28
     CreationDateTime <CreDtTm> [0..1] DateTime 28
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 28
   SecuritiesAccountStatus <SctiesAcctSts> [1..1]  C1, C2 28
     RelatedSecuritiesAccount <RltdSctiesAcct> [0..1] ± 29
     Status <Sts> [1..1] CodeSet 29
     StatusReason <StsRsn> [0..*]  30
       Reason <Rsn> [1..1]  30
{Or         Code <Cd> [1..1] CodeSet 30
Or}         Proprietary <Prtry> [1..1] Text 30
       AdditionalInformation <AddtlInf> [0..1] Text 30
   SupplementaryData <SplmtryData> [0..*] ± C3 30
4.3 Constraints
C1 PresenceRule
If Status equals COMP (Completed) then RelatedSecuritiesAccount must be present.
C2 StatusReasonRule
If Status equals REJT (Rejected) then StatusReason must be present.
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
4.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
4.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities - Securities Account Reference Data 27 December 2019
```

