---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000173"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "CustomerPaymentStatusReport pain.002.001.15 - 1"]
content_origin: "source-transcription"
---

# CustomerPaymentStatusReport pain.002.001.15 - 1

Source: [src-000173](../../../../../../../../../evidence/omitted/baf7abf3460122a33db6052d.md). Locator: heading path Business Examples / CustomerPaymentStatusReport pain.002.001.15 - 1.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P542** CustomerPaymentStatusReport pain.002.001.15 - 1

**P543** Description

**P544** As follow-up to the payment initiation by ABC Corporation, BBBBUS33 sends a CustomerPaymentStatusReport to acknowledge that the message passed technical validation and was accepted, based on the customer profile.

**P545** Business Data

**P546** CustomerPaymentStatusReport from BBBB Bank to ABC Corporation:

[T25 - complete table](../tables/tbl-0025.md)

**P547** Message Instance

**P548** <CstmrPmtStsRpt>

**P549** 	<GrpHdr>

**P550** 		<MsgId>BBBB/120928-PSR/001</MsgId>

**P551** 		<CreDtTm>2012-09-28T14:09:00</CreDtTm>

**P552** 		<InitgPty>

**P553** 			<Nm>ABC Corporation</Nm>

**P554** 			<PstlAdr>

**P555** 				<StrtNm>Times Square</StrtNm>

**P556** 				<BldgNb>7</BldgNb>

**P557** 				<PstCd>NY 10036</PstCd>

**P558** 				<TwnNm>New York</TwnNm>

**P559** 				<Ctry>US</Ctry>

**P560** 			</PstlAdr>

**P561** 		</InitgPty>

**P562** 		<DbtrAgt>

**P563** 			<FinInstnId>

**P564** 				<BICFI>BBBBUS33</BICFI>

**P565** 			</FinInstnId>

**P566** 		</DbtrAgt>

**P567** 	</GrpHdr>

**P568** 	<OrgnlGrpInfAndSts>

**P569** 		<OrgnlMsgId>ABC/120928/CCT001</OrgnlMsgId>

**P570** 		<OrgnlMsgNmId>pain.001.001.13</OrgnlMsgNmId>

**P571** 		<OrgnlCreDtTm>2012-09-28T14:07:00</OrgnlCreDtTm>

**P572** 		<OrgnlNbOfTxs>3</OrgnlNbOfTxs>

**P573** 		<OrgnlCtrlSum>11500000</OrgnlCtrlSum>

**P574** 		<GrpSts>ACCP</GrpSts>

**P575** 	</OrgnlGrpInfAndSts>

**P576** </CstmrPmtStsRpt>

