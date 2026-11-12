---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "Intraday account report"
domain: "payments"
source_ids: ["src-000004"]
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.052.001.14"]
source_locations: [{"source_id": "src-000004", "locator": "Business Examples; narrative P159; T18; XML P162-P266"}, {"source_id": "src-000004", "locator": "Word file/printed pages25,26,27"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Original fragments lack namespace/Document envelope; validation of a derived envelope is separately recorded.", "Source narrative/data/example conflicts are preserved under issue-000060."]
issue_ids: ["issue-000060"]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000007", "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.052.001.14", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["March 2026"]
---

# Intraday account report

[src-000004](../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md); P159; T18; XML P162-P266.

AAAA Banken has agreed to provide an intraday account report to its customer Finpetrol. Each business day, at 12.30PM, AAAA Banken will provide Finpetrol with an overview of all booked and expected entries since the start of the business day. On 18 October 2010, at 12.30 PM, AAAASESS sends such an intraday BankToCustomerAccountReport to Company Finpetrol. It contains two entries: one booked, and one expected item. It has been pre-agreed between the account servicer and account owner that AAAA Banken will not include (expected) balance info in this intraday report.

[Complete business-data table](../documents/src-000004/tables/tbl-0018.md)

```xml
<BkToCstmrAcctRpt>
	<GrpHdr>
		<MsgId>AAAASESS-FP-ACCR001</MsgId>
		<CreDtTm>2015-10-18T12:30:00+01:00</CreDtTm>
		<MsgPgntn>
			<PgNb>1</PgNb>
			<LastPgInd>true</LastPgInd>
		</MsgPgntn>
	</GrpHdr>
	<Rpt>
		<Id>AAAASESS-FP-ACCR001</Id>
		<CreDtTm>2015-10-18T12:30:00+01:00</CreDtTm>
		<FrToDt>
			<FrDtTm>2015-10-18T08:00:00+01:00</FrDtTm>
			<ToDtTm>2015-10-18T12:30:00+01:00</ToDtTm>
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
						<SubFmlyCd>XBCT</SubFmlyCd>
					</Fmly>
				</Domn>
			</BkTxCd>
			<NtryDtls>
				<Btch>
					<MsgId>FINP-0055</MsgId>
					<PmtInfId>FINP-0055-001</PmtInfId>
					<NbOfTxs>20</NbOfTxs>
				</Btch>
			</NtryDtls>
		</Ntry>
		<Ntry>
			<Amt Ccy="SEK">30000</Amt>
			<CdtDbtInd>CRDT</CdtDbtInd>
			<Sts>
				<Cd>PDNG</Cd>
			</Sts>
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
								<XchgRate>0.185</XchgRate>
							</CcyXchg>
						</CntrValAmt>
					</AmtDtls>
				</TxDtls>
			</NtryDtls>
		</Ntry>
	</Rpt>
</BkToCstmrAcctRpt>
```

## Actual review and validation

Original payload pages compared2026-11-09: [25](../../../../../../../evidence/omitted/004a2437c431d45e0d5e4a70.md), [26](../../../../../../../evidence/omitted/a3df1aba816c478739043508.md), [27](../../../../../../../evidence/omitted/0bc6859349e00e0dffb64fca.md). Every paragraph independently matches the Word PDF. Original fragment is well-formed; a derived exact-namespace Document wrapper passes the supplied exact XSD. Interior values and structure are unchanged. [Unresolved business/data/example discrepancies](../source-consistency.md) remain distinct from schema validity.
