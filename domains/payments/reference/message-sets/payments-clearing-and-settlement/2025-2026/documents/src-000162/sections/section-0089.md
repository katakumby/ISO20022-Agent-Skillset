---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000162"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 1", "First FIToFICustomerCreditTransfer"]
content_origin: "source-transcription"
---

# First FIToFICustomerCreditTransfer

Source: [src-000162](../../../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx). Locator: heading path Business Examples / FIToFICustomerCreditTransfer pacs.008.001.14 - 1 / First FIToFICustomerCreditTransfer.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1280** First FIToFICustomerCreditTransfer

**P1281** Business Data

**P1282** The first FIToFICustomerCreditTransfer message, from BBBBUS33 to AAAAGB2L:

[T35 - complete table](../tables/tbl-0035.md)

**P1283** Message Instance

**P1284** <FIToFICstmrCdtTrf>

**P1285** 	<GrpHdr>

**P1286** 		<MsgId>BBBB/150928-CCT/JPY/123</MsgId>

**P1287** 		<CreDtTm>2015-09-28T16:00:00</CreDtTm>

**P1288** 		<NbOfTxs>1</NbOfTxs>

**P1289** 		<SttlmInf>

**P1290** 			<SttlmMtd>COVE</SttlmMtd>

**P1291** 			<InstgRmbrsmntAgt>

**P1292** 				<FinInstnId>

**P1293** 					<BICFI>CCCCJPJT</BICFI>

**P1294** 				</FinInstnId>

**P1295** 			</InstgRmbrsmntAgt>

**P1296** 			<InstdRmbrsmntAgt>

**P1297** 				<FinInstnId>

**P1298** 					<BICFI>AAAAJPJT</BICFI>

**P1299** 				</FinInstnId>

**P1300** 			</InstdRmbrsmntAgt>

**P1301** 		</SttlmInf>

**P1302** 		<InstgAgt>

**P1303** 			<FinInstnId>

**P1304** 				<BICFI>BBBBUS33</BICFI>

**P1305** 			</FinInstnId>

**P1306** 		</InstgAgt>

**P1307** 		<InstdAgt>

**P1308** 			<FinInstnId>

**P1309** 				<BICFI>AAAAGB2L</BICFI>

**P1310** 			</FinInstnId>

**P1311** 		</InstdAgt>

**P1312** 	</GrpHdr>

**P1313** 	<CdtTrfTxInf>

**P1314** 		<PmtId>

**P1315** 			<InstrId>BBBB/150928-CCT/JPY/123/1</InstrId>

**P1316** 			<EndToEndId>ABC/4562/2015-09-08</EndToEndId>

**P1317** 			<TxId>BBBB/150928-CCT/JPY/123/1</TxId>

**P1318** 		</PmtId>

**P1319** 		<PmtTpInf>

**P1320** 			<InstrPrty>NORM</InstrPrty>

**P1321** 		</PmtTpInf>

**P1322** 		<IntrBkSttlmAmt Ccy="JPY">10000000</IntrBkSttlmAmt>

**P1323** 		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>

**P1324** 		<ChrgBr>SHAR</ChrgBr>

**P1325** 		<Dbtr>

**P1326** 			<Nm>ABC Corporation</Nm>

**P1327** 			<PstlAdr>

**P1328** 				<StrtNm>Times Square</StrtNm>

**P1329** 				<BldgNb>7</BldgNb>

**P1330** 				<PstCd>NY 10036</PstCd>

**P1331** 				<TwnNm>New York</TwnNm>

**P1332** 				<Ctry>US</Ctry>

**P1333** 			</PstlAdr>

**P1334** 		</Dbtr>

**P1335** 		<DbtrAcct>

**P1336** 			<Id>

**P1337** 				<Othr>

**P1338** 					<Id>00125574999</Id>

**P1339** 				</Othr>

**P1340** 			</Id>

**P1341** 		</DbtrAcct>

**P1342** 		<DbtrAgt>

**P1343** 			<FinInstnId>

**P1344** 				<BICFI>BBBBUS33</BICFI>

**P1345** 			</FinInstnId>

**P1346** 		</DbtrAgt>

**P1347** 		<CdtrAgt>

**P1348** 			<FinInstnId>

**P1349** 				<BICFI>AAAAGB2L</BICFI>

**P1350** 			</FinInstnId>

**P1351** 		</CdtrAgt>

**P1352** 		<Cdtr>

**P1353** 			<Nm>DEF Electronics</Nm>

**P1354** 			<PstlAdr>

**P1355** 				<StrtNm>Mark Lane</StrtNm>

**P1356** 				<BldgNb>55</BldgNb>

**P1357** 				<PstCd>EC3R7NE</PstCd>

**P1358** 				<TwnNm>London</TwnNm>

**P1359** 				<Ctry>GB</Ctry>

**P1360** 				<AdrLine>Corn Exchange 5th Floor</AdrLine>

**P1361** 			</PstlAdr>

**P1362** 		</Cdtr>

**P1363** 		<CdtrAcct>

**P1364** 			<Id>

**P1365** 				<Othr>

**P1366** 					<Id>23683707994215</Id>

**P1367** 				</Othr>

**P1368** 			</Id>

**P1369** 		</CdtrAcct>

**P1370** 		<Purp>

**P1371** 			<Cd>GDDS</Cd>

**P1372** 		</Purp>

**P1373** 		<RmtInf>

**P1374** 			<Strd>

**P1375** 				<RfrdDocInf>

**P1376** 					<Tp>

**P1377** 						<CdOrPrtry>

**P1378** 							<Cd>CINV</Cd>

**P1379** 						</CdOrPrtry>

**P1380** 					</Tp>

**P1381** 					<Nb>4562</Nb>

**P1382** 					<RltdDt>

**P1383** 					<Tp>

**P1384** 						<Cd>INDA</Cd>

**P1385** 					</Tp>

**P1386** 					<Dt>2015-09-08</Dt>									

**P1387** 					</RltdDt>

**P1388** 				</RfrdDocInf>

**P1389** 			</Strd>

**P1390** 		</RmtInf>

**P1391** 	</CdtTrfTxInf>

**P1392** </FIToFICstmrCdtTrf>

