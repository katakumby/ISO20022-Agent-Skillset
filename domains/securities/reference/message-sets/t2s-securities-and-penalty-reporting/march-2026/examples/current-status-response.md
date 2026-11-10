---
template: false
document_kind: "source-example"
manual_curated: true
review_status: "reviewed"
title: "Current status query response"
domain: "securities"
source_ids: ["src-000374"]
message_sets: ["t2s-securities-and-penalty-reporting"]
message_ids: ["semt.027.001.01"]
source_locations: [{"source_id": "src-000374", "locator": "Business Examples; narrative P544-P545; XML P549-P684"}, {"source_id": "src-000374", "locator": "Word file/printed pages34,35,36,37,38"}]
xml_fragment_wellformedness: "pass"
extraction_transform: "Common leading paragraph indentation removed only."
limitations: ["Source examples are preserved; P284 explicitly omits the BAH and only shows business payloads. Standalone namespace/XSD validity is not claimed."]
source_text_visual_review: "pass"
review_date: "2026-11-09"
derived_envelope_xsd_check: {"result": "pass", "source_schema_id": "src-000310", "namespace": "urn:iso:std:iso:20022:tech:xsd:semt.027.001.01", "transform": "Assigned the supplied exact namespace to all payload tags and enclosed it in Document; interior values and structure unchanged. Original fragment retained.", "errors": []}
source_editions: ["march-2026"]
---

# Current status query response

[src-000374](../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart1_Target2Securities_SecuritiesAndPenaltyReporting_v2.docx`; narrative P544-P545; XML P549-P684.

**P544** Description

**P545** In this example T2S sends a Settlement Instruction Current Status Query Response containing one instruction matching the query criteria corresponding to query reference ‘QRYREF0002’. This message is sent as a response to a Settlement Instruction Current Status Query requesting all pending settlement instructions with a high priority where the securities account is ‘1000000123’.

```xml
<SctiesSttlmTxQryRspn>
	<Pgntn>
		<PgNb>1</PgNb>
		<LastPgInd>true</LastPgInd>
	</Pgntn>
	<RptGnlDtls>
		<QryRef>QRYREF0002</QryRef>
		<QryTp>STTS</QryTp>
		<ActvtyInd>true</ActvtyInd>
	</RptGnlDtls>
	<Txs>
		<StsAndRsn>
			<SttlmSts>
				<Pdg>
					<Rsn>
						<Cd>
							<Cd>LACK</Cd>
						</Cd>
						<AddtlRsnInf>SXAA014 - Failure of the settlement attempt of the settlement instruction due to a lack of securities in your securities position</AddtlRsnInf>
					</Rsn>
				</Pdg>
			</SttlmSts>
		</StsAndRsn>
		<Tx>
			<SfkpgAcct>
				<Id>1000000123</Id>
			</SfkpgAcct>
			<StsAndRsn>
				<MtchgSts>
					<Mtchd/>
				</MtchgSts>
				<SttlmSts>
					<Pdg>
						<Rsn>
							<Cd>
								<Cd>LACK</Cd>
							</Cd>
							<AddtlRsnInf>SXAA014 - Failure of the settlement attempt of the settlement instruction due to a lack of securities in your securities position</AddtlRsnInf>
						</Rsn>
					</Pdg>
				</SttlmSts>
			</StsAndRsn>
			<AcctOwnrTxId>TESTSEMT026-001</AcctOwnrTxId>
			<MktInfrstrctrTxId>2306130527744846</MktInfrstrctrTxId>
			<TxDtls>
				<TxActvty>
					<Cd>SETT</Cd>
				</TxActvty>
				<SttlmTxOrCorpActnEvtTp>
					<SctiesTxTp>
						<Cd>TRAD</Cd>
					</SctiesTxTp>
				</SttlmTxOrCorpActnEvtTp>
				<SctiesMvmntTp>DELI</SctiesMvmntTp>
				<Pmt>FREE</Pmt>
				<FinInstrmId>
					<ISIN>PF0003625005</ISIN>
				</FinInstrmId>
				<SttlmQty>
					<FaceAmt>54000.00</FaceAmt>
				</SttlmQty>
				<SttldQty>
					<FaceAmt>0</FaceAmt>
				</SttldQty>
				<PrevslySttldQty>
					<FaceAmt>0</FaceAmt>
				</PrevslySttldQty>
				<RmngToBeSttldQty>
					<FaceAmt>54000</FaceAmt>
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
				<StsDt>2025-09-24T15:06:52.976484</StsDt>
				<AckdStsTmStmp>2025-09-23T17:22:28.964428</AckdStsTmStmp>
				<MtchdStsTmStmp>2025-09-23T17:22:28.971750</MtchdStsTmStmp>
				<Prty>
					<Nmrc>0003</Nmrc>
				</Prty>
				<DlvrgSttlmPties>
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
							<Id>C5PFCSDP370670</Id>
						</SfkpgAcct>
					</Pty1>
				</RcvgSttlmPties>
				<MsgOrgtr>
					<Id>
						<Id>
							<AnyBIC>PALLPFP1000</AnyBIC>
						</Id>
					</Id>
					<RspnsblPtyId>
						<Id>
							<AnyBIC>PAAHPFP1000</AnyBIC>
						</Id>
					</RspnsblPtyId>
				</MsgOrgtr>
				<CreDtTm>2025-09-23T17:22:26.722108</CreDtTm>
			</TxDtls>
		</Tx>
	</Txs>
</SctiesSttlmTxQryRspn>
```

## Review and validation

All source example pages compared2026-11-09: [34](../../../../../assets/src-000374/source-page-renders/word-page-34.png), [35](../../../../../assets/src-000374/source-page-renders/word-page-35.png), [36](../../../../../assets/src-000374/source-page-renders/word-page-36.png), [37](../../../../../assets/src-000374/source-page-renders/word-page-37.png), [38](../../../../../assets/src-000374/source-page-renders/word-page-38.png). Independent Word-PDF text corroborates every payload paragraph (zero unmatched). The original payload is well-formed. A derived copy with only exact namespace and Document wrapper added passes the supplied exact XSD; the original fragment itself remains unchanged. [Source limitations and distinction between business rules and schema validation](../example-consistency.md).
