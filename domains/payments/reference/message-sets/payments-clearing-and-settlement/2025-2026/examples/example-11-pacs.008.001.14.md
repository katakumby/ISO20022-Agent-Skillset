---
template: false
document_kind: "message-example"
title: "Fourth FIToFICustomerCreditTransfer"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000169"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.008.001.14"]
message_families: ["pacs.008"]
source_locations: [{"source_id": "src-000162", "locator": "P1678–P1793; T38", "heading_path": ["Business Examples", "FIToFICustomerCreditTransfer pacs.008.001.14 - 1", "Fourth FIToFICustomerCreditTransfer"]}, {"source_id": "src-000169", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-abc-corporation-875623a", "participant-src-000162-example-bbbbus33", "participant-src-000162-example-ddddbebb", "participant-src-000162-example-eeeedeff", "participant-src-000162-example-ghi-semiconductors-70a6ffe"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# Fourth FIToFICustomerCreditTransfer

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Source scenario

**P1672** Fourth FIToFICustomerCreditTransfer

**P1673** Description

**P1674** On receipt of the message of BBBB Bank, EEEE Bank debits the account of BBBB Bank and credits its customer ZZ Insurances as instructed in the second payment transaction. EEEE Bank creates a new FIToFICustomerCreditTransfer to execute the first payment transaction and sends it to creditor agent DDDDBEBB through the clearing system XYZ of which both banks are members.

**P1675** Business Data

**P1676** FIToFICustomerCreditTransfer from EEEEDEFF to DDDDBEBB:

**P1677** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0038.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-11.xml) · [Source example flow](../flows/example-src-000162-08.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [EEEEDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-eeeedeff.md) | InstgAgt | /FIToFICstmrCdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [DDDDBEBB](../../../../../../../shared/reference/participants/participant-src-000162-example-ddddbebb.md) | InstdAgt | /FIToFICstmrCdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | Agt | /FIToFICstmrCdtTrf/CdtTrfTxInf/ChrgsInf[1]/Agt/FinInstnId/BICFI |
| [EEEEDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-eeeedeff.md) | Agt | /FIToFICstmrCdtTrf/CdtTrfTxInf/ChrgsInf[2]/Agt/FinInstnId/BICFI |
| [ABC Corporation](../../../../../../../shared/reference/participants/participant-src-000162-example-abc-corporation-875623a.md) | Dbtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Dbtr/Nm |
| [BBBBUS33](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus33.md) | DbtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/DbtrAgt/FinInstnId/BICFI |
| [DDDDBEBB](../../../../../../../shared/reference/participants/participant-src-000162-example-ddddbebb.md) | CdtrAgt | /FIToFICstmrCdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [GHI Semiconductors](../../../../../../../shared/reference/participants/participant-src-000162-example-ghi-semiconductors-70a6ffe.md) | Cdtr | /FIToFICstmrCdtTrf/CdtTrfTxInf/Cdtr/Nm |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.008.001.14 and wrapped in Document passed the exact supplied XSD src-000169. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table CreationDateTime 12-09-29T09:00:00; XML 2015-09-29T09:00:00.
- Table tag <Name> is retained literally; corresponding instance vocabulary uses Nm. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.
- Table tag <Type> is retained literally; corresponding instance vocabulary uses Tp. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FIToFICstmrCdtTrf>
	<GrpHdr>
		<MsgId>EEEE/150929-EUR/059</MsgId>
		<CreDtTm>2015-09-29T09:00:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>CLRG</SttlmMtd>
			<ClrSys>
				<Prtry>XYZ</Prtry>
			</ClrSys>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>EEEEDEFF</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>DDDDBEBB</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>EEEE/150929-EUR/059/1</InstrId>
			<EndToEndId>ABC/ABC-13679/2015-09-15</EndToEndId>
			<TxId>BBBB/150928-CCT/EUR/912/1</TxId>
		</PmtId>
		<PmtTpInf>
			<InstrPrty>NORM</InstrPrty>
		</PmtTpInf>
		<IntrBkSttlmAmt Ccy="EUR">499250</IntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-09-29</IntrBkSttlmDt>
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
		<ChrgsInf>
			<Amt Ccy="EUR">250</Amt>
			<Agt>
				<FinInstnId>
					<BICFI>EEEEDEFF</BICFI>
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
</FIToFICstmrCdtTrf>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-08.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
