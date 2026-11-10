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
source_locations: [{"source_id": "src-000162", "locator": "P1397–P1567; T36", "heading_path": ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 1", "Second FIToFICustomerCreditTransfer"]}, {"source_id": "src-000169", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-ddddbebb", "participant-src-000162-example-eeeedeff", "participant-src-000162-example-ghi-semiconductors-70a6ffe", "participant-src-000162-example-mr-jones-909aee6", "participant-src-000162-example-zz-insurances-01c49f4"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# Second FIToFICustomerCreditTransfer

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Source scenario

**P1393** Second FIToFICustomerCreditTransfer

**P1394** Business Data

**P1395** The second FIToFICustomerCreditTransfer, from BBBBUS33 to EEEEDEFF:

**P1396** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0036.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-09.xml) · [Source example flow](../flows/example-src-000162-08.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | InstgAgt | /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [EEEEDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-eeeedeff.md) | InstdAgt | /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | Agt | /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/ChrgsInf/Agt/FinInstnId/BICFI |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | Dbtr | /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/Dbtr/Nm |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | DbtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/DbtrAgt/FinInstnId/BICFI |
| [DDDDBEBB](../../../../../../../shared/reference/participants/participant-src-000162-example-ddddbebb.md) | CdtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/CdtrAgt/FinInstnId/BICFI |
| [GHI Semiconductors](../../../../../../../shared/reference/participants/participant-src-000162-example-ghi-semiconductors-70a6ffe.md) | Cdtr | /FIToFICstmrCdtTrf/CdtTrfTxInf[1]/Cdtr/Nm |
| [Mr. Jones](../../../../../../../shared/reference/participants/participant-src-000162-example-mr-jones-909aee6.md) | Dbtr | /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/Dbtr/Nm |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | DbtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/DbtrAgt/FinInstnId/BICFI |
| [EEEEDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-eeeedeff.md) | CdtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/CdtrAgt/FinInstnId/BICFI |
| [ZZ Insurances](../../../../../../../shared/reference/participants/participant-src-000162-example-zz-insurances-01c49f4.md) | Cdtr | /FIToFICstmrCdtTrf/CdtTrfTxInf[2]/Cdtr/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14 and wrapped in Document passed the exact supplied XSD src-000169. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table MsgId BBBB/150928-CCT/EUR/912; XML BBBB/150928-CT/EUR/912.
- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.
- Table tag <RfrdDocType> is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.
- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.
- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FIToFICstmrCdtTrf>
	<GrpHdr>
		<MsgId>BBBB/150928-CT/EUR/912</MsgId>
		<CreDtTm>2015-09-28T16:01:00</CreDtTm>
		<NbOfTxs>2</NbOfTxs>
		<TtlIntrBkSttlmAmt Ccy="EUR">504500</TtlIntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
		<SttlmInf>
			<SttlmMtd>INDA</SttlmMtd>
			<SttlmAcct>
				<Id>
					<Othr>
						<Id>29314569847</Id>
					</Othr>
				</Id>
			</SttlmAcct>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>BBBBUS33</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>EEEEDEFF</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>BBBB/150928-CCT/EUR/912/1</InstrId>
			<EndToEndId>ABC/ABC-13679/2015-09-15</EndToEndId>
			<TxId>BBBB/150928-CCT/EUR/912/1</TxId>
		</PmtId>
		<PmtTpInf>
			<InstrPrty>NORM</InstrPrty>
		</PmtTpInf>
		<IntrBkSttlmAmt Ccy="EUR">499500</IntrBkSttlmAmt>
		<InstdAmt Ccy="EUR">500000</InstdAmt>
		<ChrgBr>CRED</ChrgBr>
		<ChrgsInf>
			<Amt Ccy="EUR">500</Amt>
			<Agt>
				<FinInstnId>
					<BICFI>BBBBUS33</BICFI>
				</FinInstnId>
			</Agt>
		</ChrgsInf>
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
				<BICFI>DDDDBEBB</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<Cdtr>
			<Nm>GHI Semiconductors</Nm>
			<PstlAdr>
				<StrtNm>Avenue Brugmann</StrtNm>
				<BldgNb>415</BldgNb>
				<PstCd>1180</PstCd>
				<TwnNm>Brussels</TwnNm>
				<Ctry>BE</Ctry>
			</PstlAdr>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<IBAN>BE30001216371411</IBAN>
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
					<Nb>ABC-13679</Nb>
					<RltdDt>
					<Tp>
						<Cd>INDA</Cd>
					</Tp>
					<Dt>2015-09-15</Dt>									
					</RltdDt>		
				</RfrdDocInf>
			</Strd>
		</RmtInf>
	</CdtTrfTxInf>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>BBBB/150928-CCT/EUR/912/2</InstrId>
			<EndToEndId>BBBB/150928-ZZ/JO/164794</EndToEndId>
			<TxId>BBBB/150928-CCT/EUR/912/2</TxId>
		</PmtId>
		<PmtTpInf>
			<InstrPrty>NORM</InstrPrty>
		</PmtTpInf>
		<IntrBkSttlmAmt Ccy="EUR">5000</IntrBkSttlmAmt>
		<ChrgBr>SHAR</ChrgBr>
		<Dbtr>
			<Nm>Mr. Jones</Nm>
			<PstlAdr>
				<StrtNm>16th Street</StrtNm>
				<BldgNb>30</BldgNb>
				<PstCd>NY10023</PstCd>
				<TwnNm>New York</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</Dbtr>
		<DbtrAcct>
			<Id>
				<Othr>
					<Id>00125583145</Id>
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
				<BICFI>EEEEDEFF</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<Cdtr>
			<Nm>ZZ Insurances</Nm>
			<PstlAdr>
				<StrtNm>Friedrich-Ebert-Anlage</StrtNm>
				<BldgNb>2-14</BldgNb>
				<PstCd>D-60 325</PstCd>
				<TwnNm>Frankfurt am Main</TwnNm>
				<Ctry>DE</Ctry>
				<AdrLine>City Haus 1 10th Floor</AdrLine>
			</PstlAdr>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<IBAN>DE89370400440532014000</IBAN>
			</Id>
		</CdtrAcct>
		<RmtInf>
			<Ustrd>Contract ZZ/JO/164794</Ustrd>
		</RmtInf>
	</CdtTrfTxInf>
</FIToFICstmrCdtTrf>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-08.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
