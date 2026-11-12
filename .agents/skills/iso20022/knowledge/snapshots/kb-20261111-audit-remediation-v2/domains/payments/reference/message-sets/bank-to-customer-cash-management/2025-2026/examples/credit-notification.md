---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "Credit notification"
domain: "payments"
source_ids: ["src-000004"]
message_sets: ["bank-to-customer-cash-management"]
message_ids: ["camt.054.001.14"]
source_locations: [{"source_id": "src-000004", "locator": "Business Examples; narrative P445; T20; XML P448-P514"}, {"source_id": "src-000004", "locator": "Word file/printed pages36,37,38"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Original fragments lack namespace/Document envelope; validation of a derived envelope is separately recorded.", "Source narrative/data/example conflicts are preserved under issue-000060."]
issue_ids: ["issue-000060"]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000009", "namespace": "urn:iso:std:iso:20022:tech:xsd:camt.054.001.14", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["March 2026"]
---

# Credit notification

[src-000004](../../../../../../../evidence/omitted/52f543e2b58f688bc16fa140.md); P445; T20; XML P448-P514.

Besides providing an intraday account report at 12.30 PM (see example with BankToCustomerAccountReport), AAAA Banken and Finpetrol have agreed on a credit notification service, for all incoming credits above a certain threshold. On 18 October 2010, at 1.20 PM, AAAASESS sends a BankToCustomerDebitCreditNotification to Company Finpetrol, to advise Finpetrol of an incoming credit on its account.

[Complete business-data table](../documents/src-000004/tables/tbl-0020.md)

```xml
<BkToCstmrDbtCdtNtfctn>
	<GrpHdr>
		<MsgId>AAAASESS-FP-00001</MsgId>
		<CreDtTm>2015-10-18T13:20:00+01:00</CreDtTm>
	</GrpHdr>
	<Ntfctn>
		<Id>AAAASESS-FP-CN-98765</Id>
		<CreDtTm>2015-10-18T13:20:00+01:00</CreDtTm>
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
			<AcctSvcrRef>AAAASESS-FP-CN-98765/01</AcctSvcrRef>
			<BkTxCd>
				<Domn>
					<Cd>PAYM</Cd>
					<Fmly>
						<Cd>0001</Cd>
						<SubFmlyCd>0005</SubFmlyCd>
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
	</Ntfctn>
</BkToCstmrDbtCdtNtfctn>
```

## Actual review and validation

Original payload pages compared2026-11-09: [36](../../../../../../../evidence/omitted/b82ad6c44535e431de4033f1.md), [37](../../../../../../../evidence/omitted/01cd188506ca6cd43d3e7804.md), [38](../../../../../../../evidence/omitted/caf7ce3c3f331325f6d8a762.md). Every paragraph independently matches the Word PDF. Original fragment is well-formed; a derived exact-namespace Document wrapper passes the supplied exact XSD. Interior values and structure are unchanged. [Unresolved business/data/example discrepancies](../source-consistency.md) remain distinct from schema validity.
