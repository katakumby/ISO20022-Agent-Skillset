---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "PaymentReturn pacs.004.001.15 - 1", "Second PaymentReturn"]
content_origin: "source-transcription"
---

# Second PaymentReturn

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / PaymentReturn pacs.004.001.15 - 1 / Second PaymentReturn.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P900** Second PaymentReturn

**P901** Description

**P902** On receipt of the payment return message from CCCC Bank, BBBB Bank deducts processing charges for the return message, credits the account of AAAA Bank and forwards the payment return message to AAAA Bank.

**P903** Business Data

**P904** PaymentReturn from BBBB Bank to AAAA Bank:

[T31 - complete table](../tables/tbl-0031.md)

**P905** Message Instance

**P906** <PmtRtr>

**P907** 	<GrpHdr>

**P908** 		<MsgId>BBBB/151122-PR05</MsgId>

**P909** 		<CreDtTm>2015-11-22T11:15:00</CreDtTm>

**P910** 		<NbOfTxs>1</NbOfTxs>

**P911** 		<SttlmInf>

**P912** 			<SttlmMtd>INGA</SttlmMtd>

**P913** 		</SttlmInf>

**P914** 		<InstgAgt>

**P915** 			<FinInstnId>

**P916** 				<BICFI>BBBBIE2D</BICFI>

**P917** 			</FinInstnId>

**P918** 		</InstgAgt>

**P919** 		<InstdAgt>

**P920** 			<FinInstnId>

**P921** 				<BICFI>AAAAGB2L</BICFI>

**P922** 			</FinInstnId>

**P923** 		</InstdAgt>

**P924** 	</GrpHdr>

**P925** 	<OrgnlGrpInf>

**P926** 		<OrgnlMsgId>AAAA/151109-CCT/EUR443</OrgnlMsgId>

**P927** 		<OrgnlMsgNmId>pacs.008.001.12</OrgnlMsgNmId>

**P928** 		<OrgnlCreDtTm>2015-11-09T10:03:13</OrgnlCreDtTm>

**P929** 	</OrgnlGrpInf>

**P930** 	<TxInf>

**P931** 		<RtrId>BBBB/151122-PR05/1</RtrId>

**P932** 		<OrgnlInstrId>AAAA/151109-CCT/EUR443/1</OrgnlInstrId>

**P933** 		<OrgnlEndToEndId>CROPS/SX-25T/2015-10-13</OrgnlEndToEndId>

**P934** 		<OrgnlTxId>AAAA/151109-CCT/EUR443/1</OrgnlTxId>

**P935** 		<OrgnlIntrBkSttlmAmt Ccy="EUR">75000</OrgnlIntrBkSttlmAmt>

**P936** 		<RtrdIntrBkSttlmAmt Ccy="EUR">74650</RtrdIntrBkSttlmAmt>

**P937** 		<IntrBkSttlmDt>2015-11-22</IntrBkSttlmDt>

**P938** 		<RtrdInstdAmt Ccy="EUR">74850</RtrdInstdAmt>

**P939** 		<ChrgBr>CRED</ChrgBr>

**P940** 		<ChrgsInf>

**P941** 			<Amt Ccy="EUR">100</Amt>

**P942** 			<Agt>

**P943** 				<FinInstnId>

**P944** 					<BICFI>CCCCIE2D</BICFI>

**P945** 				</FinInstnId>

**P946** 			</Agt>

**P947** 		</ChrgsInf>

**P948** 		<ChrgsInf>

**P949** 			<Amt Ccy="EUR">100</Amt>

**P950** 			<Agt>

**P951** 				<FinInstnId>

**P952** 					<BICFI>BBBBIE2D</BICFI>

**P953** 				</FinInstnId>

**P954** 			</Agt>

**P955** 		</ChrgsInf>

**P956** 		<RtrRsnInf>

**P957** 			<Orgtr>

**P958** 				<Nm>Seed Inc.</Nm>

**P959** 			</Orgtr>

**P960** 			<Rsn>

**P961** 				<Cd>NARR</Cd>

**P962** 			</Rsn>

**P963** 			<AddtlInf>RETURN AFTER ACCEPTED PAYMENT CANCELLATION REQUEST</AddtlInf>

**P964** 		</RtrRsnInf>

**P965** 	</TxInf>

**P966** </PmtRtr>

