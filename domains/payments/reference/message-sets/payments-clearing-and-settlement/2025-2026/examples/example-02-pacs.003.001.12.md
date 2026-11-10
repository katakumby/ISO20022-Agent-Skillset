---
template: false
document_kind: "message-example"
title: "FIToFICustomerDirectDebit pacs.003.001.12"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000166"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.003.001.12"]
message_families: ["pacs.003"]
source_locations: [{"source_id": "src-000162", "locator": "P740–P835; T29", "heading_path": ["Business Examples", "FIToFICustomerDirectDebit pacs.003.001.12"]}, {"source_id": "src-000166", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaaus29", "participant-src-000162-example-ababus23", "participant-src-000162-example-bbbbus39", "participant-src-000162-example-jones-4dbd8f5", "participant-src-000162-example-virgay-6e3f97e"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# FIToFICustomerDirectDebit pacs.003.001.12

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Source scenario

**P732** FIToFICustomerDirectDebit pacs.003.001.12

**P733** Description

**P734** On 28 June 2015, following the receipt of a CustomerDirectDebitInitiation message from its customer Virgay, AAAAUS29 in its turn sends an FIToFICustomerDirectDebit message to ABABUS23, the common correspondent for AAAAUS29 and BBBBUS39, the agent of debtor Jones.

**P735** AAAAUS29 instructs ABABUS23, under Service Level CTRV - 356, to collect USD 1025 from account 123456, owned by Jones, the debtor, and serviced by BBBBUS39. The mandate related information is also provided: the mandate reference is VIRGAY123 and the mandate was signed by Jones on 13 July 2008. The last collection is due to take place on 13 July 2015. The payment is for life insurance. The requested collection date is 13 July 20102 and charges related to the handling of the instruction are shared between the creditor and the debtor.

**P736** The CustomerDirectDebitInitiation instruction sent by Virgay to AAAAUS29 is documented in the business example section of the CustomerDirectDebitInitiation message in the Payments Initiation Message Reference Guide.

**P737** Business Data

**P738** FIToFICustomerDirectDebit from AAAAUS29 to ABABUS23:

**P739** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0029.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-02.xml) · [Source example flow](../flows/example-src-000162-02.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaaus29.md) | InstgAgt | /FIToFICstmrDrctDbt/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [ABABUS23](../../../../../../../shared/reference/participants/participant-src-000162-example-ababus23.md) | InstdAgt | /FIToFICstmrDrctDbt/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [Virgay](../../../../../../../shared/reference/participants/participant-src-000162-example-virgay-6e3f97e.md) | Cdtr | /FIToFICstmrDrctDbt/DrctDbtTxInf/Cdtr/Nm |
| [AAAAUS29](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaaus29.md) | CdtrAgt | /FIToFICstmrDrctDbt/DrctDbtTxInf/CdtrAgt/FinInstnId/BICFI |
| [Jones](../../../../../../../shared/reference/participants/participant-src-000162-example-jones-4dbd8f5.md) | Dbtr | /FIToFICstmrDrctDbt/DrctDbtTxInf/Dbtr/Nm |
| [BBBBUS39](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbus39.md) | DbtrAgt | /FIToFICstmrDrctDbt/DrctDbtTxInf/DbtrAgt/FinInstnId/BICFI |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.003.001.12 and wrapped in Document passed the exact supplied XSD src-000166. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Narrative requested collection date is 13 July 20102; table and XML use 2015-07-13.

## Complete source payload

```xml
<FIToFICstmrDrctDbt>
	<GrpHdr>
		<MsgId>AAAA100628-123v</MsgId>
		<CreDtTm>2015-06-28T10:05:00</CreDtTm>
			<NbOfTxs>1</NbOfTxs>
		<IntrBkSttlmDt>2015-06-28</IntrBkSttlmDt>
		<SttlmInf>
			<SttlmMtd>INDA</SttlmMtd>
		</SttlmInf>
		<PmtTpInf>
			<InstrPrty>NORM</InstrPrty>
			<SvcLvl>
				<Prtry>CTRV-356</Prtry>
			</SvcLvl>
			<SeqTp>RCUR</SeqTp>
		</PmtTpInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>AAAAUS29</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>ABABUS23</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<DrctDbtTxInf>
		<PmtId>
			<EndToEndId>VA060713/0123</EndToEndId>
			<TxId>AAAAUS29/100628/ad458</TxId>
		</PmtId>
		<IntrBkSttlmAmt Ccy="USD">1025</IntrBkSttlmAmt>
		<InstdAmt Ccy="USD">1025</InstdAmt>
		<ChrgBr>SHAR</ChrgBr>
		<ReqdColltnDt>2015-07-13</ReqdColltnDt>
		<DrctDbtTx>
			<MndtRltdInf>
				<MndtId>VIRGAY123</MndtId>
				<DtOfSgntr>2008-07-13</DtOfSgntr>
				<FnlColltnDt>2015-07-13</FnlColltnDt>
				<Frqcy><Tp>YEAR</Tp></Frqcy>
			</MndtRltdInf>
		</DrctDbtTx>
		<Cdtr>
			<Nm>Virgay</Nm>
			<PstlAdr>
				<StrtNm>Virginia Lane</StrtNm>
					<BldgNb>36</BldgNb>
				<PstCd>NJ 07311</PstCd>
				<TwnNm>Jersey City</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<Othr>
					<Id>789123</Id>
				</Othr>
			</Id>
		</CdtrAcct>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>AAAAUS29</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<Dbtr>
			<Nm>Jones</Nm>
			<PstlAdr>
				<StrtNm>Hudson Street</StrtNm>
				<BldgNb>19</BldgNb>
				<PstCd>NJ 07302</PstCd>
				<TwnNm>Jersey City</TwnNm>
				<Ctry>US</Ctry>
			</PstlAdr>
		</Dbtr>
			<DbtrAcct>
			<Id>
				<Othr>
					<Id>123456</Id>
				</Othr>
			</Id>
		</DbtrAcct>
		<DbtrAgt>
			<FinInstnId>
				<BICFI>BBBBUS39</BICFI>
			</FinInstnId>
		</DbtrAgt>
		<Purp>
			<Cd>LIFI</Cd>
		</Purp>
		<RmtInf>
			<Ustrd>LIFE INSURANCE PAYMENT/JULY 2015</Ustrd>
		</RmtInf>
	</DrctDbtTxInf>
</FIToFICstmrDrctDbt>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-02.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
