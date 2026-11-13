---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesBalanceAccountingReport semt.003.001.12"]
content_origin: "source-transcription"
---

# SecuritiesBalanceAccountingReport semt.003.001.12

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / SecuritiesBalanceAccountingReport semt.003.001.12.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P755** SecuritiesBalanceAccountingReport semt.003.001.12

**P756** Description

**P757** The Securities Balance Accounting Report message (semt.003.001.09) is sent by the account servicer (Dresdner Bank London (DRESGB2L)) , to the account owner (Dresdner Bank Frankfurt (DRESDEFF) for account 222S , to report the holding as of 15 January 2019.

**P758** Business Data

**P759** General Information

**P760** Number of pages: 1

**P761** Statement Date: 15/01/2019

**P762** Frequency: daily

**P763** Update type: complete

**P764** Statement Basis: Traded

**P765** Activity indicator: true

**P766** Audited Indicator: True

**P767** Sub Account Indicator: false

**P768** Account and Balances

**P769** Safekeeping Account: 222S

**P770** Financial Instrument Identification for each positions:

**P771** GB0987654321 long of 4,000,000 aggregate balance

**P772** Price Type: Market

**P773** Value Type: Par value

**P774** Rate: 100.2

**P775** Holding value of the position in account base currency: GBP 12,458,799

**P776** GB0000987654 long of 6,000,000 aggregate balance

**P777** Price Type: Market

**P778** Value Type: Par value

**P779** Par Value Rate: 102

**P780** Holding value of the position in account base currency: GBP 6,012,000

**P781** GB0000000123 long of 2,000 aggregate balance

**P782** Price Type: Market

**P783** Value Type: Par value

**P784** Par Value Amount: GBP 124.23

**P785** Holding value of the position in account base currency: GBP 248,460

**P786** GB0000123456 long of 70,000 aggregate balance

**P787** Price Type: Market

**P788** Value Type: Par value

**P789** Par Value Amount: GBP 101

**P790** Holding value of the position in account base currency: GBP 70,700

**P791** Total Holding Value of the Statement in account base currency: GBP 12,456,789

**P792** Message Instance

**P793** <SctiesBalAcctgRpt>

**P794** 	<Pgntn>

**P795** 		<PgNb>1</PgNb>

**P796** 		<LastPgInd>true</LastPgInd>

**P797** 	</Pgntn>

**P798** 	<StmtGnlDtls>

**P799** 		<StmtDtTm>

**P800** 			<Dt>2019-01-15</Dt>

**P801** 		</StmtDtTm>

**P802** 		<Frqcy>

**P803** 			<Cd>DAIL</Cd>

**P804** 		</Frqcy>

**P805** 		<UpdTp>

**P806** 			<Cd>COMP</Cd>

**P807** 		</UpdTp>

**P808** 		<StmtBsis>

**P809** 			<Cd>TRAD</Cd>

**P810** 		</StmtBsis>

**P811** 		<ActvtyInd>true</ActvtyInd>

**P812** 		<AudtdInd>true</AudtdInd>

**P813** 		<SubAcctInd>false</SubAcctInd>

**P814** 	</StmtGnlDtls>

**P815** 	<SfkpgAcct>

**P816** 		<Id>222S</Id>

**P817** 	</SfkpgAcct>

**P818** 	<BalForAcct>

**P819** 		<FinInstrmId>

**P820** 			<ISIN>GB0987654321</ISIN>

**P821** 			</FinInstrmId>

**P822** 		<AggtBal>

**P823** 			<ShrtLngInd>LONG</ShrtLngInd>

**P824** 			<Qty>

**P825** 				<Qty>

**P826** 					<Qty>

**P827** 						<FaceAmt>4000000</FaceAmt>

**P828** 					</Qty>

**P829** 				</Qty>

**P830** 			</Qty>

**P831** 		</AggtBal>

**P832** 		<PricDtls>

**P833** 			<Tp>

**P834** 				<Cd>MRKT</Cd>

**P835** 			</Tp>

**P836** 				<Val>

**P837** 				<Rate>100.2</Rate>

**P838** 			</Val>

**P839** 			<ValTp>

**P840** 				<ValTp>PARV</ValTp>

**P841** 			</ValTp>

**P842** 		</PricDtls>

**P843** 		<AcctBaseCcyAmts>

**P844** 			<HldgVal>

**P845** 				<Amt Ccy="GBP">12458799</Amt>

**P846** 				<Sgn>true</Sgn>

**P847** 			</HldgVal>

**P848** 		</AcctBaseCcyAmts>

**P849** 	</BalForAcct>

**P850** 	<BalForAcct>

**P851** 		<FinInstrmId>

**P852** 			<ISIN>GB0000987654</ISIN>

**P853** 			</FinInstrmId>

**P854** 		<AggtBal>

**P855** 			<ShrtLngInd>LONG</ShrtLngInd>

**P856** 			<Qty>

**P857** 				<Qty>

**P858** 					<Qty>

**P859** 						<FaceAmt>6000000</FaceAmt>

**P860** 					</Qty>

**P861** 			</Qty>

**P862** 			</Qty>

**P863** 		</AggtBal>

**P864** 		<PricDtls>

**P865** 			<Tp>

**P866** 				<Cd>MRKT</Cd>

**P867** 			</Tp>

**P868** 				<Val>

**P869** 				<Rate>102</Rate>

**P870** 			</Val>

**P871** 			<ValTp>

**P872** 				<ValTp>PARV</ValTp>

**P873** 			</ValTp>

**P874** 		</PricDtls>

**P875** 		<AcctBaseCcyAmts>

**P876** 			<HldgVal>

**P877** 				<Amt Ccy="GBP">6012000</Amt>

**P878** 				<Sgn>true</Sgn>

**P879** 			</HldgVal>

**P880** 		</AcctBaseCcyAmts>

**P881** 	</BalForAcct>

**P882** 	<BalForAcct>

**P883** 		<FinInstrmId>

**P884** 			<ISIN>GB0000000123</ISIN>

**P885** 			</FinInstrmId>

**P886** 		<AggtBal>

**P887** 			<ShrtLngInd>LONG</ShrtLngInd>

**P888** 			<Qty>

**P889** 				<Qty>

**P890** 					<Qty>

**P891** 						<Unit>2000</Unit>

**P892** 					</Qty>

**P893** 				</Qty>

**P894** 			</Qty>

**P895** 		</AggtBal>

**P896** 		<PricDtls>

**P897** 			<Tp>

**P898** 				<Cd>MRKT</Cd>

**P899** 			</Tp>

**P900** 				<Val>

**P901** 				<Amt Ccy="GBP">124.23</Amt>

**P902** 			</Val>

**P903** 			<ValTp>

**P904** 				<ValTp>PARV</ValTp>

**P905** 			</ValTp>

**P906** 		</PricDtls>

**P907** 		<AcctBaseCcyAmts>

**P908** 			<HldgVal>

**P909** 				<Amt Ccy="GBP">248460</Amt>

**P910** 				<Sgn>true</Sgn>

**P911** 			</HldgVal>

**P912** 		</AcctBaseCcyAmts>

**P913** 	</BalForAcct>

**P914** 	<BalForAcct>

**P915** 		<FinInstrmId>

**P916** 			<ISIN>GB0000123456</ISIN>

**P917** 			</FinInstrmId>

**P918** 		<AggtBal>

**P919** 			<ShrtLngInd>LONG</ShrtLngInd>

**P920** 			<Qty>

**P921** 				<Qty>

**P922** 					<Qty>

**P923** 						<Unit>70000</Unit>

**P924** 					</Qty>

**P925** 				</Qty>

**P926** 			</Qty>

**P927** 		</AggtBal>

**P928** 		<PricDtls>

**P929** 			<Tp>

**P930** 				<Cd>MRKT</Cd>

**P931** 			</Tp>

**P932** 				<Val>

**P933** 				<Rate>101</Rate>

**P934** 			</Val>

**P935** 			<ValTp>

**P936** 				<ValTp>PARV</ValTp>

**P937** 			</ValTp>

**P938** 		</PricDtls>

**P939** 		<AcctBaseCcyAmts>

**P940** 			<HldgVal>

**P941** 				<Amt Ccy="GBP">70700</Amt>

**P942** 				<Sgn>true</Sgn>

**P943** 			</HldgVal>

**P944** 		</AcctBaseCcyAmts>

**P945** 	</BalForAcct>

**P946** 	<AcctBaseCcyTtlAmts>

**P947** 		<TtlHldgsValOfStmt>

**P948** 			<Amt Ccy="GBP">12456789</Amt>

**P949** 			<Sgn>true</Sgn>

**P950** 		</TtlHldgsValOfStmt>

**P951** 	</AcctBaseCcyTtlAmts>

**P952** </SctiesBalAcctgRpt>

