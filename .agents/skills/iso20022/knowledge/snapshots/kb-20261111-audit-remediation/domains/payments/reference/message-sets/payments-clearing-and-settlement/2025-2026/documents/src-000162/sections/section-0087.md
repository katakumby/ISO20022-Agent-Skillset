---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFIPaymentReversal pacs.007.001.14"]
content_origin: "source-transcription"
---

# FIToFIPaymentReversal pacs.007.001.14

Source: [src-000162](../../../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md). Locator: heading path Business Examples / FIToFIPaymentReversal pacs.007.001.14.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1160** FIToFIPaymentReversal pacs.007.001.14

**P1161** Description 

**P1162** On 6 July 2015, AAAAUS29 finds out that the FIToFICustomerDirectDebit message it sent to ABABUS23 on 28 June 2015, for the collection of USD 1025 from debtor Jones, was a duplicated payment instruction. As the requested collection date was 13 July 2015, AAAAUS29 decides to send an FIToFIPaymentReversal message to its correspondent ABABUS23, giving the reason for the reversal.

**P1163** Any potential charges related to the reversal will be settled outside of the message, that is as part of the monthly billing process.

**P1164** The FIToFICustomerDirectDebit instruction from AAAAUS29 to ABABUS23 is included in the business example section of the FIToFICustomerDirectDebit message.

**P1165** Business Data

**P1166** FIToFIPaymentReversal from AAAAUS29 to ABABUS23:

[T34 - complete table](../tables/tbl-0034.md)

**P1167** Message Instance

**P1168** <FIToFIPmtRvsl>

**P1169** 	<GrpHdr>

**P1170** 		<MsgId>AAAAUS29-REVERSAL/0012</MsgId>

**P1171** 		<CreDtTm>2015-07-06T10:35:00</CreDtTm>

**P1172** 		<NbOfTxs>1</NbOfTxs>

**P1173** 		<IntrBkSttlmDt>2015-07-06</IntrBkSttlmDt>

**P1174** 		<SttlmInf>

**P1175** 			<SttlmMtd>INDA</SttlmMtd>

**P1176** 		</SttlmInf>

**P1177** 		<InstgAgt>

**P1178** 			<FinInstnId>

**P1179** 				<BICFI>AAAAUS29</BICFI>

**P1180** 			</FinInstnId>

**P1181** 		</InstgAgt>

**P1182** 		<InstdAgt>

**P1183** 			<FinInstnId>

**P1184** 				<BICFI>ABABUS23</BICFI>

**P1185** 			</FinInstnId>

**P1186** 		</InstdAgt>

**P1187** 	</GrpHdr>

**P1188** 	<OrgnlGrpInf>

**P1189** 		<OrgnlMsgId>AAAA120628-123v</OrgnlMsgId>

**P1190** 		<OrgnlMsgNmId>pacs.003.001.12</OrgnlMsgNmId>

**P1191** 		<OrgnlCreDtTm>2015-06-28T10:05:00</OrgnlCreDtTm>

**P1192** 	</OrgnlGrpInf>

**P1193** 	<TxInf>

**P1194** 		<RvslId>AAAAUS29_REV2563</RvslId>

**P1195** 		<OrgnlEndToEndId>VA060327/0123</OrgnlEndToEndId>

**P1196** 		<OrgnlTxId>AAAAUS29/150628/ad458</OrgnlTxId>

**P1197** 		<RvsdIntrBkSttlmAmt Ccy="USD">1025</RvsdIntrBkSttlmAmt>

**P1198** 		<RvsdInstdAmt Ccy="USD">1025</RvsdInstdAmt>

**P1199** 		<RvslRsnInf>

**P1200** 			<Orgtr>

**P1201** 				<Id>

**P1202** 					<OrgId>

**P1203** 						<AnyBIC>AAAAUS29</AnyBIC>

**P1204** 					</OrgId>

**P1205** 				</Id>

**P1206** 			</Orgtr>

**P1207** 			<Rsn>

**P1208** 				<Cd>AM05</Cd>

**P1209** 			</Rsn>

**P1210** 		</RvslRsnInf>

**P1211** 		<OrgnlTxRef>

**P1212** 			<IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>

**P1213** 			<IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>

**P1214** 			<ReqdColltnDt>2015-07-13</ReqdColltnDt>

**P1215** 			<MndtRltdInf>

**P1216** 				<DrctDbtMndt>

**P1217** 					<MndtId>VIRGAY123</MndtId>

**P1218** 				</DrctDbtMndt>

**P1219** 			</MndtRltdInf>

**P1220** 			<Dbtr>

**P1221** 				<Pty>

**P1222** 					<Nm>Jones</Nm>

**P1223** 					<PstlAdr>

**P1224** 						<StrtNm>Hudson Street</StrtNm>

**P1225** 						<BldgNb>19</BldgNb>

**P1226** 						<PstCd>NJ 07302</PstCd>

**P1227** 						<TwnNm>Jersey City</TwnNm>

**P1228** 						<Ctry>US</Ctry>

**P1229** 					</PstlAdr>

**P1230** 				</Pty>	

**P1231** 			</Dbtr>

**P1232** 			<DbtrAcct>

**P1233** 				<Id>

**P1234** 					<Othr>

**P1235** 						<Id>123456</Id>

**P1236** 					</Othr>

**P1237** 				</Id>

**P1238** 			</DbtrAcct>

**P1239** 			<DbtrAgt>

**P1240** 				<FinInstnId>

**P1241** 					<BICFI>BBBBUS39</BICFI>

**P1242** 				</FinInstnId>

**P1243** 			</DbtrAgt>

**P1244** 			<Cdtr>

**P1245** 				<Pty>

**P1246** 					<Nm>Virgay</Nm>

**P1247** 					<PstlAdr>

**P1248** 						<StrtNm>Virginia Lane</StrtNm>

**P1249** 						<BldgNb>36</BldgNb>

**P1250** 						<PstCd>NJ 07311</PstCd>

**P1251** 						<TwnNm>Jersey City</TwnNm>

**P1252** 						<Ctry>US</Ctry>

**P1253** 					</PstlAdr>

**P1254** 				</Pty>

**P1255** 			</Cdtr>

**P1256** 		</OrgnlTxRef>

**P1257** 	</TxInf>

**P1258** </FIToFIPmtRvsl>

