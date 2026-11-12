---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Account Management ", "AccountModificationInstruction acmt.003.001.08 – 1 "]
content_origin: "source-transcription"
---

# AccountModificationInstruction acmt.003.001.08 – 1 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Account Management  / AccountModificationInstruction acmt.003.001.08 – 1 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1443** AccountModificationInstruction acmt.003.001.08 – 1 

**P1444** Description

**P1445** An AccountModificationInstruction message is sent by an account owner to an account servicer in order to instruct modifications to the existing account information. 

**P1446** This AccountModificationInstruction message instructs updates to account number XYZ123456789. It instructs the following updates:

**P1447** Addition of an end date to the investment plan

**P1448** Replacement of the direct debit payment information by payment via a credit card owned by Richard Lee. This is done by requesting the deletion (DELT) of the direct debit information and the insertion (INSE) of the new credit card payment information.

**P1449** Message Instance

**P1450** <AcctModInstr>

**P1451** 	<MsgId>

**P1452** 		<Id>123456-3</Id>

**P1453** 		<CreDtTm>2020-01-14T09:00:00</CreDtTm>

**P1454** 	</MsgId>

**P1455** 	<InstrDtls>

**P1456** 		<ModRsn>Update savings plan end date, replace direct debit by credit card</ModRsn>

**P1457** 	</InstrDtls>

**P1458** 	<InvstmtAcctSelctn>

**P1459** 		<AcctId>XYZ123456789</AcctId>

**P1460** 	</InvstmtAcctSelctn>

**P1461** 	<ModfdSvgsInvstmtPlan>

**P1462** 		<ModScpIndctn>UPDT</ModScpIndctn>

**P1463** 		<InvstmtPlan>

**P1464** 			<Frqcy>

**P1465** 				<Cd>MNTH</Cd>

**P1466** 			</Frqcy>

**P1467** 			<StartDt>2020-02-02</StartDt>

**P1468** 			<EndDt>2027-02-03</EndDt>

**P1469** 			<Qty>

**P1470** 				<Amt Ccy="EUR">523.20</Amt>

**P1471** 			</Qty>

**P1472** 			<SctyDtls>

**P1473** 				<Qty>

**P1474** 					<Pctg>100</Pctg>

**P1475** 				</Qty>

**P1476** 				<FinInstrm>

**P1477** 					<Id>

**P1478** 						<ISIN>FR1234567890</ISIN>

**P1479** 					</Id>

**P1480** 				</FinInstrm>

**P1481** 			</SctyDtls>

**P1482** 		</InvstmtPlan>

**P1483** 	</ModfdSvgsInvstmtPlan>

**P1484** 	<ModfdCshSttlm>

**P1485** 		<ModScpIndctn>DELT</ModScpIndctn>

**P1486** 		<OthrCshSttlmDtls>

**P1487** 			<SttlmCcy>EUR</SttlmCcy>

**P1488** 			<SvgsPlanPmtInstrm>

**P1489** 				<DrctDbtDtls>

**P1490** 					<DbtrAcct>

**P1491** 						<Id>

**P1492** 							<IBAN>FR12345678987654321</IBAN>

**P1493** 						</Id>

**P1494** 					</DbtrAcct>

**P1495** 					<DbtrAgt>

**P1496** 						<BICFI>ASRVFRXX</BICFI>

**P1497** 					</DbtrAgt>

**P1498** 				</DrctDbtDtls>

**P1499** 			</SvgsPlanPmtInstrm>

**P1500** 		</OthrCshSttlmDtls>

**P1501** 	</ModfdCshSttlm>

**P1502** 	<ModfdCshSttlm>

**P1503** 		<ModScpIndctn>INSE</ModScpIndctn>

**P1504** 		<OthrCshSttlmDtls>

**P1505** 			<SttlmCcy>EUR</SttlmCcy>

**P1506** 			<SvgsPlanPmtInstrm>

**P1507** 				<PmtCardDtls>

**P1508** 					<Tp>CRDT</Tp>

**P1509** 					<Nb>1234567890123456</Nb>

**P1510** 					<HldrNm>Richard Lee</HldrNm>

**P1511** 					<XpryDt>2023-09</XpryDt>

**P1512** 				</PmtCardDtls>

**P1513** 			</SvgsPlanPmtInstrm>

**P1514** 		</OthrCshSttlmDtls>

**P1515** 	</ModfdCshSttlm>

**P1516** </AcctModInstr>

