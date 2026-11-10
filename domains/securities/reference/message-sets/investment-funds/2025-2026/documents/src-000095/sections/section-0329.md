---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000095"]
source_editions: ["March 2025"]
message_ids: []
heading_path: ["Business Examples", "Statements", "CustodyStatementOfHoldings semt.002.001.02"]
content_origin: "source-transcription"
---

# CustodyStatementOfHoldings semt.002.001.02

Source: [src-000095](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart1_InvestmentFunds_2025_2026_v2.docx). Locator: heading path Business Examples / Statements / CustodyStatementOfHoldings semt.002.001.02.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P5457** CustodyStatementOfHoldings semt.002.001.02

**P5458** Description

**P5459** A CustodyStatementOfHoldings message is sent by an account servicer to the account owner of account abc123 to report its holdings as of 02 March 2007. The statement has the reference CustStat111 and there has been activity on this account since the previous statement. The holding of this fungible account is composed of:

**P5460** 1,000 units of the fund with ISIN LU1234567890. 

**P5461** 750 units of the fund with ISIN LU0987456123.

**P5462** XML Instance

**P5463** <CtdyStmtOfHldgsV02>

**P5464** 	<MsgId>

**P5465** 		<Id>ASS001</Id>

**P5466** 		<CreDtTm>2007-03-05T09:30:30</CreDtTm>

**P5467** 	</MsgId>

**P5468** 	<MsgPgntn>

**P5469** 	<PgNb>1</PgNb>

**P5470** 	<LastPgInd>true</LastPgInd>

**P5471** 	</MsgPgntn>

**P5472** 	<StmtGnlDtls>

**P5473** 		<Ref>CustStat111</Ref>

**P5474** 		<StmtDtTm>

**P5475** 			<Dt>2007-03-02</Dt>

**P5476** 		</StmtDtTm>

**P5477** 		<Frqcy>

**P5478** 			<FrqcyAsCd>YEAR</FrqcyAsCd>

**P5479** 		</Frqcy>

**P5480** 		<UpdTp>

**P5481** 			<StmtUpdTpAsCd>COMP</StmtUpdTpAsCd>

**P5482** 		</UpdTp>

**P5483** 		<ActvtyInd>true</ActvtyInd>

**P5484** 		<StmtBsis>

**P5485** 			<StmtBsisAsCd>CONT</StmtBsisAsCd>

**P5486** 		</StmtBsis>

**P5487** 	</StmtGnlDtls>

**P5488** 	<AcctDtls>

**P5489** 		<Id>

**P5490** 			<SmplId>

**P5491** 				<Prtry>

**P5492** 					<Id>abc123</Id>

**P5493** 				</Prtry>

**P5494** 			</SmplId>

**P5495** 		</Id>

**P5496** 		<FngbInd>true</FngbInd>

**P5497** 	</AcctDtls>

**P5498** 	<BalForAcct>

**P5499** 		<AggtQty>

**P5500** 			<Qty>

**P5501** 				<Unit>1000</Unit>

**P5502** 			</Qty>

**P5503** 		</AggtQty>

**P5504** 		<FinInstrmDtls>

**P5505** 			<Id>

**P5506** 				<ISIN>LU1234567890</ISIN>

**P5507** 			</Id>

**P5508** 		</FinInstrmDtls>

**P5509** 	</BalForAcct>

**P5510** 	<BalForAcct>

**P5511** 		<AggtQty>

**P5512** 			<Qty>

**P5513** 				<Unit>750</Unit>

**P5514** 			</Qty>

**P5515** 		</AggtQty>

**P5516** 		<FinInstrmDtls>

**P5517** 			<Id>

**P5518** 				<ISIN>LU0987456123</ISIN>

**P5519** 			</Id>

**P5520** 		</FinInstrmDtls>

**P5521** 	</BalForAcct>

**P5522** </CtdyStmtOfHldgsV02>

