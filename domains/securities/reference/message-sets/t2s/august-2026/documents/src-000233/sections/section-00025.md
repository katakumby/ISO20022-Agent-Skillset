---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["3 admi.006.001.01 ResendRequestV01"]
file_pages: [57]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.006.001.01"]
---

# 3 admi.006.001.01 ResendRequestV01

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 57 to 57.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 57

```text
3 admi.006.001.01
ResendRequestV01
3.1 MessageDefinition Functionality
A system member or any parties authorised by them send a ResendRequest message to the Central
System (such as the T2S platform). The purpose of this request is, that the requesting party wants to
receive the "original" message once again. This might be caused through technical problems on the
receiving side (message could not be received or processed or is missing in the message sequencing)
or for archiving purposes.
Outline
The ResendRequestV01 MessageDefinition is composed of 3 MessageBuildingBlocks:
A. MessageHeader
Set of elements to identify the resend message.
B. ResendSearchCriteria
Defines the criteria to unambiguously identify the information to be resent.
C. SupplementaryData
Additional information that cannot be captured in the structured elements and/or any other specific
block.
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <RsndReq> [1..1]  
   MessageHeader <MsgHdr> [1..1] ± 58
   ResendSearchCriteria <RsndSchCrit> [1..*]  58
     BusinessDate <BizDt> [0..1] Date 59
     SequenceNumber <SeqNb> [0..1] Text 59
     SequenceRange <SeqRg> [0..1] ± 59
     OriginalMessageNameIdentification <OrgnlMsgNmId> [0..1] Text 60
     FileReference <FileRef> [0..1] Text 60
     Recipient <Rcpt> [1..1] ± 60
   SupplementaryData <SplmtryData> [0..*] ± C3 60
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
admi.006.001.01 ResendRequestV01
Target2-Securities 57 August 2026
```

