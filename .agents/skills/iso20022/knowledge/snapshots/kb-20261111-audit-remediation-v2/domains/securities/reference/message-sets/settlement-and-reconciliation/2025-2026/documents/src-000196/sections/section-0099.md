---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000196"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "SecuritiesBalanceCustodyReport semt.002.001.12"]
content_origin: "source-transcription"
---

# SecuritiesBalanceCustodyReport semt.002.001.12

Source: [src-000196](../../../../../../../../../evidence/omitted/590a0c85882f5e6c5c9ea627.md). Locator: heading path Business Examples / SecuritiesBalanceCustodyReport semt.002.001.12.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P638** SecuritiesBalanceCustodyReport semt.002.001.12

**P639** Description

**P640** The Securities Balance Custody Report message (semt.002.001.09) is sent by the account servicer (Dresdner Bank London (DRESGB2L)), to the account owner (Dresdner Bank Frankfurt (DRESDEFF) for account 222S, to report the holding as of 15 January 2019.

**P641** Business Data

**P642** General Information

**P643** Number of pages: 1

**P644** Statement Date: 15/01/2019

**P645** Frequency: daily

**P646** Update type: complete

**P647** Statement Basis: Settled

**P648** Activity indicator: true

**P649** Sub Account Indicator: false

**P650** Account and Balances

**P651** Safekeeping Account: 222S

**P652** GB0987654321 short of 4,000,000 aggregate balance

**P653** GB0000987654 short of 6,000,000 aggregate balance

**P654** GB0000000123 short of 2,000 aggregate balance

**P655** GB0000123456 short of 70,000 aggregate balance, sub-balance of 15,000 out on loan securities that can be recalled automatically (available)

**P656** Message Instance

**P657** <SctiesBalCtdyRpt>

**P658** 	<Pgntn>

**P659** 		<PgNb>1</PgNb>

**P660** 		<LastPgInd>true</LastPgInd>

**P661** 	</Pgntn>

**P662** 	<StmtGnlDtls>

**P663** 		<StmtDtTm>

**P664** 			<Dt>2019-01-15</Dt>

**P665** 		</StmtDtTm>

**P666** 		<Frqcy>

**P667** 			<Cd>DAIL</Cd>

**P668** 		</Frqcy>

**P669** 		<UpdTp>

**P670** 			<Cd>COMP</Cd>

**P671** 		</UpdTp>

**P672** 		<StmtBsis>

**P673** 			<Cd>SETT</Cd>

**P674** 		</StmtBsis>

**P675** 		<ActvtyInd>true</ActvtyInd>

**P676** 		<SubAcctInd>false</SubAcctInd>

**P677** 	</StmtGnlDtls>

**P678** 	<SfkpgAcct>

**P679** 		<Id>222S</Id>

**P680** 	</SfkpgAcct>

**P681** 	<BalForAcct>

**P682** 		<FinInstrmId>

**P683** 			<ISIN>GB0987654321</ISIN>

**P684** 		</FinInstrmId>

**P685** 		<AggtBal>

**P686** 			<ShrtLngInd>SHOR</ShrtLngInd>

**P687** 			<Qty>

**P688** 				<Qty>

**P689** 					<Qty>

**P690** 						<FaceAmt>4000000</FaceAmt>

**P691** 					</Qty>

**P692** 				</Qty>

**P693** 			</Qty>

**P694** 		</AggtBal>

**P695** 	</BalForAcct>

**P696** 	<BalForAcct>

**P697** 		<FinInstrmId>

**P698** 			<ISIN>GB0000987654</ISIN>

**P699** 		</FinInstrmId>

**P700** 		<AggtBal>

**P701** 			<ShrtLngInd>SHOR</ShrtLngInd>

**P702** 			<Qty>

**P703** 				<Qty>

**P704** 					<Qty>

**P705** 						<FaceAmt>6000000</FaceAmt>

**P706** 					</Qty>

**P707** 				</Qty>

**P708** 			</Qty>

**P709** 		</AggtBal>

**P710** 	</BalForAcct>

**P711** 	<BalForAcct>

**P712** 		<FinInstrmId>

**P713** 			<ISIN>GB0000000123</ISIN>

**P714** 			</FinInstrmId>

**P715** 		<AggtBal>

**P716** 			<ShrtLngInd>SHOR</ShrtLngInd>

**P717** 			<Qty>

**P718** 				<Qty>

**P719** 					<Qty>

**P720** 						<Unit>2000</Unit>

**P721** 					</Qty>

**P722** 				</Qty>

**P723** 			</Qty>

**P724** 		</AggtBal>

**P725** 	</BalForAcct>

**P726** 	<BalForAcct>

**P727** 		<FinInstrmId>

**P728** 			<ISIN>GB0000123456</ISIN>

**P729** 			</FinInstrmId>

**P730** 		<AggtBal>

**P731** 			<ShrtLngInd>SHOR</ShrtLngInd>

**P732** 			<Qty>

**P733** 				<Qty>

**P734** 					<Qty>

**P735** 						<Unit>70000</Unit>

**P736** 					</Qty>

**P737** 				</Qty>

**P738** 			</Qty>

**P739** 		</AggtBal>

**P740** 		<BalBrkdwn>

**P741** 			<SubBalTp>

**P742** 				<Cd>LOAN</Cd>

**P743** 			</SubBalTp>

**P744** 			<Qty>

**P745** 				<QtyAndAvlbty>

**P746** 					<Qty>

**P747** 						<Unit>15000</Unit>

**P748** 					</Qty>

**P749** 					<AvlbtyInd>true</AvlbtyInd>

**P750** 				</QtyAndAvlbty>

**P751** 			</Qty>

**P752** 		</BalBrkdwn>

**P753** 	</BalForAcct>

**P754** </SctiesBalCtdyRpt>

