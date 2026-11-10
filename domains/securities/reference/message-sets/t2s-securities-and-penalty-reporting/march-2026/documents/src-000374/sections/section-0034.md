---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000374"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["Business Examples", "Securities Transaction Penalties Report (semt.044)"]
content_origin: "source-transcription"
---

# Securities Transaction Penalties Report (semt.044)

Source: [src-000374](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`. Locator: heading path Business Examples / Securities Transaction Penalties Report (semt.044).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1048** Securities Transaction Penalties Report (semt.044)

**P1049** Description

**P1050** In this example, T2S sends a Securities Transaction Penalties Report, which content is a Daily Penalty List, to the CSD A (CSDABIC1XXX) to inform about all the penalties that were computed for the previous business date, June 21st, 2025 (Detection Date), and for which any participant of CSD A or the CSD A itself is either imposed with or entitled to receive the penalty. This Daily Penalty List is generated on June 24th, 2025, and includes information about 4 penalties within the scope of CSD A.

**P1051** Message Instance

**P1052** <SctiesTxPnltiesRpt>

**P1053** 		<SctiesTxPnltiesRpt>

**P1054** 		<RptPgntn>

**P1055** 			<PgNb>1</PgNb>

**P1056** 			<LastPgInd>true</LastPgInd>

**P1057** 		</RptPgntn>

**P1058** 		<RptGnlDtls>

**P1059** 			<RptId>CSD-A20250624-01</RptId>

**P1060** 			<RptPrd>

**P1061** 				<Dt>2025-06-21</Dt>

**P1062** 			</RptPrd>

**P1063** 			<Frqcy>

**P1064** 				<Cd>DAIL</Cd>

**P1065** 			</Frqcy>

**P1066** 			<PnltyListTp>

**P1067** 				<Cd>FWIS</Cd>

**P1068** 			</PnltyListTp>

**P1069** 			<ActvtyInd>true</ActvtyInd>

**P1070** 		</RptGnlDtls>

**P1071** 		<AcctSvcr>

**P1072** 			<Id>

**P1073** 				<AnyBIC>CSDABIC1XXX</AnyBIC>

**P1074** 			</Id>

**P1075** 		</AcctSvcr>

**P1076** 		<Pnlty>

**P1077** 			<Ccy>EUR</Ccy>

**P1078** 			<Dt>

**P1079** 				<Dt>2025-06-21</Dt>

**P1080** 			</Dt>

**P1081** 			<PtyId>

**P1082** 				<Id>

**P1083** 					<Id>

**P1084** 						<AnyBIC>PRTAFRPPXXX</AnyBIC>

**P1085** 					</Id>

**P1086** 				</Id>

**P1087** 				<Tp>

**P1088** 					<Cd>CSDP</Cd>

**P1089** 				</Tp>

**P1090** 			</PtyId>

**P1091** 			<PnltyPerCtrPty>

**P1092** 				<AcctSvcr>

**P1093** 					<Id>

**P1094** 						<AnyBIC>CSDABIC1XXX</AnyBIC>

**P1095** 					</Id>

**P1096** 				</AcctSvcr>

**P1097** 				<PtyId>

**P1098** 					<Id>

**P1099** 						<Id>

**P1100** 							<AnyBIC>PRTBFRPPXXX</AnyBIC>

**P1101** 						</Id>

**P1102** 					</Id>

**P1103** 					<Tp>

**P1104** 						<Cd>CSDP</Cd>

**P1105** 					</Tp>

**P1106** 				</PtyId>

**P1107** 				<AggtdNetAmt>

**P1108** 					<Amt Ccy="EUR">0</Amt>

**P1109** 				</AggtdNetAmt>

**P1110** 				<PnltyDtls>

**P1111** 					<Id>

**P1112** 						<MktInfrstrctrId>202506210000001</MktInfrstrctrId>

**P1113** 						<Id>F202506210000001</Id>

**P1114** 					</Id>

**P1115** 					<Tp>SEFP</Tp>

**P1116** 					<Sts>

**P1117** 						<Sts>

**P1118** 							<Cd>ACTV</Cd>

**P1119** 						</Sts>

**P1120** 					</Sts>

**P1121** 					<CmptdAmt>

**P1122** 						<Amt Ccy="EUR">25</Amt>

**P1123** 						<CdtDbt>DBIT</CdtDbt>

**P1124** 					</CmptdAmt>

**P1125** 					<ClctnMtd>SECU</ClctnMtd>

**P1126** 					<NbOfDays>1</NbOfDays>

**P1127** 					<ClctnData>

**P1128** 						<Dt>2025-06-21</Dt>

**P1129** 						<FinInstrmAttrbts>

**P1130** 							<Id>

**P1131** 								<ISIN>ISIN00000001</ISIN>

**P1132** 							</Id>

**P1133** 							<ClssfctnTp>

**P1134** 								<AltrnClssfctn>

**P1135** 									<Id>SHRS</Id>

**P1136** 								</AltrnClssfctn>

**P1137** 							</ClssfctnTp>

**P1138** 							<Lqdty>false</Lqdty>

**P1139** 							<SctiesPnltyRateData>

**P1140** 								<MktId>

**P1141** 									<MktIdrCd>ABCD</MktIdrCd>

**P1142** 								</MktId>

**P1143** 								<SMEGrwthMkt>true</SMEGrwthMkt>

**P1144** 								<Rate>0.0025</Rate>

**P1145** 							</SctiesPnltyRateData>

**P1146** 						</FinInstrmAttrbts>

**P1147** 					</ClctnData>

**P1148** 					<RltdTx>

**P1149** 						<Ref>

**P1150** 							<AcctOwnrTxId>PARTICIPANT-A001</AcctOwnrTxId>

**P1151** 							<MktInfrstrctrTxId>T2S1000000000001</MktInfrstrctrTxId>

**P1152** 							<CtrPtyMktInfrstrctrTxId>T2S2000000000001</CtrPtyMktInfrstrctrTxId>

**P1153** 							<CmonId>T2S0000000000001</CmonId>

**P1154** 						</Ref>

**P1155** 						<RefOwnr>

**P1156** 							<Id>

**P1157** 								<AnyBIC>PRTAFRPPXXX</AnyBIC>

**P1158** 							</Id>

**P1159** 						</RefOwnr>

**P1160** 						<TxDtls>

**P1161** 							<SttlmTxOrCorpActnEvtTp>

**P1162** 								<SctiesTxTp>

**P1163** 									<Cd>TRAD</Cd>

**P1164** 								</SctiesTxTp>

**P1165** 							</SttlmTxOrCorpActnEvtTp>

**P1166** 							<SttlmDt>

**P1167** 								<Dt>

**P1168** 									<Dt>2025-06-21</Dt>

**P1169** 								</Dt>

**P1170** 							</SttlmDt>

**P1171** 							<SfkpgAcct>

**P1172** 								<Id>1000000123</Id>

**P1173** 							</SfkpgAcct>

**P1174** 							<AcctOwnr>

**P1175** 								<Id>

**P1176** 									<AnyBIC>PRTAFRPPXXX</AnyBIC>

**P1177** 								</Id>

**P1178** 							</AcctOwnr>

**P1179** 							<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P1180** 							<Pmt>APMT</Pmt>

**P1181** 							<PstngQty>

**P1182** 								<Unit>100000</Unit>

**P1183** 							</PstngQty>

**P1184** 							<CshAcct>

**P1185** 								<Prtry>2000000123</Prtry>

**P1186** 							</CshAcct>

**P1187** 							<CshAcctOwnr>

**P1188** 								<Id>

**P1189** 									<OrgId>

**P1190** 										<AnyBIC>PBKAFRPPXXX</AnyBIC>

**P1191** 									</OrgId>

**P1192** 								</Id>

**P1193** 							</CshAcctOwnr>

**P1194** 							<PstngAmt>

**P1195** 								<Amt Ccy="EUR">750000</Amt>

**P1196** 								<CdtDbt>CRDT</CdtDbt>

**P1197** 							</PstngAmt>

**P1198** 							<AckdStsTmStmp>2025-06-21T13:30:00Z</AckdStsTmStmp>

**P1199** 							<MtchdStsTmStmp>2025-06-21T13:30:15Z</MtchdStsTmStmp>

**P1200** 							<SttlmStsFlng>

**P1201** 								<Rsn>

**P1202** 									<Cd>

**P1203** 										<Cd>PREA</Cd>

**P1204** 									</Cd>

**P1205** 									<AddtlRsnInf>Instruction failed because Participant A had it on hold</AddtlRsnInf>

**P1206** 								</Rsn>

**P1207** 							</SttlmStsFlng>

**P1208** 							<BizDayEvt>

**P1209** 								<Tp>

**P1210** 									<Prtry>

**P1211** 										<Id>EDVP</Id>

**P1212** 										<SchmeNm>EVTP</SchmeNm>

**P1213** 										<Issr>T2S</Issr>

**P1214** 									</Prtry>

**P1215** 								</Tp>

**P1216** 								<SchdldTm>2025-06-21T16:00:00Z</SchdldTm>

**P1217** 								<StartTm>2025-06-21T16:00:03Z</StartTm>

**P1218** 								<EndTm>2025-06-21T16:01:45Z</EndTm>

**P1219** 							</BizDayEvt>

**P1220** 						</TxDtls>

**P1221** 					</RltdTx>

**P1222** 				</PnltyDtls>

**P1223** 				<PnltyDtls>

**P1224** 					<Id>

**P1225** 						<MktInfrstrctrId>202506210000002</MktInfrstrctrId>

**P1226** 						<Id>N202506210000002</Id>

**P1227** 					</Id>

**P1228** 					<Tp>SEFP</Tp>

**P1229** 					<Sts>

**P1230** 						<Sts>

**P1231** 							<Cd>ACTV</Cd>

**P1232** 						</Sts>

**P1233** 					</Sts>

**P1234** 					<CmptdAmt>

**P1235** 						<Amt Ccy="EUR">25</Amt>

**P1236** 						<CdtDbt>CRDT</CdtDbt>

**P1237** 					</CmptdAmt>

**P1238** 					<ClctnMtd>SECU</ClctnMtd>

**P1239** 					<NbOfDays>1</NbOfDays>

**P1240** 					<ClctnData>

**P1241** 						<Dt>2025-06-21</Dt>

**P1242** 						<FinInstrmAttrbts>

**P1243** 							<Id>

**P1244** 								<ISIN>ISIN00000001</ISIN>

**P1245** 							</Id>

**P1246** 							<ClssfctnTp>

**P1247** 								<AltrnClssfctn>

**P1248** 									<Id>SHRS</Id>

**P1249** 								</AltrnClssfctn>

**P1250** 							</ClssfctnTp>

**P1251** 							<Lqdty>false</Lqdty>

**P1252** 							<SctiesPnltyRateData>

**P1253** 								<MktId>

**P1254** 									<MktIdrCd>ABCD</MktIdrCd>

**P1255** 								</MktId>

**P1256** 								<SMEGrwthMkt>true</SMEGrwthMkt>

**P1257** 								<Rate>0.0025</Rate>

**P1258** 							</SctiesPnltyRateData>

**P1259** 						</FinInstrmAttrbts>

**P1260** 					</ClctnData>

**P1261** 					<RltdTx>

**P1262** 						<Ref>

**P1263** 							<AcctOwnrTxId>PARTICIPANT-A002</AcctOwnrTxId>

**P1264** 							<MktInfrstrctrTxId>T2S2000000000002</MktInfrstrctrTxId>

**P1265** 							<CtrPtyMktInfrstrctrTxId>T2S1000000000002</CtrPtyMktInfrstrctrTxId>

**P1266** 							<CmonId>T2S0000000000002</CmonId>

**P1267** 						</Ref>

**P1268** 						<RefOwnr>

**P1269** 							<Id>

**P1270** 								<AnyBIC>PRTAFRPPXXX</AnyBIC>

**P1271** 							</Id>

**P1272** 						</RefOwnr>

**P1273** 						<TxDtls>

**P1274** 							<SttlmTxOrCorpActnEvtTp>

**P1275** 								<SctiesTxTp>

**P1276** 									<Cd>TRAD</Cd>

**P1277** 								</SctiesTxTp>

**P1278** 							</SttlmTxOrCorpActnEvtTp>

**P1279** 							<SttlmDt>

**P1280** 								<Dt>

**P1281** 									<Dt>2025-06-21</Dt>

**P1282** 								</Dt>

**P1283** 							</SttlmDt>

**P1284** 							<SfkpgAcct>

**P1285** 								<Id>1000000123</Id>

**P1286** 							</SfkpgAcct>

**P1287** 							<AcctOwnr>

**P1288** 								<Id>

**P1289** 									<AnyBIC>PRTAFRPPXXX</AnyBIC>

**P1290** 								</Id>

**P1291** 							</AcctOwnr>

**P1292** 							<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P1293** 							<Pmt>APMT</Pmt>

**P1294** 							<PstngQty>

**P1295** 								<Unit>100000</Unit>

**P1296** 							</PstngQty>

**P1297** 							<CshAcct>

**P1298** 								<Prtry>2000000123</Prtry>

**P1299** 							</CshAcct>

**P1300** 							<CshAcctOwnr>

**P1301** 								<Id>

**P1302** 									<OrgId>

**P1303** 										<AnyBIC>PBKAFRPPXXX</AnyBIC>

**P1304** 									</OrgId>

**P1305** 								</Id>

**P1306** 							</CshAcctOwnr>

**P1307** 							<PstngAmt>

**P1308** 								<Amt Ccy="EUR">800000</Amt>

**P1309** 								<CdtDbt>DBIT</CdtDbt>

**P1310** 							</PstngAmt>

**P1311** 							<AckdStsTmStmp>2025-06-21T14:30:00Z</AckdStsTmStmp>

**P1312** 							<MtchdStsTmStmp>2025-06-21T14:30:15Z</MtchdStsTmStmp>

**P1313** 							<SttlmStsFlng>

**P1314** 								<Rsn>

**P1315** 									<Cd>

**P1316** 										<Cd>CLAC</Cd>

**P1317** 									</Cd>

**P1318** 									<AddtlRsnInf>Instruction failed because Participant B has insufficient securities to settle</AddtlRsnInf>

**P1319** 								</Rsn>

**P1320** 							</SttlmStsFlng>

**P1321** 							<BizDayEvt>

**P1322** 								<Tp>

**P1323** 									<Prtry>

**P1324** 										<Id>EDVP</Id>

**P1325** 										<SchmeNm>EVTP</SchmeNm>

**P1326** 										<Issr>T2S</Issr>

**P1327** 									</Prtry>

**P1328** 								</Tp>

**P1329** 								<SchdldTm>2025-06-21T16:00:00Z</SchdldTm>

**P1330** 								<StartTm>2025-06-21T16:00:03Z</StartTm>

**P1331** 								<EndTm>2025-06-21T16:01:45Z</EndTm>

**P1332** 							</BizDayEvt>

**P1333** 						</TxDtls>

**P1334** 					</RltdTx>

**P1335** 				</PnltyDtls>

**P1336** 			</PnltyPerCtrPty>

**P1337** 			<PnltyPerCtrPty>

**P1338** 				<AcctSvcr>

**P1339** 					<Id>

**P1340** 						<AnyBIC>CSDZBIC1XXX</AnyBIC>

**P1341** 					</Id>

**P1342** 				</AcctSvcr>

**P1343** 				<PtyId>

**P1344** 					<Id>

**P1345** 						<Id>

**P1346** 							<AnyBIC>PRTZESMMXXX</AnyBIC>

**P1347** 						</Id>

**P1348** 					</Id>

**P1349** 					<Tp>

**P1350** 						<Cd>CSDP</Cd>

**P1351** 					</Tp>

**P1352** 				</PtyId>

**P1353** 				<AggtdNetAmt>

**P1354** 					<Amt Ccy="EUR">6.25</Amt>

**P1355** 					<CdtDbt>DBIT</CdtDbt>

**P1356** 				</AggtdNetAmt>

**P1357** 				<PnltyDtls>

**P1358** 					<Id>

**P1359** 						<MktInfrstrctrId>202506210000003</MktInfrstrctrId>

**P1360** 						<Id>F202506210000003</Id>

**P1361** 					</Id>

**P1362** 					<Tp>SEFP</Tp>

**P1363** 					<Sts>

**P1364** 						<Sts>

**P1365** 							<Cd>ACTV</Cd>

**P1366** 						</Sts>

**P1367** 					</Sts>

**P1368** 					<CmptdAmt>

**P1369** 						<Amt Ccy="EUR">6.25</Amt>

**P1370** 						<CdtDbt>DBIT</CdtDbt>

**P1371** 					</CmptdAmt>

**P1372** 					<ClctnMtd>CASH</ClctnMtd>

**P1373** 					<NbOfDays>1</NbOfDays>

**P1374** 					<ClctnData>

**P1375** 						<Dt>2025-06-21</Dt>

**P1376** 						<FinInstrmAttrbts>

**P1377** 							<Id>

**P1378** 								<ISIN>ISIN00000009</ISIN>

**P1379** 							</Id>

**P1380** 							<ClssfctnTp>

**P1381** 								<AltrnClssfctn>

**P1382** 									<Id>SHRS</Id>

**P1383** 								</AltrnClssfctn>

**P1384** 							</ClssfctnTp>

**P1385** 						</FinInstrmAttrbts>

**P1386** 						<DscntRate>

**P1387** 							<Rate>0.0006944444</Rate>

**P1388** 						</DscntRate>

**P1389** 					</ClctnData>

**P1390** 					<RltdTx>

**P1391** 						<Ref>

**P1392** 							<AcctOwnrTxId>PARTICIPANT-A003</AcctOwnrTxId>

**P1393** 							<MktInfrstrctrTxId>T2S1000000000003</MktInfrstrctrTxId>

**P1394** 							<CtrPtyMktInfrstrctrTxId>T2S2000000000003</CtrPtyMktInfrstrctrTxId>

**P1395** 							<CmonId>T2S0000000000003</CmonId>

**P1396** 						</Ref>

**P1397** 						<RefOwnr>

**P1398** 							<Id>

**P1399** 								<AnyBIC>PRTAFRPPXXX</AnyBIC>

**P1400** 							</Id>

**P1401** 						</RefOwnr>

**P1402** 						<TxDtls>

**P1403** 							<SttlmTxOrCorpActnEvtTp>

**P1404** 								<SctiesTxTp>

**P1405** 									<Cd>TRAD</Cd>

**P1406** 								</SctiesTxTp>

**P1407** 							</SttlmTxOrCorpActnEvtTp>

**P1408** 							<SttlmDt>

**P1409** 								<Dt>

**P1410** 									<Dt>2025-06-21</Dt>

**P1411** 								</Dt>

**P1412** 							</SttlmDt>

**P1413** 							<SfkpgAcct>

**P1414** 								<Id>1000000123</Id>

**P1415** 							</SfkpgAcct>

**P1416** 							<AcctOwnr>

**P1417** 								<Id>

**P1418** 									<AnyBIC>PRTAFRPPXXX</AnyBIC>

**P1419** 								</Id>

**P1420** 							</AcctOwnr>

**P1421** 							<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P1422** 							<Pmt>APMT</Pmt>

**P1423** 							<PstngQty>

**P1424** 								<Unit>0</Unit>

**P1425** 							</PstngQty>

**P1426** 							<CshAcct>

**P1427** 								<Prtry>2000000123</Prtry>

**P1428** 							</CshAcct>

**P1429** 							<CshAcctOwnr>

**P1430** 								<Id>

**P1431** 									<OrgId>

**P1432** 										<AnyBIC>PBKAFRPPXXX</AnyBIC>

**P1433** 									</OrgId>

**P1434** 								</Id>

**P1435** 							</CshAcctOwnr>

**P1436** 							<PstngAmt>

**P1437** 								<Amt Ccy="EUR">900000</Amt>

**P1438** 								<CdtDbt>DBIT</CdtDbt>

**P1439** 							</PstngAmt>

**P1440** 							<AckdStsTmStmp>2025-06-21T15:30:00Z</AckdStsTmStmp>

**P1441** 							<MtchdStsTmStmp>2025-06-21T15:30:15Z</MtchdStsTmStmp>

**P1442** 							<SttlmStsFlng>

**P1443** 								<Rsn>

**P1444** 									<Cd>

**P1445** 										<Cd>MONY</Cd>

**P1446** 									</Cd>

**P1447** 									<AddtlRsnInf>Instruction failed because Participant A has insufficient cash to settle</AddtlRsnInf>

**P1448** 								</Rsn>

**P1449** 							</SttlmStsFlng>

**P1450** 							<BizDayEvt>

**P1451** 								<Tp>

**P1452** 									<Prtry>

**P1453** 										<Id>EDVP</Id>

**P1454** 										<SchmeNm>EVTP</SchmeNm>

**P1455** 										<Issr>T2S</Issr>

**P1456** 									</Prtry>

**P1457** 								</Tp>

**P1458** 								<SchdldTm>2025-06-21T16:00:00Z</SchdldTm>

**P1459** 								<StartTm>2025-06-21T16:00:03Z</StartTm>

**P1460** 								<EndTm>2025-06-21T16:01:45Z</EndTm>

**P1461** 							</BizDayEvt>

**P1462** 						</TxDtls>

**P1463** 					</RltdTx>

**P1464** 				</PnltyDtls>

**P1465** 			</PnltyPerCtrPty>

**P1466** 		</Pnlty>

**P1467** 		<Pnlty>

**P1468** 			<Ccy>EUR</Ccy>

**P1469** 			<Dt>

**P1470** 				<Dt>2025-06-21</Dt>

**P1471** 			</Dt>

**P1472** 			<PtyId>

**P1473** 				<Id>

**P1474** 					<Id>

**P1475** 						<AnyBIC>PRTBFRPPXXX</AnyBIC>

**P1476** 					</Id>

**P1477** 				</Id>

**P1478** 				<Tp>

**P1479** 					<Cd>CSDP</Cd>

**P1480** 				</Tp>

**P1481** 			</PtyId>

**P1482** 			<PnltyPerCtrPty>

**P1483** 				<AcctSvcr>

**P1484** 					<Id>

**P1485** 						<AnyBIC>CSDABIC1XXX</AnyBIC>

**P1486** 					</Id>

**P1487** 				</AcctSvcr>

**P1488** 				<PtyId>

**P1489** 					<Id>

**P1490** 						<Id>

**P1491** 							<AnyBIC>PRTAFRPPXXX</AnyBIC>

**P1492** 						</Id>

**P1493** 					</Id>

**P1494** 					<Tp>

**P1495** 						<Cd>CSDP</Cd>

**P1496** 					</Tp>

**P1497** 				</PtyId>

**P1498** 				<AggtdNetAmt>

**P1499** 					<Amt Ccy="EUR">0</Amt>

**P1500** 				</AggtdNetAmt>

**P1501** 				<PnltyDtls>

**P1502** 					<Id>

**P1503** 						<MktInfrstrctrId>202506210000001</MktInfrstrctrId>

**P1504** 						<Id>N202506210000001</Id>

**P1505** 					</Id>

**P1506** 					<Tp>SEFP</Tp>

**P1507** 					<Sts>

**P1508** 						<Sts>

**P1509** 							<Cd>ACTV</Cd>

**P1510** 						</Sts>

**P1511** 					</Sts>

**P1512** 					<CmptdAmt>

**P1513** 						<Amt Ccy="EUR">25</Amt>

**P1514** 						<CdtDbt>CRDT</CdtDbt>

**P1515** 					</CmptdAmt>

**P1516** 					<ClctnMtd>SECU</ClctnMtd>

**P1517** 					<NbOfDays>1</NbOfDays>

**P1518** 					<ClctnData>

**P1519** 						<Dt>2025-06-21</Dt>

**P1520** 						<FinInstrmAttrbts>

**P1521** 							<Id>

**P1522** 								<ISIN>ISIN00000001</ISIN>

**P1523** 							</Id>

**P1524** 							<ClssfctnTp>

**P1525** 								<AltrnClssfctn>

**P1526** 									<Id>SHRS</Id>

**P1527** 								</AltrnClssfctn>

**P1528** 							</ClssfctnTp>

**P1529** 							<Lqdty>false</Lqdty>

**P1530** 							<SctiesPnltyRateData>

**P1531** 								<MktId>

**P1532** 									<MktIdrCd>ABCD</MktIdrCd>

**P1533** 								</MktId>

**P1534** 								<SMEGrwthMkt>true</SMEGrwthMkt>

**P1535** 								<Rate>0.0025</Rate>

**P1536** 							</SctiesPnltyRateData>

**P1537** 						</FinInstrmAttrbts>

**P1538** 					</ClctnData>

**P1539** 					<RltdTx>

**P1540** 						<Ref>

**P1541** 							<AcctOwnrTxId>PARTICIPANT-B001</AcctOwnrTxId>

**P1542** 							<MktInfrstrctrTxId>T2S2000000000001</MktInfrstrctrTxId>

**P1543** 							<CtrPtyMktInfrstrctrTxId>T2S1000000000001</CtrPtyMktInfrstrctrTxId>

**P1544** 							<CmonId>T2S0000000000001</CmonId>

**P1545** 						</Ref>

**P1546** 						<RefOwnr>

**P1547** 							<Id>

**P1548** 								<AnyBIC>PRTBFRPPXXX</AnyBIC>

**P1549** 							</Id>

**P1550** 						</RefOwnr>

**P1551** 						<TxDtls>

**P1552** 							<SttlmTxOrCorpActnEvtTp>

**P1553** 								<SctiesTxTp>

**P1554** 									<Cd>TRAD</Cd>

**P1555** 								</SctiesTxTp>

**P1556** 							</SttlmTxOrCorpActnEvtTp>

**P1557** 							<SttlmDt>

**P1558** 								<Dt>

**P1559** 									<Dt>2025-06-21</Dt>

**P1560** 								</Dt>

**P1561** 							</SttlmDt>

**P1562** 							<SfkpgAcct>

**P1563** 								<Id>1000000789</Id>

**P1564** 							</SfkpgAcct>

**P1565** 							<AcctOwnr>

**P1566** 								<Id>

**P1567** 									<AnyBIC>PRTBFRPPXXX</AnyBIC>

**P1568** 								</Id>

**P1569** 							</AcctOwnr>

**P1570** 							<SctiesMvmntTp>RECE</SctiesMvmntTp>

**P1571** 							<Pmt>APMT</Pmt>

**P1572** 							<PstngQty>

**P1573** 								<Unit>100000</Unit>

**P1574** 							</PstngQty>

**P1575** 							<CshAcct>

**P1576** 								<Prtry>2000000789</Prtry>

**P1577** 							</CshAcct>

**P1578** 							<CshAcctOwnr>

**P1579** 								<Id>

**P1580** 									<OrgId>

**P1581** 										<AnyBIC>PBKBFRPPXXX</AnyBIC>

**P1582** 									</OrgId>

**P1583** 								</Id>

**P1584** 							</CshAcctOwnr>

**P1585** 							<PstngAmt>

**P1586** 								<Amt Ccy="EUR">750000</Amt>

**P1587** 								<CdtDbt>DBIT</CdtDbt>

**P1588** 							</PstngAmt>

**P1589** 							<AckdStsTmStmp>2025-06-21T13:30:00Z</AckdStsTmStmp>

**P1590** 							<MtchdStsTmStmp>2025-06-21T13:30:15Z</MtchdStsTmStmp>

**P1591** 							<SttlmStsFlng>

**P1592** 								<Rsn>

**P1593** 									<Cd>

**P1594** 										<Cd>PRCY</Cd>

**P1595** 									</Cd>

**P1596** 									<AddtlRsnInf>Instruction failed because Participant A had it on hold</AddtlRsnInf>

**P1597** 								</Rsn>

**P1598** 							</SttlmStsFlng>

**P1599** 							<BizDayEvt>

**P1600** 								<Tp>

**P1601** 									<Prtry>

**P1602** 										<Id>EDVP</Id>

**P1603** 										<SchmeNm>EVTP</SchmeNm>

**P1604** 										<Issr>T2S</Issr>

**P1605** 									</Prtry>

**P1606** 								</Tp>

**P1607** 								<SchdldTm>2025-06-21T16:00:00Z</SchdldTm>

**P1608** 								<StartTm>2025-06-21T16:00:03Z</StartTm>

**P1609** 								<EndTm>2025-06-21T16:01:45Z</EndTm>

**P1610** 							</BizDayEvt>

**P1611** 						</TxDtls>

**P1612** 					</RltdTx>

**P1613** 				</PnltyDtls>

**P1614** 				<PnltyDtls>

**P1615** 					<Id>

**P1616** 						<MktInfrstrctrId>202506210000002</MktInfrstrctrId>

**P1617** 						<Id>F202506210000002</Id>

**P1618** 					</Id>

**P1619** 					<Tp>SEFP</Tp>

**P1620** 					<Sts>

**P1621** 						<Sts>

**P1622** 							<Cd>ACTV</Cd>

**P1623** 						</Sts>

**P1624** 					</Sts>

**P1625** 					<CmptdAmt>

**P1626** 						<Amt Ccy="EUR">25</Amt>

**P1627** 						<CdtDbt>DBIT</CdtDbt>

**P1628** 					</CmptdAmt>

**P1629** 					<ClctnMtd>SECU</ClctnMtd>

**P1630** 					<NbOfDays>1</NbOfDays>

**P1631** 					<ClctnData>

**P1632** 						<Dt>2025-06-21</Dt>

**P1633** 						<FinInstrmAttrbts>

**P1634** 							<Id>

**P1635** 								<ISIN>ISIN00000001</ISIN>

**P1636** 							</Id>

**P1637** 							<ClssfctnTp>

**P1638** 								<AltrnClssfctn>

**P1639** 									<Id>SHRS</Id>

**P1640** 								</AltrnClssfctn>

**P1641** 							</ClssfctnTp>

**P1642** 							<Lqdty>false</Lqdty>

**P1643** 							<SctiesPnltyRateData>

**P1644** 								<MktId>

**P1645** 									<MktIdrCd>ABCD</MktIdrCd>

**P1646** 								</MktId>

**P1647** 								<SMEGrwthMkt>true</SMEGrwthMkt>

**P1648** 								<Rate>0.0025</Rate>

**P1649** 							</SctiesPnltyRateData>

**P1650** 						</FinInstrmAttrbts>

**P1651** 					</ClctnData>

**P1652** 					<RltdTx>

**P1653** 						<Ref>

**P1654** 							<AcctOwnrTxId>PARTICIPANT-B002</AcctOwnrTxId>

**P1655** 							<MktInfrstrctrTxId>T2S1000000000002</MktInfrstrctrTxId>

**P1656** 							<CtrPtyMktInfrstrctrTxId>T2S2000000000002</CtrPtyMktInfrstrctrTxId>

**P1657** 							<CmonId>T2S0000000000002</CmonId>

**P1658** 						</Ref>

**P1659** 						<RefOwnr>

**P1660** 							<Id>

**P1661** 								<AnyBIC>PRTBFRPPXXX</AnyBIC>

**P1662** 							</Id>

**P1663** 						</RefOwnr>

**P1664** 						<TxDtls>

**P1665** 							<SttlmTxOrCorpActnEvtTp>

**P1666** 								<SctiesTxTp>

**P1667** 									<Cd>TRAD</Cd>

**P1668** 								</SctiesTxTp>

**P1669** 							</SttlmTxOrCorpActnEvtTp>

**P1670** 							<SttlmDt>

**P1671** 								<Dt>

**P1672** 									<Dt>2025-06-21</Dt>

**P1673** 								</Dt>

**P1674** 							</SttlmDt>

**P1675** 							<SfkpgAcct>

**P1676** 								<Id>1000000789</Id>

**P1677** 							</SfkpgAcct>

**P1678** 							<AcctOwnr>

**P1679** 								<Id>

**P1680** 									<AnyBIC>PRTBFRPPXXX</AnyBIC>

**P1681** 								</Id>

**P1682** 							</AcctOwnr>

**P1683** 							<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P1684** 							<Pmt>APMT</Pmt>

**P1685** 							<PstngQty>

**P1686** 								<Unit>100000</Unit>

**P1687** 							</PstngQty>

**P1688** 							<CshAcct>

**P1689** 								<Prtry>2000000789</Prtry>

**P1690** 							</CshAcct>

**P1691** 							<CshAcctOwnr>

**P1692** 								<Id>

**P1693** 									<OrgId>

**P1694** 										<AnyBIC>PBKBFRPPXXX</AnyBIC>

**P1695** 									</OrgId>

**P1696** 								</Id>

**P1697** 							</CshAcctOwnr>

**P1698** 							<PstngAmt>

**P1699** 								<Amt Ccy="EUR">800000</Amt>

**P1700** 								<CdtDbt>CRDT</CdtDbt>

**P1701** 							</PstngAmt>

**P1702** 							<AckdStsTmStmp>2025-06-21T14:30:00Z</AckdStsTmStmp>

**P1703** 							<MtchdStsTmStmp>22025-06-21T14:30:15Z</MtchdStsTmStmp>

**P1704** 							<SttlmStsFlng>

**P1705** 								<Rsn>

**P1706** 									<Cd>

**P1707** 										<Cd>LACK</Cd>

**P1708** 									</Cd>

**P1709** 									<AddtlRsnInf>Instruction failed because Participant B has insufficient securities to settle</AddtlRsnInf>

**P1710** 								</Rsn>

**P1711** 							</SttlmStsFlng>

**P1712** 							<BizDayEvt>

**P1713** 								<Tp>

**P1714** 									<Prtry>

**P1715** 										<Id>EDVP</Id>

**P1716** 										<SchmeNm>EVTP</SchmeNm>

**P1717** 										<Issr>T2S</Issr>

**P1718** 									</Prtry>

**P1719** 								</Tp>

**P1720** 								<SchdldTm>2025-06-21T16:00:00Z</SchdldTm>

**P1721** 								<StartTm>2025-06-21T16:00:03Z</StartTm>

**P1722** 								<EndTm>2025-06-21T16:01:45Z</EndTm>

**P1723** 							</BizDayEvt>

**P1724** 						</TxDtls>

**P1725** 					</RltdTx>

**P1726** 				</PnltyDtls>

**P1727** 			</PnltyPerCtrPty>

**P1728** 			<PnltyPerCtrPty>

**P1729** 				<AcctSvcr>

**P1730** 					<Id>

**P1731** 						<AnyBIC>CSDYBIC1XXX</AnyBIC>

**P1732** 					</Id>

**P1733** 				</AcctSvcr>

**P1734** 				<PtyId>

**P1735** 					<Id>

**P1736** 						<Id>

**P1737** 							<AnyBIC>PRTYDEFFXXX</AnyBIC>

**P1738** 						</Id>

**P1739** 					</Id>

**P1740** 					<Tp>

**P1741** 						<Cd>CSDP</Cd>

**P1742** 					</Tp>

**P1743** 				</PtyId>

**P1744** 				<AggtdNetAmt>

**P1745** 					<Amt Ccy="EUR">0.38</Amt>

**P1746** 					<CdtDbt>CRDT</CdtDbt>

**P1747** 				</AggtdNetAmt>

**P1748** 				<PnltyDtls>

**P1749** 					<Id>

**P1750** 						<MktInfrstrctrId>202506210000004</MktInfrstrctrId>

**P1751** 						<Id>N202506210000004</Id>

**P1752** 					</Id>

**P1753** 					<Tp>SEFP</Tp>

**P1754** 					<Sts>

**P1755** 						<Sts>

**P1756** 							<Cd>ACTV</Cd>

**P1757** 						</Sts>

**P1758** 					</Sts>

**P1759** 					<CmptdAmt>

**P1760** 						<Amt Ccy="EUR">0.38</Amt>

**P1761** 						<CdtDbt>CRDT</CdtDbt>

**P1762** 					</CmptdAmt>

**P1763** 					<ClctnMtd>MIXE</ClctnMtd>

**P1764** 					<NbOfDays>1</NbOfDays>

**P1765** 					<ClctnData>

**P1766** 						<Dt>2025-06-21</Dt>

**P1767** 						<FinInstrmAttrbts>

**P1768** 							<Id>

**P1769** 								<ISIN>ISIN00000004</ISIN>

**P1770** 							</Id>

**P1771** 							<ClssfctnTp>

**P1772** 								<AltrnClssfctn>

**P1773** 									<Id>SHRS</Id>

**P1774** 								</AltrnClssfctn>

**P1775** 							</ClssfctnTp>

**P1776** 						</FinInstrmAttrbts>

**P1777** 						<DscntRate>

**P1778** 							<Rate>0.0006944444</Rate>

**P1779** 						</DscntRate>

**P1780** 					</ClctnData>

**P1781** 					<RltdTx>

**P1782** 						<Ref>

**P1783** 							<AcctOwnrTxId>PARTICIPANT-B004</AcctOwnrTxId>

**P1784** 							<MktInfrstrctrTxId>T2S1000000000004</MktInfrstrctrTxId>

**P1785** 							<CtrPtyMktInfrstrctrTxId>T2S2000000000004</CtrPtyMktInfrstrctrTxId>					

**P1786** 							<CmonId>T2S0000000000004</CmonId>

**P1787** 						</Ref>

**P1788** 						<RefOwnr>

**P1789** 							<Id>

**P1790** 								<AnyBIC>PRTBFRPPXXX</AnyBIC>

**P1791** 							</Id>

**P1792** 						</RefOwnr>

**P1793** 						<TxDtls>

**P1794** 							<SttlmTxOrCorpActnEvtTp>

**P1795** 								<SctiesTxTp>

**P1796** 									<Cd>TRAD</Cd>

**P1797** 								</SctiesTxTp>

**P1798** 							</SttlmTxOrCorpActnEvtTp>

**P1799** 							<SttlmDt>

**P1800** 								<Dt>

**P1801** 									<Dt>2025-06-21</Dt>

**P1802** 								</Dt>

**P1803** 							</SttlmDt>

**P1804** 							<SfkpgAcct>

**P1805** 								<Id>1000000789</Id>

**P1806** 							</SfkpgAcct>

**P1807** 							<AcctOwnr>

**P1808** 								<Id>

**P1809** 									<AnyBIC>PRTBFRPPXXX</AnyBIC>

**P1810** 								</Id>

**P1811** 							</AcctOwnr>

**P1812** 							<SctiesMvmntTp>DELI</SctiesMvmntTp>

**P1813** 							<Pmt>APMT</Pmt>

**P1814** 							<PstngQty>

**P1815** 								<Unit>3000</Unit>

**P1816** 							</PstngQty>

**P1817** 							<CshAcct>

**P1818** 								<Prtry>2000000789</Prtry>

**P1819** 							</CshAcct>

**P1820** 							<CshAcctOwnr>

**P1821** 								<Id>

**P1822** 									<OrgId>

**P1823** 										<AnyBIC>PBKBFRPPXXX</AnyBIC>

**P1824** 									</OrgId>

**P1825** 								</Id>

**P1826** 							</CshAcctOwnr>

**P1827** 							<PstngAmt>

**P1828** 								<Amt Ccy="EUR">51000</Amt>

**P1829** 								<CdtDbt>CRDT</CdtDbt>

**P1830** 							</PstngAmt>

**P1831** 							<AckdStsTmStmp>2025-06-21T15:35:00Z</AckdStsTmStmp>

**P1832** 							<MtchdStsTmStmp>2025-06-21T15:35:15Z</MtchdStsTmStmp>

**P1833** 							<SttlmStsFlng>

**P1834** 								<Rsn>

**P1835** 									<Cd>

**P1836** 										<Cd>CMON</Cd>

**P1837** 									</Cd>

**P1838** 									<AddtlRsnInf>Instruction failed because Participant Y had insufficient cash to settle</AddtlRsnInf>

**P1839** 								</Rsn>

**P1840** 							</SttlmStsFlng>

**P1841** 							<BizDayEvt>

**P1842** 								<Tp>

**P1843** 									<Prtry>

**P1844** 										<Id>EDVP</Id>

**P1845** 										<SchmeNm>EVTP</SchmeNm>

**P1846** 										<Issr>T2S</Issr>

**P1847** 									</Prtry>

**P1848** 								</Tp>

**P1849** 								<SchdldTm>2025-06-21T16:00:00Z</SchdldTm>

**P1850** 								<StartTm>2025-06-21T16:00:03Z</StartTm>

**P1851** 								<EndTm>2025-06-21T16:01:45Z</EndTm>

**P1852** 							</BizDayEvt>

**P1853** 						</TxDtls>

**P1854** 					</RltdTx>

**P1855** 				</PnltyDtls>

**P1856** 			</PnltyPerCtrPty>

**P1857** 		</Pnlty>

**P1858** 	</SctiesTxPnltiesRpt>

