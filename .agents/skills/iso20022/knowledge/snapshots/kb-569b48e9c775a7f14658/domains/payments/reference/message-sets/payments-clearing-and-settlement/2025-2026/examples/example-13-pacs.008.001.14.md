---
template: false
document_kind: "message-example"
title: "Second FIToFICustomerCreditTransfer"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000169"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1914–P2027; T40", "heading_path": ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 2", "Second FIToFICustomerCreditTransfer"]}, {"source_id": "src-000169", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-bbbbie2d", "participant-src-000162-example-biogenetics-crops-f41cbcd", "participant-src-000162-example-biogenetics-hq-918607e", "participant-src-000162-example-ccccie2d", "participant-src-000162-example-seed-inc-21a3af5"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# Second FIToFICustomerCreditTransfer

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P1908** Second FIToFICustomerCreditTransfer

**P1909** Description

**P1910** On receipt of the payment instruction, BBBB Bank debits AAAA Bank account, deducts its processing charges and sends an FIToFICustomerCreditTransfer to CCCC Bank, Dublin across the Irish RTGS system.

**P1911** Business Data

**P1912** The second FIToFICustomerCreditTransfer, sent by BBBB Bank to CCCC Bank:

**P1913** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0040.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-13.xml) · [Source example flow](../flows/example-src-000162-12.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | InstgAgt | /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | InstdAgt | /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | Agt | /FIToFICstmrCdtTrf/CdtTrfTxInf/ChrgsInf/Agt/FinInstnId/BICFI |
| [Biogenetics - CROPS](../../../../../../../shared/reference/participants/participant-src-000162-example-biogenetics-crops-f41cbcd.md) | UltmtDbtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/UltmtDbtr/Nm |
| [Biogenetics - HQ](../../../../../../../shared/reference/participants/participant-src-000162-example-biogenetics-hq-918607e.md) | Dbtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | DbtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | CdtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [Seed Inc.](../../../../../../../shared/reference/participants/participant-src-000162-example-seed-inc-21a3af5.md) | Cdtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14 and wrapped in Document passed the exact supplied XSD src-000169. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table InstrId BBBB/151109-CBJ056/1; XML BBBB/151109/-CBJ056/1.
- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.
- Table tag <Type> is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FIToFICstmrCdtTrf>
	<GrpHdr>
		<MsgId>BBBB/151109-CBJO56</MsgId>
		<CreDtTm>2015-11-09T10:13:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>CLRG</SttlmMtd>
			<ClrSys>
				<Prtry>CBJ</Prtry>
			</ClrSys>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>BBBBIE2D</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>CCCCIE2D</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>BBBB/151109/-CBJ056/1</InstrId>
			<EndToEndId>CROPS/SX-25T/2015-10-13</EndToEndId>
			<TxId>AAAA/151109-CCT/EUR/443/1</TxId>
		</PmtId>
		<IntrBkSttlmAmt Ccy="EUR">74900</IntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-11-09</IntrBkSttlmDt>
		<InstdAmt Ccy="EUR">75000</InstdAmt>
		<ChrgBr>SHAR</ChrgBr>
		<ChrgsInf>
			<Amt Ccy="EUR">100</Amt>
			<Agt>
				<FinInstnId>
					<BICFI>BBBBIE2D</BICFI>
				</FinInstnId>
			</Agt>
		</ChrgsInf>
		<UltmtDbtr>
			<Nm>Biogenetics - CROPS</Nm>
			<PstlAdr>
				<StrtNm>Growth Street</StrtNm>
				<BldgNb>17</BldgNb>
				<PstCd>G5 OTW</PstCd>
				<TwnNm>Glasgow</TwnNm>
				<Ctry>GB</Ctry>
			</PstlAdr>
		</UltmtDbtr>
		<Dbtr>
			<Nm>Biogenetics - HQ</Nm>
			<PstlAdr>
				<StrtNm>Corn Street</StrtNm>
				<BldgNb>13</BldgNb>
				<PstCd>W6 8DR</PstCd>
				<TwnNm>London</TwnNm>
				<Ctry>GB</Ctry>
			</PstlAdr>
		</Dbtr>
		<DbtrAcct>
			<Id>
				<Othr>
					<Id>46373892034012</Id>
				</Othr>
			</Id>
		</DbtrAcct>
		<DbtrAgt>
			<FinInstnId>
				<BICFI>AAAAGB2L</BICFI>
			</FinInstnId>
		</DbtrAgt>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>CCCCIE2D</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<Cdtr>
			<Nm>Seed Inc.</Nm>
			<PstlAdr>
				<StrtNm>Grain Lane</StrtNm>
				<BldgNb>27</BldgNb>
				<TwnNm>Dublin</TwnNm>
				<Ctry>IE</Ctry>
			</PstlAdr>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<IBAN>IE29CCCC93115212345678</IBAN>
			</Id>
		</CdtrAcct>
		<Purp>
			<Cd>GDDS</Cd>
		</Purp>
		<RmtInf>
			<Strd>
				<RfrdDocInf>
					<Tp>
						<CdOrPrtry>
							<Cd>CINV</Cd>
						</CdOrPrtry>
					</Tp>
					<Nb>SX-25T</Nb>
					<RltdDt>
					<Tp>
						<Cd>INDA</Cd>
					</Tp>
					<Dt>2015-10-13</Dt>									
					</RltdDt>						
				</RfrdDocInf>
			</Strd>
		</RmtInf>
	</CdtTrfTxInf>
</FIToFICstmrCdtTrf>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-12.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
