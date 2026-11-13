---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000343"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Resend Request - admi.006.001"]
content_origin: "source-transcription"
---

# Resend Request - admi.006.001

Source: [src-000343](../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart1_Target2Securities_Administration_2023_2024_v2.docx`. Locator: heading path Examples / Resend Request - admi.006.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P230** Resend Request - admi.006.001

**P231** Description

**P232** The Resend Request message is sent by a System Member to the System Transaction Administrator to request the resending of an already sent message. In this example a Resend Request with the Message Identification RESENDREQUEST01 and the corresponding sequence number “1234567890111213” and the business date 2017.11.11 is sent to T2S.

**P233** Selection criteria chosen for the message resend request:

**P234** Business Date: 2017-11-11

**P235** Sequence Number: “1234567890111213“

**P236** Date when the Report was produced:  2017-08-13

**P237** Party Technical address to which the original messages was sent: cn=smith,ou= t2s-ops, o=bnkacctt

**P238** Message Instance

**P239** <RsndReq>

**P240** 		<MsgHdr>

**P241** 			<MsgId>RESENDREQUEST01</MsgId>

**P242** 		</MsgHdr>

**P243** 		<RsndSchCrit>

**P244** 			<BizDt>2017-11-11</BizDt>

**P245** 			<SeqNb>1234567890111213</SeqNb>

**P246** 			<Rcpt>

**P247** 			 <Id>

**P248** 			  <NmAndAdr>

**P249** 				<Nm>cn=smith,ou= t2s-ops, o=bnkacctt</Nm>

**P250** 			  </NmAndAdr>

**P251** 			 </Id>				

**P252** 			</Rcpt>

**P253** 		</RsndSchCrit>

**P254**        </RsndReq>

