---
template: false
document_kind: "message-example"
title: "FIToFICustomerCreditTransfer pacs.008.001.14 - 2"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000169"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1805–P1907; T39", "heading_path": ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 2", "First FIToFICustomerCreditTransfer"]}, {"source_id": "src-000169", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaagb2l", "participant-src-000162-example-bbbbie2d", "participant-src-000162-example-biogenetics-crops-f41cbcd", "participant-src-000162-example-biogenetics-hq-918607e", "participant-src-000162-example-ccccie2d", "participant-src-000162-example-seed-inc-21a3af5"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# FIToFICustomerCreditTransfer pacs.008.001.14 - 2

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Source scenario

**P1794** FIToFICustomerCreditTransfer pacs.008.001.14 - 2

**P1795** This example covers two FIToFICustomerCreditTransfer messages. The first FIToFICustomerCreditTransfer message is sent by AAAA Bank to BBBB Bank. The second FIToFICustomerCreditTransfer message is sent by BBBB Bank to CCCC Bank.

**P1796** First FIToFICustomerCreditTransfer

**P1797** Description

**P1798** Biogenetics-Crops, Glasgow, subsidiary of Biogenetics HQ, London, has received an invoice with number SX-25T, dated 13 October 2010 from Seed Inc., Dublin: 75 thousand EUR needs to be paid to the account of Seed Inc. IE29CCCC93115212345678 held at CCCC Bank, Dublin (CCCCIE2D). Transaction charges for the payment are shared between Biogenetics and Seed Inc.

**P1799** The payment of all Biogenetics invoices is centralised at Biogenetics HQ. It assigns reference CROPS/SX-25T/

**P1800** 2015-10-13 to the payment order and passes it on to AAAA Bank (AAAAGB2L) where it holds the account

**P1801** 46373892034012. AAAA Bank sends the payment to its correspondent BBBB Bank in Dublin (BBBBIE2D).

**P1802** Business Data

**P1803** The first FIToFICustomerCreditTransfer, sent by AAAA Bank to BBBB Bank:

**P1804** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0039.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-12.xml) · [Source example flow](../flows/example-src-000162-12.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | InstgAgt | /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [BBBBIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbie2d.md) | InstdAgt | /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Biogenetics - CROPS](../../../../../../../shared/reference/participants/participant-src-000162-example-biogenetics-crops-f41cbcd.md) | UltmtDbtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/UltmtDbtr/Nm |
| [Biogenetics - HQ](../../../../../../../shared/reference/participants/participant-src-000162-example-biogenetics-hq-918607e.md) | Dbtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm |
| [AAAAGB2L](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaagb2l.md) | DbtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [CCCCIE2D](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccie2d.md) | CdtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [Seed Inc.](../../../../../../../shared/reference/participants/participant-src-000162-example-seed-inc-21a3af5.md) | Cdtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14 and wrapped in Document passed the exact supplied XSD src-000169. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.
- Table tag <Type> is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FIToFICstmrCdtTrf>
	<GrpHdr>
		<MsgId>AAAA/151109-CCT/EUR/443</MsgId>
		<CreDtTm>2015-11-09T10:09:13</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>INDA</SttlmMtd>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>AAAAGB2L</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>BBBBIE2D</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>AAAA/151109-CCT/EUR/443/1</InstrId>
			<EndToEndId>CROPS/SX-25T/2015-10-13</EndToEndId>
			<TxId>AAAA/151109-CCT/EUR/443/1</TxId>
		</PmtId>
		<IntrBkSttlmAmt Ccy="EUR">750000</IntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-11-09</IntrBkSttlmDt>
		<InstdAmt Ccy="EUR">75000</InstdAmt>
		<ChrgBr>SHAR</ChrgBr>
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
