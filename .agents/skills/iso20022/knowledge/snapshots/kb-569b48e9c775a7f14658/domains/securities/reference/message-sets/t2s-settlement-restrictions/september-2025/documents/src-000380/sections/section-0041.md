---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["Business Examples", "Intra Position Movement Pending Report (semt.034)"]
content_origin: "source-transcription"
---

# Intra Position Movement Pending Report (semt.034)

Source: [src-000380](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path Business Examples / Intra Position Movement Pending Report (semt.034).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1218** Intra Position Movement Pending Report (semt.034)

**P1219** Description

**P1220** T2S sends a ‘DAILY’ Intra Position Movement Pending Report in delta mode for the securities account ‘1000000792’ as defined within static data.

**P1221** The report contains three movements pending as of 16h00 on the current business day, the 18th of February 2025.

**P1223** Message Instance

**P1224** <IntraPosMvmntPdgRpt>

**P1225** 		<Pgntn>

**P1226** 			<PgNb>1</PgNb>

**P1227** 			<LastPgInd>true</LastPgInd>

**P1228** 		</Pgntn>

**P1229** 		<RptGnlDtls>

**P1230** 			<RptId>RID0PDR0075</RptId>

**P1231** 			<RptDtTm>

**P1232** 				<DtTm>2025-02-18T16:01:02</DtTm>

**P1233** 			</RptDtTm>

**P1234** 			<Frqcy>

**P1235** 				<Cd>DAIL</Cd>

**P1236** 			</Frqcy>

**P1237** 			<UpdTp>

**P1238** 				<Cd>DELT</Cd>

**P1239** 			</UpdTp>

**P1240** 			<ActvtyInd>true</ActvtyInd>

**P1241** 		</RptGnlDtls>

**P1242** 		<AcctOwnr>

**P1243** 			<Id>

**P1244** 				<Id>

**P1245** 					<AnyBIC>PRYXESMMXXX</AnyBIC>

**P1246** 				</Id>

**P1247** 			</Id>

**P1248** 			<RspnsblPtyId>

**P1249** 				<Id>

**P1250** 					<AnyBIC>CSDXESMMXXX</AnyBIC>

**P1251** 				</Id>

**P1252** 			</RspnsblPtyId>

**P1253** 		</AcctOwnr>

**P1254** 		<SfkpgAcct>

**P1255** 			<Id>1000000792</Id>

**P1256** 		</SfkpgAcct>

**P1257** 		<Mvmnts>

**P1258** 			<Mvmnt>

**P1259** 				<StsAndRsn>

**P1260** 					<PrcgSts>

**P1261** 						<AckdAccptd>

**P1262** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1263** 						</AckdAccptd>

**P1264** 					</PrcgSts>

**P1265** 				</StsAndRsn>

**P1266** 				<AcctOwnrTxId>ACCTOWNREF871</AcctOwnrTxId>

**P1267** 				<MktInfrstrctrTxId>T2SREF00768290</MktInfrstrctrTxId>

**P1268** 				<BalFr>

**P1269** 					<Tp>

**P1270** 						<Cd>AWAS</Cd>

**P1271** 					</Tp>

**P1272** 				</BalFr>

**P1273** 				<BalTo>

**P1274** 					<Tp>

**P1275** 						<Prtry>

**P1276** 							<Id>RSV7</Id>

**P1277** 							<Issr>T2S</Issr>

**P1278** 							<SchmeNm>RT</SchmeNm>

**P1279** 						</Prtry>

**P1280** 					</Tp>

**P1281** 				</BalTo>

**P1282** 				<FinInstrmId>

**P1283** 					<ISIN>ES0000000592</ISIN>

**P1284** 				</FinInstrmId>

**P1285** 				<SttlmQty>

**P1286** 					<Unit>35000</Unit>

**P1287** 				</SttlmQty>

**P1288** 				<IntnddSttlmDt>

**P1289** 					<Dt>2025-02-19</Dt>

**P1290** 				</IntnddSttlmDt>

**P1291** 				<StsDt>2025-02-18T09:42:56</StsDt>

**P1292** 				<SctiesSubBalId>

**P1293** 					<Id>8243366</Id>

**P1294** 				</SctiesSubBalId>

**P1295** 				<Prty>

**P1296** 					<Nmrc>0004</Nmrc>

**P1297** 				</Prty>

**P1298** 				<MsgOrgtr>

**P1299** 					<Id>

**P1300** 						<Id>

**P1301** 							<AnyBIC>PRYXESMMXXX</AnyBIC>

**P1302** 						</Id>

**P1303** 					</Id>

**P1304** 					<RspnsblPtyId>

**P1305** 						<Id>

**P1306** 							<AnyBIC>CSDXESMMXXX</AnyBIC>

**P1307** 						</Id>

**P1308** 					</RspnsblPtyId>

**P1309** 				</MsgOrgtr>

**P1310** 				<CreDtTm>2025-02-18T08:30:19</CreDtTm>

**P1311** 			</Mvmnt>

**P1312** 			<Mvmnt>

**P1313** 				<StsAndRsn>

**P1314** 					<PrcgSts>

**P1315** 						<AckdAccptd>

**P1316** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1317** 						</AckdAccptd>

**P1318** 					</PrcgSts>

**P1319** 				</StsAndRsn>

**P1320** 				<AcctOwnrTxId>ACCTOWNREF145</AcctOwnrTxId>

**P1321** 				<MktInfrstrctrTxId>T2SREF00798222</MktInfrstrctrTxId>

**P1322** 				<BalFr>

**P1323** 					<Tp>

**P1324** 						<Cd>AWAS</Cd>

**P1325** 					</Tp>

**P1326** 				</BalFr>

**P1327** 				<BalTo>

**P1328** 					<Tp>

**P1329** 						<Prtry>

**P1330** 							<Id>RSV7</Id>

**P1331** 							<Issr>T2S</Issr>

**P1332** 							<SchmeNm>RT</SchmeNm>

**P1333** 						</Prtry>

**P1334** 					</Tp>

**P1335** 				</BalTo>

**P1336** 				<FinInstrmId>

**P1337** 					<ISIN>ES0000000592</ISIN>

**P1338** 				</FinInstrmId>

**P1339** 				<SttlmQty>

**P1340** 					<Unit>200000</Unit>

**P1341** 				</SttlmQty>

**P1342** 				<IntnddSttlmDt>

**P1343** 					<Dt>2025-02-19</Dt>

**P1344** 				</IntnddSttlmDt>

**P1345** 				<StsDt>2025-02-18T13:34:16</StsDt>

**P1346** 				<SctiesSubBalId>

**P1347** 					<Id>8243366</Id>

**P1348** 				</SctiesSubBalId>

**P1349** 				<Prty>

**P1350** 					<Nmrc>0003</Nmrc>

**P1351** 				</Prty>

**P1352** 				<MsgOrgtr>

**P1353** 					<Id>

**P1354** 						<Id>

**P1355** 							<AnyBIC>PRYXESMMXXX</AnyBIC>

**P1356** 						</Id>

**P1357** 					</Id>

**P1358** 					<RspnsblPtyId>

**P1359** 						<Id>

**P1360** 							<AnyBIC>CSDXESMMXXX</AnyBIC>

**P1361** 						</Id>

**P1362** 					</RspnsblPtyId>

**P1363** 				</MsgOrgtr>

**P1364** 				<CreDtTm>2025-08-18T12:56:52</CreDtTm>

**P1365** 			</Mvmnt>

**P1366** 			<Mvmnt>

**P1367** 				<StsAndRsn>

**P1368** 					<PrcgSts>

**P1369** 						<AckdAccptd>

**P1370** 							<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1371** 						</AckdAccptd>

**P1372** 					</PrcgSts>

**P1373** 				</StsAndRsn>

**P1374** 				<AcctOwnrTxId>ACCTOWNREF997</AcctOwnrTxId>

**P1375** 				<MktInfrstrctrTxId>T2SREF00879423</MktInfrstrctrTxId>

**P1376** 				<BalFr>

**P1377** 					<Tp>

**P1378** 						<Prtry>

**P1379** 							<Id>BLK1</Id>

**P1380** 							<Issr>T2S</Issr>

**P1381** 							<SchmeNm>RT</SchmeNm>

**P1382** 						</Prtry>

**P1383** 					</Tp>

**P1384** 				</BalFr>

**P1385** 				<BalTo>

**P1386** 					<Tp>

**P1387** 						<Cd>AWAS</Cd>

**P1388** 					</Tp>

**P1389** 				</BalTo>

**P1390** 				<FinInstrmId>

**P1391** 					<ISIN>ES0000008932</ISIN>

**P1392** 				</FinInstrmId>

**P1393** 				<SttlmQty>

**P1394** 					<Unit>12000</Unit>

**P1395** 				</SttlmQty>

**P1396** 				<IntnddSttlmDt>

**P1397** 					<Dt>2025-02-20</Dt>

**P1398** 				</IntnddSttlmDt>

**P1399** 				<StsDt>2025-02-18T15:36:23</StsDt>

**P1400** 				<SctiesSubBalId>

**P1401** 					<Id>563892</Id>

**P1402** 				</SctiesSubBalId>

**P1403** 				<Prty>

**P1404** 					<Nmrc>0002</Nmrc>

**P1405** 				</Prty>

**P1406** 				<MsgOrgtr>

**P1407** 					<Id>

**P1408** 						<Id>

**P1409** 							<AnyBIC>PRYXESMMXXX</AnyBIC>

**P1410** 						</Id>

**P1411** 					</Id>

**P1412** 					<RspnsblPtyId>

**P1413** 						<Id>

**P1414** 							<AnyBIC>CSDXESMMXXX</AnyBIC>

**P1415** 						</Id>

**P1416** 					</RspnsblPtyId>

**P1417** 				</MsgOrgtr>

**P1418** 				<CreDtTm>2025-02-18T14:43:34</CreDtTm>

**P1419** 			</Mvmnt>

**P1420** 		</Mvmnts>

**P1421** </IntraPosMvmntPdgRpt>

