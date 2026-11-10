---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["40 reda.020.001.01 SecuritiesAccountStatusAdviceV01", "40.2 Structure"]
file_pages: [2119]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.020.001.01"]
---

# 40.2 Structure

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 2119 to 2119.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2119

```text
40.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesAcctStsAdvc> [1..1]  
   MessageHeader <MsgHdr> [0..1]  2119
     MessageIdentification <MsgId> [1..1] Text 2120
     CreationDateTime <CreDtTm> [0..1] DateTime 2120
     OriginalBusinessInstruction <OrgnlBizInstr> [0..1] ± 2120
   SecuritiesAccountStatus <SctiesAcctSts> [1..1]  C1, C2 2120
     RelatedSecuritiesAccount <RltdSctiesAcct> [0..1] ± 2121
     Status <Sts> [1..1] CodeSet 2121
     StatusReason <StsRsn> [0..*]  2122
       Reason <Rsn> [1..1]  2122
{Or         Code <Cd> [1..1] CodeSet 2122
Or}         Proprietary <Prtry> [1..1] Text 2122
       AdditionalInformation <AddtlInf> [0..1] Text 2122
   SupplementaryData <SplmtryData> [0..*] ± C3 2122
40.3 Constraints
C1 PresenceRule
If Status equals COMP (Completed) then RelatedSecuritiesAccount must be present.
C2 StatusReasonRule
If Status equals REJT (Rejected) then StatusReason must be present.
C3 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
40.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
40.4.1 MessageHeader <MsgHdr>
Presence: [0..1]
Definition: Common business identification for the message.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.020.001.01 SecuritiesAccountStatusAdviceV01
Target2-Securities 2119 August 2026
```

