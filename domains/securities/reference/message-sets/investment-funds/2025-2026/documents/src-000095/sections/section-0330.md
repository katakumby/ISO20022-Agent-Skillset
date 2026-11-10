---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Statements", "AccountingStatementOfHoldings semt.003.001.02"]
content_origin: "source-transcription"
---

# AccountingStatementOfHoldings semt.003.001.02

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Statements / AccountingStatementOfHoldings semt.003.001.02.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5523** AccountingStatementOfHoldings semt.003.001.02

**P5524** Description

**P5525** The AccountingStatementOfHoldings message is sent by an account servicer to the account owner of account xyz123, to report its holdings as of 02 February 2007. The statement is an audited statement, with the statement reference AccStat111. This fungible account xyz123 is divided into 2 sub-accounts:

**P5526** Fungible sub-account xyz123-1 contains 6,000 units of the fund with ISIN LU4561237890, which represents a holding value of 3,000 EUR with the net asset value per unit of 0.5 EUR.

**P5527** This account also contains: 2,500 units of the fund with ISIN LU0001112222, which represents a holding value of 5,000 EUR, with the Net Asset Value per unit of 2 EUR; and 7,000 units of the fund with ISIN LU9157326840, which represents a holding value of 7,000 EUR, with the net asset value per unit of 1 EUR.

**P5528** There is no activity on the fungible sub-account xyz123-2.

**P5529** The value of all the holdings contained in account xyz123 is 15,000 EUR.

**P5530** XML Instance

**P5531** <AcctgStmtOfHldgsV02>

**P5532** 	<MsgId>

**P5533** 		<Id>ASS002</Id>

**P5534** 		<CreDtTm>2007-02-20T09:30:30</CreDtTm>

**P5535** 	</MsgId>

**P5536** 	<MsgPgntn>

**P5537** 		<PgNb>1</PgNb>

**P5538** 		<LastPgInd>true</LastPgInd>

**P5539** 	</MsgPgntn>

**P5540** 	<StmtGnlDtls>

**P5541** 		<Ref>AccStat111</Ref>

**P5542** 		<StmtDtTm>

**P5543** 			<Dt>2007-02-02</Dt>

**P5544** 		</StmtDtTm>

**P5545** 		<Frqcy>

**P5546** 			<FrqcyAsCd>YEAR</FrqcyAsCd>

**P5547** 		</Frqcy>

**P5548** 		<UpdTp>

**P5549** 			<StmtUpdTpAsCd>COMP</StmtUpdTpAsCd>

**P5550** 		</UpdTp>

**P5551** 		<ActvtyInd>true</ActvtyInd>

**P5552** 		<StmtBsis>

**P5553** 			<StmtBsisAsCd>CONT</StmtBsisAsCd>

**P5554** 		</StmtBsis>

**P5555** 		<AudtdInd>true</AudtdInd>

**P5556** 	</StmtGnlDtls>

**P5557** 	<AcctDtls>

**P5558** 		<Id>

**P5559** 			<SmplId>

**P5560** 				<Prtry>

**P5561** 					<Id>xyz123</Id>

**P5562** 				</Prtry>

**P5563** 			</SmplId>

**P5564** 		</Id>

**P5565** 		<FngbInd>true</FngbInd>

**P5566** 	</AcctDtls>

**P5567** 	<SubAcctDtls>

**P5568** 		<Id>

**P5569** 			<SmplId>

**P5570** 				<Prtry>

**P5571** 					<Id>xyz123-1</Id>

**P5572** 				</Prtry>

**P5573** 			</SmplId>

**P5574** 		</Id>

**P5575** 		<FngbInd>true</FngbInd>

**P5576** 		<ActvtyInd>true</ActvtyInd>

**P5577** 		<BalForSubAcct>

**P5578** 			<AggtQty>

**P5579** 				<Qty>

**P5580** 					<Unit>6000</Unit>

**P5581** 				</Qty>

**P5582** 			</AggtQty>

**P5583** 			<HldgVal Ccy="EUR">3000</HldgVal>

**P5584** 			<FinInstrmDtls>

**P5585** 				<Id>

**P5586** 					<ISIN>LU4561237890</ISIN>

**P5587** 				</Id>

**P5588** 			</FinInstrmDtls>

**P5589** 			<PricDtls>

**P5590** 				<Val>

**P5591** 					<Amt Ccy="EUR">0.5</Amt>

**P5592** 				</Val>

**P5593** 				<Tp>NAVL</Tp>

**P5594** 			</PricDtls>

**P5595** 		</BalForSubAcct>

**P5596** 		<BalForSubAcct>

**P5597** 			<AggtQty>

**P5598** 				<Qty>

**P5599** 					<Unit>2500</Unit>

**P5600** 				</Qty>

**P5601** 			</AggtQty>

**P5602** 			<HldgVal Ccy="EUR">5000</HldgVal>

**P5603** 			<FinInstrmDtls>

**P5604** 				<Id>

**P5605** 					<ISIN>LU0001112222</ISIN>

**P5606** 				</Id>

**P5607** 			</FinInstrmDtls>

**P5608** 			<PricDtls>

**P5609** 				<Val>

**P5610** 					<Amt Ccy="EUR">2</Amt>

**P5611** 				</Val>

**P5612** 				<Tp>NAVL</Tp>

**P5613** 			</PricDtls>

**P5614** 		</BalForSubAcct>

**P5615** 	<BalForSubAcct>

**P5616** 		<AggtQty>

**P5617** 			<Qty>

**P5618** 				<Unit>7000</Unit>

**P5619** 			</Qty>

**P5620** 		</AggtQty>

**P5621** 		<HldgVal Ccy="EUR">7000</HldgVal>

**P5622** 		<FinInstrmDtls>

**P5623** 			<Id>

**P5624** 				<ISIN>LU9157326840</ISIN>

**P5625** 			</Id>

**P5626** 		</FinInstrmDtls>

**P5627** 		<PricDtls>

**P5628** 			<Val>

**P5629** 				<Amt Ccy="EUR">1</Amt>

**P5630** 			</Val>

**P5631** 			<Tp>NAVL</Tp>

**P5632** 		</PricDtls>

**P5633** 	</BalForSubAcct>

**P5634** 	</SubAcctDtls>

**P5635** 	<SubAcctDtls>

**P5636** 		<Id>	

**P5637** 			<SmplId>

**P5638** 				<Prtry>

**P5639** 					<Id>xyz123-2</Id>

**P5640** 				</Prtry>

**P5641** 			</SmplId>

**P5642** 		</Id>

**P5643** 		<FngbInd>true</FngbInd>

**P5644** 		<ActvtyInd>false</ActvtyInd>

**P5645** 	</SubAcctDtls>

**P5646** 	<TtlVals>

**P5647** 		<TtlHldgsValOfStmt Ccy="EUR">15000</TtlHldgsValOfStmt>

**P5648** 	</TtlVals>

**P5649** </AcctgStmtOfHldgsV02>

