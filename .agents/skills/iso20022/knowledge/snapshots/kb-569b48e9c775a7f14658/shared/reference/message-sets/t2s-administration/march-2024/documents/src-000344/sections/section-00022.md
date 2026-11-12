---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 admi.006.001.01 ResendRequestV01"]
file_pages: [27]
content_origin: "source-text-extraction"
mentioned_message_ids: ["admi.006.001.01"]
---

# 3 admi.006.001.01 ResendRequestV01

Source: [src-000344](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 27 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 27

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
   MessageHeader <MsgHdr> [1..1] ± 28
   ResendSearchCriteria <RsndSchCrit> [1..*]  28
     BusinessDate <BizDt> [0..1] Date 29
     SequenceNumber <SeqNb> [0..1] Text 29
     SequenceRange <SeqRg> [0..1] ± 29
     OriginalMessageNameIdentification <OrgnlMsgNmId> [0..1] Text 30
     FileReference <FileRef> [0..1] Text 30
     Recipient <Rcpt> [1..1] ± 30
   SupplementaryData <SplmtryData> [0..*] ± C3 30
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
admi.006.001.01 ResendRequestV01
Target2-Securities - Administration - Maintenance 2023 -
2024
27 March 2024
```

