---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Receipt Acknowledgement - admi.007.001"]
content_origin: "source-transcription"
---

# Receipt Acknowledgement - admi.007.001

Source: [src-000343](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`. Locator: heading path Examples / Receipt Acknowledgement - admi.007.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P255** Receipt Acknowledgement - admi.007.001

**P256** Description 1

**P257** The Receipt Acknowledgement is used in this usage by T2S to inform a T2S Actor (Sender), that an incoming message has caused an error during its processing. It reports the error which occurred in an error code and, if available, in a textual description. In this example a Receipt Acknowledgement “Inbound Processing Rejection” referring to an incoming message with the ID INCOMINGMSG03 with error code “I012” and description “IICR001-The party technical 3 address does not exist” is sent to the corresponding party.

**P258** Message Instance 1

**P260** <RctAck>

**P261** 	<MsgId>

**P262** 		<MsgId>NONREF</MsgId>

**P263** 	</MsgId>

**P264** 	<Rpt>

**P265** 		<RltdRef>

**P266** 			<Ref>INCOMINGMSG03</Ref>

**P267** 		</RltdRef>

**P268** 		<ReqHdlg>

**P269** 			<StsCd>I012</StsCd>

**P270** 			<Desc>IICR001-The party technical address does not exist</Desc>

**P271** 		</ReqHdlg>

**P272** 	</Rpt>

**P273** </RctAck>

**P274** Description 2

**P275** The Receipt Acknowledgement Validation Result Resend message is used in this usage to inform the sender of a message that his request for resending a message could be successfully processed by T2S. It reports the positive status in a coded form. 

**P276** In this example a Receipt Acknowledgement “Validation Result Resend” referring to an incoming message with the ID RESENDREQOK01 with status code “OK” is sent to the corresponding party.

**P277** Message Instance 2

**P278** <RctAck>

**P279** 	<MsgId>

**P280** 		<MsgId>NONREF</MsgId>

**P281** 	</MsgId>

**P282** 	<Rpt>

**P283** 		<RltdRef>

**P284** 			<Ref>RESENDREQOK01</Ref>

**P285** 		</RltdRef>

**P286** 		<ReqHdlg>

**P287** 			<StsCd>OK</StsCd>

**P288** 		</ReqHdlg>

**P289** 	</Rpt>

**P290** </RctAck>

