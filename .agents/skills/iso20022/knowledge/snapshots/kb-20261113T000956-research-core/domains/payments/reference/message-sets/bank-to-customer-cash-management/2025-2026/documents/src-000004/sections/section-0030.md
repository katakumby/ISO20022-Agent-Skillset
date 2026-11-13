---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000004"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["Business Examples", "BankToCustomerAccountReport camt.052.001.14"]
content_origin: "source-transcription"
---

# BankToCustomerAccountReport camt.052.001.14

Source: [src-000004](../../../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md). Locator: heading path Business Examples / BankToCustomerAccountReport camt.052.001.14.

Extracted evidence. Pagination, drawing completeness, and source semantics remain subject to visual review.

**P157** BankToCustomerAccountReport camt.052.001.14

**P158** Description

**P159** AAAA Banken has agreed to provide an intraday account report to its customer Finpetrol. Each business day, at 12.30PM, AAAA Banken will provide Finpetrol with an overview of all booked and expected entries since the start of the business day. On 18 October 2010, at 12.30 PM, AAAASESS sends such an intraday BankToCustomerAccountReport to Company Finpetrol. It contains two entries: one booked, and one expected item. It has been pre-agreed between the account servicer and account owner that AAAA Banken will not include (expected) balance info in this intraday report.

**P160** Business Data

[T18 - complete table](../tables/tbl-0018.md)

**P161** Message Instance

**P162** <BkToCstmrAcctRpt>

**P163** 	<GrpHdr>

**P164** 		<MsgId>AAAASESS-FP-ACCR001</MsgId>

**P165** 		<CreDtTm>2015-10-18T12:30:00+01:00</CreDtTm>

**P166** 		<MsgPgntn>

**P167** 			<PgNb>1</PgNb>

**P168** 			<LastPgInd>true</LastPgInd>

**P169** 		</MsgPgntn>

**P170** 	</GrpHdr>

**P171** 	<Rpt>

**P172** 		<Id>AAAASESS-FP-ACCR001</Id>

**P173** 		<CreDtTm>2015-10-18T12:30:00+01:00</CreDtTm>

**P174** 		<FrToDt>

**P175** 			<FrDtTm>2015-10-18T08:00:00+01:00</FrDtTm>

**P176** 			<ToDtTm>2015-10-18T12:30:00+01:00</ToDtTm>

**P177** 		</FrToDt>

**P178** 		<Acct>

**P179** 			<Id>

**P180** 				<Othr>

**P181** 					<Id>50000000054910000003</Id>

**P182** 				</Othr>

**P183** 			</Id>

**P184** 			<Ownr>

**P185** 				<Nm>FINPETROL</Nm>

**P186** 			</Ownr>

**P187** 			<Svcr>

**P188** 				<FinInstnId>

**P189** 					<Nm>AAAA BANKEN</Nm>

**P190** 					<PstlAdr>

**P191** 						<Ctry>SE</Ctry>

**P192** 					</PstlAdr>

**P193** 				</FinInstnId>

**P194** 			</Svcr>

**P195** 		</Acct>

**P196** 		<Ntry>

**P197** 			<Amt Ccy="SEK">200000</Amt>

**P198** 			<CdtDbtInd>DBIT</CdtDbtInd>

**P199** 			<Sts>

**P200** 				<Cd>BOOK</Cd>

**P201** 			</Sts>

**P202** 			<BookgDt>

**P203** 				<DtTm>2015-10-18T10:15:00+01:00</DtTm>

**P204** 			</BookgDt>

**P205** 			<ValDt>

**P206** 				<Dt>2015-10-18</Dt>

**P207** 			</ValDt>

**P208** 			<AcctSvcrRef>AAAASESS-FP-ACCR-01</AcctSvcrRef>

**P209** 			<BkTxCd>

**P210** 				<Domn>

**P211** 					<Cd>PMNT</Cd>

**P212** 					<Fmly>

**P213** 						<Cd>ICDT</Cd>

**P214** 						<SubFmlyCd>XBCT</SubFmlyCd>

**P215** 					</Fmly>

**P216** 				</Domn>

**P217** 			</BkTxCd>

**P218** 			<NtryDtls>

**P219** 				<Btch>

**P220** 					<MsgId>FINP-0055</MsgId>

**P221** 					<PmtInfId>FINP-0055-001</PmtInfId>

**P222** 					<NbOfTxs>20</NbOfTxs>

**P223** 				</Btch>

**P224** 			</NtryDtls>

**P225** 		</Ntry>

**P226** 		<Ntry>

**P227** 			<Amt Ccy="SEK">30000</Amt>

**P228** 			<CdtDbtInd>CRDT</CdtDbtInd>

**P229** 			<Sts>

**P230** 				<Cd>PDNG</Cd>

**P231** 			</Sts>

**P232** 			<ValDt>

**P233** 				<Dt>2015-10-18</Dt>

**P234** 			</ValDt>

**P235** 			<AcctSvcrRef>AAAASESS-FP-CONF-FX</AcctSvcrRef>

**P236** 			<BkTxCd>

**P237** 				<Domn>

**P238** 					<Cd>PMNT</Cd>

**P239** 					<Fmly>

**P240** 						<Cd>RCDT</Cd>

**P241** 						<SubFmlyCd>XBCT</SubFmlyCd>

**P242** 					</Fmly>

**P243** 				</Domn>

**P244** 			</BkTxCd>

**P245** 			<NtryDtls>

**P246** 				<TxDtls>

**P247** 					<Refs>

**P248** 						<InstrId>FP-004567-FX</InstrId>

**P249** 						<EndToEndId>AAAASS1085FINPSS</EndToEndId>

**P250** 					</Refs>

**P251** 					<Amt Ccy="EUR">3255</Amt>

**P252** 					<CdtDbtInd>CRDT</CdtDbtInd>

**P253** 					<AmtDtls>

**P254** 						<CntrValAmt>

**P255** 							<Amt Ccy="EUR">3255</Amt>

**P256** 								<CcyXchg>

**P257** 								<SrcCcy>EUR</SrcCcy>

**P258** 								<XchgRate>0.185</XchgRate>

**P259** 							</CcyXchg>

**P260** 						</CntrValAmt>

**P261** 					</AmtDtls>

**P262** 				</TxDtls>

**P263** 			</NtryDtls>

**P264** 		</Ntry>

**P265** 	</Rpt>

**P266** </BkToCstmrAcctRpt>

