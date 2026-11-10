---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000359"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["Examples", "Intra-balance Movement Cancellation Report - camt.083.001"]
content_origin: "source-transcription"
---

# Intra-balance Movement Cancellation Report - camt.083.001

Source: [src-000359](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart1_Target2Securities_IntraBalanceMovement_2023_2024_v2.docx`. Locator: heading path Examples / Intra-balance Movement Cancellation Report - camt.083.001.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1291** Intra-balance Movement Cancellation Report - camt.083.001

**P1292** Description

**P1293** In this example a Statement of pending cancellation instructions for all the Intra-Balance Movements that still have an accepted status at the generation of the report (the 3rd of February 2015 at 06:21:10) within the dedicated cash account ‘9000000123’ is depicted.

**P1294** Message instance

**P1295** <Document>

**P1296** 	<IntraBalMvmntCxlRpt>

**P1297** 		<Id>

**P1298** 			<Id>NONREF</Id>

**P1299** 		</Id>

**P1300** 		<Pgntn>

**P1301** 			<PgNb>1</PgNb>

**P1302** 			<LastPgInd>true</LastPgInd>

**P1303** 		</Pgntn>

**P1304** 		<RptGnlDtls>

**P1305** 			<RptId>T66901</RptId>

**P1306** 			<RptPrd>

**P1307** 				<FrDtTmToDtTm>

**P1308** 					<FrDtTm>2015-02-03T06:21:10</FrDtTm>

**P1309** 					<ToDtTm>2015-02-03T06:21:12</ToDtTm>

**P1310** 				</FrDtTmToDtTm>

**P1311** 			</RptPrd>

**P1312** 			<Frqcy>

**P1313** 				<Cd>DAIL</Cd>

**P1314** 			</Frqcy>

**P1315** 			<UpdTp>

**P1316** 				<Cd>DELT</Cd>

**P1317** 			</UpdTp>

**P1318** 			<ActvtyInd>true</ActvtyInd>

**P1319** 		</RptGnlDtls>

**P1320** 		<RptOrErr>

**P1321** 			<Cxls>

**P1322** 				<CshAcct>

**P1323** 					<Id>

**P1324** 						<Othr>

**P1325** 							<Id>9000000123</Id>

**P1326** 						</Othr>

**P1327** 					</Id>

**P1328** 				</CshAcct>

**P1329** 				<CshAcctOwnr>

**P1330** 					<Id>

**P1331** 						<Id>

**P1332** 							<AnyBIC>PBPTYBICXXX</AnyBIC>

**P1333** 						</Id>

**P1334** 					</Id>

**P1335** 				</CshAcctOwnr>

**P1336** 				<PrcgSts>

**P1337** 					<AckdAccptd>

**P1338** 						<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1339** 					</AckdAccptd>

**P1340** 				</PrcgSts>

**P1341** 				<Cxl>

**P1342** 					<ReqRef>MSG410</ReqRef>

**P1343** 					<StsDt>2011-02-03T15:20:37</StsDt>

**P1344** 					<TxId>

**P1345** 						<AcctOwnrTxId>REF0123</AcctOwnrTxId>

**P1346** 						<MktInfrstrctrTxId>T1390</MktInfrstrctrTxId>

**P1347** 					</TxId>

**P1348** 					<UndrlygIntraBal>

**P1349** 						<SttlmAmt>

**P1350** 							<AmtWthCcy Ccy="EUR">50000</AmtWthCcy>

**P1351** 						</SttlmAmt>

**P1352** 						<SttlmDt>

**P1353** 							<Dt>2010-01-09</Dt>

**P1354** 						</SttlmDt>

**P1355** 						<BalFr>

**P1356** 							<Tp>

**P1357** 								<Prtry>

**P1358** 									<Id>DLVR</Id>

**P1359** 									<Issr>T2S</Issr>

**P1360** 									<SchmeNm>RT</SchmeNm>

**P1361** 								</Prtry>

**P1362** 							</Tp>

**P1363** 						</BalFr>

**P1364** 						<BalTo>

**P1365** 							<Tp>

**P1366** 								<Prtry>

**P1367** 									<Id>BLKA</Id>

**P1368** 									<Issr>T2S</Issr>

**P1369** 									<SchmeNm>RT</SchmeNm>

**P1370** 								</Prtry>

**P1371** 							</Tp>

**P1372** 						</BalTo>

**P1373** 					</UndrlygIntraBal>

**P1374** 				</Cxl>

**P1375** 			</Cxls>

**P1376** 		</RptOrErr>

**P1377** 	</IntraBalMvmntCxlRpt>

**P1378** </Document>

