---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Statements", "StatementOfInvestmentFundTransactions semt.006.001.02"]
content_origin: "source-transcription"
---

# StatementOfInvestmentFundTransactions semt.006.001.02

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Statements / StatementOfInvestmentFundTransactions semt.006.001.02.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5687** StatementOfInvestmentFundTransactions semt.006.001.02

**P5688** Description

**P5689** A StatementOfInvestmentFundTransactions (semt.006.001.02) is sent by an account servicer to the account owner of account 123456. This statement contains only the transactions with a trade date between 02 February 2015 and 02 March 2015 (inclusive). The statement has the reference TransStat111 and reports the following transactions: 

**P5690** The subscription to 1,500 units of the fund with ISIN FR1234567890. The transaction is executed and the units are registered.

**P5691** The subscription to 2,500 units of the fund with ISIN FR0567891234. The transaction is executed and the units are registered.

**P5692** The transfer in of 500 units of the fund with ISIN FR0567891234. The transaction is executed and the units are registered.

**P5693** XML Instance

**P5694** <StmtOfInvstmtFndTxs>

**P5695** 	<MsgId>

**P5696** 			<Id>AC0016</Id>

**P5697** 			<CreDtTm>2020-03-03T09:30:30</CreDtTm>

**P5698** 	</MsgId>

**P5699** 	<MsgPgntn>

**P5700** 			<PgNb>1</PgNb>

**P5701** 			<LastPgInd>true</LastPgInd>

**P5702** 	</MsgPgntn>

**P5703** 	<StmtGnlDtls>

**P5704** 			<Ref>TransStat111</Ref>

**P5705** 			<StmtPrd>

**P5706** 					<FrDt>2020-02-02</FrDt>

**P5707** 					<ToDt>2020-03-02</ToDt>

**P5708** 			</StmtPrd>

**P5709** 			<UpdTp>COMP</UpdTp>

**P5710** 			<ActvtyInd>true</ActvtyInd>

**P5711** 	</StmtGnlDtls>

**P5712** 	<InvstmtAcctDtls>

**P5713** 		<Id>

**P5714** 			<Prtry>

**P5715** 				<Id>123456</Id>

**P5716** 			</Prtry>

**P5717** 		</Id>

**P5718** 	</InvstmtAcctDtls>

**P5719** 	<TxOnAcct>

**P5720** 			<Id>

**P5721** 				<ISIN>FR1234567890</ISIN>

**P5722** 			</Id>

**P5723** 			<TxDtls>

**P5724** 				<EvtTp>

**P5725** 					<TxTp>

**P5726** 						<Tp>SUBS</Tp>

**P5727** 					</TxTp>

**P5728** 				</EvtTp>

**P5729** 			<SttldTxInd>true</SttldTxInd>

**P5730** 			<RegdTxInd>true</RegdTxInd>

**P5731** 			<UnitsQty>

**P5732** 				<Unit>1500</Unit>

**P5733** 			</UnitsQty>

**P5734** 			<CdtDbt>CRDT</CdtDbt>

**P5735** 			<TradDtTm>

**P5736** 				<Dt>2020-02-16</Dt>

**P5737** 			</TradDtTm>

**P5738** 			<CumDvddInd>true</CumDvddInd>

**P5739** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P5740** 			</TxDtls>

**P5741** 	</TxOnAcct>

**P5742** 	<TxOnAcct>

**P5743** 			<Id>

**P5744** 				<ISIN>FR0567891234</ISIN>

**P5745** 			</Id>

**P5746** 			<TxDtls>

**P5747** 				<EvtTp>

**P5748** 					<TxTp>

**P5749** 						<Tp>SUBS</Tp>

**P5750** 					</TxTp>

**P5751** 				</EvtTp>

**P5752** 				<SttldTxInd>true</SttldTxInd>

**P5753** 			<RegdTxInd>true</RegdTxInd>

**P5754** 			<UnitsQty>

**P5755** 				<Unit>2500</Unit>

**P5756** 			</UnitsQty>

**P5757** 			<CdtDbt>CRDT</CdtDbt>

**P5758** 			<TradDtTm>

**P5759** 				<Dt>2020-02-17</Dt>

**P5760** 			</TradDtTm>

**P5761** 			<CumDvddInd>true</CumDvddInd>

**P5762** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P5763** 			</TxDtls>

**P5764** 	</TxOnAcct>

**P5765** 	<TxOnAcct>

**P5766** 			<Id>

**P5767** 				<ISIN>FR0567891234</ISIN>

**P5768** 			</Id>

**P5769** 			<TxDtls>

**P5770** 				<EvtTp>

**P5771** 					<TxTp>

**P5772** 						<Tp>TRIN</Tp>

**P5773** 					</TxTp>

**P5774** 				</EvtTp>

**P5775** 				<SttldTxInd>true</SttldTxInd>

**P5776** 			<RegdTxInd>true</RegdTxInd>

**P5777** 			<UnitsQty>

**P5778** 				<Unit>500</Unit>

**P5779** 			</UnitsQty>

**P5780** 			<CdtDbt>CRDT</CdtDbt>

**P5781** 			<TradDtTm>

**P5782** 				<Dt>2020-02-17</Dt>

**P5783** 			</TradDtTm>

**P5784** 			<CumDvddInd>true</CumDvddInd>

**P5785** 			<PrtlyExctdInd>false</PrtlyExctdInd>

**P5786** 		</TxDtls>

**P5787** 	</TxOnAcct>

**P5788** </StmtOfInvstmtFndTxs>

