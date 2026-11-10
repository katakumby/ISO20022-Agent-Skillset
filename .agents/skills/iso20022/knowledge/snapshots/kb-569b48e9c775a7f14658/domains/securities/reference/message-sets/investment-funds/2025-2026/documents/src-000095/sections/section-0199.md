---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Account Management ", "AccountDetailsConfirmation acmt.002.001.08"]
content_origin: "source-transcription"
---

# AccountDetailsConfirmation acmt.002.001.08

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Account Management  / AccountDetailsConfirmation acmt.002.001.08.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1309** AccountDetailsConfirmation acmt.002.001.08

**P1310** Description

**P1311** An AccountDetailsConfirmation message is sent from an account servicer to an account owner to confirm the opening of an account. 

**P1312** This AccountDetailsConfirmation message confirms the opening of account number XYZ123456789, which was instructed via the 'AccountOpeningInstruction acmt.001.001.08 - 1' message above, with reference 123456-1. This message confirms that the account is active. 

**P1313** The complete set of account information, account parties information, investment plan and cash settlement information that was specified in the AccountOpeningInstruction message is returned in the AccountDetailsConfirmation message.

**P1314** Message Instance

**P1315** <AcctDtlsConf>

**P1316** 	<MsgId>

**P1317** 		<Id>123456-2</Id>

**P1318** 		<CreDtTm>2020-01-06T14:30:30</CreDtTm>

**P1319** 	</MsgId>

**P1320** 	<ConfDtls>

**P1321** 		<ConfTp>

**P1322** 			<Cd>ACCO</Cd>

**P1323** 		</ConfTp>

**P1324** 	</ConfDtls>

**P1325** 	<InvstmtAcct>

**P1326** 		<Id>XYZ123456789</Id>

**P1327** 		<AcctSts>

**P1328** 			<Nbld>

**P1329** 				<NoSpcfdRsn>NORE</NoSpcfdRsn>

**P1330** 			</Nbld>

**P1331** 		</AcctSts>

**P1332** 		<OwnrshTp>

**P1333** 			<Cd>JOIN</Cd>

**P1334** 		</OwnrshTp>

**P1335** 		<StmtFrqcy>

**P1336** 			<Cd>MNTH</Cd>

**P1337** 		</StmtFrqcy>

**P1338** 		<RefCcy>EUR</RefCcy>

**P1339** 		<TaxWhldgMtd>WTHD</TaxWhldgMtd>

**P1340** 		<ReqrdSgntriesNb>1</ReqrdSgntriesNb>

**P1341** 		<FndFmlyNm>Pension Equity Growth</FndFmlyNm>

**P1342** 	</InvstmtAcct>

**P1343** 	<AcctPties>

**P1344** 		<PrncplAcctPty>

**P1345** 			<PmryOwnr>

**P1346** 				<Pty>

**P1347** 					<IndvPrsn>

**P1348** 						<GvnNm>Richard</GvnNm>

**P1349** 						<Nm>Lee</Nm>

**P1350** 						<BirthDt>1961-05-09</BirthDt>

**P1351** 						<PstlAdr>

**P1352** 							<AdrTp>

**P1353** 								<Cd>HOME</Cd>

**P1354** 							</AdrTp>

**P1355** 							<MlngInd>true</MlngInd>

**P1356** 							<RegnAdrInd>true</RegnAdrInd>

**P1357** 							<AdrLine>Avenue Ariane 152</AdrLine>

**P1358** 							<PstCd>75005</PstCd>

**P1359** 							<TwnNm>Paris</TwnNm>

**P1360** 							<Ctry>FR</Ctry>

**P1361** 						</PstlAdr>

**P1362** 						<Ctznsh>

**P1363** 							<Ntlty>FR</Ntlty>

**P1364** 							<MnrInd>false</MnrInd>

**P1365** 						</Ctznsh>

**P1366** 					</IndvPrsn>

**P1367** 				</Pty>

**P1368** 				<MnyLndrgChck>

**P1369** 					<Cd>PASS</Cd>

**P1370** 				</MnyLndrgChck>

**P1371** 				<SgntryRghtInd>true</SgntryRghtInd>

**P1372** 			</PmryOwnr>

**P1373** 		</PrncplAcctPty>

**P1374** 		<ScndryOwnr>

**P1375** 			<Pty>

**P1376** 				<IndvPrsn>

**P1377** 					<GvnNm>Suzanne</GvnNm>

**P1378** 					<Nm>Plessey</Nm>

**P1379** 					<BirthDt>1962-05-16</BirthDt>

**P1380** 					<PstlAdr>

**P1381** 						<AdrTp>

**P1382** 							<Cd>HOME</Cd>

**P1383** 							</AdrTp>

**P1384** 						<MlngInd>true</MlngInd>

**P1385** 						<RegnAdrInd>true</RegnAdrInd>

**P1386** 						<AdrLine>Avenue Ariane 152</AdrLine>

**P1387** 						<PstCd>75005</PstCd>

**P1388** 						<TwnNm>Paris</TwnNm>

**P1389** 						<Ctry>FR</Ctry>

**P1390** 					</PstlAdr>

**P1391** 					<Ctznsh>

**P1392** 						<Ntlty>FR</Ntlty>

**P1393** 						<MnrInd>false</MnrInd>

**P1394** 					</Ctznsh>

**P1395** 				</IndvPrsn>

**P1396** 			</Pty>

**P1397** 			<MnyLndrgChck>

**P1398** 				<Cd>PASS</Cd>

**P1399** 			</MnyLndrgChck>

**P1400** 			<SgntryRghtInd>false</SgntryRghtInd>

**P1401** 		</ScndryOwnr>

**P1402** 	</AcctPties>

**P1403** 	<SvgsInvstmtPlan>

**P1404** 		<Frqcy>

**P1405** 			<Cd>YEAR</Cd>

**P1406** 		</Frqcy>

**P1407** 		<StartDt>2020-02-02</StartDt>

**P1408** 		<Qty>

**P1409** 			<Amt Ccy="EUR">523.20</Amt>

**P1410** 		</Qty>

**P1411** 		<SctyDtls>

**P1412** 			<Qty>

**P1413** 				<Pctg>100</Pctg>

**P1414** 			</Qty>

**P1415** 			<FinInstrm>

**P1416** 				<Id>

**P1417** 					<ISIN>FR1234567890</ISIN>

**P1418** 				</Id>

**P1419** 				<Nm>Pension Equity Growth Europe B</Nm>

**P1420** 			<SctiesForm>BEAR</SctiesForm>

**P1421** 					<DstrbtnPlcy>ACCU</DstrbtnPlcy>

**P1422** 			</FinInstrm>

**P1423** 		</SctyDtls>

**P1424** 	</SvgsInvstmtPlan>

**P1425** 	<CshSttlm>

**P1426** 		<OthrCshSttlmDtls>

**P1427** 			<SttlmCcy>EUR</SttlmCcy>

**P1428** 			<SvgsPlanPmtInstrm>

**P1429** 				<DrctDbtDtls>

**P1430** 					<DbtrAcct>

**P1431** 						<Id>

**P1432** 							<IBAN>FR12345678987654321</IBAN>

**P1433** 						</Id>

**P1434** 					</DbtrAcct>

**P1435** 					<DbtrAgt>

**P1436** 						<BICFI>ASRVFRXX</BICFI>

**P1437** 					</DbtrAgt>

**P1438** 				</DrctDbtDtls>

**P1439** 			</SvgsPlanPmtInstrm>

**P1440** 		</OthrCshSttlmDtls>

**P1441** 	</CshSttlm>

**P1442** </AcctDtlsConf>

