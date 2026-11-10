---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesTransactionPendingReport semt.018.001.15"]
content_origin: "source-transcription"
---

# SecuritiesTransactionPendingReport semt.018.001.15

Source: [src-000196](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart1_SettlementAndReconciliation_2025_2026_v2.docx). Locator: heading path Business Examples / SecuritiesTransactionPendingReport semt.018.001.15.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1255** SecuritiesTransactionPendingReport semt.018.001.15

**P1256** Description

**P1257** On the 15 January 2019, the account servicer, Dresdner Bank London (DRESGB2L), sends to its customer Dresdner Bank Frankfurt (DRESDEFF) a Securities Transaction Pending Report (semt.018.001.08), per status, of its pending transactions. In the below example only one is pending

**P1258** Business Data

**P1259** Number of Pages: 1

**P1260** Report Number: 124

**P1261** Statement Date: 15/01/2019

**P1262** Frequency: daily

**P1263** Update Type: complete

**P1264** Report Structure: status

**P1265** Activity Indicator: true

**P1266** Safekeeping Account: 222s

**P1267** Status and Reason: unmatched, quantity differs

**P1268** Message Instance

**P1269** <SctiesTxPdgRpt>

**P1270** 	<Pgntn>

**P1271** 		<PgNb>1</PgNb>

**P1272** 		<LastPgInd>true</LastPgInd>

**P1273** 	</Pgntn>

**P1274** 	<StmtGnlDtls>

**P1275** 		<RptNb>

**P1276** 			<Shrt>124</Shrt>

**P1277** 		</RptNb>

**P1278** 		<StmtDtTm>

**P1279** 			<Dt>2019-01-15</Dt>

**P1280** 		</StmtDtTm>

**P1281** 		<Frqcy>

**P1282** 			<Cd>DAIL</Cd>

**P1283** 		</Frqcy>

**P1284** 		<UpdTp>

**P1285** 		<Cd>COMP</Cd>

**P1286** 		</UpdTp>

**P1287** 		<StmtStr>STAT</StmtStr>

**P1288** 		<ActvtyInd>true</ActvtyInd>

**P1289** 	</StmtGnlDtls>

**P1290** 	<SfkpgAcct>

**P1291** 		<Id>222S</Id>

**P1292** 	</SfkpgAcct>

**P1293** 	<Sts>

**P1294** 		<StsAndRsn>

**P1295** 			<MtchgSts>

**P1296** 				<Umtchd>

**P1297** 					<Rsn>

**P1298** 						<Cd>

**P1299** 							<Cd>DQUA</Cd>

**P1300** 						</Cd>

**P1301** 					</Rsn>

**P1302** 				</Umtchd>

**P1303** 			</MtchgSts>

**P1304** 		</StsAndRsn>

**P1305** 	<Tx>

**P1306** 		<AcctOwnrTxId>FRTJ123DEL1</AcctOwnrTxId>

**P1307** 		<TxDtls>

**P1308** 			<TxActvty>

**P1309** 				<Cd>SETT</Cd>

**P1310** 			</TxActvty>

**P1311** 			<SttlmTxOrCorpActnEvtTp>

**P1312** 				<SctiesTxTp>

**P1313** 					<Cd>TRAD</Cd>

**P1314** 				</SctiesTxTp>

**P1315** 			</SttlmTxOrCorpActnEvtTp>

**P1316** 			<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P1317** 			<Pmt>FREE</Pmt>

**P1318** 			<FinInstrmId>

**P1319** 				<ISIN>GB0000000123</ISIN>

**P1320** 			</FinInstrmId>

**P1321** 			<PstngQty>

**P1322** 				<Qty>

**P1323** 					<Unit>2000</Unit>

**P1324** 				</Qty>

**P1325** 			</PstngQty>

**P1326** 			<XpctdSttlmDt>

**P1327** 				<Dt>2019-01-18</Dt>

**P1328** 			</XpctdSttlmDt>

**P1329** 			<SttlmDt>

**P1330** 				<Dt>

**P1331** 					<Dt>2019-01-15</Dt>

**P1332** 				</Dt>

**P1333** 			</SttlmDt>

**P1334** 			<DlvrgSttlmPties>

**P1335** 				<Pty1>

**P1336** 					<Id>

**P1337** 						<PrtryId>

**P1338** 							<Id>123</Id>

**P1339** 							<Issr>CRST</Issr>

**P1340** 						</PrtryId>

**P1341** 					</Id>

**P1342** 				</Pty1>

**P1343** 				<Pty2>

**P1344** 					<Id>

**P1345** 						<AnyBIC>DRESDEFF</AnyBIC>

**P1346** 					</Id>

**P1347** 				</Pty2>

**P1348** 				<Pty3>

**P1349** 					<Id>

**P1350** 						<AnyBIC>MGTCDE55</AnyBIC>

**P1351** 					</Id>

**P1352** 				</Pty3>

**P1353** 			</DlvrgSttlmPties>

**P1354** 			<RcvgSttlmPties>

**P1355** 				<Dpstry>

**P1356** 					<Id>

**P1357** 						<AnyBIC>CRSTGB22</AnyBIC>

**P1358** 					</Id>

**P1359** 				</Dpstry>

**P1360** 				<Pty1>

**P1361** 					<Id>

**P1362** 						<PrtryId>

**P1363** 							<Id>456</Id>

**P1364** 							<Issr>CRST</Issr>

**P1365** 						</PrtryId>

**P1366** 					</Id>

**P1367** 				</Pty1>

**P1368** 				<Pty2>

**P1369** 					<Id>

**P1370** 						<AnyBIC>CFPIDEFF</AnyBIC>

**P1371** 					</Id>

**P1372** 				</Pty2>

**P1373** 			</RcvgSttlmPties>

**P1374** 			</TxDtls>

**P1375** 		</Tx>

**P1376** 	</Sts>

**P1377** </SctiesTxPdgRpt>

