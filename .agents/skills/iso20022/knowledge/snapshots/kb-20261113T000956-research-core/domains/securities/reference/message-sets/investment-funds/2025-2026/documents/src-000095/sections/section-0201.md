---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Account Management ", "AccountModificationInstruction acmt.003.001.08 – 2 "]
content_origin: "source-transcription"
---

# AccountModificationInstruction acmt.003.001.08 – 2 

Source: [src-000095](../../../../../../../../../evidence/omitted/ffbc05daa043e55c6bd0cc1a.md). Locator: heading path Business Examples / Account Management  / AccountModificationInstruction acmt.003.001.08 – 2 .

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P1518** AccountModificationInstruction acmt.003.001.08 – 2 

**P1519** Description

**P1520** An AccountModificationInstruction message is sent by an account owner to an account servicer in order to instruct modifications to the existing account information.

**P1521** This AccountModificationInstruction message instructs updates to account number 66666666. It instructs updates (UPDT) to the primary owner (Martin Johnson) data set because the following information is now available

**P1522** Customer conduct classification is standard (STAN)

**P1523** Risk level is low (LOWW)

**P1524** Know Your Customer Check is ordinary (ORDN)

**P1525** MiFID classification is eligible (ELIG)

**P1526** Message Instance

**P1527** <AcctModInstr>

**P1528** 	<MsgId>

**P1529** 		<Id>123456-12</Id>

**P1530** 		<CreDtTm>2020-01-06T16:30:00</CreDtTm>

**P1531** 	</MsgId>

**P1532** 	<InvstmtAcctSelctn>	

**P1533** 		<AcctId>66666666</AcctId>

**P1534** 	</InvstmtAcctSelctn>

**P1535** 	<ModfdAcctPties>

**P1536** 		<ModScpIndctn>UPDT</ModScpIndctn>

**P1537** 		<PrncplAcctPty>

**P1538** 			<PmryOwnr>

**P1539** 				<Pty>

**P1540** 					<IndvPrsn>

**P1541** 						<GvnNm>Martin</GvnNm>

**P1542** 						<Nm>Johnson</Nm>

**P1543** 						<BirthDt>1957-05-11</BirthDt>

**P1544** 					</IndvPrsn>

**P1545** 				</Pty>

**P1546** 				<ModfdInvstrPrflVldtn>

**P1547** 					<ModScpIndctn>INSE</ModScpIndctn>

**P1548** 					<InvstrPrflVldtn>

**P1549** 						<CstmrCndctClssfctn>

**P1550** 							<Cd>STAN</Cd>

**P1551** 						</CstmrCndctClssfctn>

**P1552** 						<RskLvl>

**P1553** 							<Cd>LOWW</Cd>

**P1554** 						</RskLvl>

**P1555** 						<KnowYourCstmrChckTp>

**P1556** 							<Cd>ORDN</Cd>

**P1557** 						</KnowYourCstmrChckTp>

**P1558** 					</InvstrPrflVldtn>

**P1559** 				</ModfdInvstrPrflVldtn>

**P1560** 				<MiFIDClssfctn>

**P1561** 					<Clssfctn>ELIG</Clssfctn>

**P1562** 				</MiFIDClssfctn>

**P1563** 			</PmryOwnr>

**P1564** 		</PrncplAcctPty>

**P1565** 	</ModfdAcctPties>

**P1566** </AcctModInstr>

