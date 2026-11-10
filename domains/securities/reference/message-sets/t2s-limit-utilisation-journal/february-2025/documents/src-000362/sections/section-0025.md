---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LimitUtilisationJournal"
source_ids: ["src-000362"]
source_editions: ["february-2025"]
message_ids: []
heading_path: ["Business Examples", "Example #1: Business Report", "Message example"]
content_origin: "source-transcription"
---

# Message example

Source: [src-000362](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`. Locator: heading path Business Examples / Example #1: Business Report / Message example.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P179** Message example

**P180** Limit Utilisation Journal Query - camt.064.001.01

**P182**   <LmtUtlstnJrnlQry>

**P183** 	 <MsgHdr>

**P184** 		<MsgId>REFABC</MsgId>

**P185** 	 </MsgHdr>

**P186** 	 <SchCrit>

**P187** 		   <LmtTp>ACOL</LmtTp>

**P188** 			<JrnlActvtyDt>2015-01-09</JrnlActvtyDt>

**P189** 			<BilLmtCtrPtyId>

**P190** 				<Id>

**P191** 					<Id>

**P192** 						<AnyBIC>PAYBKBICXXX</AnyBIC>

**P193** 					</Id>

**P194** 				</Id>

**P195** 				<RspnsblPtyId>

**P196** 					<Id>

**P197** 						<AnyBIC>CBAABIC1XXX</AnyBIC>

**P198** 					</Id>

**P199** 				</RspnsblPtyId>

**P200** 			</BilLmtCtrPtyId>

**P201** 	 </SchCrit>

**P202** 	</LmtUtlstnJrnlQry>

**P205** Limit Utilisation Journal Report - camt.065.001.01

**P207** <LmtUtlstnJrnlRpt>

**P208** 	<MsgHdr>

**P209** 		<MsgId>NONREF</MsgId>

**P210** 		<OrgnlBizInstr>

**P211** 			<MsgId>REFABC</MsgId>

**P212** 		</OrgnlBizInstr>

**P213** 	</MsgHdr>

**P214** 	<Pgntn>

**P215** 		<PgNb>1</PgNb>

**P216** 		<LastPgInd>true</LastPgInd>

**P217** 	</Pgntn>

**P218** 	<RptOrErr>

**P219** 			<BizRpt>

**P220** 				<LmtId>

**P221** 					<AcctId>

**P222** 					  <Othr>

**P223** 						  <Id>9000000123</Id>

**P224** 					  </Othr>

**P225** 					</AcctId>

**P226** 					<Tp>ACOL</Tp>

**P227** 					<LmtCcy>EUR</LmtCcy>

**P228** 					<AcctOwnr>

**P229** 						<FinInstnId>

**P230** 						<BICFI>PAYBKBICXXX</BICFI>

**P231** 						</FinInstnId>

**P232** 					</AcctOwnr>

**P233** 					<BilLmtCtrPtyId>

**P234** 						<Id>

**P235** 							<Id>

**P236** 								<AnyBIC>PAYBKBICXXX</AnyBIC>

**P237** 							</Id>

**P238** 						</Id>

**P239** 						<RspnsblPtyId>

**P240** 							<Id>

**P241** 								<AnyBIC>CBAABIC1XXX</AnyBIC>

**P242** 							</Id>

**P243** 						</RspnsblPtyId>

**P244** 					</BilLmtCtrPtyId>

**P245** 				</LmtId>

**P246** 				<LmtRpt>

**P247** 					<LmtJrnl>

**P248** 						<Lmt>

**P249** 							<Amt>

**P250** 								<Amt>

**P251** 								<AmtWthCcy Ccy="EUR">100000</AmtWthCcy>

**P252** 								</Amt>

**P253** 								<CdtDbtInd>CRDT</CdtDbtInd>

**P254** 							</Amt>

**P255** 							<UtlstnAmt>

**P256** 								<Amt>

**P257** 								<AmtWthCcy Ccy="EUR">40000</AmtWthCcy>

**P258** 								</Amt>

**P259** 								<CdtDbtInd>DBIT</CdtDbtInd>

**P260** 							</UtlstnAmt>

**P261** 							<AvlblAmt>

**P262** 								<Amt>

**P263** 								<AmtWthCcy Ccy="EUR">60000</AmtWthCcy>

**P264** 								</Amt>

**P265** 								<CdtDbtInd>CRDT</CdtDbtInd>

**P266** 							</AvlblAmt>

**P267** 						</Lmt>

**P268** 						<JrnlActvtyDt>2015-01-09</JrnlActvtyDt>

**P269** 						<JrnlNtry>

**P270** 							<JrnlDt>

**P271** 								<Dt>2015-01-09</Dt>

**P272** 							</JrnlDt>

**P273** 							<CdtDbtInd>DBIT</CdtDbtInd>

**P274** 							<Amt>

**P275** 							<AmtWthCcy Ccy="EUR">15000</AmtWthCcy>

**P276** 							</Amt>

**P277** 							<NtryRef>T2SREF1234</NtryRef>

**P278** 							<TxId>AOREF123</TxId>

**P279** 							<AcctSvcrRef>ASREFABC</AcctSvcrRef>

**P280** 						</JrnlNtry>

**P281** 						<JrnlNtry>

**P282** 							<JrnlDt>

**P283** 								<Dt>2015-01-09</Dt>

**P284** 							</JrnlDt>

**P285** 							<CdtDbtInd>DBIT</CdtDbtInd>

**P286** 							<Amt>

**P287** 							<AmtWthCcy Ccy="EUR">12000</AmtWthCcy>

**P288** 							</Amt>

**P289** 							<NtryRef>T2SREF2345</NtryRef>

**P290** 							<TxId>AOREF234</TxId>

**P291** 							<AcctSvcrRef>ASREFBCD</AcctSvcrRef>

**P292** 						</JrnlNtry>

**P293** 						<JrnlNtry>

**P294** 							<JrnlDt>

**P295** 								<Dt>2015-01-09</Dt>

**P296** 							</JrnlDt>

**P297** 							<CdtDbtInd>DBIT</CdtDbtInd>

**P298** 							<Amt>

**P299** 							<AmtWthCcy Ccy="EUR">13000</AmtWthCcy>

**P300** 							</Amt>

**P301** 							<NtryRef>T2SREF3456</NtryRef>

**P302** 							<TxId>AOREF345</TxId>

**P303** 							<AcctSvcrRef>ASREFCDE</AcctSvcrRef>

**P304** 						</JrnlNtry>

**P305** 					</LmtJrnl>

**P306** 				</LmtRpt>

**P307** 			</BizRpt>

**P308** 	</RptOrErr>

**P309** </LmtUtlstnJrnlRpt>

