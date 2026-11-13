---
template: false
document_kind: "message-example"
title: "Third FIToFICustomerCreditTransfer"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000169"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1572–P1671; T37", "heading_path": ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 1", "Third FIToFICustomerCreditTransfer"]}, {"source_id": "src-000169", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-abc-corporation-51d6618", "participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-bbbbus66"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# Third FIToFICustomerCreditTransfer

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P1568** Third FIToFICustomerCreditTransfer

**P1569** Business Data

**P1570** The third FIToFICustomerCreditTransfer, from BBBBUS33 to BBBBUS66:

**P1571** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0037.md) · [Literal XML payload](../../../../../../../evidence/archived/8bd354eeedd1d889c81450a5.md) · [Source example flow](../flows/example-src-000162-08.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | InstgAgt | /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [BBBBUS66](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus66.md) | InstdAgt | /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | Dbtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | DbtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [BBBBUS66](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus66.md) | CdtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-51d6618.md) | Cdtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14 and wrapped in Document passed the exact supplied XSD src-000169. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.
- Table tag <RfrdDocType> is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FIToFICstmrCdtTrf>
	<GrpHdr>
		<MsgId>BBBB/150928-CCT/USD/897</MsgId>
		<CreDtTm>2015-09-28T16:02:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<TtlIntrBkSttlmAmt Ccy="USD">1000000</TtlIntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-06-29</IntrBkSttlmDt>
		<SttlmInf>
			<SttlmMtd>INDA</SttlmMtd>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>BBBBUS66</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>ABC/150928/CCT001/3</InstrId>
			<EndToEndId>ABC/987-AC/2015-09-27</EndToEndId>
			<TxId>BBBB/150928-CCT/USD/897</TxId>
		</PmtId>
		<PmtTpInf>
			<InstrPrty>NORM</InstrPrty>
		</PmtTpInf>
		<IntrBkSttlmAmt Ccy="USD">1000000</IntrBkSttlmAmt>
		<ChrgBr>SHAR</ChrgBr>
		<Dbtr>
			<Nm>ABC Corporation</Nm>
			<PstlAdr>
				<StrtNm>Times Square</StrtNm>
				<BldgNb>7</BldgNb>
				<PstCd>NY 10036</PstCd>
				<TwnNm>New York</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</Dbtr>
		<DbtrAcct>
			<Id>
				<Othr>
					<Id>00125574999</Id>
				</Othr>
			</Id>
		</DbtrAcct>
		<DbtrAgt>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</DbtrAgt>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>BBBBUS66</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<Cdtr>
			<Nm>ABC Corporation</Nm>
			<PstlAdr>
				<Dept>Treasury Department</Dept>
				<StrtNm>Bush Street</StrtNm>
				<BldgNb>13</BldgNb>
				<PstCd>CA 94108</PstCd>
				<TwnNm>San Francisco</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<Othr>
					<Id>4895623</Id>
				</Othr>
			</Id>
		</CdtrAcct>
		<Purp>
			<Cd>INTC</Cd>
		</Purp>
		<RmtInf>
			<Strd>
				<RfrdDocInf>
					<Tp>
						<CdOrPrtry>
							<Cd>CINV</Cd>
						</CdOrPrtry>
					</Tp>
					<Nb>987-AC</Nb>
					<RltdDt>
					<Tp>
						<Cd>INDA</Cd>
					</Tp>
					<Dt>2015-09-27</Dt>									
					</RltdDt>					
				</RfrdDocInf>
			</Strd>
		</RmtInf>
	</CdtTrfTxInf>
</FIToFICstmrCdtTrf>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-08.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
