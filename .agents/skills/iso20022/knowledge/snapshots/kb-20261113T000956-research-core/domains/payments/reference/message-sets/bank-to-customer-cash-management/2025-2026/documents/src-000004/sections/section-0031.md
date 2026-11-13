---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "BankToCustomerStatement camt.053.001.14"]
content_origin: "source-transcription"
---

# BankToCustomerStatement camt.053.001.14

Source: [src-000004](../../../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Locator: heading path Business Examples / BankToCustomerStatement camt.053.001.14.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P267** BankToCustomerStatement camt.053.001.14

**P268** Description

**P269** On 18 October 2010, at 5.00 PM, AAAASESS sends an end-of-day BankToCustomerStatement to Company Finpetrol. It contains all booked items during the business day.

**P270** Business Data

[T19 - complete table](../tables/tbl-0019.md)

**P271** Message Instance

**P272** <BkToCstmrStmt>

**P273** 	<GrpHdr>

**P274** 		<MsgId>AAAASESS-FP-STAT001</MsgId>

**P275** 		<CreDtTm>2015-10-18T17:00:00+01:00</CreDtTm>

**P276** 		<MsgPgntn>

**P277** 			<PgNb>1</PgNb>

**P278** 			<LastPgInd>true</LastPgInd>

**P279** 		</MsgPgntn>

**P280** 	</GrpHdr>

**P281** 	<Stmt>

**P282** 		<Id>AAAASESS-FP-STAT001</Id>

**P283** 		<CreDtTm>2015-10-18T17:00:00+01:00</CreDtTm>

**P284** 		<FrToDt>

**P285** 			<FrDtTm>2015-10-18T08:00:00+01:00</FrDtTm>

**P286** 			<ToDtTm>2015-10-18T17:00:00+01:00</ToDtTm>

**P287** 		</FrToDt>

**P288** 		<Acct>

**P289** 			<Id>

**P290** 				<Othr>

**P291** 					<Id>50000000054910000003</Id>

**P292** 				</Othr>

**P293** 			</Id>

**P294** 			<Ownr>

**P295** 				<Nm>FINPETROL</Nm>

**P296** 			</Ownr>

**P297** 			<Svcr>

**P298** 				<FinInstnId>

**P299** 					<Nm>AAAA BANKEN</Nm>

**P300** 					<PstlAdr>

**P301** 						<Ctry>SE</Ctry>

**P302** 					</PstlAdr>

**P303** 				</FinInstnId>

**P304** 			</Svcr>

**P305** 		</Acct>

**P306** 		<Bal>

**P307** 			<Tp>

**P308** 				<CdOrPrtry>

**P309** 					<Cd>OPBD</Cd>

**P310** 				</CdOrPrtry>

**P311** 			</Tp>

**P312** 			<Amt Ccy="SEK">500000</Amt>

**P313** 			<CdtDbtInd>CRDT</CdtDbtInd>

**P314** 			<Dt>

**P315** 				<Dt>2015-10-15</Dt>

**P316** 			</Dt>

**P317** 		</Bal>

**P318** 		<Bal>

**P319** 			<Tp>

**P320** 				<CdOrPrtry>

**P321** 					<Cd>CLBD</Cd>

**P322** 				</CdOrPrtry>

**P323** 			</Tp>

**P324** 			<Amt Ccy="SEK">435678.50</Amt>

**P325** 			<CdtDbtInd>CRDT</CdtDbtInd>

**P326** 			<Dt>

**P327** 				<Dt>2015-10-18</Dt>

**P328** 			</Dt>

**P329** 		</Bal>

**P330** 		<Ntry>

**P331** 			<Amt Ccy="SEK">105678.50</Amt>

**P332** 			<CdtDbtInd>CRDT</CdtDbtInd>

**P333** 			<Sts>

**P334** 				<Cd>BOOK</Cd>

**P335** 			</Sts>

**P336** 			<BookgDt>

**P337** 				<DtTm>2015-10-18T13:15:00+01:00</DtTm>

**P338** 			</BookgDt>

**P339** 			<ValDt>

**P340** 				<Dt>2015-10-18</Dt>

**P341** 			</ValDt>

**P342** 			<AcctSvcrRef>AAAASESS-FP-CN_98765/01</AcctSvcrRef>

**P343** 			<BkTxCd>

**P344** 				<Domn>

**P345** 					<Cd>PMNT</Cd>

**P346** 					<Fmly>

**P347** 						<Cd>RCDT</Cd>

**P348** 						<SubFmlyCd>BOOK</SubFmlyCd>

**P349** 					</Fmly>

**P350** 				</Domn>

**P351** 			</BkTxCd>

**P352** 			<NtryDtls>

**P353** 				<TxDtls>

**P354** 					<Refs>

**P355** 						<EndToEndId>MUELL/FINP/RA12345</EndToEndId>

**P356** 					</Refs>

**P357** 					<Amt Ccy="SEK">0</Amt>

**P358** 					<CdtDbtInd>CRDT</CdtDbtInd>

**P359** 					<RltdPties>

**P360** 						<Dbtr>

**P361** 							<Pty>

**P362** 								<Nm>MUELLER</Nm>

**P363** 							</Pty>

**P364** 						</Dbtr>

**P365** 					</RltdPties>

**P366** 				</TxDtls>

**P367** 			</NtryDtls>

**P368** 		</Ntry>

**P369** 		<Ntry>

**P370** 			<Amt Ccy="SEK">200000</Amt>

**P371** 			<CdtDbtInd>DBIT</CdtDbtInd>

**P372** 			<Sts>

**P373** 				<Cd>BOOK</Cd>

**P374** 			</Sts>

**P375** 			<BookgDt>

**P376** 				<DtTm>2015-10-18T10:15:00+01:00</DtTm>

**P377** 			</BookgDt>

**P378** 			<ValDt>

**P379** 				<Dt>2015-10-18</Dt>

**P380** 			</ValDt>

**P381** 			<AcctSvcrRef>AAAASESS-FP-ACCR-01</AcctSvcrRef>

**P382** 			<BkTxCd>

**P383** 				<Domn>

**P384** 					<Cd>PMNT</Cd>

**P385** 					<Fmly>

**P386** 						<Cd>ICDT</Cd>

**P387** 						<SubFmlyCd>DMCT</SubFmlyCd>

**P388** 					</Fmly>

**P389** 				</Domn>

**P390** 			</BkTxCd>

**P391** 			<NtryDtls>

**P392** 				<Btch>

**P393** 					<MsgId>FINP-0055</MsgId>

**P394** 					<PmtInfId>FINP-0055/001</PmtInfId>

**P395** 					<NbOfTxs>20</NbOfTxs>

**P396** 				</Btch>

**P397** 			</NtryDtls>

**P398** 		</Ntry>

**P399** 		<Ntry>

**P400** 			<Amt Ccy="SEK">30000</Amt>

**P401** 			<CdtDbtInd>CRDT</CdtDbtInd>

**P402** 			<Sts>

**P403** 				<Cd>BOOK</Cd>

**P404** 			</Sts>

**P405** 			<BookgDt>

**P406** 				<DtTm>2015-10-18T15:15:00+01:00</DtTm>

**P407** 			</BookgDt>

**P408** 			<ValDt>

**P409** 				<Dt>2015-10-18</Dt>

**P410** 			</ValDt>

**P411** 			<AcctSvcrRef>AAAASESS-FP-CONF-FX</AcctSvcrRef>

**P412** 			<BkTxCd>

**P413** 				<Domn>

**P414** 					<Cd>PMNT</Cd>

**P415** 					<Fmly>

**P416** 						<Cd>RCDT</Cd>

**P417** 						<SubFmlyCd>XBCT</SubFmlyCd>

**P418** 					</Fmly>

**P419** 				</Domn>

**P420** 			</BkTxCd>

**P421** 			<NtryDtls>

**P422** 				<TxDtls>

**P423** 					<Refs>

**P424** 						<InstrId>FP-004567-FX</InstrId>

**P425** 						<EndToEndId>AAAASS1085FINPSS</EndToEndId>

**P426** 					</Refs>

**P427** 					<Amt Ccy="EUR">3255</Amt>

**P428** 					<CdtDbtInd>CRDT</CdtDbtInd>

**P429** 					<AmtDtls>

**P430** 						<CntrValAmt>

**P431** 							<Amt Ccy="EUR">3255</Amt>

**P432** 							<CcyXchg>

**P433** 								<SrcCcy>EUR</SrcCcy>

**P434** 								<XchgRate>0.1085</XchgRate>

**P435** 							</CcyXchg>

**P436** 						</CntrValAmt>

**P437** 					</AmtDtls>

**P438** 				</TxDtls>

**P439** 			</NtryDtls>

**P440** 		</Ntry>

**P441** 	</Stmt>

**P442** </BkToCstmrStmt>

