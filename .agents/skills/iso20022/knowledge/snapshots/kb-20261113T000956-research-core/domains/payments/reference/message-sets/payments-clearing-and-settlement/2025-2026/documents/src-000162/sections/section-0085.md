---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "PaymentReturn pacs.004.001.15 - 2", "First PaymentReturn"]
content_origin: "source-transcription"
---

# First PaymentReturn

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / PaymentReturn pacs.004.001.15 - 2 / First PaymentReturn.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P969** First PaymentReturn

**P970** Description

**P971** On 28 June 2015, upon receipt of a direct debit instruction received from ABABUS23 for the collection of USD 1025, and after having checked the instruction, BBBBUS39 realises that the account specified for debtor Jones does not allow direct debits. BBBBUS39 therefore decides to send a PaymentReturn message to ABABUS23, specifying the reason, and taking charges for USD 50.

**P972** Business Data

**P973** PaymentReturn from BBBBUS39 to ABABUS23:

[T32 - complete table](../tables/tbl-0032.md)

**P974** Message Instance

**P975** <PmtRtr>

**P976** 	<GrpHdr>

**P977** 		<MsgId>BBBBUS39-RETURN-0123</MsgId>

**P978** 		<CreDtTm>2015-06-29T11:15:00</CreDtTm>

**P979** 		<NbOfTxs>1</NbOfTxs>

**P980** 		<SttlmInf>

**P981** 			<SttlmMtd>INGA</SttlmMtd>

**P982** 		</SttlmInf>

**P983** 		<InstgAgt>

**P984** 			<FinInstnId>

**P985** 				<BICFI>BBBBUS39</BICFI>

**P986** 			</FinInstnId>

**P987** 		</InstgAgt>

**P988** 		<InstdAgt>

**P989** 			<FinInstnId>

**P990** 				<BICFI>ABABUS23</BICFI>

**P991** 			</FinInstnId>

**P992** 		</InstdAgt>

**P993** 	</GrpHdr>

**P994** 	<OrgnlGrpInf>

**P995** 		<OrgnlMsgId>ABABUS23-589cd</OrgnlMsgId>

**P996** 		<OrgnlMsgNmId>pacs.003.001.12</OrgnlMsgNmId>

**P997** 		<OrgnlCreDtTm>2015-06-28T15:02:00</OrgnlCreDtTm>

**P998** 	</OrgnlGrpInf>

**P999** 	<TxInf>

**P1000** 		<RtrId>AB/RETURN765</RtrId>

**P1001** 		<OrgnlInstrId>VA060327/0123</OrgnlInstrId>

**P1002** 		<RtrdIntrBkSttlmAmt Ccy="USD">975</RtrdIntrBkSttlmAmt>

**P1003** 		<IntrBkSttlmDt>2015-07-29</IntrBkSttlmDt>

**P1004** 		<ChrgBr>CRED</ChrgBr>

**P1005** 		<ChrgsInf>

**P1006** 			<Amt Ccy="USD">50</Amt>

**P1007** 			<Agt>

**P1008** 				<FinInstnId>

**P1009** 					<BICFI>BBBBUS39</BICFI>

**P1010** 				</FinInstnId>

**P1011** 			</Agt>

**P1012** 		</ChrgsInf>

**P1013** 		<RtrRsnInf>

**P1014** 			<Orgtr>

**P1015** 				<Id>

**P1016** 					<OrgId>

**P1017** 						<AnyBIC>BBBBUS39</AnyBIC>

**P1018** 					</OrgId>

**P1019** 				</Id>

**P1020** 			</Orgtr>

**P1021** 			<Rsn>

**P1022** 				<Cd>AG01</Cd>

**P1023** 			</Rsn>

**P1024** 		</RtrRsnInf>

**P1025** 		<OrgnlTxRef>

**P1026** 			<IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>

**P1027** 			<IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>

**P1028** 			<ReqdColltnDt>2015-07-13</ReqdColltnDt>

**P1029** 			<MndtRltdInf>

**P1030** 				<DrctDbtMndt>

**P1031** 					<MndtId>VIRGAY123</MndtId>

**P1032** 				</DrctDbtMndt>

**P1033** 			</MndtRltdInf>

**P1034** 			<Dbtr>

**P1035** 				<Pty>

**P1036** 					<Nm>Jones</Nm>

**P1037** 					<PstlAdr>

**P1038** 						<StrtNm>Hudson Street</StrtNm>

**P1039** 						<BldgNb>19</BldgNb>

**P1040** 						<PstCd>NJ 07302</PstCd>

**P1041** 						<TwnNm>Jersey City</TwnNm>

**P1042** 						<Ctry>US</Ctry>

**P1043** 					</PstlAdr>

**P1044** 				</Pty>	

**P1045** 			</Dbtr>

**P1046** 			<Cdtr>

**P1047** 				<Pty>

**P1048** 					<Nm>Virgay</Nm>

**P1049** 					<PstlAdr>

**P1050** 						<StrtNm>Virginia Lane</StrtNm>

**P1051** 						<BldgNb>36</BldgNb>

**P1052** 						<PstCd>NJ 07311</PstCd>

**P1053** 						<TwnNm>Jersey City</TwnNm>

**P1054** 						<Ctry>US</Ctry>

**P1055** 					</PstlAdr>

**P1056** 				</Pty>

**P1057** 			</Cdtr>

**P1058** 		</OrgnlTxRef>

**P1059** 	</TxInf>

**P1060** </PmtRtr>

