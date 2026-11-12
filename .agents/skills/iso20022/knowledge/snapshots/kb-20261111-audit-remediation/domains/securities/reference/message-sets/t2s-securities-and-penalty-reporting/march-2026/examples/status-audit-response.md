---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Status audit trail response"
domain: "securities"
source_ids: ["src-000374"]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.027.001.01"]
source_locations: [{"source_id": "src-000374", "locator": "Business Examples; narrative P687-P688; XML P692-P920"}, {"source_id": "src-000374", "locator": "Word file/printed pages38,39,40,41,42,43,44,45"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Source examples are preserved; P284 explicitly omits the BAH and only shows business payloads. Standalone namespace/XSD validity is not claimed."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000310", "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.027.001.01", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["march-2026"]
---

# Status audit trail response

[src-000374](../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; narrative P687-P688; XML P692-P920.

**P687** Description

**P688** In this example T2S sends a Settlement Instruction Status Audit Trail Query Response containing two instructions matching the query criteria corresponding to query reference ‘QRYREF0003’. This message is sent as a response to a Settlement Instruction Status Audit Trail Query requesting all settlement instructions that were matched on or before the 25th of September 2025.

```xml
<SctiesSttlmTxQryRspn>
	<Pgntn>
		<PgNb>1</PgNb>
		<LastPgInd>true</LastPgInd>
	</Pgntn>
	<RptGnlDtls>
		<QryRef>QRYREF0003</QryRef>
		<QryTp>STPD</QryTp>
		<ActvtyInd>true</ActvtyInd>
	</RptGnlDtls>
	<Txs>
		<StsAndRsn>
			<MtchgSts>
				<Mtchd/>
			</MtchgSts>
			<Sttld/>
		</StsAndRsn>
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
						<Dt>2025-09-23</Dt>
					</Dt>
				</TradDt>
				<IntnddSttlmDt>
					<Dt>
						<Dt>2025-09-23</Dt>
					</Dt>
				</IntnddSttlmDt>
				<FctvSttlmDt>
					<Dt>2025-09-23</Dt>
				</FctvSttlmDt>
				<AckdStsTmStmp>2025-09-23T18:04:41.492392</AckdStsTmStmp>
				<MtchdStsTmStmp>2025-09-23T18:04:41.511189</MtchdStsTmStmp>
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
				<CreDtTm>2025-09-23T18:04:39.676727</CreDtTm>
			</TxDtls>
		</Tx>
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
			<AcctSvcrTxId>INITSEMT026-001</AcctSvcrTxId>
			<MktInfrstrctrTxId>2306130527746201</MktInfrstrctrTxId>
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
					<ISIN>PF0003625005</ISIN>
				</FinInstrmId>
				<SttlmQty>
					<FaceAmt>52650.00</FaceAmt>
				</SttlmQty>
				<SttldQty>
					<FaceAmt>52650.00</FaceAmt>
				</SttldQty>
				<PrevslySttldQty>
					<FaceAmt>0</FaceAmt>
				</PrevslySttldQty>
				<RmngToBeSttldQty>
					<FaceAmt>0</FaceAmt>
				</RmngToBeSttldQty>
				<SttlmAmt>
					<Amt Ccy="EUR">0</Amt>
				</SttlmAmt>
				<TradDt>
					<Dt>
						<Dt>2025-09-23</Dt>
					</Dt>
				</TradDt>
				<IntnddSttlmDt>
					<Dt>
						<Dt>2025-09-23</Dt>
					</Dt>
				</IntnddSttlmDt>
				<FctvSttlmDt>
					<Dt>2025-09-23</Dt>
				</FctvSttlmDt>
				<AckdStsTmStmp>2025-09-23T17:47:28.907861</AckdStsTmStmp>
				<MtchdStsTmStmp>2025-09-23T17:47:28.919318</MtchdStsTmStmp>
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
				<CreDtTm>2025-09-23T17:47:26.064069</CreDtTm>
			</TxDtls>
		</Tx>
	</Txs>
</SctiesSttlmTxQryRspn>
```

## Review and validation

All source example pages compared2026-11-09: [38](../../../../../../../evidence/omitted/0a0f174c6967d81e417cc064.md), [39](../../../../../../../evidence/omitted/7e5af0c870455e059c4c5104.md), [40](../../../../../../../evidence/omitted/a44f7dfca9441908fe6d427c.md), [41](../../../../../../../evidence/omitted/c41c515a5e257a3baffd3549.md), [42](../../../../../../../evidence/omitted/ef0e10a675384c42c17dd8f1.md), [43](../../../../../../../evidence/omitted/0f3af205e6d0e6f1c0097849.md), [44](../../../../../../../evidence/omitted/d88663f57c36f5282e9cad25.md), [45](../../../../../../../evidence/omitted/3514e22d53e63969c2d9fcbd.md). Independent Word-PDF text corroborates every payload paragraph (zero unmatched). The original payload is well-formed. A derived copy with only exact namespace and Document wrapper added passes the supplied exact XSD; the original fragment itself remains unchanged. [Source limitations and distinction between business rules and schema validation](../example-consistency.md).
