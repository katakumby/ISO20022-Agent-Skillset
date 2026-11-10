---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "needs-review"
title: "Instruction query response"
domain: "securities"
source_ids: ["src-000374"]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.027.001.01"]
source_locations: [{"source_id": "src-000374", "locator": "Business Examples; narrative P419-P420; XML P424-P541"}, {"source_id": "src-000374", "locator": "Word file/printed pages31,32,33,34"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Source examples are preserved; P284 explicitly omits the BAH and only shows business payloads. Standalone namespace/XSD validity is not claimed."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000310", "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.027.001.01", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
issue_ids: ["issue-000057"]
source_editions: ["march-2026"]
---

# Instruction query response

[src-000374](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; narrative P419-P420; XML P424-P541.

**P419** Description

**P420** In this example T2S sends a Settlement Instruction Query Response containing one instruction matching the query criteria corresponding to query reference ‘QRYREF0001’. This message is sent as a response to a Settlement Instruction Query requesting all settlement instructions where the securities account is ‘1000000123’ and the settlement quantity is greater than or equal to 50000 units and less than or equal to 60000 units.

```xml
<SctiesSttlmTxQryRspn>
	<Pgntn>
		<PgNb>1</PgNb>
		<LastPgInd>true</LastPgInd>
	</Pgntn>
	<RptGnlDtls>
		<QryRef>QRYREF0001</QryRef>
		<QryTp>INST</QryTp>
		<ActvtyInd>true</ActvtyInd>
	</RptGnlDtls>
	<Txs>
		<Tx>
			<SfkpgAcct>
				<Id>1000000123</Id>
			</SfkpgAcct>
			<StsAndRsn>
				<MtchgSts>
					<Mtchd/>
				</MtchgSts>
				<Sttld/>
			</StsAndRsn>
			<AcctOwnrTxId>NONREF</AcctOwnrTxId>
			<AcctSvcrTxId>INITSEMT026-002</AcctSvcrTxId>
			<MktInfrstrctrTxId>2306130527746616</MktInfrstrctrTxId>
			<TxDtls>
				<TxActvty>
					<Cd>SETT</Cd>
				</TxActvty>
				<SttlmTxOrCorpActnEvtTp>
					<SctiesTxTp>
						<Cd>TRAD</Cd>
					</SctiesTxTp>
				</SttlmTxOrCorpActnEvtTp>
				<SctiesMvmntTp>RECE</SctiesMvmntTp>
				<Pmt>FREE</Pmt>
				<FinInstrmId>
					<ISIN>ISIN00000456</ISIN>
				</FinInstrmId>
				<SttlmQty>
					<Unit>52650</Unit>
				</SttlmQty>
				<SttldQty>
					<Unit>52650</Unit>
				</SttldQty>
				<PrevslySttldQty>
					<Unit>0</Unit>
				</PrevslySttldQty>
				<RmngToBeSttldQty>
					<Unit>0</Unit>
				</RmngToBeSttldQty>
				<SttlmAmt>
					<Amt Ccy="EUR">0</Amt>
				</SttlmAmt>
				<TradDt>
					<Dt>
						<Dt>2025-09-25</Dt>
					</Dt>
				</TradDt>
				<IntnddSttlmDt>
					<Dt>
						<Dt>2025-09-25</Dt>
					</Dt>
				</IntnddSttlmDt>
				<FctvSttlmDt>
					<Dt>2025-09-25</Dt>
				</FctvSttlmDt>
				<AckdStsTmStmp>2025-09-25T18:04:41.492392</AckdStsTmStmp>
				<MtchdStsTmStmp>2025-09-25T18:04:41.511189</MtchdStsTmStmp>
				<Prty>
					<Nmrc>0004</Nmrc>
				</Prty>
				<DlvrgSttlmPties>
					<Dpstry>
						<Id>
							<AnyBIC>PAAHPFP1000</AnyBIC>
						</Id>
					</Dpstry>
					<Pty1>
						<Id>
							<AnyBIC>PAAHPFP1000</AnyBIC>
						</Id>
						<SfkpgAcct>
							<Id>C5PFISSA362070</Id>
						</SfkpgAcct>
					</Pty1>
				</DlvrgSttlmPties>
				<RcvgSttlmPties>
					<Dpstry>
						<Id>
							<AnyBIC>PAAHPFP1000</AnyBIC>
						</Id>
					</Dpstry>
					<Pty1>
						<Id>
							<AnyBIC>PALLPFP1000</AnyBIC>
						</Id>
						<SfkpgAcct>
							<Id>1000000123</Id>
						</SfkpgAcct>
					</Pty1>
				</RcvgSttlmPties>
				<MsgOrgtr>
					<Id>
						<Id>
							<AnyBIC>PAAHPFP1000</AnyBIC>
						</Id>
					</Id>
					<RspnsblPtyId>
						<Id>
							<AnyBIC>TCSOTCS0XXX</AnyBIC>
						</Id>
					</RspnsblPtyId>
				</MsgOrgtr>
				<CreDtTm>2025-09-25T18:04:39.676727</CreDtTm>
			</TxDtls>
		</Tx>
	</Txs>
</SctiesSttlmTxQryRspn>
```

## Review and validation

All source example pages compared2026-11-09: [31](../../../../../assets/src-000374/source-page-renders/word-page-31.png), [32](../../../../../assets/src-000374/source-page-renders/word-page-32.png), [33](../../../../../assets/src-000374/source-page-renders/word-page-33.png), [34](../../../../../assets/src-000374/source-page-renders/word-page-34.png). Independent Word-PDF text corroborates every payload paragraph (zero unmatched). The original payload is well-formed. A derived copy with only exact namespace and Document wrapper added passes the supplied exact XSD; the original fragment itself remains unchanged. [Source limitations and distinction between business rules and schema validation](../example-consistency.md).
