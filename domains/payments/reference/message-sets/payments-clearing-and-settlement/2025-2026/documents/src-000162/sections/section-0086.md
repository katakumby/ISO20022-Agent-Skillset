---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "PaymentReturn pacs.004.001.15 - 2", "Second PaymentReturn"]
content_origin: "source-transcription"
---

# Second PaymentReturn

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / PaymentReturn pacs.004.001.15 - 2 / Second PaymentReturn.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1061** Second PaymentReturn

**P1062** Description 

**P1063** On 29 June 2015, upon receipt of a PaymentReturn message from BBBBUS39, ABABUS23 forwards the PaymentReturn instruction to AAAAUS29, the account servicer for creditor Virgay. It forwards the reason for the return and takes USD 35 for charges.  Virgay will be informed about the debit on its account through its statement.

**P1064** Business Data

**P1065** PaymentReturn from ABABUS23 to AAAAUS29:

[T33 - complete table](../tables/tbl-0033.md)

**P1066** Message Instance

**P1067** <PmtRtr>

**P1068** 	<GrpHdr>

**P1069** 		<MsgId>ABABUS23RETURN-546</MsgId>

**P1070** 		<CreDtTm>2015-06-29T13:28:00</CreDtTm>

**P1071** 		<NbOfTxs>1</NbOfTxs>

**P1072** 		<SttlmInf>

**P1073** 			<SttlmMtd>INGA</SttlmMtd>

**P1074** 		</SttlmInf>

**P1075** 		<InstgAgt>

**P1076** 			<FinInstnId>

**P1077** 				<BICFI>ABABUS23</BICFI>

**P1078** 			</FinInstnId>

**P1079** 		</InstgAgt>

**P1080** 		<InstdAgt>

**P1081** 			<FinInstnId>

**P1082** 				<BICFI>AAAAUS29</BICFI>

**P1083** 			</FinInstnId>

**P1084** 		</InstdAgt>

**P1085** 	</GrpHdr>

**P1086** 	<OrgnlGrpInf>

**P1087** 		<OrgnlMsgId>AAAA060327-123v</OrgnlMsgId>

**P1088** 		<OrgnlMsgNmId>pacs.003.001.12</OrgnlMsgNmId>

**P1089** 		<OrgnlCreDtTm>2015-06-28T10:05:00</OrgnlCreDtTm>

**P1090** 	</OrgnlGrpInf>

**P1091** 	<TxInf>

**P1092** 		<RtrId>ABABUS23/RETURN765</RtrId>

**P1093** 		<RtrdIntrBkSttlmAmt Ccy="USD">1110</RtrdIntrBkSttlmAmt>

**P1094** 		<IntrBkSttlmDt>2015-06-29</IntrBkSttlmDt>

**P1095** 		<ChrgBr>CRED</ChrgBr>

**P1096** 		<ChrgsInf>

**P1097** 			<Amt Ccy="USD">50</Amt>

**P1098** 			<Agt>

**P1099** 				<FinInstnId>

**P1100** 					<BICFI>BBBBUS39</BICFI>

**P1101** 				</FinInstnId>

**P1102** 			</Agt>

**P1103** 		</ChrgsInf>

**P1104** 		<ChrgsInf>

**P1105** 			<Amt Ccy="USD">35</Amt>

**P1106** 			<Agt>

**P1107** 				<FinInstnId>

**P1108** 					<BICFI>ABABUS23</BICFI>

**P1109** 				</FinInstnId>

**P1110** 			</Agt>

**P1111** 		</ChrgsInf>

**P1112** 		<RtrRsnInf>

**P1113** 			<Orgtr>

**P1114** 				<Id>

**P1115** 					<OrgId>

**P1116** 						<AnyBIC>BBBBUS39</AnyBIC>

**P1117** 					</OrgId>

**P1118** 				</Id>

**P1119** 			</Orgtr>

**P1120** 			<Rsn>

**P1121** 				<Cd>AG01</Cd>

**P1122** 			</Rsn>

**P1123** 		</RtrRsnInf>

**P1124** 		<OrgnlTxRef>

**P1125** 			<IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>

**P1126** 			<IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>

**P1127** 			<ReqdColltnDt>2015-07-13</ReqdColltnDt>

**P1128** 			<MndtRltdInf>

**P1129** 				<DrctDbtMndt>

**P1130** 					<MndtId>VIRGAY123</MndtId>

**P1131** 				</DrctDbtMndt>

**P1132** 			</MndtRltdInf>

**P1133** 			<Dbtr>

**P1134** 				<Pty>

**P1135** 					<Nm>Jones</Nm>

**P1136** 					<PstlAdr>

**P1137** 						<StrtNm>Hudson Street</StrtNm>

**P1138** 						<BldgNb>19</BldgNb>

**P1139** 						<PstCd>NJ 07302</PstCd>

**P1140** 						<TwnNm>Jersey City</TwnNm>

**P1141** 						<Ctry>US</Ctry>

**P1142** 					</PstlAdr>

**P1143** 				</Pty>	

**P1144** 			</Dbtr>

**P1145** 			<Cdtr>

**P1146** 				<Pty>

**P1147** 					<Nm>Virgay</Nm>

**P1148** 					<PstlAdr>

**P1149** 						<StrtNm>Virginia Lane</StrtNm>

**P1150** 						<BldgNb>36</BldgNb>

**P1151** 						<PstCd>NJ 07311</PstCd>

**P1152** 						<TwnNm>Jersey City</TwnNm>

**P1153** 						<Ctry>US</Ctry>

**P1154** 					</PstlAdr>

**P1155** 				</Pty>

**P1156** 			</Cdtr>

**P1157** 		</OrgnlTxRef>

**P1158** 	</TxInf>

**P1159** </PmtRtr>

