---
template: false
document_kind: "message-example"
title: "FinancialInstitutionCreditTransfer pacs.009.001.13 - 2"
review_status: "needs-review"
manual_curated: true
domain: "payments"
source_ids: ["src-000162", "src-000170"]
message_sets: ["payments-clearing-and-settlement"]
message_ids: ["pacs.009.001.13"]
message_families: ["pacs.009"]
source_locations: [{"source_id": "src-000162", "locator": "P2213–P2283; T43", "heading_path": ["Business Examples", "FinancialInstitutionCreditTransfer pacs.009.001.13 - 2", "First FinancialInstitutionCreditTransfer"]}, {"source_id": "src-000170", "locator": "targetNamespace urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13; /xs:schema/xs:element[@name=\"Document\"]"}]
participant_ids: ["participant-src-000162-example-aaaafrpp", "participant-src-000162-example-bbbbittt", "participant-src-000162-example-ccccsess", "participant-src-000162-example-ddddlull", "participant-src-000162-example-ffffsess"]
issue_ids: ["issue-000059"]
limitations: ["Supplied historical example; no current institution identity is inferred.", "Literal payload has no namespace/Document envelope. Validation applies only to an explicitly derived namespace-qualified Document copy."]
source_editions: ["2025-2026", "March 2026"]
---

# FinancialInstitutionCreditTransfer pacs.009.001.13 - 2

[src-000162](../../../../../../../evidence/omitted/530a772f5cf631826741f05d.md)

## Source scenario

**P2200** FinancialInstitutionCreditTransfer pacs.009.001.13 - 2

**P2201** This example covers three FinancialInstitutionCreditTransfer messages.

**P2202** The first FinancialInstitutionCreditTransfer message is sent by AAAAFRPP to CCCCSESS.

**P2203** The second FinancialInstitutionCreditTransfer message is sent by CCCCSESS to FFFFSESS.

**P2204** The second FinancialInstitutionCreditTransfer message is sent by FFFFSESS to DDDDLULL.

**P2205** First FinancialInstitutionCreditTransfer

**P2206** Description

**P2207** On 20 October 2015, AAAAFRPP agrees on a foreign exchange deal with BBBBITTT: 100 million SEK is sold against 10,621,575.00 EUR (exchange rate 9.4148). The deal is confirmed with common reference BBBBTT4148AAAAPP.

**P2208** On the same day AAAAFRPP sends a FinancialInstitutionCreditTransfer message to its SEK correspondent CCCCSESS. They instruct CCCCSESS to debit their account 123456789 with value date 22 October 2015 to pay 100 million SEK to BBBBITTT.

**P2209** BBBBITTT has communicated the following settlement instructions: the SEK amount is to be credited to the SEK sub- account of their account 995566ZZ876 with DDDDLULL. DDDDLULL owns a SEK account 24538877443 with FFFF Bank (FFFFSESS).

**P2210** Business Data

**P2211** The first FinancialInstitutionCreditTransfer message, from AAAAFRPP to CCCCSESS:

**P2212** Message Instance

[Complete source Business Data table](../documents/src-000162/tables/tbl-0043.md) · [Literal XML payload](../../../../../../../evidence/archived/1f1d49681cdc6a32c7074201.md) · [Source example flow](../flows/example-src-000162-16.md)

## Participants in this instance

