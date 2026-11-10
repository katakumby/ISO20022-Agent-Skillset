---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000380"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["Business Examples", "Securities Settlement Conditions Modification Request Report (semt.031)"]
content_origin: "source-transcription"
---

# Securities Settlement Conditions Modification Request Report (semt.031)

Source: [src-000380](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart1_Target2Securities_SettlementRestrictions_v2.docx`. Locator: heading path Business Examples / Securities Settlement Conditions Modification Request Report (semt.031).

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P758** Securities Settlement Conditions Modification Request Report (semt.031)

**P759** Description

**P760** T2S sends a Securities Settlement Conditions Modification Report for all the Settlement Instructions and Intra-position Movement Instructions executed on the 3rd of February 2025 within the securities account ‘1000000123’ and ‘1000000124’.

**P761** As this report is generated at party level, it also indicates that the securities accounts ‘1000000123’ and ‘1000000124’ are the only SACs in the Party scope which has modifications to be reported.

**P763** Message Instance

**P764** <SctiesSttlmCondsModReqRpt>

**P765** 		<Pgntn>

**P766** 			<PgNb>1</PgNb>

**P767** 			<LastPgInd>true</LastPgInd>

**P768** 		</Pgntn>

**P769** 		<RptGnlDtls>

**P770** 			<RptId>T5678</RptId>

**P771** 			<RptPrd>

**P772** 				<FrDtTmToDtTm>

**P773** 					<FrDtTm>2025-02-03T06:20:03</FrDtTm>

**P774** 					<ToDtTm>2025-02-03T06:20:06</ToDtTm>

**P775** 				</FrDtTmToDtTm>

**P776** 			</RptPrd>

**P777** 			<Frqcy>

**P778** 				<Cd>DAIL</Cd>

**P779** 			</Frqcy>

**P780** 			<UpdTp>

**P781** 				<Cd>COMP</Cd>

**P782** 			</UpdTp>

**P783** 			<ActvtyInd>true</ActvtyInd>

**P784** 		</RptGnlDtls>

**P785** 		<Mods>

**P786** 			<AcctOwnr>

**P787** 				<Id>

**P788** 					<Id>

**P789** 						<AnyBIC>BNKAFRPPXXX</AnyBIC>

**P790** 					</Id>

**P791** 				</Id>

**P792** 			</AcctOwnr>

**P793** 			<SfkpgAcct>

**P794** 				<Id>1000000123</Id>

**P795** 			</SfkpgAcct>

**P796** 			<PrcgSts>

**P797** 				<Cmpltd/>

**P798** 			</PrcgSts>

**P799** 			<Mod>

**P800** 				<ReqRef>ABCDEF</ReqRef>

**P801** 				<StsDt>2025-02-03T02:10:10</StsDt>

**P802** 				<ReqDtls>

**P803** 					<Ref>

**P804** 						<AcctOwnrTxId>REFABCD</AcctOwnrTxId>

**P805** 					</Ref>

**P806** 					<Prty>

**P807** 						<Nmrc>0003</Nmrc>

**P808** 					</Prty>

**P809** 				</ReqDtls>

**P810** 				<Undrlyg>

**P811** 					<SttlmTx>

**P812** 						<FinInstrmId>

**P813** 							<ISIN>ISIN00000001</ISIN>

**P814** 						</FinInstrmId>

**P815** 						<SttlmQty>

**P816** 							<Qty>

**P817** 								<Unit>100000</Unit>

**P818** 							</Qty>

**P819** 						</SttlmQty>

**P820** 						<SttlmAmt>

**P821** 							<Amt Ccy="EUR">575000</Amt>

**P822** 							<CdtDbtInd>CRDT</CdtDbtInd>

**P823** 						</SttlmAmt>

**P824** 						<TradDt>

**P825** 							<Dt>

**P826** 								<Dt>2025-02-01</Dt>

**P827** 							</Dt>

**P828** 						</TradDt>

**P829** 						<SttlmDt>

**P830** 							<Dt>

**P831** 								<Dt>2025-02-03</Dt>

**P832** 							</Dt>

**P833** 						</SttlmDt>

**P834** 						<RcvgSttlmPties>

**P835** 							<Dpstry>

**P836** 								<Id>

**P837** 									<AnyBIC>CSDBBIC1XXX</AnyBIC>

**P838** 								</Id>

**P839** 							</Dpstry>

**P840** 							<Pty1>

**P841** 								<Id>

**P842** 									<AnyBIC>CSDPBBICXXX</AnyBIC>

**P843** 								</Id>

**P844** 							</Pty1>

**P845** 						</RcvgSttlmPties>

**P846** 					</SttlmTx>

**P847** 				</Undrlyg>

**P848** 			</Mod>

**P849** 			<Mod>

**P850** 				<ReqRef>ABCDEF</ReqRef>

**P851** 				<StsDt>2025-02-03T01:12:10</StsDt>

**P852** 				<ReqDtls>

**P853** 					<Ref>

**P854** 						<AcctOwnrTxId>REFABCD</AcctOwnrTxId>

**P855** 					</Ref>

**P856** 					<Prty>

**P857** 						<Nmrc>0003</Nmrc>

**P858** 					</Prty>

**P859** 				</ReqDtls>

**P860** 				<Undrlyg>

**P861** 					<IntraPosMvmnt>

**P862** 						<FinInstrmId>

**P863** 							<ISIN>ISIN00000003</ISIN>

**P864** 						</FinInstrmId>

**P865** 						<SttlmQty>

**P866** 							<Unit>2300</Unit>

**P867** 						</SttlmQty>

**P868** 						<SttlmDt>

**P869** 							<Dt>2025-02-03</Dt>

**P870** 						</SttlmDt>

**P871** 						<BalFr>

**P872** 							<Tp>

**P873** 								<Cd>AWAS</Cd>

**P874** 							</Tp>

**P875** 						</BalFr>

**P876** 						<BalTo>

**P877** 							<Tp>

**P878** 								<Prtry>

**P879** 									<Id>BLK1</Id>

**P880** 									<Issr>T2S</Issr>

**P881** 									<SchmeNm>RT</SchmeNm>

**P882** 								</Prtry>

**P883** 							</Tp>

**P884** 						</BalTo>

**P885** 						<Prty>

**P886** 							<Nmrc>0004</Nmrc>

**P887** 						</Prty>

**P888** 					</IntraPosMvmnt>

**P889** 				</Undrlyg>

**P890** 			</Mod>

**P891** 			<Mod>

**P892** 				<ReqRef>123DEF</ReqRef>

**P893** 				<StsDt>2025-02-03T01:21:10</StsDt>

**P894** 				<ReqDtls>

**P895** 					<Ref>

**P896** 						<AcctOwnrTxId>REF123</AcctOwnrTxId>

**P897** 					</Ref>

**P898** 					<PrtlSttlmInd>PART</PrtlSttlmInd>

**P899** 				</ReqDtls>

**P900** 				<Undrlyg>

**P901** 					<SttlmTx>

**P902** 						<FinInstrmId>

**P903** 							<ISIN>ISIN00000004</ISIN>

**P904** 						</FinInstrmId>

**P905** 						<SttlmQty>

**P906** 							<Qty>

**P907** 								<Unit>100000</Unit>

**P908** 							</Qty>

**P909** 						</SttlmQty>

**P910** 						<SttlmAmt>

**P911** 							<Amt Ccy="EUR">575000</Amt>

**P912** 							<CdtDbtInd>CRDT</CdtDbtInd>

**P913** 						</SttlmAmt>

**P914** 						<TradDt>

**P915** 							<Dt>

**P916** 								<Dt>2025-02-01</Dt>

**P917** 							</Dt>

**P918** 						</TradDt>

**P919** 						<SttlmDt>

**P920** 							<Dt>

**P921** 								<Dt>2025-02-03</Dt>

**P922** 							</Dt>

**P923** 						</SttlmDt>

**P924** 						<RcvgSttlmPties>

**P925** 							<Dpstry>

**P926** 								<Id>

**P927** 									<AnyBIC>CSDBBIC1XXX</AnyBIC>

**P928** 								</Id>

**P929** 							</Dpstry>

**P930** 							<Pty1>

**P931** 								<Id>

**P932** 									<AnyBIC>CSDPBBICXXX</AnyBIC>

**P933** 								</Id>

**P934** 							</Pty1>

**P935** 						</RcvgSttlmPties>

**P936** 					</SttlmTx>

**P937** 				</Undrlyg>

**P938** 			</Mod>

**P939** 		</Mods>

**P940** 		<Mods>

**P941** 			<AcctOwnr>

**P942** 				<Id>

**P943** 					<Id>

**P944** 						<AnyBIC>BNKAFRPPXXX</AnyBIC>

**P945** 					</Id>

**P946** 				</Id>

**P947** 			</AcctOwnr>

**P948** 			<SfkpgAcct>

**P949** 				<Id>1000000124</Id>

**P950** 			</SfkpgAcct>

**P951** 			<PrcgSts>

**P952** 				<Cmpltd/>

**P953** 			</PrcgSts>

**P954** 			<Mod>

**P955** 				<ReqRef>124DEF</ReqRef>

**P956** 				<StsDt>2025-02-03T01:21:10</StsDt>

**P957** 				<ReqDtls>

**P958** 					<Ref>

**P959** 						<AcctOwnrTxId>REF124</AcctOwnrTxId>

**P960** 					</Ref>

**P961** 					<PrtlSttlmInd>PART</PrtlSttlmInd>

**P962** 				</ReqDtls>

**P963** 				<Undrlyg>

**P964** 					<SttlmTx>

**P965** 						<FinInstrmId>

**P966** 							<ISIN>ISIN00000005</ISIN>

**P967** 						</FinInstrmId>

**P968** 						<SttlmQty>

**P969** 							<Qty>

**P970** 								<Unit>100000</Unit>

**P971** 							</Qty>

**P972** 						</SttlmQty>

**P973** 						<SttlmAmt>

**P974** 							<Amt Ccy="EUR">575000</Amt>

**P975** 							<CdtDbtInd>CRDT</CdtDbtInd>

**P976** 						</SttlmAmt>

**P977** 						<TradDt>

**P978** 							<Dt>

**P979** 								<Dt>2025-02-01</Dt>

**P980** 							</Dt>

**P981** 						</TradDt>

**P982** 						<SttlmDt>

**P983** 							<Dt>

**P984** 								<Dt>2025-02-03</Dt>

**P985** 							</Dt>

**P986** 						</SttlmDt>

**P987** 						<RcvgSttlmPties>

**P988** 							<Dpstry>

**P989** 								<Id>

**P990** 									<AnyBIC>CSDBBIC1XXX</AnyBIC>

**P991** 								</Id>

**P992** 							</Dpstry>

**P993** 							<Pty1>

**P994** 								<Id>

**P995** 									<AnyBIC>CSDPBBICXXX</AnyBIC>

**P996** 								</Id>

**P997** 							</Pty1>

**P998** 						</RcvgSttlmPties>

**P999** 					</SttlmTx>

**P1000** 				</Undrlyg>

**P1001** 			</Mod>

**P1002** 		</Mods>

**P1003** 	</SctiesSttlmCondsModReqRpt>

**P1004**   


