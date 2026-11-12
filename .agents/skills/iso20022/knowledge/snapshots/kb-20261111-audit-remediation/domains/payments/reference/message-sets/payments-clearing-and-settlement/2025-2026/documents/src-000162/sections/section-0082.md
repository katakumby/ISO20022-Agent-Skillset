---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "PaymentReturn pacs.004.001.15 - 1", "First PaymentReturn"]
content_origin: "source-transcription"
---

# First PaymentReturn

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / PaymentReturn pacs.004.001.15 - 1 / First PaymentReturn.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P838** First PaymentReturn

**P839** Description

**P840** On receipt of an FIToFIPaymentCancellationRequest message from BBBB Bank, CCCC Bank checks with Seed Inc. whether it is willing to return the credited funds. Seed Inc. accepts to return the amount credited onto its account (EUR 74850) without requesting compensation. CCCC Bank sends a PaymentReturn message to BBBB Bank.

**P841** Business Data

**P842** PaymentReturn from CCCC Bank to BBBB Bank:

[T30 - complete table](../tables/tbl-0030.md)

**P843** Message Instance

**P844** <PmtRtr>

**P845** 	<GrpHdr>

**P846** 		<MsgId>CCCC/151122-PR007</MsgId>

**P847** 		<CreDtTm>2015-11-22T10:37:00</CreDtTm>

**P848** 		<NbOfTxs>1</NbOfTxs>

**P849** 		<SttlmInf>

**P850** 			<SttlmMtd>CLRG</SttlmMtd>

**P851** 			<ClrSys>

**P852** 				<Prtry>CBJ</Prtry>

**P853** 			</ClrSys>

**P854** 		</SttlmInf>

**P855** 		<InstgAgt>

**P856** 			<FinInstnId>

**P857** 				<BICFI>CCCCIE2D</BICFI>

**P858** 			</FinInstnId>

**P859** 		</InstgAgt>

**P860** 		<InstdAgt>

**P861** 			<FinInstnId>

**P862** 				<BICFI>BBBBIE2D</BICFI>

**P863** 			</FinInstnId>

**P864** 		</InstdAgt>

**P865** 	</GrpHdr>

**P866** 	<OrgnlGrpInf>

**P867** 		<OrgnlMsgId>BBBB/151109-CBJ056</OrgnlMsgId>

**P868** 		<OrgnlMsgNmId>pacs.008.001.12</OrgnlMsgNmId>

**P869** 		<OrgnlCreDtTm>2015-11-09T10:13:00</OrgnlCreDtTm>

**P870** 	</OrgnlGrpInf>

**P871** 	<TxInf>

**P872** 		<RtrId>CCCC/151122-PR007</RtrId>

**P873** 		<OrgnlInstrId>BBBB/151109-CBJ056/1</OrgnlInstrId>

**P874** 		<OrgnlEndToEndId>CROPS/SX-25T/2015-10-13</OrgnlEndToEndId>

**P875** 		<OrgnlTxId>AAAA/151109-CCT/EUR443/1</OrgnlTxId>

**P876** 		<OrgnlIntrBkSttlmAmt Ccy="EUR">74900</OrgnlIntrBkSttlmAmt>

**P877** 		<RtrdIntrBkSttlmAmt Ccy="EUR">74750</RtrdIntrBkSttlmAmt>

**P878** 		<IntrBkSttlmDt>2015-11-22</IntrBkSttlmDt>

**P879** 		<RtrdInstdAmt Ccy="EUR">74850</RtrdInstdAmt>

**P880** 		<ChrgBr>CRED</ChrgBr>

**P881** 		<ChrgsInf>

**P882** 			<Amt Ccy="EUR">100</Amt>

**P883** 			<Agt>

**P884** 				<FinInstnId>

**P885** 					<BICFI>CCCCIE2D</BICFI>

**P886** 				</FinInstnId>

**P887** 			</Agt>

**P888** 		</ChrgsInf>

**P889** 		<RtrRsnInf>

**P890** 			<Orgtr>

**P891** 				<Nm>Seed Inc.</Nm>

**P892** 			</Orgtr>

**P893** 			<Rsn>

**P894** 				<Cd>NARR</Cd>

**P895** 			</Rsn>

**P896** 			<AddtlInf>RETURN AFTER ACCEPTED PAYMENT CANCELLATION REQUEST</AddtlInf>

**P897** 		</RtrRsnInf>

**P898** 	</TxInf>

**P899** </PmtRtr>

