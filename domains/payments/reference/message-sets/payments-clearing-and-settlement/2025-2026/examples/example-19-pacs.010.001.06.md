---
template: false
document_kind: "message-example"
title: "FinancialInstitutionDirectDebit pacs.010.001.06"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000171"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.010.001.06"]
message_families: ["pacs.010"]
source_locations: [{"source_id": "src-000162", "locator": "P2425–P2503; T46", "heading_path": ["Business Examples", "FinancialInstitutionDirectDebit pacs.010.001.06 "]}, {"source_id": "src-000171", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-mmmmbebb", "participant-src-000162-example-nnnndeff", "participant-src-000162-example-ooooatww", "participant-src-000162-example-ppppdkkk", "participant-src-000162-example-qqqqfrpp"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# FinancialInstitutionDirectDebit pacs.010.001.06

[src-000162](../../../../../../../raw-input/payments_clearing_and_settlement/ISO20022_MDRPart1_PaymentsClearingAndSettlement_2025_2026_v2.docx)

## Source scenario

**P2418** FinancialInstitutionDirectDebit pacs.010.001.06

**P2419** Description

**P2420** Bank MMMM instructs Bank NNNN to debit the account of Bank PPPP for 2500 EUR and Bank OOOO for 5000 EUR in favour of its account at Bank QQQQ with value date 21 November 2015.

**P2421** Business Data

**P2422** The FinancialInstitutionDirectDebit message, from Bank MMMMBEBB to Bank NNNNDEFF:

**P2424** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0046.md) · [Literal XML payload](../../../../../assets/src-000162/examples/example-19.xml) · [Source example flow](../flows/example-src-000162-19.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [MMMMBEBB](../../../../../../../shared/reference/participants/participant-src-000162-example-mmmmbebb.md) | InstgAgt | /FIDrctDbt/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [NNNNDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-nnnndeff.md) | InstdAgt | /FIDrctDbt/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [QQQQFRPP](../../../../../../../shared/reference/participants/participant-src-000162-example-qqqqfrpp.md) | CdtrAgt | /FIDrctDbt/CdtInstr/CdtrAgt/FinInstnId/BICFI |
| [MMMMBEBB](../../../../../../../shared/reference/participants/participant-src-000162-example-mmmmbebb.md) | Cdtr | /FIDrctDbt/CdtInstr/Cdtr/FinInstnId/BICFI |
| [PPPPDKKK](../../../../../../../shared/reference/participants/participant-src-000162-example-ppppdkkk.md) | Dbtr | /FIDrctDbt/CdtInstr/DrctDbtTxInf[1]/Dbtr/FinInstnId/BICFI |
| [NNNNDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-nnnndeff.md) | DbtrAgt | /FIDrctDbt/CdtInstr/DrctDbtTxInf[1]/DbtrAgt/FinInstnId/BICFI |
| [OOOOATWW](../../../../../../../shared/reference/participants/participant-src-000162-example-ooooatww.md) | Dbtr | /FIDrctDbt/CdtInstr/DrctDbtTxInf[2]/Dbtr/FinInstnId/BICFI |
| [NNNNDEFF](../../../../../../../shared/reference/participants/participant-src-000162-example-nnnndeff.md) | DbtrAgt | /FIDrctDbt/CdtInstr/DrctDbtTxInf[2]/DbtrAgt/FinInstnId/BICFI |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.010.001.06 and wrapped in Document passed the exact supplied XSD src-000171. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table CreditInstruction tag <CdtTrfTxInf>; XML root child <CdtInstr>.

## Complete source payload

```xml
<FIDrctDbt>
	<GrpHdr>
		<MsgId>MMMM/151121 PPPP_OOOO_EUR</MsgId>
		<CreDtTm>2015-11-20T16:00:00</CreDtTm>
		<NbOfTxs>2</NbOfTxs>
		<InstgAgt>
			<FinInstnId>
				<BICFI>MMMMBEBB</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>NNNNDEFF</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtInstr>
		<CdtId>MMMM/151121 PPPP_OOOO_EUR_7500</CdtId>
		<BtchBookg>true</BtchBookg>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>QQQQFRPP</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<CdtrAgtAcct>
			<Id>
				<IBAN>DE89370400440532013000</IBAN>
			</Id>
		</CdtrAgtAcct>
		<Cdtr>
				<FinInstnId>
					<BICFI>MMMMBEBB</BICFI>
				</FinInstnId>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<IBAN>FR1420041010050500013M02606</IBAN>
			</Id>
		</CdtrAcct>
		<DrctDbtTxInf>
			<PmtId>
				<InstrId>MMMM/151121 PPPP_OOOO_EUR_2500</InstrId>
				<EndToEndId>REFERENCE0001</EndToEndId>
				<TxId>PPPP _2500</TxId>
			</PmtId>
			<IntrBkSttlmAmt Ccy="EUR">2500</IntrBkSttlmAmt>
			<IntrBkSttlmDt>2015-11-21</IntrBkSttlmDt>
			<Dbtr>
				<FinInstnId>
					<BICFI>PPPPDKKK</BICFI>
				</FinInstnId>
			</Dbtr>
			<DbtrAgt>
				<FinInstnId>
					<BICFI>NNNNDEFF</BICFI>
				</FinInstnId>
			</DbtrAgt>
		</DrctDbtTxInf>
		<DrctDbtTxInf>
			<PmtId>
				<InstrId>MMMM/151121 PPPP_OOOO_EUR_5000</InstrId>
				<EndToEndId>REFERENCE0002</EndToEndId>
				<TxId>OOOO_5000</TxId>
			</PmtId>
			<IntrBkSttlmAmt Ccy="EUR">5000</IntrBkSttlmAmt>
			<IntrBkSttlmDt>2015-11-21</IntrBkSttlmDt>
			<Dbtr>
				<FinInstnId>
					<BICFI>OOOOATWW</BICFI>
				</FinInstnId>
			</Dbtr>
			<DbtrAgt>
				<FinInstnId>
						<BICFI>NNNNDEFF</BICFI>
				</FinInstnId>
			</DbtrAgt>
		</DrctDbtTxInf>
	</CdtInstr>
</FIDrctDbt>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-19.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