| Source participant | Role field | Precise payload path |
| --- | --- | --- |
| [AAAAFRPP](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaafrpp.md) | InstgAgt | /FICdtTrf/GrpHdr/InstgAgt/FinInstnId/BICFI |
| [CCCCSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ccccsess.md) | InstdAgt | /FICdtTrf/GrpHdr/InstdAgt/FinInstnId/BICFI |
| [FFFFSESS](../../../../../../../shared/reference/participants/participant-src-000162-example-ffffsess.md) | IntrmyAgt1 | /FICdtTrf/CdtTrfTxInf/IntrmyAgt1/FinInstnId/BICFI |
| [AAAAFRPP](../../../../../../../shared/reference/participants/participant-src-000162-example-aaaafrpp.md) | Dbtr | /FICdtTrf/CdtTrfTxInf/Dbtr/FinInstnId/BICFI |
| [DDDDLULL](../../../../../../../shared/reference/participants/participant-src-000162-example-ddddlull.md) | CdtrAgt | /FICdtTrf/CdtTrfTxInf/CdtrAgt/FinInstnId/BICFI |
| [BBBBITTT](../../../../../../../shared/reference/participants/participant-src-000162-example-bbbbittt.md) | Cdtr | /FICdtTrf/CdtTrfTxInf/Cdtr/FinInstnId/BICFI |


## Validation and source limitations

The literal payload parses as well-formed XML. On2026-11-09, a working copy with every element qualified into urn:iso:std:iso:20022:tech:xsd:pacs.009.001.13 and wrapped in Document passed the exact supplied XSD src-000170. The source payload remains unchanged. This is schema validation, not business-rule validation or a claim of table/XML equality.

[Complete source differences and precise locators](source-discrepancies.md)

- Table tag <BIC> is retained literally; corresponding instance vocabulary uses BICFI. Exact containing paths remain visible in the complete instance; this table label is not an XSD declaration.

## Complete source payload

```xml
<FICdtTrf>
	<GrpHdr>
		<MsgId>AAAA/151020-SEK/005</MsgId>
		<CreDtTm>2015-10-20T11:03:00</CreDtTm>
		<NbOfTxs>1</NbOfTxs>
		<SttlmInf>
			<SttlmMtd>INDA</SttlmMtd>
			<SttlmAcct>
				<Id>
					<Othr>
						<Id>123456789</Id>
					</Othr>
				</Id>
			</SttlmAcct>
		</SttlmInf>
		<InstgAgt>
			<FinInstnId>
				<BICFI>AAAAFRPP</BICFI>
			</FinInstnId>
		</InstgAgt>
		<InstdAgt>
			<FinInstnId>
				<BICFI>CCCCSESS</BICFI>
			</FinInstnId>
		</InstdAgt>
	</GrpHdr>
	<CdtTrfTxInf>
		<PmtId>
			<InstrId>AAAA/151020-SEK/005/1</InstrId>
			<EndToEndId>BBBBTT4148AAAAPP</EndToEndId>
			<TxId>AAAA/151020-SEK/005/1</TxId>
		</PmtId>
		<IntrBkSttlmAmt Ccy="SEK">100000000</IntrBkSttlmAmt>
		<IntrBkSttlmDt>2015-10-22</IntrBkSttlmDt>
		<IntrmyAgt1>
			<FinInstnId>
				<BICFI>FFFFSESS</BICFI>
			</FinInstnId>
		</IntrmyAgt1>
		<Dbtr>
			<FinInstnId>
				<BICFI>AAAAFRPP</BICFI>
			</FinInstnId>
		</Dbtr>
		<CdtrAgt>
			<FinInstnId>
				<BICFI>DDDDLULL</BICFI>
			</FinInstnId>
		</CdtrAgt>
		<CdtrAgtAcct>
			<Id>
				<Othr>
					<Id>24538877443</Id>
				</Othr>
			</Id>
		</CdtrAgtAcct>
		<Cdtr>
			<FinInstnId>
				<BICFI>BBBBITTT</BICFI>
			</FinInstnId>
		</Cdtr>
		<CdtrAcct>
			<Id>
				<Othr>
					<Id>995566ZZ876</Id>
				</Othr>
			</Id>
			<Ccy>SEK</Ccy>
		</CdtrAcct>
	</CdtTrfTxInf>
</FICdtTrf>
```

<!-- CLEARING-EXAMPLE-FLOW -->
[Source flow and shared scoped participants](../flows/example-src-000162-16.md)
<!-- /CLEARING-EXAMPLE-FLOW -->
