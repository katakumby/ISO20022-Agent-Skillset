---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesTransactionPostingReport semt.017.001.14"]
content_origin: "source-transcription"
---

# SecuritiesTransactionPostingReport semt.017.001.14

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesTransactionPostingReport semt.017.001.14.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1138** SecuritiesTransactionPostingReport semt.017.001.14

**P1139** Description

**P1140** On the 15 January 2019, the account servicer, Dresdner Bank London (DRESGB2L), sends to its customer Dresdner Bank Frankfurt (DRESDEFF) a Securities Transaction Posting Report (semt.017.001.07) including all the transactions that settled over a period of time.

**P1141** Business Data

**P1142** Number of Pages: 1

**P1143** Report Number: 124

**P1144** Statement Period: from 24/01/2019 to 25/01/2019

**P1145** Frequency: daily

**P1146** Update Type: complete

**P1147** Statement Basis: settled

**P1148** Activity Indicator: true

**P1149** Sub Account Indicator: false

**P1150** Safekeeping Account: 222s

**P1151** Financial Instrument: GB0000987654

**P1152** Message Instance

**P1153** <SctiesTxPstngRpt>

**P1154** 	<Pgntn>

**P1155** 		<PgNb>1</PgNb>

**P1156** 		<LastPgInd>true</LastPgInd>

**P1157** 	</Pgntn>

**P1158** 	<StmtGnlDtls>

**P1159** 		<RptNb>

**P1160** 			<Shrt>124</Shrt>

**P1161** 		</RptNb>

**P1162** 		<StmtPrd>

**P1163** 			<FrDtToDt>

**P1164** 				<FrDt>2019-01-14</FrDt>

**P1165** 				<ToDt>2019-01-15</ToDt>

**P1166** 			</FrDtToDt>

**P1167** 		</StmtPrd>

**P1168** 		<Frqcy>

**P1169** 			<Cd>DAIL</Cd>

**P1170** 		</Frqcy>

**P1171** 		<UpdTp>

**P1172** 			<Cd>COMP</Cd>

**P1173** 		</UpdTp>

**P1174** 		<StmtBsis>

**P1175** 			<Cd>SETT</Cd>

**P1176** 		</StmtBsis>

**P1177** 		<ActvtyInd>true</ActvtyInd>

**P1178** 		<SubAcctInd>false</SubAcctInd>

**P1179** 	</StmtGnlDtls>

**P1180** 	<SfkpgAcct>

**P1181** 		<Id>222S</Id>

**P1182** 	</SfkpgAcct>

**P1183** 	<FinInstrmDtls>

**P1184** 		<FinInstrmId>

**P1185** 			<ISIN>GB0000987654</ISIN>

**P1186** 		</FinInstrmId>

**P1187** 		<Tx>

**P1188** 			<AcctOwnrTxId>FRTJ123REC1</AcctOwnrTxId>

**P1189** 			<TxDtls>

**P1190** 				<TxActvty>

**P1191** 					<Cd>SETT</Cd>

**P1192** 				</TxActvty>

**P1193** 				<SttlmTxOrCorpActnEvtTp>

**P1194** 					<SctiesTxTp>

**P1195** 						<Cd>TRAD</Cd>

**P1196** 					</SctiesTxTp>

**P1197** 				</SttlmTxOrCorpActnEvtTp>

**P1198** 				<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P1199** 				<Pmt>FREE</Pmt>

**P1200** 				<PstngQty>

**P1201** 					<Qty>

**P1202** 						<FaceAmt>6000000</FaceAmt>

**P1203** 					</Qty>

**P1204** 				</PstngQty>

**P1205** 				<FctvSttlmDt>

**P1206** 					<Dt>2019-01-15</Dt>

**P1207** 				</FctvSttlmDt>

**P1208** 				<DlvrgSttlmPties>

**P1209** 					<Dpstry>

**P1210** 						<Id>

**P1211** 							<AnyBIC>CRSTGB22</AnyBIC>

**P1212** 						</Id>

**P1213** 					</Dpstry>

**P1214** 					<Pty1>

**P1215** 						<Id>

**P1216** 							<PrtryId>

**P1217** 								<Id>456</Id>

**P1218** 								<Issr>CRST</Issr>

**P1219** 							</PrtryId>

**P1220** 						</Id>

**P1221** 					</Pty1>

**P1222** 					<Pty2>

**P1223** 						<Id>

**P1224** 							<AnyBIC>CPFIDEFF</AnyBIC>

**P1225** 						</Id>

**P1226** 					</Pty2>

**P1227** 				</DlvrgSttlmPties>

**P1228** 				<RcvgSttlmPties>

**P1229** 					<Pty1>

**P1230** 						<Id>

**P1231** 							<PrtryId>

**P1232** 								<Id>123</Id>

**P1233** 								<Issr>CRST</Issr>

**P1234** 							</PrtryId>

**P1235** 						</Id>

**P1236** 					</Pty1>

**P1237** 					<Pty2>

**P1238** 						<Id>

**P1239** 							<AnyBIC>DRESDEFF</AnyBIC>

**P1240** 						</Id>

**P1241** 					</Pty2>

**P1242** 					<Pty3>

**P1243** 						<Id>

**P1244** 							<AnyBIC>MGTCDE55</AnyBIC>

**P1245** 						</Id>

**P1246** 						<SfkpgAcct>

**P1247** 							<Id>111S</Id>

**P1248** 						</SfkpgAcct>

**P1249** 					</Pty3>

**P1250** 				</RcvgSttlmPties>

**P1251** 			</TxDtls>

**P1252** 		</Tx>

**P1253** 	</FinInstrmDtls>

**P1254** </SctiesTxPstngRpt>

