---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "End-of-day statement"
domain: "payments"
source_ids: ["src-000004"]
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.053.001.14"]
source_locations: [{"source_id": "src-000004", "locator": "Business Examples; narrative P269; T19; XML P272-P442"}, {"source_id": "src-000004", "locator": "Word file/printed pages30,31,32,33,34,35"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Original fragments lack namespace/Document envelope; validation of a derived envelope is separately recorded.", "Source narrative/data/example conflicts are preserved under issue-000060."]
issue_ids: ["issue-000060"]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000008", "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.053.001.14", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["March 2026"]
---

# End-of-day statement

[src-000004](../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart1_BankToCustomerCashManagement_2025_2026_v2.docx); P269; T19; XML P272-P442.

On 18 October 2010, at 5.00 PM, AAAASESS sends an end-of-day BankToCustomerStatement to Company Finpetrol. It contains all booked items during the business day.

[Complete business-data table](../documents/src-000004/tables/tbl-0019.md)

```xml
<BkToCstmrStmt>
	<GrpHdr>
		<MsgId>AAAASESS-FP-STAT001</MsgId>
		<CreDtTm>2015-10-18T17:00:00+01:00</CreDtTm>
		<MsgPgntn>
			<PgNb>1</PgNb>
			<LastPgInd>true</LastPgInd>
		</MsgPgntn>
	</GrpHdr>
	<Stmt>
		<Id>AAAASESS-FP-STAT001</Id>
		<CreDtTm>2015-10-18T17:00:00+01:00</CreDtTm>
		<FrToDt>
			<FrDtTm>2015-10-18T08:00:00+01:00</FrDtTm>
			<ToDtTm>2015-10-18T17:00:00+01:00</ToDtTm>
		</FrToDt>
		<Acct>
			<Id>
				<Othr>
					<Id>50000000054910000003</Id>
				</Othr>
			</Id>
			<Ownr>
				<Nm>FINPETROL</Nm>
			</Ownr>
			<Svcr>
				<FinInstnId>
					<Nm>AAAA BANKEN</Nm>
					<PstlAdr>
						<Ctry>SE</Ctry>
					</PstlAdr>
				</FinInstnId>
			</Svcr>
		</Acct>
		<Bal>
			<Tp>
				<CdOrPrtry>
					<Cd>OPBD</Cd>
				</CdOrPrtry>
			</Tp>
			<Amt Ccy="SEK">500000</Amt>
			<CdtDbtInd>CRDT</CdtDbtInd>
			<Dt>
				<Dt>2015-10-15</Dt>
			</Dt>
		</Bal>
		<Bal>
			<Tp>
				<CdOrPrtry>
					<Cd>CLBD</Cd>
				</CdOrPrtry>
			</Tp>
			<Amt Ccy="SEK">435678.50</Amt>
			<CdtDbtInd>CRDT</CdtDbtInd>
			<Dt>
				<Dt>2015-10-18</Dt>
			</Dt>
		</Bal>
		<Ntry>
			<Amt Ccy="SEK">105678.50</Amt>
			<CdtDbtInd>CRDT</CdtDbtInd>
			<Sts>
				<Cd>BOOK</Cd>
			</Sts>
			<BookgDt>
				<DtTm>2015-10-18T13:15:00+01:00</DtTm>
			</BookgDt>
			<ValDt>
				<Dt>2015-10-18</Dt>
			</ValDt>
			<AcctSvcrRef>AAAASESS-FP-CN_98765/01</AcctSvcrRef>
			<BkTxCd>
				<Domn>
					<Cd>PMNT</Cd>
					<Fmly>
						<Cd>RCDT</Cd>
						<SubFmlyCd>BOOK</SubFmlyCd>
					</Fmly>
				</Domn>
			</BkTxCd>
			<NtryDtls>
				<TxDtls>
					<Refs>
						<EndToEndId>MUELL/FINP/RA12345</EndToEndId>
					</Refs>
					<Amt Ccy="SEK">0</Amt>
					<CdtDbtInd>CRDT</CdtDbtInd>
					<RltdPties>
						<Dbtr>
							<Pty>
								<Nm>MUELLER</Nm>
							</Pty>
						</Dbtr>
					</RltdPties>
				</TxDtls>
			</NtryDtls>
		</Ntry>
		<Ntry>
			<Amt Ccy="SEK">200000</Amt>
			<CdtDbtInd>DBIT</CdtDbtInd>
			<Sts>
				<Cd>BOOK</Cd>
			</Sts>
			<BookgDt>
				<DtTm>2015-10-18T10:15:00+01:00</DtTm>
			</BookgDt>
			<ValDt>
				<Dt>2015-10-18</Dt>
			</ValDt>
			<AcctSvcrRef>AAAASESS-FP-ACCR-01</AcctSvcrRef>
			<BkTxCd>
				<Domn>
					<Cd>PMNT</Cd>
					<Fmly>
						<Cd>ICDT</Cd>
						<SubFmlyCd>DMCT</SubFmlyCd>
					</Fmly>
				</Domn>
			</BkTxCd>
			<NtryDtls>
				<Btch>
					<MsgId>FINP-0055</MsgId>
					<PmtInfId>FINP-0055/001</PmtInfId>
					<NbOfTxs>20</NbOfTxs>
				</Btch>
			</NtryDtls>
		</Ntry>
		<Ntry>
			<Amt Ccy="SEK">30000</Amt>
			<CdtDbtInd>CRDT</CdtDbtInd>
			<Sts>
				<Cd>BOOK</Cd>
			</Sts>
			<BookgDt>
				<DtTm>2015-10-18T15:15:00+01:00</DtTm>
			</BookgDt>
			<ValDt>
				<Dt>2015-10-18</Dt>
			</ValDt>
			<AcctSvcrRef>AAAASESS-FP-CONF-FX</AcctSvcrRef>
			<BkTxCd>
				<Domn>
					<Cd>PMNT</Cd>
					<Fmly>
						<Cd>RCDT</Cd>
						<SubFmlyCd>XBCT</SubFmlyCd>
					</Fmly>
				</Domn>
			</BkTxCd>
			<NtryDtls>
				<TxDtls>
					<Refs>
						<InstrId>FP-004567-FX</InstrId>
						<EndToEndId>AAAASS1085FINPSS</EndToEndId>
					</Refs>
					<Amt Ccy="EUR">3255</Amt>
					<CdtDbtInd>CRDT</CdtDbtInd>
					<AmtDtls>
						<CntrValAmt>
							<Amt Ccy="EUR">3255</Amt>
							<CcyXchg>
								<SrcCcy>EUR</SrcCcy>
								<XchgRate>0.1085</XchgRate>
							</CcyXchg>
						</CntrValAmt>
					</AmtDtls>
				</TxDtls>
			</NtryDtls>
		</Ntry>
	</Stmt>
</BkToCstmrStmt>
```

## Actual review and validation

Original payload pages compared2026-11-09: [30](../../../../../assets/src-000004/source-page-renders/word-page-30.png), [31](../../../../../assets/src-000004/source-page-renders/word-page-31.png), [32](../../../../../assets/src-000004/source-page-renders/word-page-32.png), [33](../../../../../assets/src-000004/source-page-renders/word-page-33.png), [34](../../../../../assets/src-000004/source-page-renders/word-page-34.png), [35](../../../../../assets/src-000004/source-page-renders/word-page-35.png). Every paragraph independently matches the Word PDF. Original fragment is well-formed; a derived exact-namespace Document wrapper passes the supplied exact XSD. Interior values and structure are unchanged. [Unresolved business/data/example discrepancies](../source-consistency.md) remain distinct from schema validity.
