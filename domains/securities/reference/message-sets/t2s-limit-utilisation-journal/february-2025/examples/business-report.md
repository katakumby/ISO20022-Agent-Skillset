---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Business report example"
domain: "securities"
source_ids: ["src-000362"]
message_sets: ["t2s-limit-utilisation-journal"]
message_ids: ["camt.064.001.01", "camt.065.001.01"]
source_locations: [{"source_id": "src-000362", "locator": "P169–P309; Business Examples; original payload excerpts"}, {"source_id": "src-000362", "locator": "Word file/printed pages19,20,21"}]
flow_ids: ["flow-src-000362-p137-pull-mode"]
limitations: ["These are supplied illustrative examples. Payload fragments omit BAH and document namespace wrapper; not claimed as standalone schema-valid messages."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
xml_fragment_wellformedness: "pass"
source_editions: ["february-2025"]
---

# Business report example

Source [src-000362](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_LimitUtilisationJournal_MessageSet/ISO20022_MDRPart1_Target2Securities_LimitUtilisationJournal_v2.docx`; P169–P309. P162 says the complete instances are embedded in BAH, while the shown excerpts contain only the business message.

**P169** In this example the “LimitUtilisationJournalQuery” is used by an NCB (A) "CBAABIC1XXX”, participating in T2S, to query via camt.064 the journal utilisation of Auto-collateralisation limits for the payment bank “PAYBKBICXXX” on January 9th, 2015, as the current business date, which corresponds to Limit Utilisation activity date.

**P170** The result of this query is sent using “LimitUtilisationJournalReport” (camt.065) containing the Auto-collateralisation limit, associated limit information and corresponding journal transaction activity of the utilisation of the limit for the bank linked to the Dedicated Cash Account identified by “9000000123”. 

**P171** In this example, the following limit information is returned:

**P172** Limit Amount: 100000 Euros;

**P173** Utilisation: 40000 Euros;

**P174** Available: 60000 Euros;

**P175** Journal Activity :

**P176** 15000 Euros Debit for Entry Reference T2SREF1234

**P177** 12000 Euros Debit for Entry Reference T2SREF2345

**P178** 13000 Euros Debit for Entry Reference T2SREF3456

## Query

[camt.064.001.01](../../../../messages/camt.064.001.01/index.md); P182–P202.

```xml
  <LmtUtlstnJrnlQry>
	 <MsgHdr>
		<MsgId>REFABC</MsgId>
	 </MsgHdr>
	 <SchCrit>
		   <LmtTp>ACOL</LmtTp>
			<JrnlActvtyDt>2015-01-09</JrnlActvtyDt>
			<BilLmtCtrPtyId>
				<Id>
					<Id>
						<AnyBIC>PAYBKBICXXX</AnyBIC>
					</Id>
				</Id>
				<RspnsblPtyId>
					<Id>
						<AnyBIC>CBAABIC1XXX</AnyBIC>
					</Id>
				</RspnsblPtyId>
			</BilLmtCtrPtyId>
	 </SchCrit>
	</LmtUtlstnJrnlQry>
```

## Report

[camt.065.001.01](../../../../messages/camt.065.001.01/index.md); P207–P309.

```xml
<LmtUtlstnJrnlRpt>
	<MsgHdr>
		<MsgId>NONREF</MsgId>
		<OrgnlBizInstr>
			<MsgId>REFABC</MsgId>
		</OrgnlBizInstr>
	</MsgHdr>
	<Pgntn>
		<PgNb>1</PgNb>
		<LastPgInd>true</LastPgInd>
	</Pgntn>
	<RptOrErr>
			<BizRpt>
				<LmtId>
					<AcctId>
					  <Othr>
						  <Id>9000000123</Id>
					  </Othr>
					</AcctId>
					<Tp>ACOL</Tp>
					<LmtCcy>EUR</LmtCcy>
					<AcctOwnr>
						<FinInstnId>
						<BICFI>PAYBKBICXXX</BICFI>
						</FinInstnId>
					</AcctOwnr>
					<BilLmtCtrPtyId>
						<Id>
							<Id>
								<AnyBIC>PAYBKBICXXX</AnyBIC>
							</Id>
						</Id>
						<RspnsblPtyId>
							<Id>
								<AnyBIC>CBAABIC1XXX</AnyBIC>
							</Id>
						</RspnsblPtyId>
					</BilLmtCtrPtyId>
				</LmtId>
				<LmtRpt>
					<LmtJrnl>
						<Lmt>
							<Amt>
								<Amt>
								<AmtWthCcy Ccy="EUR">100000</AmtWthCcy>
								</Amt>
								<CdtDbtInd>CRDT</CdtDbtInd>
							</Amt>
							<UtlstnAmt>
								<Amt>
								<AmtWthCcy Ccy="EUR">40000</AmtWthCcy>
								</Amt>
								<CdtDbtInd>DBIT</CdtDbtInd>
							</UtlstnAmt>
							<AvlblAmt>
								<Amt>
								<AmtWthCcy Ccy="EUR">60000</AmtWthCcy>
								</Amt>
								<CdtDbtInd>CRDT</CdtDbtInd>
							</AvlblAmt>
						</Lmt>
						<JrnlActvtyDt>2015-01-09</JrnlActvtyDt>
						<JrnlNtry>
							<JrnlDt>
								<Dt>2015-01-09</Dt>
							</JrnlDt>
							<CdtDbtInd>DBIT</CdtDbtInd>
							<Amt>
							<AmtWthCcy Ccy="EUR">15000</AmtWthCcy>
							</Amt>
							<NtryRef>T2SREF1234</NtryRef>
							<TxId>AOREF123</TxId>
							<AcctSvcrRef>ASREFABC</AcctSvcrRef>
						</JrnlNtry>
						<JrnlNtry>
							<JrnlDt>
								<Dt>2015-01-09</Dt>
							</JrnlDt>
							<CdtDbtInd>DBIT</CdtDbtInd>
							<Amt>
							<AmtWthCcy Ccy="EUR">12000</AmtWthCcy>
							</Amt>
							<NtryRef>T2SREF2345</NtryRef>
							<TxId>AOREF234</TxId>
							<AcctSvcrRef>ASREFBCD</AcctSvcrRef>
						</JrnlNtry>
						<JrnlNtry>
							<JrnlDt>
								<Dt>2015-01-09</Dt>
							</JrnlDt>
							<CdtDbtInd>DBIT</CdtDbtInd>
							<Amt>
							<AmtWthCcy Ccy="EUR">13000</AmtWthCcy>
							</Amt>
							<NtryRef>T2SREF3456</NtryRef>
							<TxId>AOREF345</TxId>
							<AcctSvcrRef>ASREFCDE</AcctSvcrRef>
						</JrnlNtry>
					</LmtJrnl>
				</LmtRpt>
			</BizRpt>
	</RptOrErr>
</LmtUtlstnJrnlRpt>
```

The example values and identifier strings are preserved exactly, including source whitespace inside AnyBIC values where present. [Source pull flow](../flows/flow-src-000362-p137-pull-mode.md).

## Review evidence

Full source scenario, numeric values, identifiers, XML labels/attributes and split boundaries compared against [Word19](../../../../../assets/src-000362/source-page-renders/word-page-19.png), [Word20](../../../../../assets/src-000362/source-page-renders/word-page-20.png), [Word21](../../../../../assets/src-000362/source-page-renders/word-page-21.png). Both payload fragments parse as well-formed XML; this does not establish XSD validity without the omitted namespace/document wrapper. Checked2026-11-09.
